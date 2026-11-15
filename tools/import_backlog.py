#!/usr/bin/env python3
"""Import the SecureSecretary product backlog CSV as GitHub issues.

Default is a dry run (creates nothing). Real creation needs --create.
Standard library only. Uses only the gh command line (gh auth login).
"""
import argparse
import collections
import csv
import json
import re
import subprocess
import sys
import time

PROJECT_NUMBER = "1"  # Team Board
PAUSE_SECONDS = 2
SOURCE_LINE = "Source: SecureSecretary_Product_Backlog_v3.csv"
EMPTY_STORY_TEXT = ("Story and acceptance criteria must be written by the "
                    "Product Owner before this item enters a sprint.")

# Sprint milestones: name -> due date (end of the Tuesday)
MILESTONES = {
    "Sprint 2": "2026-11-17", "Sprint 3": "2026-11-24",
    "Sprint 4": "2026-12-01", "Sprint 5": "2026-12-08",
    "Sprint 6": "2026-12-15", "Sprint 7": "2026-12-22",
    "Sprint 8": "2026-12-29", "Sprint 9": "2027-01-05",
    "Sprint 10": "2027-01-12", "Sprint 11": "2027-01-19",
}

# Labels: name -> short description
LABELS = {
    "type:build": "Build a feature or part of the app",
    "type:learn": "Learning task (study or practice)",
    "type:security": "Security work",
    "type:doc": "Documentation task",
    "type:test": "Testing task",
    "type:install": "Install or set up a tool",
    "moscow:must": "MoSCoW: must have",
    "moscow:should": "MoSCoW: should have",
    "moscow:could": "MoSCoW: could have",
    "moscow:wont-for-now": "MoSCoW: will not do for now",
    "area:1": "Area 1: login, security and testing",
    "area:2": "Area 2: database, calendar and board",
    "area:3": "Area 3: Flutter screens",
    "area:4": "Area 4: AI secretary and coach",
    "area:5": "Area 5: machine learning and scam checker",
    "area:all": "Whole team",
    "needs-refinement": "Story and acceptance criteria still to be written",
    "wont-for-now": "Not planned for now",
}


def slug(text):
    """'Won't for now' -> 'wont-for-now'; 'Must' -> 'must'."""
    text = text.strip().lower().replace("'", "").replace("\u2019", "")
    return re.sub(r"[^a-z0-9]+", "-", text).strip("-")


def area_labels(cell):
    labels = []
    for part in cell.split(","):
        part = part.strip().lower()
        if part:
            labels.append("area:" + part)  # "all" -> area:all
    return labels


def build_issue(row):
    pb_id = row["ID"].strip()
    labels = ["type:" + slug(row["Type"]), "moscow:" + slug(row["MoSCoW"])]
    labels += area_labels(row["Suggested area"])

    match = re.search(r"\d+", row["Suggested sprint"])  # first whole number
    milestone = "Sprint " + match.group() if match else None
    if milestone is None:
        labels.append("wont-for-now")

    story = row["User story"].strip()
    criteria = row["Acceptance criteria"].strip()
    if story:
        body = [story, "", "**Acceptance criteria**", criteria]
    else:
        labels.append("needs-refinement")
        body = [EMPTY_STORY_TEXT]

    table_fields = [("Size", "Size"), ("Depends on", "Depends on"),
                    ("Suggested area", "Suggested area"), ("MoSCoW", "MoSCoW"),
                    ("Type", "Type"), ("Change mark", "Change mark")]
    table = []
    for header, column in table_fields:
        value = row[column].strip().replace("\n", " ")
        if value:
            table.append("| %s | %s |" % (header, value))
    if table:
        body += ["", "| Field | Value |", "| --- | --- |"] + table
    body += ["", SOURCE_LINE]

    return {"id": pb_id, "title": "%s %s" % (pb_id, row["Title"].strip()),
            "body": "\n".join(body), "labels": labels, "milestone": milestone}


def read_issues(path):
    with open(path, encoding="utf-8-sig", newline="") as handle:
        return [build_issue(row) for row in csv.DictReader(handle)]


def dry_run(issues):
    by_milestone = collections.Counter(i["milestone"] or "no milestone"
                                       for i in issues)
    by_label = collections.Counter(l for i in issues for l in i["labels"])
    print("DRY RUN: nothing is created.\n")
    print("Labels to create (if missing): %d" % len(LABELS))
    print("Milestones to create (if missing): %d" % len(MILESTONES))
    print("Issues: %d\n" % len(issues))
    print("Issues per milestone:")
    for name in MILESTONES:
        print("  %-10s %d" % (name, by_milestone.get(name, 0)))
    print("  %-10s %d\n" % ("none", by_milestone.get("no milestone", 0)))
    print("Label counts:")
    for name in LABELS:
        print("  %-22s %d" % (name, by_label.get(name, 0)))
    print("\nOne line per issue:")
    for i in issues:
        print("  %-6s %-10s %s" % (i["id"], i["milestone"] or "-",
                                   ", ".join(i["labels"])))


