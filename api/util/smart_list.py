from typing import Callable


class SmartList(list):
    cur_pos = 0

    def find(self, func: Callable):
        length = len(self)
        for i in range(length):
            item = self[(self.cur_pos + i) % length]
            if func(item):
                self.cur_pos = (self.cur_pos + i) % length
                return item
        raise IndexError
