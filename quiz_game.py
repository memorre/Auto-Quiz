"""Quiz windows with immediate feedback, wrong-question redo,
and safe return to the main menu (no circular imports)."""

import tkinter as tk
from tkinter import messagebox
import random
from typing import List, Dict, Any

from user_manager import UserManager
from question_bank import QuestionBank


# ────────────────────────────────────────────────────────────────
class _BaseQuiz:
    """Shared widgets and helpers."""

    def __init__(self):
        self.var_choice = None
        self.lbl_q = None
        self.radio: List[tk.Radiobutton] = []

    def _build(self, root: tk.Tk | tk.Toplevel) -> None:
        self.var_choice = tk.IntVar(master=root)
        self.lbl_q = tk.Label(
            root, text="", wraplength=420, justify="left", fg="white"
        )
        self.lbl_q.pack(pady=12)

        for i in range(4):
            rb = tk.Radiobutton(
                root, text="", variable=self.var_choice, value=i, anchor="w"
            )
            rb.pack(fill="x", padx=40)
            self.radio.append(rb)

        tk.Button(root, text="Next", command=self._next).pack(pady=8)
        # Finish & save progress
        tk.Button(root, text="Finish & Save",
             command = self._finish_early).pack(pady=5)
        # Exit immediately, discarding the current question only
        tk.Button(root, text="Exit (without saving)",
             command = self._return_menu_no_save).pack(pady=5)
         # extra hint
        tk.Label(root, text="Tip: Finish = save progress · Exit = skip save process",
             fg = "lightgray", font = ("Arial", 8)).pack(pady=(4, 2))

    # local import avoids circular dependency
    def _return_menu_no_save(self) -> None:
        self.root.destroy()
        from main_menu import MainMenuWindow
        MainMenuWindow(self.um)


# ────────────────────────────────────────────────────────────────
class QuizWindow(_BaseQuiz):
    """Random quiz session."""

    def __init__(self, um: UserManager, bank: QuestionBank):
        self.root = tk.Tk()
        self.root.title("Statistics Quiz")
        super().__init__()

        self.um = um
        self.questions = bank.random_questions(10)
        self.idx = 0
        self.score = 0
        self.answered = 0
        self.finished_early = False

        self._build(self.root)
        self._show()
        self.root.mainloop()

    # ---------------- internal flow ----------------
    def _show(self) -> None:
        q = self.questions[self.idx]
        self.lbl_q.config(text=f"Q{self.idx + 1}. {q['question']}")
        for i, opt in enumerate(q["options"]):
            self.radio[i].config(text=opt, value=i)
        self.var_choice.set(-1)

    def _next(self) -> None:
        choice = self.var_choice.get()
        if choice == -1:
            messagebox.showwarning("Warning", "Select an option first.")
            return

        self.answered += 1
        q = self.questions[self.idx]
        correct_text = q["options"][q["answer"]]

        if choice == q["answer"]:
            self.score += 1
            messagebox.showinfo("Correct", "Good job!")
        else:
            messagebox.showinfo("Incorrect", f"Wrong. Correct: {correct_text}")
            self.um.add_wrong(q)

        self.idx += 1
        if self.idx < len(self.questions):
            self._show()
        else:
            self._finish()

    def _finish_early(self) -> None:
        if self.var_choice.get() != -1 and self.idx < len(self.questions):
            # count the currently answered question first
            self._next()
            return
        self.finished_early = True
        self._finish()

    def _finish(self) -> None:
        total = self.answered if self.finished_early else len(self.questions)
        self.um.add_history(self.score, total)
        messagebox.showinfo("Result", f"Score: {self.score}/{total}")
        self.root.destroy()
        from main_menu import MainMenuWindow
        MainMenuWindow(self.um)


# ────────────────────────────────────────────────────────────────
class QuizWindowWrong(_BaseQuiz):
    """Redo wrong-question session (keeps looping until all correct)."""

    def __init__(self, um: UserManager, wrong_qs: List[Dict[str, Any]]):
        self.root = tk.Tk()
        self.root.title("Redo Wrong Questions")
        super().__init__()

        self.um = um
        self.questions = wrong_qs.copy()      # mutable working list
        random.shuffle(self.questions)
        self.idx = 0

        self._build(self.root)
        self._show()
        self.root.mainloop()

    # ───────── helper ─────────
    def _show(self) -> None:
        """Display the current question; if list empty, return to menu."""
        if not self.questions:
            messagebox.showinfo("Great!", "All wrong questions answered correctly!")
            self.root.destroy()
            from main_menu import MainMenuWindow
            MainMenuWindow(self.um)
            return

        q = self.questions[self.idx]
        self.lbl_q.config(text=f"Wrong Q{self.idx + 1}: {q['question']}")
        for i, opt in enumerate(q["options"]):
            self.radio[i].config(text=opt, value=i)
        self.var_choice.set(-1)

    # ───────── core logic ─────────
    def _next(self) -> None:
        choice = self.var_choice.get()
        if choice == -1:
            messagebox.showwarning("Warning", "Select an option.")
            return

        q = self.questions[self.idx]
        correct_text = q["options"][q["answer"]]

        if choice == q["answer"]:
            # correct → remove from both on-screen list & persistent wrong list
            if messagebox.askyesno("Correct", "Correct! Remove from wrong list?"):
                self.um.remove_wrong(q)
                self.questions.pop(self.idx)
                # do NOT advance idx, because we just removed current item
            else:
                # user chose to keep it → advance idx
                self.idx += 1
        else:
            # still wrong → keep it, advance idx
            messagebox.showinfo("Incorrect", f"Wrong. Correct: {correct_text}")
            self.idx += 1

        # ===== wrap-around logic =====
        if self.idx >= len(self.questions):
            # reached end of list but still有错题：重新从头开始下一轮
            self.idx = 0
            if self.questions:          # list non-empty ⇒ start another loop
                random.shuffle(self.questions)   # optional：再洗牌
                messagebox.showinfo("Next Round", "Let's try the remaining wrong questions again!")

        self._show()

    def _finish_early(self) -> None:
        """User clicked 'Return to Menu' without clearing all wrong questions."""
        self.root.destroy()
        from main_menu import MainMenuWindow
        MainMenuWindow(self.um)