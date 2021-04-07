from time import sleep, time
import os
import subprocess

a=time()
def clock():
    """
    The clock function returns the amount of time that had passed since the code had begun execution in minutes
    :return:
    """
    return (time() - a) // 60


cmd1="tasklist /V | findstr Team | findstr Microsoft"
# process=str(os.system(cmd1))
process=subprocess.check_output(cmd1,shell=True).decode("utf-8")

PID=list(filter(lambda x: x!="",list(process.strip().split(" "))))[1]

print("\t\t<---Execute this program after joining the meeting--->")

duration=int(input("For How many minutes due you want to stay in the meeting....\n"))
while clock() < duration:
	sleep(60)

cmd2="tasklist /V | findstr Team | findstr Calendar"
cmd3="tasklist /V | findstr Teams | findstr Call"
#print(check)

try:
	check=subprocess.check_output(cmd3,shell=True)
	cmd4="taskkill /PID "+ PID
	cmd5="taskkill /PID "+ PID
	os.system(cmd4)
	print("Minimize window is Terminated")
	sleep(5)
	os.system(cmd5)
	print("Sucessfully exited the meeting....")
	


except subprocess.CalledProcessError :
	try:
		check=subprocess.check_output(cmd2,shell=True)
		pass
	except subprocess.CalledProcessError :
		cmd5="taskkill /PID "+ PID
		sleep(1)
		os.system(cmd5)
		print("Sucessfully exited the meeting....")
