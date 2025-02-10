import os
import investpy
import pandas as pd
from datetime import datetime, timedelta

def fetch_economic_calendar(from_date, to_date):
    """Fetch economic calendar data for the given date range."""
    try:
        data = investpy.economic_calendar(from_date=from_date, to_date=to_date)
        return data
    except Exception as e:
        print(f"Error fetching data: {e}")
        return None

def save_data_to_csv(data, file_path):
    """Save the fetched data to a CSV file."""
    try:
        df = pd.DataFrame(data)
        df.to_csv(file_path, index=False)
        print(f"Data saved to {file_path}")
    except Exception as e:
        print(f"Error saving data to file: {e}")

def generate_filename():
    """Generate filename based on current date."""
    today = datetime.today()
    filename = today.strftime("%Y%m%d") + '_economic_calendar.xlsx'
    return filename

def file_exists(filename):
    """Check if the file exists in the Results folder."""
    return os.path.isfile(os.path.join('Results', filename))

def summarize_data(data):
    """Summarize the data as needed."""
    summary = data
    return summary

def save_summary_to_excel(summary, file_path):
    """Save the summary data to an Excel file."""
    try:
        summary.to_excel(file_path, index=False)
        print(f"Summary saved to {file_path}")
    except Exception as e:
        print(f"Error saving summary to Excel: {e}")

if __name__ == "__main__":
    from_date = '01/01/2020'
    to_date = '02/10/2025'
    csv_file_path = 'economic_data.csv'
    results_folder = 'Results'
    
    # Ensure the Results folder exists
    os.makedirs(results_folder, exist_ok=True)

    # Fetch and save economic calendar data
    data = fetch_economic_calendar(from_date, to_date)
    if data is not None:
        save_data_to_csv(data, csv_file_path)

        # Generate filename for the summary report
        summary_filename = generate_filename()
        summary_file_path = os.path.join(results_folder, summary_filename)

        if file_exists(summary_file_path):
            print(f"The report for the date {summary_filename} already exists.")
        else:
            # Read data from CSV file
            df = pd.read_csv(csv_file_path)
            # Summarize data
            summary = summarize_data(df)
            # Save summary to Excel file in Results folder
            save_summary_to_excel(summary, summary_file_path)
            print(f"The report for the date {summary_filename} has been created.")