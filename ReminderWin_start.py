
from tools.ReminderWin import *

reminder = ReminderWin('./config_yaml/reminder_config.yaml', './project_tasks_json/jobs_list.json')

reminder.start()