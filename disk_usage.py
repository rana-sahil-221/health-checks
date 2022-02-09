#!/usr/bin/env python3
import os
import shutil
import sys

def check_reboot():
    """Returns true if the computer has a pending reboot"""
    return os.path.exists("/run/reboot-required")

def check_disk_usage(disk, min_gb,min_percent):
    """Returns if there is enough free disk, false otherwise"""
    du = shutil.disk_usage(disk)
    percent_free = 100 * du.free / du.total
    #calculate how many free gigabytes
    gigabytes_free = du.free / 2**30
    if percent_free < min_percent or gigabytes_free < min_gb:
    	return True
    return False


def check_root_full():
    """ Return True is the root partition is full, False otherwise"""
    return check_disk_usage(disk="/",min_gb=2, min_percent=10)


def main():

    checks = [
        (check_reboot, "Pending Reboot"),
        (check_root_full, "Root partition is Full"),
    ]
    everything_ok = True
    for check,msg in checks:
        if check():
            print(msg)
            everything_ok = False

    if not everything_ok:
       sys.exit(1)

    print("Everything is OK")
    sys.exit(0)

main()
