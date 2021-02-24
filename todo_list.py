import os
from datetime import datetime

import pandas as pd
pd.set_option('display.width', 1000)
pd.set_option('display.max_columns', 1000)
TODO_DIR = 'data/todo_lists'
if not os.path.exists(TODO_DIR):
    os.makedirs(TODO_DIR)

PROG_NEW = 0
PROG_STARTED = 1
PROG_MOST = 2
PROG_DONE = 3


class Todo:
    def __init__(self, name):
        self.name = name
        self.filepath = os.path.join(TODO_DIR, f'{self.name}.todo')
        self.todo_df = pd.DataFrame()
        self.load()

    def save(self):
        self.todo_df.to_pickle(self.filepath)

    def load(self):
        try:
            self.todo_df = pd.read_pickle(self.filepath)
        except FileNotFoundError as e:
            self.todo_df = pd.DataFrame(
                columns=['name', 'progress', 'user_added', 'notes', 'date_added', 'date_completed',
                       'tags'])
            self.save()

    def add_todo(self, name, **kwargs):
        progress = kwargs.pop('progress', PROG_NEW)
        self.todo_df = self.todo_df.append({'name': name, 'progress':progress, **kwargs}, ignore_index=True)


if __name__ == '__main__':
    test_list = Todo('test')
    test_list.add_todo('Make todo list bot', progress=1, notes="Make this bot actually record todo lists and shit.",
                       date_added=datetime.now(), tags=['programming', 'organisation', 'discord-bot'])
    test_list.save()

