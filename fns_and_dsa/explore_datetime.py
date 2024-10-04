from datetime import datetime, date, timedelta

def display_current_datetime():
    current_date = datetime.now()
    current_date = current_date.strftime("%Y-%m-%d %H:%M:%S") 
    return f"Current date and time: {current_date}"

current_date = display_current_datetime()
print(current_date)

number_of_days = int(input("Enter the number of days to add to the current date: "))

def calculate_future_date():
    current_date = date.today()
    future_date = current_date + timedelta(days=number_of_days)
    future_date = future_date.strftime("%Y-%m-%d") 
    print(f"Future date: {future_date}")

calculate_future_date()