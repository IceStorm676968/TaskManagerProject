# -*- coding: utf-8 -*-
"""Модуль графического интерфейса приложения."""

import tkinter as tk
from tkinter import messagebox
from classes import Task, TaskManager


class TaskManagerApp:
    """Класс GUI для управления задачами."""

    def __init__(self, root: tk.Tk):
        self.manager = TaskManager()
        self.root = root
        self.root.title("Менеджер задач")
        self.root.geometry("450x400")
        self.setup_ui()

    def setup_ui(self):
        """Создание элементов интерфейса."""
        # Поля ввода
        tk.Label(self.root, text="Название:").grid(
            row=0, column=0, sticky="w", padx=10, pady=5
        )
        self.title_entry = tk.Entry(self.root, width=35)
        self.title_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(self.root, text="Описание:").grid(
            row=1, column=0, sticky="nw", padx=10, pady=5
        )
        self.desc_text = tk.Text(self.root, height=4, width=26)
        self.desc_text.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(self.root, text="Срок (ГГГГ-ММ-ДД):").grid(
            row=2, column=0, sticky="w", padx=10, pady=5
        )
        self.date_entry = tk.Entry(self.root, width=35)
        self.date_entry.grid(row=2, column=1, padx=10, pady=5)

        # Кнопки
        btn_frame = tk.Frame(self.root)
        btn_frame.grid(row=3, column=0, columnspan=2, pady=10)

        tk.Button(
            btn_frame,
            text="Добавить задачу",
            command=self.add_task,
            bg="#e1e1e1",
            width=15,
        ).pack(side="left", padx=5)
        tk.Button(
            btn_frame,
            text="Удалить задачу",
            command=self.delete_task,
            bg="#e1e1e1",
            width=15,
        ).pack(side="left", padx=5)

        # Список задач
        self.tasks_listbox = tk.Listbox(self.root, width=55, height=10)
        self.tasks_listbox.grid(
            row=4, column=0, columnspan=2, padx=10, pady=10
        )
        self.update_listbox()

    def add_task(self):
        """Обработка добавления задачи."""
        title = self.title_entry.get().strip()
        description = self.desc_text.get("1.0", tk.END).strip()
        due_date = self.date_entry.get().strip()

        if title and description and due_date:
            task = Task(title, description, due_date)
            self.manager.add_task(task)
            self.update_listbox()
            self.clear_inputs()
        else:
            messagebox.showwarning("Ошибка", "Заполните все поля!")

    def delete_task(self):
        """Обработка удаления выбранной задачи."""
        selected = self.tasks_listbox.curselection()
        if selected:
            self.manager.delete_task(selected[0])
            self.update_listbox()
        else:
            messagebox.showwarning(
                "Предупреждение", "Выберите задачу из списка!"
            )

    def update_listbox(self):
        """Обновление списка задач в интерфейсе."""
        self.tasks_listbox.delete(0, tk.END)
        for task in self.manager.tasks:
            self.tasks_listbox.insert(
                tk.END, f"{task.title} (до {task.due_date})"
            )

    def clear_inputs(self):
        """Очистка полей ввода."""
        self.title_entry.delete(0, tk.END)
        self.desc_text.delete("1.0", tk.END)
        self.date_entry.delete(0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManagerApp(root)
    root.mainloop()