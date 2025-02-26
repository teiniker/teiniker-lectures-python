import date

if __name__ == '__main__':
    # Verify implementation
    assert date.is_leap_year(2000)
    assert date.is_leap_year(2020)
    assert not date.is_leap_year(2021)
    assert not date.is_leap_year(2100)
