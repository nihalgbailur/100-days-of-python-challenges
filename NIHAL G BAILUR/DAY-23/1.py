def is_leap(year):
    """Return True for leap years, False otherwise."""
    return (
        year % 4  == 0 and
        (year % 100 != 0 or year % 400 == 0)
    )

def days_in_month(year, month):
    """Return number of days in that month of that year."""
    # Guard against invalid month numbers
    if not 1 <= month <= 12:
        return 'Invalid Month'

    # Handle February in a leap year
    if month == 2 and is_leap(year):
        return 29

    # A lookup for all other months
    month_days = {
        1: 31,  2: 28,  3: 31,  4: 30,
        5: 31,  6: 30,  7: 31,  8: 31,
        9: 30, 10: 31, 11: 30, 12: 31
    }
    return month_days[month]

print(days_in_month(2017, 2))  # → 28
