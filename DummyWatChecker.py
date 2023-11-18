import time
import random
import threading



class DummyWatChecker:
    def __init__(self, id: int, amount: int, randLeft: int, randRight: int, incValue: int):
        self.id = id
        self.amount = amount
        self.randLeft = randLeft
        self.randRight = randRight
        self.incValue = incValue
        self.timerstart()

    def random_change(self):
        while True:
            self.amount = random.randint(self.randLeft, self.randRight)
            print(self.amount)
            time.sleep(10)
    
    def inc_change(self):
        while True:
            self.amount += self.incValue
            time.sleep(10)

    def timerstart(self):
        thread = threading.Timer(1, self.random_change)
        thread.start()

whole_wat_checker = DummyWatChecker(0, 1, 400, 600, 4)
tv_wat_checker = DummyWatChecker(1, 0, 50, 100, 1)
airCon_wat_checker = DummyWatChecker(2, 0, 50, 100, 1)
oven_wat_checker = DummyWatChecker(3, 0, 50, 100, 1)
stove_wat_checker = DummyWatChecker(4, 0, 50, 100, 1)
wat_checker_list = [tv_wat_checker, airCon_wat_checker, oven_wat_checker, stove_wat_checker]

gas_checker = DummyWatChecker(-1, 0, 100, 500, 1)

    
while True:
    input()
    print("id: " + whole_wat_checker.id + ", value: " + whole_wat_checker.amount)
    for wat_checker in wat_checker_list:
        ratio = wat_checker.amount / whole_wat_checker.amount
        print("id: " + wat_checker.id + ", value: " + wat_checker.amount + ", " + ratio + "%")
    print("id: " + gas_checker.id + ", value: " + gas_checker.amount)
    