import tkinter as tk


class Task:
    def __init__(self, task_id, title, deadline, description=""):
        self.task_id = task_id
        self.title = title
        self.deadline = deadline
        self.description = description

    def update_task(self, todo_list, task_id, title, deadline, description):
        pass

    def change_status(self, todo_list, task_id, status):
        pass
