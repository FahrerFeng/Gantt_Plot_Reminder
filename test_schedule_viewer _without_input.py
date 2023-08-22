from tools.ScheduleViewer import *

if __name__ == '__main__':
    sv = ScheduleViewer('./config_yaml/schedule_viewer_config.yaml', './project_tasks_json/jobs_list.json')
    sv.show_gantt_chart()
    sv.show_mission_content()
