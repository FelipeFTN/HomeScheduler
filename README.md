# Home Scheduler

This is a simple home scheduler that allows you to schedule tasks for your home. You can add, edit, and delete tasks. You can also mark tasks as completed. The tasks are stored in Json files.
**This is quite a pesonal project.** I plan to use this in my home. I will be adding more features as I go along.
I will be integrating this code into my Raspberry Pi, which will control the alarm system for my home.

## features

Everything is setup inside the `schedules` folder. The `schedules` folder contains the json files for each day, or a single file for all the days, which contains the configuration for the scheduler.

Take a look at the `schedules` folder to see how the json files are structured.

## How to run

The scheduler is a simple command line application. You can run it by executing the `main.py` file.
You also need to pass as an argument the json file in which you will be using on your schedule.

```bash
    python3 main.py daily
```
