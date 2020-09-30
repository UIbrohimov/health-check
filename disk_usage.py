
import shutil
import os
import sys

def check_disk_usage(disk, min_gb, min_percent):
	""" 
	This function works the disk usage out and checks if here is
	enough space available
	
	"""
	du = shutil.disk_usage(disk)
	percent_free = du.free / du.total * 100
	# print(percent_free)
	gigabytes_free = du.free / 2 ** 30
	# print(gigabytes_free)
	if percent_free < min_percent or gigabytes_free < min_gb:
		return True
	return False

def check_root_full():
	""" Returns True if the root partition is full, False otherwse """
	return check_disk_usage(disk="/", min_gb=2, min_percent=10)

def check_reboot():
    """ This returns a True if a computer is pending a reboot. """
    return os.path.exists("/run/reboot-required")

def main():
    if check_reboot():
        print("Pending reboot.")
        sys.exit(1)
    if check_root_full():
    	print("Root partition is full.")
    	sys.exit(1)

    print("Everything is ok!")
    sys.exit(0)

main()

