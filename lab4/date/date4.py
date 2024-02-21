import datetime

date1 = datetime.datetime(2023, 6, 15, 8, 20, 0)
date2 = datetime.datetime(2023, 6, 10, 10, 30, 0)

difference = date1 - date2

differenceInSeconds = difference.total_seconds()

print("Difference in seconds:", differenceInSeconds)
