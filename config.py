import json
import sys

# default location to check
configPath = "config.json"

# check if user passed in custom config location
if len(sys.argv) == 3:
    # a flag and value has been passsed
    if sys.argv[1] == '-config' or sys.argv[1] == '--config':
        configPath = sys.argv[2]
    else:
        print("Unspported flag passed: " + sys.argv[1])
        sys.exit()

with open(configPath, 'r') as f:
    config = json.load(f)

# NOTIFICATIONS
NOTIFICATION = config['notifications']['show_notification']
PLAY_SOUND = config['notifications']['sound']['play']
SOUND_FILE = config['notifications']['sound']['file']
PLAYER = config['notifications']['sound']['player']

# IMGUR
CLIENT_ID = config['imgur']['client_id']