import plotly.figure_factory as ff
import json
import pandas as pd
from datetime import datetime
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


class ScheduleViewer:
    def __init__(self, yaml_path, json_path):
        with open(json_path, 'r') as f:
            json_data = json.load(f)
        self.json_data = json_data
        self.job_line = []
        create_timeline(self.json_data, self.job_line)
        self.schedule_table = pd.DataFrame([])
        self.color_table = []
        with open(yaml_path, 'r') as f:
            color_table = yaml.safe_load(f)
        self.color_table = color_table['color_table']

    def show_gantt_chart(self):
        current_time = datetime.now()
        # 按照年、月、日的格式进行格式化
        formatted_time = current_time.strftime("%Y-%m-%d")

        # 创建一个颜色字典，将每个任务索引映射到特定颜色
        fig = ff.create_gantt(self.job_line, colors=self.color_table,
                              index_col='index', show_hover_fill=True, show_colorbar=True, showgrid_x=True,
                              group_tasks=True)
        fig.add_vline(x=formatted_time)
        fig.show()

    def show_mission_content(self):
        self.schedule_table = pd.DataFrame(self.job_line, columns=['Task', 'Content'])
        fig = ff.create_table(self.schedule_table, height_constant=20)
        fig.show()