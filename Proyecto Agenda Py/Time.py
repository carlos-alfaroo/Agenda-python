class Time:
    # Constructor 
    def __init__(self, hour = 0, minute = 0, second = 0):
        self.Hour = hour
        self.Minute = minute
        self.Second = second

    # Getters
    @property
    def Hour(self): return self._hour
    @property
    def Minute(self): return self._minute
    @property
    def Second(self): return self._second
    
    # Setters
    @Hour.setter
    def Hour(self, value): self._hour = value if (value >= 0 and value < 24) else 0
    @Minute.setter
    def Minute(self, value): self._minute = value if (value >= 0 and value < 60) else 0
    @Second.setter
    def Second(self, value): self._second = value if (value >= 0 and value < 60) else 0

    # Methods
    def toString(self): return f"{self._hour:02}/{self._minute:02}/{self._second:02}"

    # inc hour
    def incHour(self):
        self._hour += 1
        if self._hour > 23:
            self._hour = 0
    # inc minute
    def incMinute(self):
        self._minute += 1
        if self._minute > 59:
            self._minute = 0
            self.incHour()
    # inc second
    def incSecond(self):
        self._second += 1
        if self._second > 59:
            self._second = 0 
            self.incMinute()
    # dec hour
    def decHour(self):
        self._hour -= 1
        if self._hour < 0:
            self._hour = 23
    # dec minute
    def decMinute(self):
        self._minute -= 1
        if self._minute < 0:
            self._minute = 59
            self.decHour()
        
    #dec second
    def decSecond(self):
        self._second -= 1
        if self._second < 0:
            self._second = 59
            self.decMinute()
