
"""Load statistics question bank"""

import os, json, random
from typing import List, Dict, Any


class QuestionBank:
    DATA_DIR = os.path.join("data", "banks")

    def __init__(self, filename: str):
        self.filepath = os.path.join(self.DATA_DIR, filename)
        os.makedirs(self.DATA_DIR, exist_ok=True)
        self._ensure_file()
        self.questions: List[Dict[str, Any]] = self._load()

    def random_questions(self, n=10):
        return random.sample(self.questions, k=min(n, len(self.questions)))

    # ------------ file helpers ------------
    def _load(self):
        with open(self.filepath, "r", encoding="utf-8") as f:
            return json.load(f)

    def _ensure_file(self):
        if not os.path.exists(self.filepath):
            with open(self.filepath, "w", encoding="utf-8") as f:
                json.dump([], f)
