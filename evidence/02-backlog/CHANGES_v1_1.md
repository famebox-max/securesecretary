# CHANGES v1.1 (backlog v2 to v3)

Plan v1.1: Flutter mobile app instead of React web app, new items PB-38 and PB-39, and four items written out for the next sprint (PB-11 to PB-14).

**For all 39 rows:** a new last column "Change mark" was added (12 columns now). It is empty for unchanged items. Nothing was deleted or reordered, and the v2 file was not touched.

Changed or added items: PB-03, PB-08, PB-31, PB-38, PB-39. Refined items: PB-11, PB-12, PB-13, PB-14.

---

## PB-03  [CHANGED v1.1]

**Reason:** The team decided to build a Flutter mobile app instead of a React web app, so the first interface learning item must teach Flutter and Dart.

**Fields changed:** Title, User story, Acceptance criteria, Change mark

### Title

BEFORE:

> React with Tailwind hello world

AFTER:

> Flutter and Dart hello world

### User story

BEFORE:

> As a team member, I want to build a React page styled with Tailwind, so that I understand how our web interface is made. (React = a JavaScript library for building web pages. Tailwind CSS = a set of ready-made style names that make pages look good quickly.)

AFTER:

> As a team member, I want to build a small Flutter app with one screen, a heading and a button that changes the text when tapped, so that I understand how the screens of our mobile app are made. (Flutter = a free toolkit for building mobile apps that run on phones. Dart = the programming language we use to write Flutter apps. Emulator = a pretend phone that runs on your laptop.)

### Acceptance criteria

BEFORE:

> 1) A 5-line note and a small working example are saved in our "learning" folder.
> 2) The page runs on my laptop, shows a styled heading, and a button that changes the text when clicked.
> 3) I explained it in 3 minutes at the Friday help meeting.

AFTER:

> 1) A 5-line note and a small working example are saved in our "learning" folder.
> 2) The app runs on my emulator, on my phone or, as a fallback only, in the Chrome browser. It shows the heading, and the button changes the text when tapped.
> 3) I explained it in 3 minutes at the Friday help meeting.

### Change mark

BEFORE:

> (empty)

AFTER:

> [CHANGED v1.1]

---

## PB-08  [CHANGED v1.1]

**Reason:** The first working path now starts in the Flutter app, not a web page. The item also needs the new Flutter learning item (PB-38) and the architecture and API list (PB-39) first.

**Fields changed:** Title, Acceptance criteria, Depends on, Change mark

### Title

BEFORE:

> Walking skeleton: one task from the web page to the database and back

AFTER:

> Walking skeleton: one task from the Flutter app to the database and back

### Acceptance criteria

BEFORE:

> 1) The React page sends the task to the FastAPI backend and it is saved in PostgreSQL.
> 2) After I refresh the page, the saved task is still shown.
> 3) The whole thing starts with one documented command (Docker if the laptop can run it, otherwise a run script) and was merged by pull request.

AFTER:

> 1) The Flutter app sends the task to the FastAPI backend and it is saved in PostgreSQL.
> 2) After I close and reopen the app, the saved task is still shown.
> 3) The whole thing starts with one documented command (Docker if the laptop can run it, otherwise a run script) and was merged by pull request.

### Depends on

BEFORE:

> PB-01, PB-02, PB-03, PB-04, PB-05

AFTER:

> PB-01, PB-02, PB-03, PB-04, PB-05, PB-38, PB-39

### Change mark

BEFORE:

> (empty)

AFTER:

> [CHANGED v1.1]

---

## PB-31  [CHANGED v1.1]

**Reason:** Flutter needs the Flutter SDK, a code editor and a place to run the app. Node.js and npm were only needed for React, so they are removed.

**Fields changed:** User story, Acceptance criteria, Change mark

### User story

BEFORE:

> As a team member, I want my laptop to have all the tools we need installed and checked, so that I can start the learning items in Sprint 2 without losing time. (Git = the tool that records changes to code; a commit is one saved set of changes. Python = the programming language of our backend. Node.js = a tool that lets a laptop run JavaScript, which React needs. npm = the tool that installs JavaScript packages. pgAdmin = a free window for looking at a PostgreSQL database.)

AFTER:

> As a team member, I want my laptop to have all the tools we need installed and checked, so that I can start the learning items in Sprint 2 without losing time. (Git = the tool that records changes to code; a commit is one saved set of changes. Python = the programming language of our backend. Flutter SDK = the toolkit we install to build our mobile app; it includes the Dart language. flutter doctor = a Flutter command that checks if your setup is complete. Code editor = a program for writing code. Emulator = a pretend phone that runs on your laptop. pgAdmin = a free window for looking at a PostgreSQL database.)

### Acceptance criteria

BEFORE:

> 1) git --version, python --version, node --version and npm --version each show a version number, and I posted one screenshot of these checks in the team group.
> 2) My commits show my own name and GitHub email.
> 3) For PostgreSQL and Docker, either pgAdmin opens and docker --version works, or I told the team why my laptop cannot run them.

