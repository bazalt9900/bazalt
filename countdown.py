"""
===========================================
NEW YEAR COUNTDOWN
===========================================
Counts days, hours, and minutes until New Year 2027.
Just run: python countdown.py

Example output:
=== COUNTDOWN TO NEW YEAR 2027 ===
147 days, 3 hours, 12 minutes left!
===========================================
"""

from datetime import datetime

target_date = datetime(2027, 1, 1, 0, 0, 0)
now = datetime.now()
difference = target_date - now

days = difference.days
hours = difference.seconds // 3600
minutes = (difference.seconds % 3600) // 60

print("=== COUNTDOWN TO NEW YEAR 2027 ===\n")
print(f"{days} days, {hours} hours, {minutes} minutes left!")
print("\nTime is ticking...")