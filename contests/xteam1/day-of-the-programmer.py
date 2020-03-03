prDay = 256


class Year:
    def __init__(self, year):
        self.year = year

    def get_dev_day(self):
        if self.is_leap(self.year):
            return '12.09.'+str(self.year)
        else:
            return '13.09.'+str(self.year)
    def is_leap(self, year):
        pass


class SwitchYear(Year):
    def get_dev_day(self):
        return '28.10.1918'

# 31 14-28 31 30  31  30  31  30  31  30
# 31 43    74 104 135 136 167 197 228 258
class JulianYear(Year):
    def is_leap(self, year):
        return year%4 == 0
    
class GeorgianYear(Year):
    def is_leap(self, year):
        if year%400 == 0:
            return True
        if year%4 == 0 and year%100 != 0:
            return True
        return False

def solve(year):
    theYear = createYear(year)
    print(theYear.get_dev_day())

def createYear(year):
    if year >=1700 and year <=1917:
        return JulianYear(year)

    if year >=1919:
        return GeorgianYear(year)

    return SwitchYear(year)

solve(2016)