import os
import time
from linux_setup import Red,Green,Yellow,Purple,Cyan

# making a preference file to restrict installation of snap during apt update..
def nosnap():
    current_path = os.getcwd()+"/"
    nosnap = open(f"{current_path}nosnap.pref","w+")
    nosnap.writelines(["Package: snapd\n","Pin: release a=*\n","Pin-Priority: -10\n"])
    os.system(f"sudo mv {current_path}/nosnap.pref /etc/apt/preferences.d/")

# Installing firefox as a deb package insted of snap version
# Remember firefox is uninstalled during removal of snap
def firefox_deb():
    current_path = os.getcwd()+"/"
    os.system("sudo add-apt-repository ppa:mozillateam/ppa")
    os.system("sudo apt update")
    os.system("sudo apt install -t 'o=LP-PPA-mozillateam' firefox -y")
    time.sleep(1)
    unsnap_ff = open(f"{current_path}mozillateamppa","w+")
    unsnap_ff.writelines(["Package: firefox*\n","Pin: release o=LP-PPA-mozillateam\n","Pin-Priority: 501\n"])
    os.system(f"sudo mv {current_path}/mozillateamppa /etc/apt/preferences.d/")

if os.geteuid() == 0:#checking sudo permission
    current_path = os.getcwd()+"/"
    packages_name = open(f"{current_path}snap-list.txt","r+")
    snap_list = packages_name.readlines()
    if snap_list!= None or []:
        for package in snap_list:
            os.system(f"sudo snap remove --purge {package}")#removing each snap packages
            os.system("sudo apt remove --autoremove snapd -y")#removing snap itself!
            break
        print(Cyan("Wait ..."))
        time.sleep(2)
        nosnap()# calling nosnap preference 
        print(Yellow("Snap removed from system!.."))
        print(Cyan("Updating system one last time!.."))
        os.system("sudo apt update")#updating system
        print(Cyan("Installing software-store without snap!.."))
        os.system("sudo apt install --install-suggests gnome-software -y")#Installing gnome-software-store without snap
        ff_confirm = input(Purple("\nNow firefox has removed from system. Do you want to install it again? [Y/n]"))#asking about firefox reinstallation!
        if ff_confirm.lower() == "y":
                firefox_deb()#installing firefox as non snap package
        else:
            print(Green("Script sucessful \n Happy coding!.."))
    else:
        print(Red("Unexpeted error in removing snap! try again.."))
else:
    exit(Red("You need to have root privileges to run this script.\n try running with sudo!"))
