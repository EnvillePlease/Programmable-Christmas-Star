# Programmable Christmas Tree Star
![banner](https://github.com/modmypi/Programmable-Christmas-Star/blob/master/github_star.png)

Bring some Raspberry Pi based festive cheer to your Christmas this year with the ModMyPi [Christmas Star](https://www.modmypi.com/raspberry-pi-christmas-tree-star) and bring your tree to life!

## What's in this repository

This repository should be used by cloning the repo first using

`git clone https://github.com/modmypi/Programmable-Christmas-Star`

Which will give you a copy locally.

Inside there is a script called `star.py` which contains a [GPIO Zero](https://github.com/RPi-Distro/python-gpiozero) compatible code allowing you to simply create and use the Star with only a couple of lines of Python.

To switch on the Star you can use:

```
from star import Star

star = Star()

star.on()
```

There are several example files to shouw you what can be done with the star:

### Example files

* `all_on.py` - turns on all of the LEDs.
* `in_out.py` - blinks the inner and outer ring of LEDs alternately.
* `random_leds.py` - turns on and off all the LEDs
* `slow_walk.py` - slowly walks around the LEDs increasing pace until they can't go any faster.
* `twinkle.py` - a pulsing walking pattern around the LEDs.

These files can all be run using:
`sudo python3 name_of_example.py`

## Star Commander
You can follow the [tutorial on our website](https://www.modmypi.com/blog/christmas-tree-star-guide) and learn how to use the Star Commander script.

This script allows you to command how the start glows from the command line over SSH. There are 4 built in modes (plus an off switch) to control the star with ease without having to climb the tree and attach a monitor each time.

Let us know how you get on with the Star and we hope you have a Merry Christmas.

## Christmas Service
I have added an additional directory called Christmas-Service to this forked version of the original repo.  This will allow you to setup a routine (example one included in the folder) that automatically starts when the pi is booted.  Simply follow the instructions below to set up.

Login as your local adiministrator (pi or equivalent).  Then from your terminal type following to setup a service user called christmas and its associated home area.
- sudo -s
- useradd --system --shell /usr/sbin/nologin --home /opt/christmas christmas
- mkdir /opt/christmas

Now we need to make sure that the user has enough permissions to access the GPIO, so we need to add it to some groups.  **DO NOT ADD THEM INTO THE SUDO GROUP**
- usermod -a -G dialout,cdrom,audio,video,plugdev,games,input,netdev,spi,i2c,gpio christmas

That will ensure it has access to the various interfaces, but no elevated permissions.

Now lets go to the christmas users home area and clone the repository, this assumes you have git and all the necessary pre-requisites for using the christmas star already installed.
- cd /opt/christmas
- git clone https://github.com/EnvillePlease/Programmable-Christmas-Star

Now we need to copy the service file to the correct location to be set up later.
- cp /opt/christmas/Programmable-Christmas-Star/Christmas-Service/Christmas.service /etc/systemd/system/Christmas.service

Now let's set ownership and execute permissions for the repo and python scripts.  *This assumes you are still in the /opt/christmas directory*
- chown -R christmas:christmas Programmable-Christmas-Star/
- cd Programmable-Christmas-Star
- chmod +x *.py
- cd Christmas-Service
- chmod +x *.py

Okay, so everything is in place and ready to go, we just need to enable the service and start it.  We'll start by going into the systemd services location to confirm the file we copied is there and then enable it.
- cd /etc/systemd/system
- ls Christmas.*

Hopefully that will return the Christmas.service file.  If it doesn't you need to make sure you've copied the file as stated earlier (you'll need to repermission it too). Next we enable the service.
- systemctl enable Christmas

This will hopefully return a result stating that the symbolic link has been sucessfully created.  If it has we just need to start the service like so.
- systemctl start Christmas

And off we go!  If you shutdown or reboot, the service will automatically start on boot up.

Happy Holidays!
