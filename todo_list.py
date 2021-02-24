import os

import pandas as pd

TODO_DIR = 'data/todo_lists'


class Todo:
    def __init__(self, name):
        self.name = name
        self.todo_df = pd.DataFrame(index=['name', 'complete', 'user_added', 'notes', 'date_added', 'date_completed',
                                           'tags'])

    def save(self):
        self.todo_df.to_pickle(os.path.join(TODO_DIR, f'{self.name}.todo'))
    def load