# -*- coding: utf-8 -*-
"""Модуль логики и классов управления задачами."""

import json


class Task:
    """Класс, описывающий отдельную задачу."""

    def __init__(self, title: str, description: str, due_date: str):
        """Инициализация задачи.

        :param title: Название задачи
        :param description: Описание задачи
        :param due_date: Срок выполнения
        """
        self.title = title
        self.description = description
        self.due_date = due_date


class TaskManager:
    """Класс для управления списком задач и файловыми операциями."""

    def __init__(self, filename: str = "tasks.json"):
        """Инициализация менеджера задач."""
        self.filename = filename
        self.tasks = []
        self.load_from_file()

    def add_task(self, task: Task):
        """Добавление задачи в список и сохранение."""
        self.tasks.append(task)
        self.save_to_file()

    def delete_task(self, index: int):
        """Удаление задачи по индексу."""
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
            self.save_to_file()

    def save_to_file(self):
        """Сохранение задач в JSON-файл."""
        data = [
            {
                "title": task.title,
                "description": task.description,
                "due_date": task.due_date,
            }
            for task in self.tasks
        ]
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    def load_from_file(self):
        """Загрузка задач из JSON-файла."""
        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                data = json.load(f)
                self.tasks = [
                    Task(item["title"], item["description"], item["due_date"])
                    for item in data
                ]
        except (FileNotFoundError, json.JSONDecodeError):
            self.tasks = []