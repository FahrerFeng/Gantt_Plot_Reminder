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
    "mission name": ,
    "index":  ,
    "begin-time": "YYYY-MM-DD",
    "end-time": "YYYY-MM-DD",
    "content": ,
    "submission": [
      {
        "mission name": ,
        "index": ,
        "begin-time": "YYYY-MM-DD",
        "end-time": "YYYY-MM-DD",
        "content": ,
        "submission": []
      },
```
The key "index" is used to set the level of a task and also denotes the color to plot. You can add any other keys according to your requirement. However, please don't delete any keys in the example. Otherwise, it may cause a compile error. 

The configuration of plotting and reminder function are saved in "schedule_viewer_config.yaml" and "reminder_config.yaml". The explaination of each parameter is given as a comment upon the value.

## Plot Gantt Chart
Run "test_schedule_viewer_without_input.py" and then you can see the plot. You can also use pyinstaller library to pack this function into a .exe file. In this case, use the followiing command in your anaconda prompt or cmd:
```
pyinstaller -w -F test_schedule_viewer.py
```
After running this command, you will get a .exe file in folder "dist". The python file "test_schedule_viewer.py" offer you a flexible way by given the certain paths of the configuration file "schedule_viewer_config.yaml" and your task list (.json) file. **Don't give the relative paths. Otherwise, compile errors!**

## Task Reminder
The reminder function is realized in "Reminder_start.py" and "ReminderWin_start.py". The "Reminder_start.py" sends the notification using a window. The "ReminderWin_start.py" sends as a windows notification, which may take place on the lower right corner of your screen. The "ReminderWin_start.py" may send some warnings or errors in you prompt. It is the problem of win10toast library, which are not solved yet. However, those warning tips will not break the program. Therefore, please ignore them :) .

The "reminder_config.yaml" contains all the parameter of the reminder. You can set the date, time, even time periode to send the notification. All the parameters are explained in its comment.

My final propose is to implement a real-time notification feature. If this function is packaged as an exe, the task list must be packaged within this exe too. However, the task list is updated irregularly. To solve this problem, I utilize the windows batch operation. You can create a batch file using the following code:
```
CALL <path of your anaconda activate.bat> <path of the "AnacondaFile" folder>

CALL conda activate gantt

cd <path, where you save the codes of this project>
python <ReminderWin_start.py or Reminder_start.py>
```
The "activate.bat" is saved under \Anaconda\AnacondaFile\Scripts. You only need to find your anaconda install path. 

After doing this， you can set this batch file as a boot startup item. Furthermore, after changing the json file, please restart batch too. I'm thinking of having the program re-read the json file in a certain frequency, so that we don't have to manually restart or wait until the next boot to see the update. If you already have a better way of doing this, feel free to leave a comment!
## Remark
Sincerely welcome your message and thank you for your help in advance!
