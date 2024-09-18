'''
What if you want to add more devices to the devices.txt file? You can open the file in append mode and then ask the user to provide the name of the new devices. Complete the following steps to create a script:

Open a new file and save it as 07_file-access_actvity.py.
For the open() function use the mode a, which will allow you to append a item to the devices.txt file.
Inside a while True: loop, embed an input() function command that asks the user for the new device.
Set the value of the user's input to a variable named newItem.
Use an if statement that breaks the loop if the user types exit and prints the statement "All done!".
Use the command file.write(newItem + “\n”) to add the new user provided device.
Run and troubleshoot your script until you get output similar to Example 1.

Example 1: Output for Script 07_file-access_activity.py

==== RESTART: /home/user/Documents/GitHub/07_file-access_sol_activity.py ====
Enter device name: Cisco 1941 Router
Enter device name: Cisco 2950 Catalyst Switch
Enter device name: exit
All done!
>>>
'''