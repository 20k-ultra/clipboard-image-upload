import pyperclip as clipboard
import time
import subprocess
import pyimgur
import os
import config

def isImage():
  proc = subprocess.Popen(['bash','-c', '/usr/bin/xclip -selection clipboard -t TARGETS -o'],stdout=subprocess.PIPE)
  counter = 0
  while counter < 30:
    line = proc.stdout.readline()
    if "image/png" in str(line):
      return True
    counter += 1
  return False

def upload():
  process = subprocess.Popen(['bash','-c','/usr/bin/xclip -selection clipboard -t image/png -o > /tmp/clipboard_image.png'],stdout=subprocess.PIPE)
  process.wait()
  im = pyimgur.Imgur(config.CLIENT_ID)
  uploaded_image = im.upload_image("/tmp/clipboard_image.png")
  return uploaded_image.link

def init():
  # set some starting clipboard data
  # empty string comparison doesn't trigger difference condition
  previousPasta = "\n"
  clipboard.copy(previousPasta)
  while True:
    if previousPasta != clipboard.paste():
      # set pasta so we only check isImage for new data
      previousPasta = clipboard.paste()
      # new data in clipboard
      if isImage():
        # it's an image so upload
        link = upload()
        if link:
          clipboard.copy(link)
          if config.PLAY_SOUND:
            subprocess.Popen(['bash','-c', config.PLAYER + ' ' + config.SOUND_FILE],stdout=subprocess.PIPE)
          if config.NOTIFICATION:
            subprocess.call(['notify-send','Clipboard Image Uploaded!',link])
    time.sleep(1)

# START
init()