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
        self.thread = threading.Timer(1, self.random_change)
        self.thread.start()
        self.exitFlag = False

    def random_change(self):
        while not self.exitFlag:
            self.amount = random.randint(self.randLeft, self.randRight)
            # print(self.amount)
            time.sleep(1)
    
    def inc_change(self):
        while not self.exitFlag:
            self.amount += self.incValue
            time.sleep(1)
        

# ファイルを直接実行時のみ実行される(import DummyWatChecker.py で実行されない)
if __name__ == "__main__": 
    whole_wat_checker = DummyWatChecker(0, 1, 400, 600, 4)
    tv_wat_checker = DummyWatChecker(1, 0, 50, 100, 1)
    airCon_wat_checker = DummyWatChecker(2, 0, 50, 100, 1)
    oven_wat_checker = DummyWatChecker(3, 0, 50, 100, 1)
    stove_wat_checker = DummyWatChecker(4, 0, 50, 100, 1)
    wat_checker_list = [tv_wat_checker, airCon_wat_checker, oven_wat_checker, stove_wat_checker]

    gas_checker = DummyWatChecker(-1, 0, 100, 500, 1)
    while True:
        op = input()
        if op == "exit":
            whole_wat_checker.exitFlag = True
            for wat_checker in wat_checker_list:
                wat_checker.exitFlag = True
            gas_checker.exitFlag = True
            
            whole_wat_checker.thread.join()
            for wat_checker in wat_checker_list:
                wat_checker.thread.join()
            gas_checker.thread.join()
            break
        print("id: ",whole_wat_checker.id,", value: ",whole_wat_checker.amount)
        for wat_checker in wat_checker_list:
            ratio = wat_checker.amount / whole_wat_checker.amount
            print("id: ",wat_checker.id, ", value: ", wat_checker.amount, ", ", ratio, "%")
        print("id: ", gas_checker.id, ", value: ", gas_checker.amount)
    