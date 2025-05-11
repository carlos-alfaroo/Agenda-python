class Person:
    #Constructor
    def __init__(self, firstName = "Not defined", lastName = "Not defined", age = 1):
        self.FirstName = firstName
        self.LastName = lastName
        self.Age = age

    #getters
    @property
    def FirstName(self): return self._firstName
    @property
    def LastName(self): return self._lastName
    @property
    def Age(self): return self._age

    #setters
    @FirstName.setter
    def FirstName(self, firstName):
        self._firstName = firstName if (firstName != "") else "Not defined"
    @LastName.setter
    def LastName(self, lastName):
        self._lastName = lastName if (lastName != "") else "Not defined"
    @Age.setter
    def Age(self, age):
        self._age = age if (age > 0 and age < 130) else 1

    #methods
    def toString(self):
        return f"First name: {self._firstName}     Last name: {self._lastName}      Age: {self._age}"