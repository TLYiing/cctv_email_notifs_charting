import pandas as pd
import numpy as np
import os
import re
import seaborn as sns
import datetime as dt
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter

cwd = os.getcwd()
input_folder = cwd+"\\INPUT"
os.chdir(input_folder)

# Function to get user input for date range
def filter_data(data, usr_input_start, usr_input_end):
    date_format = "%d/%m/%Y"
    
    start_date = dt.datetime.strptime(usr_input_start, date_format)
    end_date = dt.datetime.strptime(usr_input_end, date_format) + pd.Timedelta(days=1)

    data_filt = data[(data['EVENT TIME']>=start_date)&(data['EVENT TIME']<=end_date)]
    return data_filt

# Function to extract information using regular expressions and convert event time to datetime
def extract_info(text):
    event_type = re.search(r'EVENT TYPE:\s+(\w+)', text)
    if event_type:
        event_type = event_type.group(1)
   
    event_time = re.search(r'EVENT TIME:\s+([\d\-,:]+)', text)
    if event_time:
        event_time = event_time.group(1)
        event_time = dt.datetime.strptime(event_time, '%Y-%m-%d,%H:%M:%S')  # Convert event time to datetime object

    nvr_name = re.search(r'NVR NAME:\s+([\w]+)', text)
    if nvr_name:
        nvr_name = nvr_name.group(1)
    camera_name_num = re.search(r'CAMERA NAME\(NUM\):\s+([.\w\s\(\)]+)', text)
    if camera_name_num:
        camera_name_num = camera_name_num.group(1).strip()
        camera_name, camera_num = map(str.strip, camera_name_num.split('(',1))
        camera_num = camera_num.strip(')')
    else:
        camera_name = None
        camera_num = None

    return event_type, event_time, nvr_name, camera_name, camera_num

# Function to get user input for date range
def get_usr_date_range():
    # date_format = "%d/%m/%Y"
    date_pattern = r'^\d{2}/\d{2}/\d{4}$'
    usr_input_start = input("Input the START date range as DD/MM/YYYY\n(for visualisation)")
    # Validate input format
    if not re.match(date_pattern, usr_input_start):
        usr_input_start = input("Invalid date format. Please enter the START date in DD/MM/YYYY format.")

    usr_input_end = input("Input the END date range as DD/MM/YYYY\n(for visualisation)")

    if not re.match(date_pattern, usr_input_end):
        usr_input_end = ("Invalid date format. Please enter the END date in DD/MM/YYYY format.")

    return (usr_input_start, usr_input_end)


# Plot each day's data in a separate subplot
def plot_graphs(data_filt, vsl_name):
   for i, (date, day_data) in enumerate(data_filt.groupby(data_filt['EVENT TIME'].dt.date)):
      day_data = pd.DataFrame(day_data)
      print(date)
      activity_counts =day_data.groupby('CAMERA NUM').resample('5T', on='EVENT TIME').count().reset_index(level='CAMERA NUM', names='camnum')
      camera_nums = activity_counts['camnum'].unique()
      print(camera_nums)


      # Formatting the plot
      plt.figure(figsize=(15,6))
      plt.xlabel('Date/Time', fontsize=20)
      plt.ylabel('Number of Activities',fontsize=20)
      plt.title('Number of Activities Each 5 Minutes Throughout the Day - '+vsl_name,fontsize=25)
      plt.grid(True)
      plt.tight_layout()

      # Plot using seaborn
      sns.lineplot(data=activity_counts, x='EVENT TIME', y='Body', hue='camnum', style='camnum', markers=True)

   # # Set plot axis
      ax = plt.gca()
      start_time = dt.datetime.combine(date, dt.time(0, 0, 0))
      end_time = dt.datetime.combine(date, dt.time(23,59,59))
      ax.set_xlim([start_time, end_time])
      # ax.set_ylim([0,5])
      date_format = DateFormatter('%d-%m/%H:%M')
      ax.xaxis.set_major_formatter(date_format)   


      # Rotate x-axis labels for better readability
      plt.xticks(rotation=30, fontsize=15)
      plt.yticks(fontsize=15)
      plt.legend(title="Camera Channel", loc = "upper left", fontsize = 15, title_fontsize='xx-large')
      plt.show()
      plt.close()

def main():
    usr_input_start, usr_input_end = get_usr_date_range()
    for vsl_name in ["Athenia", "Metis"]:
        filename = vsl_name+" CCTV.csv"
        df_raw = pd.read_csv(filename)
        data = df_raw[["Body"]].copy()
        # Apply the function to extract information
        data['EVENT TYPE'], data['EVENT TIME'], data['NVR NAME'], data['CAMERA NAME'], data['CAMERA NUM'] = zip(*data['Body'].apply(extract_info))
        data_filt = filter_data(data, usr_input_start, usr_input_end)
        plot_graphs(data_filt, vsl_name)

main()