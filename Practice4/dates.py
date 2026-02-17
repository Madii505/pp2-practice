from datetime import datetime, timedelta

now = datetime.now()
print("Current datetime:", now)

formatted = now.strftime("%Y-%m-%d %H:%M:%S")
print("Formatted:", formatted)

future = now + timedelta(days=7)
print("After 7 days:", future)

past = now - timedelta(days=7)
print("7 days ago:", past)

difference = future - now
print("Difference in days:", difference.days)
