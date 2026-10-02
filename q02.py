class Counter:
    def __init__(self):
        self.counter=0
    def increment(self):
        self.counter+=1
    def deccrement(self):
        if self.counter <=0:
            raise ValueError("Counter can't be less than 0")
        self.counter-=1
    def reset(self):
        self.counter=0
    def get_value(self):
        print(self.counter)

counter_1=Counter()
counter_1.increment()
counter_1.increment()
counter_1.increment()
counter_1.deccrement()
counter_1.deccrement()
counter_1.increment()
counter_1.get_value()
counter_1.reset()
counter_1.get_value()