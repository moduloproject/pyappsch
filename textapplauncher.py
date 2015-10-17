#!/usr/bin/python3
import os	
import re
name=""
pexec=""
def addToFunction(location):
	for filename in os.listdir(location):
		appname=open(location+filename) 
		for line in appname:
			if "Name=" in line:
				name=line.rstrip().replace('Name=','')
				regex = re.compile('[^a-zA-Z]')
				nospacename=regex.sub('', name)
			if "Exec=" in line:
					pexec=line.rstrip().replace('Exec=','')
		# Create function
		with open("checkinput.py", "a") as myfile:
			myfile.write('	'+nospacename+'="'+name+'"\n')
			myfile.write("	if userinput in "+nospacename+":\n")
			myfile.write("		print('Program name: "+name+"')\n")
			myfile.write("		print('Exec command: "+pexec+"')\n")
			myfile.write("")
			myfile.write("		print(\n) \n")
		print(name)

home = os.path.expanduser("~")
addToFunction("/usr/share/applications/")
addToFunction(home+"/.local/share/applications/")

# Import function
from checkinput import checkinput

userinput=input("These are the programs you can launch. Pick one: ")

# Clears the screen, making the visibility of the new results much clearer
os.system('clear')

print("These are some of the programs that you can use:\n")

# Call Function
checkinput(userinput)

# Clear function
open('checkinput.py', 'w').close()
with open("checkinput.py", "a") as myfile:
	myfile.write("#!/usr/bin/python3")
	myfile.write("\n")
	myfile.write("def checkinput(userinput):")
	myfile.write("\n")
