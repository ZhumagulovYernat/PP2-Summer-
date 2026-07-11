from datetime import datetime, timedelta


today = datetime.now()

five_days_ago = today - timedelta(days=5)

print("Current date:", today)
print("Five days ago:", five_days_ago)


yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)

print("Yesterday:", yesterday.date())
print("Today:", today.date())
print("Tomorrow:", tomorrow.date())


date_with_microseconds = datetime.now()

without_microseconds = date_with_microseconds.replace(microsecond=0)

print("With microseconds:", date_with_microseconds)
print("Without microseconds:", without_microseconds)


date1 = datetime(2026, 7, 11, 12, 0, 0)
date2 = datetime(2026, 7, 10, 12, 0, 0)

difference = date1 - date2

print("Difference in seconds:", difference.total_seconds())