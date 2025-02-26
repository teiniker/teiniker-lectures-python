from org.se.lab.date import is_leap_year

if __name__ == '__main__':
    # Verify implementation
    assert is_leap_year(2000)
    assert is_leap_year(2020)
    assert not is_leap_year(2021)
    assert not is_leap_year(2100)
