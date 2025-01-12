from typing import List
from todo.task import Task
import sqlite3


class TodoList:
    def __init__(self):
        self.tasks: List[Task] = []

    def add_task(self, task: Task):
        pass

    def delete_task(self, task_id: str):
        pass

    def list_tasks(self):
        pass

    def search_tasks(self, keyword: str):
        pass

    def save_to_file(self, filename: str):
        pass

    def load_from_file(self, filename: str):
        pass
