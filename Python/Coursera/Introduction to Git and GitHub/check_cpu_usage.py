#!/usr/bin/env python3

# sudo python3 -m pip install --upgrade pip
# sudo python3 -m pip install psutil for Ubuntu 19.10

import psutil

def check_cpu_usage(percent):
    usage = psutil.cpu_percent(1)
    print("DEBUG: usage: {}".format(usage))
    return usage < percent

if not check_cpu_usage(75):
    print("ERROR! CPU is overloaded")
else:
    print("Everything ok")