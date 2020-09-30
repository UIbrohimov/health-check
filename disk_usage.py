import shutil

import sys


def check_disk_usage(disk, min_gb, min_percent):
	""" 
	This function works the disk usage out and checks if here is
	enough space available
	
	"""
	du = shutil.disk_usage(disk)
	percent_free = du.free / du.total * 100
	print(percent_free)
	gigabytes_free = du.free / 2 ** 30
	print(gigabytes_free)
	if percent_free < min_percent or gigabytes_free < min_gb:
		return False
	return True

if not check_disk_usage(disk="/", min_gb=2, min_percent=10):
	print("ERROR: Not enough disk space!")
	sys.exit(1)

print("Everything ok.")
sys.exit(0)
