# Import the product backlog as GitHub issues

`import_backlog.py` reads the backlog CSV and creates labels, sprint milestones and one issue per row.

1. Needs Python 3 and the GitHub CLI (`gh`). Log in with `gh auth login`, then run `gh auth refresh -s project` once so issues can be added to the board.
2. Dry run (default, creates nothing, prints counts and one line per issue):
   `python3 tools/import_backlog.py --repo famebox-max/securesecretary --csv evidence/02-backlog/SecureSecretary_Product_Backlog_v3.csv`
3. Real run: the same command with `--create` at the end.
4. Safe to run twice: existing labels, milestones and issues (matched by `PB-xx`) are skipped.
5. On any `gh` error it stops, prints the exact error and the issues already created.
6. No assignees are set. Owners are chosen at sprint planning.
7. Never put a token or password in any file. Login only through `gh auth login`.
