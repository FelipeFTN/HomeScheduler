from playsound import playsound
import datetime
import time 
import os

class Schedule:
    ### Schedule variables
    schedule=[]
    times_in_schedule=[]
    time_format=""
    time_title=""
    time_song=""
    weekdays=[]

    ### Validations variables
    valid_formats=[]
    valid_song_ext=[]

    ### Global variables
    linux_ap=""
    mac_ap=""
    os=""


    def __init__(self, valid_formats, valid_song_ext, os, mac_ap, linux_ap, weekdays):
        self.valid_formats=valid_formats
        self.valid_song_ext=valid_song_ext
        self.weekdays=weekdays
        self.linux_ap=linux_ap
        self.mac_ap=mac_ap
        self.os=os

    def init_schedule(self, schedule):
        self.time_format=schedule['format']
        self.time_song=schedule['song']
        self.schedule=schedule

        for t in schedule['schedule']:
            self.times_in_schedule.append(t['time'])

        err = self.validate_schedule()

        print(self.times_in_schedule)

        return err

    def run_schedule(self):
        current_time = time.strftime('%X')[0:5] # "00:00:00" -> "00:00"

        while current_time not in self.times_in_schedule:
            # Stuck schedule in this loop
            # checking for time update
            current_time = time.strftime('%X')[0:5] # "00:00:00" -> "00:00"
            if current_time == "00:00":
                print("[+] New day, new schedule.")

                # Re-init schedule
                self.init_schedule(self.schedule)
                return self.run_schedule()

            time.sleep(5)

        for t in self.schedule['schedule']:
            # I know it's duplicated code, but, who cares?
            if current_time == "00:00":
                print("[+] New day, new schedule.")

                # Re-init schedule
                self.init_schedule(self.schedule)
                return self.run_schedule()

            if t['time'] == current_time:
                self.time_title = t['title']
                break
            
            if self.is_in_exception_day(t):
                print(f"[+] Skipping exception on {t['title']} - {t['time']}")
                continue

        # Schedule execution function will be called here
        self.times_in_schedule.remove(current_time)
        self.execute_schedule()

    def execute_schedule(self):
        # Possibly the worst way to do this. But should work.
        if self.os == "Linux":
            playsound(f"./songs/{self.time_song}")
            # os.system(f"say {self.time_title}") # Not working properly yet
        elif self.os == "Darwin":
            playsound(f"./songs/{self.time_song}")
            os.system(f"say {self.time_title}")
        else:
            print("[x] Please use a real operating system.")
            return None
        
        return self.run_schedule()

    def validate_schedule(self):
        if self.time_format not in self.valid_formats:
            return f"[x] Invalid schedule time format: {self.time_format}"

        song_ext="." + self.time_song.split(".")[1]
        if song_ext not in self.valid_song_ext:
            return f"[x] Invalid schedule song extension: {song_ext}"

        return "no-error"

    def is_in_exception_day(self, t):
        if t == None or 'exception' not in t:
            return False

        i = datetime.date.today().weekday()
        exceptions = t['exception'].split(',')

        if self.weekdays[i] in exceptions:
            return True

        return False
