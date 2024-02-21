import datetime

currentDataTime = datetime.datetime.now()

CurrentDataTimeDropMicroSeconds = currentDataTime.replace(microsecond=0)

print(CurrentDataTimeDropMicroSeconds)









