from schedule import Schedule
import platform

### Default selected schedule
# This should only be used in case of no arguments passed
DEFAULT_SCHEDULE="daily.json"

### Schedule value
# This will store the current schedule in use
SCHEDULE=""

### Weekdays
# This is just a dict with the weekdays' names
# In order to use as a map for exceptions
WEEKDAYS=["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]

### Validations
# This variables should be used to validate default bahaviours/values from schedule
VALID_FORMATS=["24h", "12h", "24", "12"]
VALID_SONG_EXT=[".mp3"]

### Operating System
OPERATING_SYSTEM=platform.system()

### Audio Player
# This should be used to play the songs
# I will use mpg123 for Linux and afplay for MacOS
# I will not implement Windows support
MAC_AUDIO_PLAYER="afplay"
LINUX_AUDIO_PLAYER="mpg123"

### Schedule Class
# I will do this to avoid using default __init__ class function
# It's not the best practice, but I don't care too much.
s = Schedule(
        VALID_FORMATS,
        VALID_SONG_EXT,
        OPERATING_SYSTEM,
        MAC_AUDIO_PLAYER,
        LINUX_AUDIO_PLAYER,
        WEEKDAYS
    )
