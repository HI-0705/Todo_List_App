import tkinter as tk
from views.task_view import TaskView


def main():
    root = tk.Tk()
    TaskView(root)
    root.mainloop()


if __name__ == "__main__":
    main()
