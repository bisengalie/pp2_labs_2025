from datetime import datetime, timedelta
#1 subtract five days
current_date = datetime.now()
new_date = current_date - timedelta(days=5)
print("Date after subtracting 5 days:", new_date.strftime("%Y-%m-%d"))

#2 print today,yesterday,tomorrow
today = datetime.now()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)

print("Yesterday:", yesterday.strftime("%Y-%m-%d"))
print("Today:", today.strftime("%Y-%m-%d"))
print("Tomorrow:", tomorrow.strftime("%Y-%m-%d"))

#3 drop microseconds
now = datetime.now()
now_without_microseconds = now.replace(microsecond=0)
print("Datetime without microseconds:", now_without_microseconds)


#4 calculate difference between two dates in seconds
date1 = datetime(2024, 2, 15, 12, 0, 0)  # Example date
date2 = datetime(2024, 2, 20, 14, 30, 0) # Another example date

difference = abs((date2 - date1).total_seconds())
print("Difference in seconds:", difference)