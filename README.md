# Gantt_Plot_Reminder
This project works on drawing a Gantt chart of the project and sending reminders to the user at specific times.
## Pre-requirements
The "environment.yml" file describes all the libraries used in this gantt_plot_reminder project. If you have already installed anaconda, you can easily create a new virtual environment by typing the following command in anaconda prompt:
```
conda env create -f environment.yml
```
**Before typing this command, make sure that your anaconda prompt has opened the right path, where environment.yml is saved!**

## Data Type
Your task list must be saved as a json file under folder "project_task_json". The file "jobs_lists.json" shows a basic data structure to plot the gantt chart and can also be used for the reminder function. A base json structure for this project is given as:
```
  {
    "mission name": ...,
    "index": ...,
    "begin-time": "YYYY-MM-DD",
    "end-time": "YYYY-MM-DD",
    "content": ...,
    "submission": [
      {
        "mission name": ...,
        "index": ...,
        "begin-time": "YYYY-MM-DD",
        "end-time": "YYYY-MM-DD",
        "content": ...,
        "submission": []
      },
```
You can add any other keys according to your requirement. However, please don't delete any keys in the example. Otherwise, it may cause a compile error. 

