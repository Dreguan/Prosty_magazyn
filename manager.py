class NotEnoughDataException(Exception):
    pass

class NotEnoughMoneyException(Exception):
    pass

class NotEnoughStockException(Exception):
    pass

class NoActionException(Exception):
    pass

class NotEnoughParametersException(Exception):
    pass

class Manager:
    def __init__(self, reader):
        self.reader = reader
        self.history = []
        self.account = 0
        self.stock = {}
        self.actions = {}

    def modify_account(self, value):
        if self.account + value < 0:
            raise NotEnoughMoneyException()
        self.account += value

    def add_history(self, row):
        self.history.append(row)

    def modify_stock(self, item, qty):
        if item not in self.stock:
            self.stock[item] = 0
        if self.stock[item] + qty < 0:
            raise NotEnoughStockException()
        self.stock[item] += qty

    def action(self, name, parameters):
        def action_in(callback):
            self.actions[name] = (parameters, callback)
        return action_in

    def process(self):
        while True:
            action = self.reader.get_line()[0]
            if action == "stop":
                break
            if action not in self.actions:
                raise NoActionException()
            parameters, callback = self.actions[action]
            rows = self.reader.get_line(parameters)
            if callback(self, rows):
                self.add_history([action] + rows)

    def process_action(self, action, rows):
        parameters, callback = self.actions[action]
        if len(rows) != parameters:
            raise NoActionException()
        if callback(self, rows):
            self.add_history([action] + rows)

    def review(self, start, end):
        return self.history[int(start):int(end)]

    def save(self):
        self.reader.writer(self.history)


class Reader:
    def __init__(self, path):
        self.pathfile = path
        self.file = open(path)

    def get_line(self, count=1):
        countlist = []
        for i in range(count):
            readline = self.file.readline()
            if not readline:
                raise NotEnoughDataException("Za mało danych w pliku")
            countlist.append(readline.strip())
        return countlist

    def writer(self, history):
        self.file.close()
        with open("in.txt", "w") as f:
            for row in history:
                f.write("\n".join(row) + "\n")
            f.write("stop\n")
        self.file = open(self.pathfile)

