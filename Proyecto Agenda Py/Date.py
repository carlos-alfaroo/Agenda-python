class Date:
    #Constructor
    def __init__(self, day = 1, month = 1, year = 1900):
        self.Year = year
        self.Month = month
        self.Day = day
    
    #getters
    @property
    def Year(self): return self._year
    @property
    def Month(self): return self._month
    @property
    def Day(self): return self._day
    
    #setters
    @Year.setter
    def Year(self, year):
        self._year = year if (year >= 1900) else 1900
    @Month.setter
    def Month(self, month):
        self._month = month if (month > 0 and month < 13) else 1
    @Day.setter
    def Day(self, day):
        maxDay = 0
        if (self._month == 1 or self._month == 3 or self._month == 5 or self._month == 7 or self._month == 8 or self._month == 10 or self._month == 12):
            maxDay = 31
        else:
            if(self._month == 4 or self._month == 6 or self._month == 9 or self._month == 11):
                maxDay = 30
            else:
                if (self.leapYear()):
                    maxDay = 29
                else: 
                    maxDay = 28
        self._day = day if (day > 0 and day <= maxDay) else 1

    #methods
    def toString(self):
        DD = MM = YYYY = None
        DD = f"0{self._day}" if (self._day < 10) else f"{self._day}"
        MM = f"0{self._month}" if (self._month < 10) else f"{self._month}"
        #YYYY = f"self._year:04d
        if(self._year < 10):
            YYYY = f"000{self._year}"
        else:
            if(self._year < 100): YYYY = f"00{self._year}"
            else:
                if(self._year < 1000): YYYY = f"0{self._year}"
                else: YYYY = f"{self._year}"
        
        return f"{DD}/{MM}/{YYYY}"
    
    #year increment
    def incYear(self): self._year += 1
    #month increment
    def incMonth(self):
        self._month += 1
        if (self._month > 12):
            self._month = 1
            self.incYear()
    #day increment
    def incDay(self):
        self._day += 1
        maxDay = None
        if(self._month == 1  or self._month == 3 or self._month == 5 or self._month == 7 or self._month == 8 or self._month == 10 or self._month == 12):
            maxDay = 31
        else:
            if(self._month == 4 or self._month == 6 or self._month == 9 or self._month == 11):
                maxDay = 30
            else: 
                if(self.leapYear()): maxDay = 29
                else: maxDay = 28
        if(self._day > maxDay):
            self._day = 1
            self.incMonth()

    #year decrement
    def decYear(self): 
        self._year -= 1
        if(self._year < 1900):
            self._year = 1900
            print("Year can not be less than 1900.")    
    
    #month decrement
    def decMonth(self):
        self._month -= 1
        if(self._month < 1): 
            self._month = 12
            self.decYear()

    #day decrement
    def decDay(self):
        self._day -= 1
        maxDay = None
        if(self._month == 1  or self._month == 3 or self._month == 5 or self._month == 7 or self._month == 8 or self._month == 10 or self._month == 12):
            maxDay = 31
        else:
            if(self._month == 4 or self._month == 6 or self._month == 9 or self._month == 11):
                maxDay = 30
            else: 
                if(self.leapYear()): maxDay = 29
                else: maxDay = 28
        if(self._day < 1):
            self._day = maxDay
            self.decMonth()

    #Leap Year function
    def leapYear(self):
        return (self._year % 4 == 0 and (self._year % 100 != 0 or self._year % 400 == 0))