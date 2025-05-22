
# Statistics Quiz 

A lightweight multiple-choice quiz program that helps you review
introductory statistics concepts.  
Developed as the **COMP9001 Python Project Challenge (5 %)** to
demonstrate object-oriented design, file I/O, simple data analytics, and a
GUI built with Tkinter.

---

## 1 · Quick Start

```bash
# clone / unzip the project, then:
cd stat_quiz_project_v3

# install runtime dependencies
pip install matplotlib          # Tkinter ships with Python

# launch
python main.py

Python 3.9+ is recommended.
On macOS, if the GUI fails to open, run brew reinstall python-tk.

⸻

2 · Folder Layout

.
├─ main.py                 # entry point
├─ login.py
├─ main_menu.py
├─ quiz_game.py            # quiz & wrong-question windows
├─ stats.py                # accuracy charts (Matplotlib)
├─ question_bank.py
├─ user_manager.py
├─ data/
│   ├─ banks/
│   │   └─ statistics.json   # 50 unique questions
│   └─ users/                # generated per-user at runtime
└─ README.md

Deleting data/users/ resets all user progress.

⸻

3 · Key Features

Function	Details
Login / Register	Enter any username → profile file auto-created
Random Quiz	10 questions/session, instant Correct / Incorrect pop-ups
Wrong-Question Redo	Loops until every wrong question is answered correctly (or you exit)
Persistent Storage	User history & wrong list saved as JSON
Statistics Dashboard	Daily / Weekly / Monthly / Yearly accuracy plotted with Matplotlib (number above each point = attempts)
Finish & Save vs Exit	Finish & Save records progress; Exit skips the current question and returns to menu


⸻

4 · Editing the Question Bank

Open data/banks/statistics.json; each entry looks like:

{
  "question": "Approximately what percentage of observations fall within ±2σ?",
  "options": ["68 %", "95 %", "99.7 %", "50 %"],
  "answer": 1                     // zero-based index
}

Add, remove, or edit questions as needed. The app reloads the file at start-up.

⸻

5 · Troubleshooting

Issue	Fix
ModuleNotFoundError: matplotlib	pip install matplotlib
Tk window too small / font tiny (macOS)	brew reinstall python-tk
Statistics chart window empty	Complete at least one quiz so history exists


⸻

6 · License

MIT — feel free to fork / adapt for educational purposes.

⸻

Created by <Tao Ye> — COMP9001 Final Project, 2025.

