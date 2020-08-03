class Clock(object):
    def __init__(self, time):
        self.time = time
    def print_time(self):
        time = '6:30'
        print(self.time)
    def print_times(self, time):
        print(time)    
    
boston_clock = Clock('5:30')
paris_clock = boston_clock
paris_clock.time = '10:30'
boston_clock.print_time()

clock = Clock('5:30')
clock.print_time()
clock.print_times('10:30')