AFTER:

> 1) git --version, python --version and flutter --version each show a version number, and I posted a screenshot of these and of the flutter doctor result in the team group.
> 2) My commits show my own name and GitHub email.
> 3) For PostgreSQL and Docker, either pgAdmin opens and docker --version works, or I told the team why my laptop cannot run them. I also said where I can run the Flutter hello app (emulator, phone, or Chrome as a fallback).

### Change mark

BEFORE:

> (empty)

AFTER:

> [CHANGED v1.1]

---

## PB-11  [REFINED]

**Reason:** The next sprint needs this item ready to start. The User story and Acceptance criteria were empty.

**Fields changed:** User story, Acceptance criteria, Change mark

### User story

BEFORE:

> EMPTY

AFTER:

> As a team member, I want to build one small example each of a TOTP code, AES-256 encryption and HTTPS, so that I understand the security tools we will use for login and for protecting stored data. (TOTP = a time-based one-time password: a 6-digit code from an authenticator app that changes after a short time. AES-256 = a strong way to lock (encrypt) data so that only a person with the key can read it. Key = the secret value used to lock and unlock data. HTTPS = the secure way an app talks to a server, so that others cannot read the messages. Environment variable = a setting kept on your laptop, outside the code.)

### Acceptance criteria

BEFORE:

> EMPTY

AFTER:

> 1) A 5-line note and one small working example each of a TOTP code, AES-256 encryption and HTTPS are saved in our "learning" folder.
> 2) The AES-256 example reads its key from an environment variable; the key is never written in the code, and a search of the code for the key text finds nothing.
> 3) I explained it in 3 minutes at the Friday help meeting.

### Change mark

BEFORE:

> (empty)

AFTER:

> [REFINED]

---

## PB-12  [REFINED]

**Reason:** The next sprint needs this item ready to start. The User story and Acceptance criteria were empty.

**Fields changed:** User story, Acceptance criteria, Change mark

### User story

BEFORE:

> EMPTY

AFTER:

> As a user with Personal and Work tasks, I want to enter a 6-digit code from an authenticator app after my password, so that nobody can open my account with only my password. (Multi-factor login = logging in with two proofs, here the password and a code. TOTP = a time-based one-time password: a code that an authenticator app makes and that changes after a short time. Authenticator app = a phone app that shows the code. pytest = a Python tool for running automatic tests.)

### Acceptance criteria

BEFORE:

> EMPTY

AFTER:

> 1) After the right password, a Flutter screen asks for the 6-digit code, and only a right code lets me in.
> 2) A wrong code is rejected and counts toward the same 5-try lock as wrong passwords.
> 3) A pytest test checks that a right code works and a wrong code fails.

### Change mark

BEFORE:

> (empty)

AFTER:

> [REFINED]

---

## PB-13  [REFINED]

**Reason:** The next sprint needs this item ready to start. The User story and Acceptance criteria were empty.

**Fields changed:** User story, Acceptance criteria, Change mark

### User story

BEFORE:

> EMPTY

AFTER:

> As a team member, I want our FastAPI backend to call an AI model through an API, so that our secretary and coach can answer questions without the app ever holding a secret key. (AI model = a program that writes answers to questions; we use the free option chosen in PB-37. API key = a secret password that lets our program use the AI service. Environment variable = a setting kept on your laptop, outside the code. .gitignore = a file that tells git which files never to save in the repository.)

### Acceptance criteria

BEFORE:

> EMPTY

AFTER:

> 1) The API key is read from an environment variable and is not in the repository: I showed the .gitignore line, and a search of the repository for the key text finds nothing.
> 2) A question sent to the FastAPI backend gets a reply from the AI model.
> 3) If the AI service fails or the free limit is reached, the user sees a friendly error message and not a crash.

### Change mark

BEFORE:

> (empty)

AFTER:

> [REFINED]

---

## PB-14  [REFINED]

**Reason:** The next sprint needs this item ready to start. The User story and Acceptance criteria were empty.

**Fields changed:** User story, Acceptance criteria, Change mark

### User story

BEFORE:

> EMPTY

AFTER:

> As a student using Learn mode, I want the coach to give step-by-step hints before the full answer, so that I try to solve the problem myself and learn more. (Prototype = a first small version made to test an idea. Hint = a small clue that helps without giving the answer. Go or no-go = a decision to continue with the idea or to stop.)

### Acceptance criteria

BEFORE:

> EMPTY

AFTER:

> 1) 20 sample questions are saved in a file, and each has three steps of hints: a nudging question, a pointer to the idea, and a worked step.
> 2) The full answer comes only after three attempts, and a results table lists for each question: hints helped (yes/no) and full answer held back (yes/no).
> 3) A written go or no-go decision with a reason is saved in our "docs" folder.

### Change mark

BEFORE:

> (empty)

AFTER:

> [REFINED]

---