class GhError(Exception):
    pass


def gh(args, stdin=None):
    """Run one gh command. Stop with the exact error if it fails."""
    result = subprocess.run(["gh"] + args, input=stdin,
                            capture_output=True, text=True)
    if result.returncode != 0:
        message = result.stderr.strip() or result.stdout.strip()
        raise GhError("gh %s\n%s" % (" ".join(args[:3]), message))
    return result.stdout


def label_color(name):
    if name.startswith("type:"):
        return "1d76db"
    if name.startswith("moscow:"):
        return "e99695"
    if name.startswith("area:"):
        return "5319e7"
    return "fbca04"


def create_labels(repo):
    have = {l["name"] for l in json.loads(
        gh(["label", "list", "--repo", repo, "--limit", "200",
            "--json", "name"]))}
    made = 0
    for name, description in LABELS.items():
        if name in have:
            print("label exists, skipped: %s" % name)
            continue
        gh(["label", "create", name, "--repo", repo,
            "--description", description, "--color", label_color(name)])
        print("label created: %s" % name)
        made += 1
        time.sleep(PAUSE_SECONDS)
    return made


def create_milestones(repo):
    have = {m["title"] for m in json.loads(
        gh(["api", "repos/%s/milestones" % repo, "--method", "GET",
            "-f", "state=all", "-f", "per_page=100"]))}
    made = 0
    for name, due in MILESTONES.items():
        if name in have:
            print("milestone exists, skipped: %s" % name)
            continue
        gh(["api", "repos/%s/milestones" % repo, "-f", "title=" + name,
            "-f", "due_on=%sT23:59:59Z" % due, "-f", "state=open"])
        print("milestone created: %s (due %s)" % (name, due))
        made += 1
        time.sleep(PAUSE_SECONDS)
    return made


def create_issues(repo, issues, created, board_failed):
    owner = repo.split("/")[0]
    done = set()
    for item in json.loads(gh(["issue", "list", "--repo", repo, "--state",
                               "all", "--limit", "1000", "--json",
                               "number,title"])):
        found = re.match(r"\s*(PB-\d+)\b", item["title"])
        if found:
            done.add(found.group(1))
    skipped = 0
    for issue in issues:
        if issue["id"] in done:
            print("issue exists, skipped: %s" % issue["id"])
            skipped += 1
            continue
        args = ["issue", "create", "--repo", repo, "--title", issue["title"],
                "--body-file", "-"]
        for label in issue["labels"]:
            args += ["--label", label]
        if issue["milestone"]:
            args += ["--milestone", issue["milestone"]]
        url = gh(args, stdin=issue["body"]).strip().splitlines()[-1]
        created.append(issue["id"])
        print("created %s -> %s" % (issue["id"], url))
        try:
            gh(["project", "item-add", PROJECT_NUMBER, "--owner", owner,
                "--url", url])
        except GhError as error:
            board_failed.append(url)
            print("  could not add to the board: %s" % error)
        time.sleep(PAUSE_SECONDS)
    return skipped


def create_all(repo, issues):
    created, board_failed = [], []
    try:
        labels = create_labels(repo)
        milestones = create_milestones(repo)
        skipped = create_issues(repo, issues, created, board_failed)
    except GhError as error:
        print("\nERROR, stopped.\n%s" % error)
        print("Issues already created in this run: %s"
              % (", ".join(created) or "none"))
        sys.exit(1)
    print("\nSUMMARY: labels created %d, milestones created %d, "
          "issues created %d, issues skipped %d"
          % (labels, milestones, len(created), skipped))
    if board_failed:
        print("\nThese issues are NOT on the board. Manual steps: open the "
              "Team Board, click '+ Add item', search each issue number "
              "and add it:")
        for url in board_failed:
            print("  " + url)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", required=True, help="owner/name")
    parser.add_argument("--csv", required=True, help="path to backlog CSV")
    parser.add_argument("--create", action="store_true",
                        help="really create (default is a dry run)")
    args = parser.parse_args()
    issues = read_issues(args.csv)
    if args.create:
        create_all(args.repo, issues)
    else:
        dry_run(issues)


if __name__ == "__main__":
    main()
