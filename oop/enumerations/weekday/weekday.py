from enum import Enum

class Weekday(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7

day_map_german = {
    Weekday.MONDAY:'Montag',
    Weekday.TUESDAY:'Dienstag',
    Weekday.WEDNESDAY:'Mittwoch', 
    Weekday.THURSDAY:'Donnerstag',
    Weekday.FRIDAY:'Freitag',
    Weekday.SATURDAY:'Samstag',
    Weekday.SUNDAY:'Sonntag'
}

def print_day_german(day):
    print(day_map_german[day])

def is_working_day(day):
    if day == Weekday.MONDAY or day == Weekday.TUESDAY or day == Weekday.WEDNESDAY or day == Weekday.THURSDAY or day == Weekday.FRIDAY:
        return True
    else:
        return False


print(Weekday.TUESDAY)
print_day_german(Weekday.TUESDAY)

assert is_working_day(Weekday.WEDNESDAY)
assert is_working_day(Weekday.FRIDAY)
assert not is_working_day(Weekday.SATURDAY)
assert not is_working_day(Weekday.SUNDAY)
