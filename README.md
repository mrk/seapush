#SEAPUSH v.130726 README

![](https://github.com/mrk/seapush/blob/master/seapush.png?raw=true)

 [Ableton's Push controller](https://www.ableton.com/push/) is great, but it's become infamous for the inconsistent white-level calibration on its LEDs.  and since its default color scheme involves so much white, it can be a torturous experience for aesthetically nitpicky types like you and me.

seapush is a python script that applies a custom [seapunk](http://images.google.com/images?q=seapunk) color scheme to the Push controller's LEDs.  it does not change Push's functionality in any way, except to make it more beautiful.

**NOTE: this version of seapush has only been tested with Ableton Live v.9.0.5, and is not compatible with earlier versions.**

this script is a modification of [dreznicek's decompiled push skin default script for Live 9.0.5](https://github.com/dreznicek/AbletonLive9_SkinDefault/tree/9.0.5).

<< BONUS:: "YO DAWG I HEARD U LIKE SEAPUNK" :: my custom seapunk textmate color theme (compatible w both TextMate and SublimeText) so you can modify my seapunk color scheme using a seapunk color scheme //  n.b. this color scheme was a modification of another i had been using but can't remember which; happy to add a citation when i know whom to credit >>


##Installation and Use ##

1. Click the "Download ZIP" button on the right sidebar of this github page and use the file contained in the downloaded .zip archive - some people have had problems making this script work and using the file from the .zip archive seems to solve it.
2.  **On Mac OS X:** Right-click your Ableton Live application and select "Show Package Contents", and navigate to "Contents/App-Resources/MIDI Remote Scripts/" or **On Windows:** navigate to "C:\Program Files\Ableton\Live x.x.x\Resources\MIDI Remote Scripts"
2. Locate the "Push" directory and make a copy of it to store in a safe place on your computer.  If anything goes wrong while you're tinkering with the python scripts inside, you can replace your modified Push directory with your saved copy to restore Push to its default behavior.
3. Add the SkinDefault.py file from this repo to the Push folder.  Note there is already a file in the Push folder called "SkinDefault.pyc"; adding the .py file from this repo will override and overwrite the .pyc file, so make sure you have it backed up!
4. Restart Ableton Live if it's already running.
5. Enjoy your sexy new Push!
6. You can further modify the SkinDefaults.py file to your heart's content.  Info and discussion on color variable names and conventions for this script can be found on [this thread in the Ableton forums](https://forum.ableton.com/viewtopic.php?f=55&t=192043).

##License ##

[![Creative Commons License](http://i.creativecommons.org/l/by/3.0/88x31.png)](http://creativecommons.org/licenses/by/3.0/)
This work is licensed under a [Creative Commons Attribution 3.0 Unported License](http://creativecommons.org/licenses/by/3.0/).
