

def week(i):
    switch_case={
        0:'Sunday',
        1: 'Monday',
        2: 'Tuesday',
        3: 'Wednesday',
        4: 'Thursday',
        5: 'Friday',
        6: 'Saturday'
    }
    return switch_case.get(i,"Invalid day of week")
print(week(7))