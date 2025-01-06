class WeekDayError(Exception):
    pass


class Weeker:
    def __init__(self, day):
        self.weekdays = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
        if day not in self.weekdays:
            raise WeekDayError()
        self.day = day

    def __str__(self):
        return self.day

    def add_days(self, n):
        index = self.weekdays.index(self.day)
        new_index = (index + n) % 7
        self.day = self.weekdays[new_index]

    def subtract_days(self, n):
        index = self.weekdays.index(self.day)
        new_index = (index - n) % 7
        self.day = self.weekdays[new_index]


try:
    weekday = Weeker('Mon')
    print(weekday)
    weekday.add_days(15)
    print(weekday)
    weekday.subtract_days(23)
    print(weekday)
    weekday = Weeker('Monday')
except WeekDayError:
    print("Sorry, I can't serve your request.")
