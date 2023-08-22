from tools.Reminder import *

reminder = Reminder('./config_yaml/reminder_config.yaml', './project_tasks_json/jobs_list.json')

reminder.start()