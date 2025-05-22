
"""Main menu window"""

import tkinter as tk
from question_bank import QuestionBank
from quiz_game import QuizWindow, QuizWindowWrong
from stats import StatsWindow


class MainMenuWindow:
    def __init__(self, user_manager):
        self.um = user_manager
        self.root = tk.Tk()
        self.root.title("Statistics Quiz - Menu")

        tk.Label(self.root, text=f"User: {self.um.username}", font=("Arial", 12, "bold")).pack(pady=15)

        tk.Button(self.root, text="Start Quiz", command=self._start_quiz)                .pack(fill="x", padx=60, pady=6)

        tk.Button(self.root, text="Redo Wrong Questions", command=self._redo_wrong)                .pack(fill="x", padx=60, pady=6)

        tk.Button(self.root, text="View Statistics", command=lambda: StatsWindow(self.um))                .pack(fill="x", padx=60, pady=6)

        tk.Button(self.root, text="Exit", command=self.root.destroy).pack(pady=15)

        self.root.mainloop()

    # ---------- actions ----------
    def _start_quiz(self):
        bank = QuestionBank("statistics.json")
        self.root.destroy()
        QuizWindow(self.um, bank)

    def _redo_wrong(self):
        wrong = self.um.get_wrong()
        if not wrong:
            tk.messagebox.showinfo("Info", "No wrong questions yet!")
            return
        self.root.destroy()
        QuizWindowWrong(self.um, wrong)
