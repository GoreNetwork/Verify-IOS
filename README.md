# Verify-IOS

The IPs.csv is where you put the devices you want to check out. 
Column A is there for people to look at, it's not used by the program at all
Column B is where the IP address is that the program will try and SSH to
Column C is where you put the name of the IOS that you hope the device is running

Run verify_ios.py and it will propt you for a username and password it will use to SSH to the router/switch where it will run "show ver"
It will then look at the IOS file the device is running, then compair it to what was in the IPS.csv, and spit a result out to results.csv
