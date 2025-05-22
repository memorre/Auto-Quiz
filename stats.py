
"""Statistics with attempts and accuracy"""

import tkinter as tk
from tkinter import ttk
from datetime import datetime
from typing import List, Tuple
import matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from user_manager import UserManager

matplotlib.use("TkAgg")


class StatsWindow:
    def __init__(self, um: UserManager):
        self.um = um
        self.root = tk.Toplevel()
        self.root.title("Performance Statistics")
        self._tabs()
        self.root.mainloop()

    def _tabs(self):
        tabs = ttk.Notebook(self.root)
        tabs.pack(expand=True, fill="both")
        for p in ("daily", "weekly", "monthly", "yearly"):
            f = ttk.Frame(tabs)
            tabs.add(f, text=p.capitalize())
            self._plot(f, p)

    def _plot(self, parent, period: str):
        data = self._aggregate(period)
        if not data:
            tk.Label(parent, text="No data yet").pack(pady=30)
            return
        labels, correct, total = zip(*data)
        accuracy = [c / t * 100 for c, t in zip(correct, total)]

        fig = Figure(figsize=(4, 3))
        ax = fig.add_subplot(111)
        ax.plot(labels, accuracy, marker="o")
        for x, y, t in zip(labels, accuracy, total):
            ax.annotate(str(t), (x, y), textcoords="offset points", xytext=(0, 8), ha="center")
        ax.set_ylabel("Accuracy (%)")
        ax.set_title("Accuracy (numbers above points = attempts)")
        ax.tick_params(axis="x", rotation=40)

        canvas = FigureCanvasTkAgg(fig, master=parent)
        canvas.get_tk_widget().pack(fill="both", expand=True)
        canvas.draw()

    def _aggregate(self, period: str) -> List[Tuple[str, int, int]]:
        buckets = {}
        for rec in self.um.get_history():
            dt = datetime.fromisoformat(rec["time"])
            if period == "daily":
                key = dt.strftime("%Y-%m-%d")
            elif period == "weekly":
                key = f"{dt.strftime('%Y')}-W{dt.strftime('%W')}"
            elif period == "monthly":
                key = dt.strftime("%Y-%m")
            else:
                key = dt.strftime("%Y")
            correct, total = buckets.get(key, (0, 0))
            buckets[key] = (correct + rec["correct"], total + rec["total"])
        return sorted((k, c, t) for k, (c, t) in buckets.items())