## PB-38  [ADDED v1.1]

**Reason:** New item. A Flutter app needs its own learning step (screens, state, calling the backend) before the walking skeleton PB-08.

**BEFORE:** this item did not exist.

**AFTER (new row):**

- **ID:** PB-38
- **Type:** LEARN
- **Title:** Dart and Flutter basics: screens, state, and calling our backend
- **User story:** As a team member, I want to learn how a Flutter app shows screens, keeps state and calls our backend, so that I can build the real screens of our app and connect them to the FastAPI backend. (Dart = the programming language we use to write Flutter apps. Flutter = a free toolkit for building mobile apps. Screen = one page of the app that the user sees. State = the data a screen remembers and shows right now, so the screen changes when the data changes. HTTP = the way the app sends a request to the backend and gets a reply.)
- **Acceptance criteria:** 1) A 5-line note and a small working example are saved in our "learning" folder. / 2) A screen shows a list that updates when I add an item (this is "state"). / 3) The app calls the PB-02 /hello address over HTTP and shows the reply; I explained it in 3 minutes at the Friday help meeting.
- **MoSCoW:** Must
- **Size:** M (3h)
- **Suggested sprint:** 2
- **Depends on:** PB-02, PB-03
- **Suggested area:** 3
- **Holiday risk:** (empty)
---

## PB-39  [ADDED v1.1]

**Reason:** New item. The whole team needs one shared picture of the parts, the database tables and the API addresses before PB-08 is built.

**BEFORE:** this item did not exist.

**AFTER (new row):**

- **ID:** PB-39
- **Type:** DOC
- **Title:** Architecture sketch, database tables and API list
- **User story:** As a team member, I want one clear architecture sketch, a list of database tables and a list of API addresses, so that all six of us build parts that fit together. (Architecture = the plan that shows the main parts of a system and how they connect. Database table = a grid in the database that stores one kind of data, with a column for each detail. API address = an address the app calls to ask the backend to do something; each has a method, which is the kind of request, such as read or send. AI model = a program that writes answers to questions. AI key = the secret password for the AI service.)
- **Acceptance criteria:** 1) A one-page picture shows how the Flutter app, the FastAPI backend, PostgreSQL and the AI model connect, and states that only the backend holds the AI key and database access. / 2) A list of database tables (users, tasks, events) with their columns, and a list of API addresses (sign-up, login, tasks) with method, input and output. / 3) One teammate reviewed it and the files are in our "docs" folder.
- **MoSCoW:** Must
- **Size:** M (3h)
- **Suggested sprint:** 3
- **Depends on:** PB-02, PB-04
- **Suggested area:** 1, 2
- **Holiday risk:** (empty)
---

## QUESTIONS

Things that are unclear or inconsistent. I did not guess; where I had to write something, I say what I did.

1. **PB-08 sprint timing.** PB-08 says "3 (may start in 2 if the learning finishes early)", but it now depends on PB-39, which is in sprint 3. PB-08 cannot start in sprint 2 unless PB-39 moves. I did not change any sprint (R8). Which should it be?
2. **Missing Flutter dependencies.** PB-12 needs a Flutter screen, and PB-10 and PB-17 build screens, but their "Depends on" does not include PB-38 (screens and state). R8 says change no other "Depends on". Should PB-38 be added to them later?
3. **PB-12, missing pieces.** No item builds the Flutter password login screen (PB-09 has no screen), and no item says how a user first adds the secret to the authenticator app (set-up step). PB-12 only covers the code screen after the password. Where should these go?
4. **PB-11, criteria 1 and 3.** R7 gave only the technical content (one example each; key from an environment variable). To reach three criteria I copied the style of the other LEARN items (5-line note in "learning" folder; Friday help meeting explanation). Please confirm.
5. **PB-13, "the user sees a friendly error".** PB-13 has no app screen (it depends on PB-02 and PB-37 only). I wrote the text as given. How should this be tested: in the backend reply, or in the Flutter app?
6. **PB-14, three attempts and hints.** "Full answer only after three attempts" and "three steps of hints" can be read in two ways (three tries by the student, or three hint steps shown). I wrote both exactly as given. Also unclear: are the hints written by hand or made by the AI model (PB-14 depends on PB-13), and in which folder is the question file saved?
7. **PB-38, HTTP or HTTPS.** R5 says the app calls /hello "over HTTP", but the architecture (section 6) says HTTPS. I used HTTP as written, assuming it is for local learning only. Also, R5 puts "the app calls /hello ... shows the reply" and "I explained it in 3 minutes" together in criterion 3; I kept them in one criterion.
8. **Item size.** PB-03 stays S (2h) although it now covers Flutter, Dart and running an emulator or phone for the first time. PB-38 is M (3h). These may be tight for beginners. I did not change any size (R8).
9. **Git steps not done here.** Branch backlog-v3, the commit, the pull request, the review and the screenshot must be done by the team. The git status and git log proof could not be produced from these files alone.
