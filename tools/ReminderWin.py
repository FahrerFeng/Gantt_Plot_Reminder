import schedule
import time
from win10toast import ToastNotifier
import datetime
import json
import pandas as pd
import yaml


def create_timeline(json_data, job_line):
    for data in json_data:
        mission = {
            "Task": data["mission name"],
            "index": data["index"],
            "Start": data["begin-time"],
            "Finish": data["end-time"],
            "Content": data["content"],
        }
        job_line.append(mission)
        if "submission" in data and isinstance(data["submission"], list):
            create_timeline(data["submission"], job_line)


class ReminderWin:
    def __init__(self, config_file, json_path):
        # project name
        self.project_name = 'project_name'
        # early_remind_time: How many days before the start date to start sending notifications
        self.early_remind_time = 0
        # last_remind_time: How many days before the end date to stop sending notifications
        self.last_remind_time = 0
        # when should the reminder send the notification, default only on monday
        self.remind_weekdays = [1]
        # list of reminder time point
        self.remind_time_points = ['17:45']

        # Update Schedule
        with open(json_path, 'r') as f:
            json_data = json.load(f)
        mission_line = []
        create_timeline(json_data, mission_line)
        self.mission_line = pd.DataFrame(mission_line)

        # initialize all properties
        self.load_settings_from_yaml(config_file)

    def set_project_name(self, name):
        self.project_name = name

    # How many days before the start date to start sending notifications
    def set_early_remind_time(self, days):
        self.early_remind_time = days

    # How many days before the end date to stop sending notifications
    def set_last_remind_time(self, days):
        self.last_remind_time = days

    # Set the days, when should the reminder send the notification
    def set_remind_weekdays(self, days: list):
        self.remind_weekdays = days

    # Set the reminding time points
    def set_remind_time_points(self, time_points: list):
        self.remind_time_points = time_points

    def load_settings_from_yaml(self, config_file):
        with open(config_file, 'r') as f:
            settings = yaml.safe_load(f)

        if 'project_name' in settings:
            self.project_name = settings['project_name']

        if 'early_remind_time' in settings:
            self.early_remind_time = settings['early_remind_time']

        if 'last_remind_time' in settings:
            self.last_remind_time = settings['last_remind_time']

        if 'remind_weekdays' in settings:
            self.remind_weekdays = [item - 1 for item in settings['remind_weekdays']]

        if 'remind_time_points' in settings:
            self.remind_time_points = settings['remind_time_points']

    def send_notification(self, message_text):
        toaster = ToastNotifier()
        toaster.show_toast(self.project_name, message_text)

    # Set the new reminding date
    def update_mission_line(self):
        def update_dates(row):
            start_date = datetime.datetime.strptime(row['Start'], "%Y-%m-%d")
            end_date = datetime.datetime.strptime(row['Finish'], "%Y-%m-%d")

            updated_start = start_date - datetime.timedelta(days=self.early_remind_time)
            updated_end = end_date - datetime.timedelta(days=self.last_remind_time)

            row['Remind-start'] = updated_start.strftime("%Y-%m-%d")
            row['Remind-end'] = updated_end.strftime("%Y-%m-%d")

            return row

        self.mission_line = self.mission_line.apply(update_dates, axis=1)

    def check_and_send_notification(self):
        # read the current time
        current_time = datetime.datetime.now().date()
        # read the weekday of today
        current_weekday = datetime.datetime.now().weekday()
        for _, row in self.mission_line.iterrows():
            start_date = datetime.datetime.strptime(row['Remind-start'], "%Y-%m-%d").date()
            end_date = datetime.datetime.strptime(row['Remind-end'], "%Y-%m-%d").date()

            if start_date <= current_time <= end_date and current_weekday in self.remind_weekdays:
                notification_content = f"{row['Task']}\nContent: {row['Content']}\nStart: {row['Start']}\nEnd: {row['Finish']}"
                # print(notification_content)
                self.send_notification(notification_content)

    def start(self):
        self.update_mission_line()
        for item in self.remind_time_points:
            schedule.every().day.at(item).do(self.check_and_send_notification)
        while True:
            schedule.run_pending()
            time.sleep(1)
