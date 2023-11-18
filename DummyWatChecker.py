import time
import random
import threading



class DummyWatChecker:
    id: int
    amount: int
    def __init__(self, id: int, amount: int):
        self.id = id
        self.amount = amount

    def random_change(self):
        while True:
            self.amount = random.randint(50, 100)
            print(self.amount)
            time.sleep(3)
    
    def inc_change(self):
        while True:
            self.amount += 1
            time.sleep(3)

    def timerstart(self):
        thread = threading.Timer(1, self.random_change)
        thread.start()

wat_checker = DummyWatChecker(0, 0)
wat_checker.timerstart()
op = input()
print(wat_checker.id, wat_checker.amount)
    
        
    