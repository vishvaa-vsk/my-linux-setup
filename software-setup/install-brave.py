import os
import time

if os.geteuid() == 0:
    os.system("sudo apt install apt-transport-https curl")
    time.sleep(0.5)
    os.system("sudo curl -fsSLo /usr/share/keyrings/brave-browser-archive-keyring.gpg https://brave-browser-apt-release.s3.brave.com/brave-browser-archive-keyring.gpg")
    time.sleep(0.5)
    print("\n\033[96m {}\033[00m" .format("Wait.. Adding brave-browser repository to system!"))
    os.system('echo "deb [signed-by=/usr/share/keyrings/brave-browser-archive-keyring.gpg arch=amd64] https://brave-browser-apt-release.s3.brave.com/ stable main"|sudo tee /etc/apt/sources.list.d/brave-browser-release.list')
    os.system('sudo apt update')
    time.sleep(0.5)
    print("\n\033[93m {}\033[00m" .format("Installing Brave-Browser"))
    os.system("sudo apt install brave-browser -y")
    print("\n\033[92m {}\033[00m".format("Brave Browser installed sucessfully!..\n"))
else:
    exit("\033[91m {}\033[00m" .format("You need to have root privileges to run this script.\n try running with sudo!"))