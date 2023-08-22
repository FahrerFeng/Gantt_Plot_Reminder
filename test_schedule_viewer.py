from tools.ScheduleViewer import *

if __name__ == '__main__':
    input_config_path = input("Please add the path of a configuration file:")
    input_job_path = input("Please add the path of the task file:")
    # sv = ScheduleViewer('./config_yaml/schedule_viewer_config.yaml', './project_tasks_json/faps_jobs.json')
    sv = ScheduleViewer(input_config_path, input_job_path)
    sv.show_gantt_chart()
    sv.show_mission_content()
