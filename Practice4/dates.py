from datetime import datetime, timedelta

# Subtract five days
print("Five days ago:", datetime.now() - timedelta(days=5))

# Yesterday, today, tomorrow
today = datetime.now()
print("Yesterday:", today - timedelta(days=1))
print("Today:", today)
print("Tomorrow:", today + timedelta(days=1))

# Drop microseconds
print("Without microseconds:", today.replace(microsecond=0))

# Difference between two dates in seconds
date1 = datetime(2025, 1, 1)
date2 = datetime(2025, 1, 10)
diff = (date2 - date1).total_seconds()
print("Difference in seconds:", diff)