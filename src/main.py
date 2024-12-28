### by & to: FelipeFTN.
### (No GPT/Copilot used).
### :)

import json
import sys

from global_envs import *

if len(sys.argv) == 1:
    print(f"[+] No schedule provided, using  default: '{DEFAULT_SCHEDULE}'")
    SCHEDULE=DEFAULT_SCHEDULE
else:
    SCHEDULE=sys.argv[1]

if ".json" not in SCHEDULE:
    SCHEDULE=SCHEDULE.strip() + ".json"

with open(f'schedules/{SCHEDULE}') as schedule_file:
    schedule = json.load(schedule_file)

    err = s.init_schedule(schedule)
    if err != "no-error":
        print(err)
        sys.exit()

    s.run_schedule()
