from datetime import datetime, timedelta
today_date=input("What is todays date? (YYYY-MM-DD): ")
try:
    today_date=datetime.strptime(today_date, "%Y-%m-%d")
    tomorrow_date= today_date + timedelta(days=1)
    real_tomorrow_date=tomorrow_date.strftime("%Y-%m-%d")
    print("Next date:",real_tomorrow_date)
except: print("Input format ERROR. Correct Format: YYYY-MM-DD")