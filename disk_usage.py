import socket
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

def check_no_network():
	""" Returns True if it fails to resolve Google's URL, false otherwise """
	try:
		socket.gethostbyname("www.google.com")
		return False
	except:
		return True

def main():
	checks = [
		(check_reboot, "Pending reboot."),
		(check_root_full, "Root partition is full."),
		(check_no_network, "No woking network.")
	]
	everything_ok = True
	for check, msg in checks:
		if check():
			print(msg)
			everything_ok = False

	if not everything_ok:
		sys.exit(1)			

	print("Everything is ok!")
	sys.exit(0)

main()

