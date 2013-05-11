Logit - Log a note from your terminal
=====================================

Some times you just need to write something down.  Since I spend most of my day at the command line anyways, this is just a simple means to accomplish that.  Usage is as follows:

* pip install -e git+git://github.com/cgallemore/logit.git#egg=logit or clone the project and python setup.py install
* Open a terminal and logit:

Usage: 
  >>> logit "When you come to a fork in the road, take it."
  >>> cat ~/.logit/*.log
  When you come to a fork in the road, take it.
  >>> logit "A nickel ain't worth a dime anymore." -s
  When you come to a fork in the road, take it.
  A nickel ain't worth a dime anymore
  >>> logit -h
  usage: logit [-h] [-s] [-f FILE] message
  positional arguments:
    message               The message you want to log.
  optional arguments:
    -h, --help            show this help message and exit
    -s, --show            Show the log file after writing to it.
    -f FILE, --file FILE  The file to write to.

By default logit will write a daily log file in the format logit-mm-dd-yyyy.log to your home directory.  If you wish to write those files elsewhere, you can set the following environment variable:

* export LOGIT_LOCATION='/Users/cgallemore/Dropbox/logit'

Now, the daily log file will be written to the logit folder in your Dropbox folder.
