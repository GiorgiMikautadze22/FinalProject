class Timer:
    def __init__(self, hour = 0, minute = 0, second = 0):
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        return f"{str(self.hour).zfill(2)}:{str(self.minute).zfill(2)}:{str(self.second).zfill(2)}"

    def next_second(self):
        self.second += 1
        if self.second == 60:
            self.second = 0
            self.minute += 1
            if self.minute == 60:
                self.minute = 0
                self.hour += 1
                self.hour %= 24

    def prev_second(self):
        self.second -= 1
        if self.second < 0:
            self.second = 59
            self.minute -= 1
            if self.minute < 0:
                self.minute = 59
                self.hour -= 1
                self.hour %= 24

timer = Timer(23, 59, 59)
print(timer)
timer.next_second()
print(timer)
timer.prev_second()
print(timer)
