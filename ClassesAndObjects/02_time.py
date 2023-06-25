class Time:
    max_hours = 23
    max_minutes = 59
    max_seconds = 59

    def __init__(self, hours, minutes, seconds):
        self.set_time(hours, minutes, seconds)

    def set_time(self, hours, minutes, seconds):
        if 0 <= hours <= self.max_hours and 0 <= minutes <= self.max_minutes and 0 <= seconds <= self.max_seconds:
            self.hours = hours
            self.minutes = minutes
            self.seconds = seconds
        else:
            raise ValueError("Invalid time values.")

    def get_time(self):
        return f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"

    def next_second(self):
        self.seconds += 1
        self.update_time()
        return self.get_time()

    def update_time(self):
        if self.seconds > self.max_seconds:
            self.seconds = 0
            self.minutes += 1
            if self.minutes > self.max_minutes:
                self.minutes = 0
                self.hours += 1
                if self.hours > self.max_hours:
                    self.hours = 0

time = Time(23, 59, 59)
print(time.get_time())
print(time.next_second())