import os
from datetime import datetime, timedelta

def get_monday_date():
    today = datetime.today()
    start = today - timedelta(days=today.weekday())
    return start

def get_sunday_date(start):
    end = start + timedelta(days=6)
    return end

def generate_filename(start, end):
    start_date_str = start.strftime("%A, %B %d")
    end_date_str = end.strftime("%A, %B %d")
    filename = f"{start_date_str} - {end_date_str}.txt"
    return filename

def file_exists(filename):
    return os.path.isfile(os.path.join('Results', filename))

def read_data(file_path):
    with open(file_path, 'r') as file:
        data = file.readlines()
    return data

def summarize_data(data):
    summary = ""
    for item in data:
        # Assuming item is a tuple with the format (time, importance, name, actual, forecast, prior, source)
        time, importance, name, actual, forecast, prior, source = item.strip().split(',')
        summary += f"{time} - {importance} - {name} - {actual} - {forecast} - {prior} - {source}\n"
    return summary

def save_summary(summary, file_path):
    with open(file_path, 'w') as file:
        file.write(summary)

if __name__ == "__main__":
    start_date = get_monday_date()
    end_date = get_sunday_date(start_date)
    filename = generate_filename(start_date, end_date)

    if file_exists(filename):
        print(f"The report for the week {filename} already exists.")
    else:
        data = read_data('economic_data.txt')
        summary = summarize_data(data)
        save_summary(summary, os.path.join('Results', filename))
        print(f"The report for the week {filename} has been created.")