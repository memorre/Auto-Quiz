
"""Manage user data: history and wrong questions"""

import os, json
from datetime import datetime
from typing import Dict, Any, List


class UserManager:
    DATA_DIR = os.path.join("data", "users")

    def __init__(self):
        os.makedirs(self.DATA_DIR, exist_ok=True)
        self.username: str | None = None
        self.profile: Dict[str, Any] = {}

    # ---------------- login ----------------
    def login(self, username: str) -> None:
        self.username = username
        path = self._path()
        if os.path.exists(path):
            with open(path, "r", encoding="utf-8") as f:
                self.profile = json.load(f)
        else:
            self.profile = {"history": [], "wrong": []}
            self._save()

    # ---------------- history ----------------
    def add_history(self, correct: int, total: int) -> None:
        self.profile["history"].append({
            "time": datetime.now().isoformat(timespec="seconds"),
            "correct": correct,
            "total": total
        })
        self._save()

    def get_history(self) -> List[Dict[str, Any]]:
        return list(self.profile.get("history", []))

    # ---------------- wrong questions ----------------
    def add_wrong(self, q: Dict[str, Any]) -> None:
        if q not in self.profile["wrong"]:
            self.profile["wrong"].append(q)
            self._save()

    def remove_wrong(self, q: Dict[str, Any]) -> None:
        if q in self.profile["wrong"]:
            self.profile["wrong"].remove(q)
            self._save()

    def get_wrong(self) -> List[Dict[str, Any]]:
        return list(self.profile.get("wrong", []))

    # ---------------- helpers ----------------
    def _path(self):
        return os.path.join(self.DATA_DIR, f"{self.username}.json")

    def _save(self):
        with open(self._path(), "w", encoding="utf-8") as f:
            json.dump(self.profile, f, ensure_ascii=False, indent=2)
