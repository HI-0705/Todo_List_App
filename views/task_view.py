import uuid
import tkinter as tk
import datetime
from tkcalendar import Calendar
from todo.todo_list import TodoList
from todo.task import Task


class TaskView:
    def __init__(self, master):
        self.master = master
        self.master.title("Task List App")
        self.master.geometry("316x420")

        # ﾀｲﾄﾙ
        self.title_label = tk.Label(
            self.master, text="Task List App", font=("Helvetica", 16)
        )
        self.title_label.grid(row=0, column=0, columnspan=2, pady=(20, 10))

        # ﾀｽｸ入力ﾌﾚｰﾑ
        self.task_frame = tk.LabelFrame(self.master, text="New Task", padx=10, pady=10)
        self.task_frame.grid(row=1, column=0, columnspan=2, sticky="ew", padx=20)

        # ﾀｲﾄﾙ入力
        self.title_label = tk.Label(self.task_frame, text="ﾀｽｸ:")
        self.title_label.grid(row=0, column=0, sticky="w")
        self.title_entry = tk.Entry(self.task_frame, width=30)
        self.title_entry.grid(row=0, column=1, padx=5)

        # 期限
        self.deadline_label = tk.Label(self.task_frame, text="期限:")
        self.deadline_label.grid(row=2, column=0, sticky="w")
        self.deadline_var = tk.StringVar()
        self.deadline_entry = tk.Entry(
            self.task_frame, textvariable=self.deadline_var, width=30
        )
        self.deadline_entry.grid(row=2, column=1, padx=5)

        # ﾎﾞﾀﾝﾌﾚｰﾑ
        self.button_frame = tk.Frame(self.master)
        self.button_frame.grid(row=2, column=0, columnspan=2, pady=(10, 10))

        # 追加ﾎﾞﾀﾝ
        self.add_button = tk.Button(
            self.button_frame,
            text="追加",
            command=self.add_task_button_clicked,
            width=10,
        )
        self.add_button.pack(side=tk.LEFT, padx=5)

        # ｶﾚﾝﾀﾞｰﾎﾞﾀﾝ
        self.add_button = tk.Button(
            self.button_frame,
            text="ｶﾚﾝﾀﾞｰ",
            command=self.open_calendar,
            width=10,
        )
        self.add_button.pack(side=tk.LEFT, padx=5)

        # ﾀｽｸﾘｽﾄ
        self.task_list = tk.Listbox(self.master, width=45)
        self.task_list.grid(
            row=3, column=0, columnspan=2, padx=20, pady=(0, 20), sticky="nsew"
        )
        self.todo_list = TodoList()

        # 設定
        self.set_button_button = tk.Button(
            self.master, text="設定", width=4, height=1, command=self.open_settings
        )
        self.set_button_button.grid(row=4, column=1, padx=(0, 20), sticky="e")

    def open_calendar(self):
        # ｶﾚﾝﾀﾞｰ作成
        today = datetime.date.today()
        self.calendar = Calendar(
            self.master,
            selectmode="day",
            year=today.year,
            month=today.month,
            day=today.day,
        )
        self.calendar.grid(
            row=3, column=0, columnspan=2, padx=20, pady=(0, 20), sticky="nsew"
        )

        # 日付に設定
        self.calendar.bind("<<CalendarSelected>>", self.set_deadline)

    def set_deadline(self, _):
        self.deadline_var.set(self.calendar.selection_get().strftime("%Y-%m-%d"))
        self.calendar.destroy()

    def add_task_button_clicked(self):
        # ﾀｽｸﾘｽﾄに追加する
        task = Task(
            task_id=str(uuid.uuid4()),
            title=self.title_entry.get(),
            deadline=self.deadline_entry.get(),
            description="",
        )
        task.add_task(self.todo_list)
        self.clear_entries(self.title_entry, self.deadline_var)

    def clear_entries(self, title_entry, deadline_var):
        # 入力欄を空にする
        title_entry.delete(0, tk.END)
        deadline_var.set("")

    def open_settings(self):
        # 設定処理
        pass
