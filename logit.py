import argparse
import errno
import os
import sys
from datetime import datetime

logit_location = os.environ.get('LOGIT_LOCATION', os.path.expanduser('~/.logit'))


def _logit(message, show=None, file=None):
    try:
        os.makedirs(logit_location)
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise

    # Write one log file per day, opening and appending to throughout the day.
    now = datetime.now()
    file_name = file or os.path.join(logit_location, "logit-%s.log" % (now.strftime('%m-%d-%Y')))
    with open(file_name, 'a+') as f:
        if file:
            f.write("".join((message, '\n')))
        else:
            f.write("".join(("%s: " % now.strftime('%H:%M:%S'), message, '\n')))

    if show:
        with open(file_name, 'r') as f:
            sys.stdout.write(f.read())


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("message", help="The message you want to log.")
    parser.add_argument('-s', '--show', action='store_true', default=False,
                        help="Show the log file after writing to it.")
    parser.add_argument('-f', '--file', help="The file to write to.")
    args = parser.parse_args()

    _logit(args.message, args.show, args.file)
