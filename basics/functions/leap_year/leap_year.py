def is_leap_year(year:int)->bool:
    """Check if a given year is a leap year or not."""
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


if __name__ == '__main__':

    # Verify implementation
    assert is_leap_year(2000)
    assert is_leap_year(2020)
    assert not is_leap_year(2021)
    assert not is_leap_year(2100)
