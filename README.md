## clipboard-image-upload
------------------------

Watches the clipboard for image data to be uploaded to Imgur. This is useful when using **[Flameshot](https://github.com/lupoDharkael/flameshot)** and clicking the **`Copy`** button to automatically upload and copy the url to clipboard instantly.

By default the script will anonymously upload to Imgur but working on account uploads.

## [Dependencies](#dependencies)
------------------------

* python 3
* [pyimgur](https://github.com/Damgaard/PyImgur)
* [pyperclip](https://github.com/asweigart/pyperclip)
* [xclip](https://github.com/astrand/xclip)
* audio player
  * Specify your own audio player in the config. I used [mpv](https://mpv.io/installation/) because that's what I had installed.
* and uh GNU/Linux

## [Install](#install)
------------------------

Install **[xclip](https://github.com/astrand/xclip)** to your system and add your own audio player to the config file. You can install the python dependencies with pip3:


```
pip3 install -r requirements.txt
```

## [How to use](#how-to-use)
------------------------

Add your **`client_id`** to the **`config.json`** file before running as you need the **`client_id`** even for anonymously uploading images to imgur. See [Obtaining Imgur account access](#obtaining-imgur-client-id).

Run the following to start the script:

```
python3 watch.py
```

However I am running the script with a systemd service file.

Some settings can be changed in the **`config.json`** which is located in this script's folder.

## [Troubleshooting](#troubelshotting)
------------------------

Make sure you add your applications **`client_id`** to the config file. See below for how to create an application and obtaning its **`client_id`**.

Make sure your audio player is working and added to the config file. I'm using **[mpv](https://mpv.io/installation/)** and it works good.

Also, I had issues installing pyaudio on my debian (stretch) machine. Reading the **[downloads](http://people.csail.mit.edu/hubert/pyaudio/#downloads)** page gave enough information to fix it.


## [Obtaining Imgur account access](#obtaining-imgur-client-id)
------------------------

You'll need to get a **`client_id`** to anonymously upload images to imgur.

Visit the register an application **[page](https://api.imgur.com/oauth2/addclient)** and select **"*anonymous usage without user authorization*"** type. Imgur won't show you the secret again so write it down now if you want.

## [Things to add](#to-do)
------------------------
* **Imgur account upload**
  * This wasn't added yet because the **`access_token`** you generate expires after 1 month. However the script can request a new one by using the **`refresh_token`** that was given when the **`access_token`** was generated.
* **Save image to file without xclip**
  * xclip provides a way to check the clipboard data target so we can see if it's **`image/png`** type. Need to figure out a way to do that with python. And pasting image data to file...
* **Use Python to play the audio file instead of requiring a player be on the system.**

