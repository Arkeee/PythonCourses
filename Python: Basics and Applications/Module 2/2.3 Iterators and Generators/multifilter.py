class multifilter:
    def judge_half(self):
        return True if self.pos >= self.neg else False

    def judge_any(self):
        return True if self.pos >= 1 else False

    def judge_all(self):
        return True if self.neg == 0 else False

    def __init__(self, lst, *funcs, judge=judge_any):
        self.iterable = lst
        self.index = 0
        self.pos = 0
        self.neg = 0
        self.judge = judge
        self.funcs = funcs

    def __iter__(self):
        return self

    def __next__(self):
        self.pos = self.neg = 0
        if self.index < len(self.iterable):
            self.index += 1
            for func in self.funcs:
                if func(self.iterable[self.index - 1]):
                    self.pos += 1
                else:
                    self.neg += 1
            if self.judge(self):
                return self.iterable[self.index - 1]
            else:
                return self.__next__()
        self.index = 0
        raise StopIteration
