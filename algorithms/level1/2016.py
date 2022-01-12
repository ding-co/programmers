from datetime import datetime
def solution(a, b):
    week = "MON TUE WED THU FRI SAT SUN".split()
    return week[datetime(2016, a, b).weekday()]

# Other solution
# def solution(a, b):
#     week_day = ["THU", "FRI", "SAT", "SUN", "MON", "TUE", "WED"]
#     mon = [31, 29, 31, 30, 31, 30 , 31, 31, 30, 31, 30, 31]
#     return week_day[sum(mon[:a - 1], b) % 7]
    