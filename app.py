import datetime
from datetime import date

today = datetime.datetime.now()
bday = datetime.datetime(2023,12,16,14,45)
time_diff = bday - today
print(f"Your birthday is in {time_diff}")
