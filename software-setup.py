import subprocess
import os
import time

def check_root():
    if os.geteuid() != 0:
        exit("\033[91m {}\033[00m" .format("You need to have root privileges to run this script.\n try running with sudo!"))

def check_distro():
    try:
        lsb_id = subprocess.check_output("lsb_release -i", shell=True).decode("utf-8")
        id = lsb_id.split(":")[-1].lower().strip()
    except Exception:
        id = "unknown"
    return id

def basic_setup():
    if check_distro() == "debian" or "ubuntu":
        os.system("sudo apt install git curl wget -y")
    else:
        print("\033[91m {}\033[00m".format("Can't find your distribution type.. this is only for debian based distributions!."))

def brave_browser():
    if check_distro() == "debian" or "ubuntu":
        os.system("sudo apt install apt-transport-https curl -y")
        time.sleep(0.3)
        
        os.system("sudo curl -fsSLo /usr/share/keyrings/brave-browser-archive-keyring.gpg https://brave-browser-apt-release.s3.brave.com/brave-browser-archive-keyring.gpg")
        time.sleep(0.3)
        
        print("\n\033[96m {}\033[00m" .format("Wait.. Adding brave-browser repository to system!\n"))
        os.system('echo "deb [signed-by=/usr/share/keyrings/brave-browser-archive-keyring.gpg arch=amd64] https://brave-browser-apt-release.s3.brave.com/ stable main"|sudo tee /etc/apt/sources.list.d/brave-browser-release.list')
        os.system('sudo apt update')
        time.sleep(0.3)
        
        print("\n\033[93m {}\033[00m" .format("Installing Brave-Browser\n"))
        os.system("sudo apt install brave-browser -y")
        
        print("\n\033[92m {}\033[00m".format("Brave Browser installed sucessfully!..\n"))
    else:
        print("\033[91m {}\033[00m".format("Can't find your distribution type.. this is only for debian based distributions!."))

def spotify():
    if check_distro() == "debian" or "ubuntu":
        os.system("curl -sS https://download.spotify.com/debian/pubkey_7A3A762FAFD4A51F.gpg | sudo gpg --dearmor --yes -o /etc/apt/trusted.gpg.d/spotify.gpg")
        os.system('echo "deb http://repository.spotify.com stable non-free" | sudo tee /etc/apt/sources.list.d/spotify.list')
        print("\n\033[96m {}\033[00m" .format("Updating packages & installing spotify\n"))
        time.sleep(0.2)
        os.system("sudo apt-get update && sudo apt-get install spotify-client -y")
        print("\n\033[92m {}\033[00m".format("Spotify installed sucessfully!..\n"))
    else:
        print("\033[91m {}\033[00m".format("Can't find your distribution type.. this is only for debian based distributions!."))

def vscode():
    if check_distro() == "debian" or "ubuntu":
        os.system("sudo apt install apt-transport-https curl")
        print("\033[96m {}\033[00m" .format("Wait.. Adding vscode repo!..\n"))
        time.sleep(0.3)
        os.system("curl https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > microsoft.gpg")
        time.sleep(0.1)
        os.system("sudo install -o root -g root -m 644 microsoft.gpg /usr/share/keyrings/microsoft-archive-keyring.gpg")
        os.system("sudo touch /etc/apt/sources.list.d/vscode.list")
        os.system("echo 'deb [arch=amd64,arm64,armhf signed-by=/usr/share/keyrings/microsoft-archive-keyring.gpg] https://packages.microsoft.com/repos/vscode stable main' | sudo tee -a /etc/apt/sources.list.d/vscode.list")
        print("\033[93m {}\033[00m".format("Added vscode repo to system!..\n"))
        time.sleep(0.2)
        os.system("sudo apt-get install apt-transport-https")
        os.system("sudo apt-get update")
        print("\033[93m {}\033[00m".format("Installing vscode!..\n"))
        os.system("sudo apt-get install code -y")
        os.system("sudo rm microsoft.gpg")
        print("\n\033[92m {}\033[00m".format("VScode installed sucessfully!..\n"))
    else:
        print("\033[91m {}\033[00m".format("Can't find your distribution type.. this is only for debian based distributions!."))

def fix_amdgpu_drivers():
    if check_distro() == "debian":
        lspci = str(subprocess.check_output("lspci -nn | grep VGA", shell=True).decode("utf-8"))
        if lspci.find("AMD")!= -1:
            os.system("sudo apt purge *nvidia*")
            print("\033[96m {}\033[00m" .format("Removed proprietary nvidia drivers!..\n"))
            os.system("echo 'deb http://deb.debian.org/debian buster main contrib non-free' | sudo tee -a /etc/apt/sources.list")
            print("\033[96m {}\033[00m" .format("Updating packages and repo!..\n"))
            os.system("sudo apt update")
            print("\033[93m {}\033[00m".format("Fixing AMD GPU drivers!...\n"))
            os.system("sudo apt-get install firmware-amd-graphics libgl1-mesa-dri libglx-mesa0 mesa-vulkan-drivers xserver-xorg-video-all firmware-linux firmware-linux-nonfree libdrm-amdgpu1 xserver-xorg-video-amdgpu -y")
            print("\n\033[92m {}\033[00m".format("AMD GPU drivers installed sucessfully!..\nReboot to see changes\n"))
        else:
            print("\033[91m {}\033[00m".format("This is only for AMD GPUs/APUs!..\n"))
    else:
        print("\033[91m {}\033[00m".format("Can't find your distribution type.. this is only for debian based distributions!."))

def desnap():
    if check_distro() == "ubuntu":
        if os.path.exists("desnap-ubuntu.py"):
            os.system("sudo python3 desnap-ubuntu.py")
        else:
            print("\033[91m {}\033[00m".format("Can't find desnap-ubuntu.py in your directory!..\n Try again with it..\n"))
    else:
        print("\033[91m {}\033[00m".format("This is only for Ubuntu !..\n"))

def configure_preload():
    if check_distro() == "debian" or "ubuntu":
        sysmem = str(subprocess.check_output("grep MemTotal /proc/meminfo",shell=True).decode("utf-8")).split()
        if int(sysmem[1]) >= 4000000:
            os.system("sudo apt install preload -y")
            print("\n\033[91m {}\033[00m".format("Preload installed sucessfully\n"))
            print("\033[93m {}\033[00m".format("Check preload status by 'sudo systemctl status preload'\n"))
        else:
            print("\033[91m {}\033[00m".format("Preload is only advisable for 4GB+ installed RAM...\n"))

def nodejs_install():
    if check_distro() == "debian" or "ubuntu":
        choice = int(input("\033[95m {}\033[00m" .format("Choose one below:\n 1. Install Node.js LTS\n 2. Install Current Version of Node.js\nEnter choice: ")))
        if choice ==1:
            os.system("curl -fsSL https://deb.nodesource.com/setup_lts.x | sudo -E bash -")
            print("\033[96m {}\033[00m".format("Installing node.js!..."))
            time.sleep(0.2)
            os.system("sudo apt install nodejs")
            print("\n\033[92m {}\033[00m".format("node.js LTS version installed sucessfully\n"))
        elif choice==2:
            os.system("curl -fsSL https://deb.nodesource.com/setup_current.x | sudo -E bash -")
            print("\033[96m {}\033[00m".format("Installing node.js!..."))
            time.sleep(0.2)
            os.system("sudo apt install nodejs")
            print("\n\033[92m {}\033[00m".format("Current version of node.js installed sucessfully\n"))
    else:
        print("\033[91m {}\033[00m".format("This script is only for debian based distros!...\n"))

def pulseAudio():
    if check_distro() == "debian" or "ubuntu":
        os.system("sudo apt install pulseaudio pavucontrol -y")
        print("\n\033[92m {}\033[00m".format("Pulse audio installed sucessfully\n"))
    else:
        print("\033[91m {}\033[00m".format("This script is only for debian based distros!...\n"))

    
if __name__ == "__main__":
    check_root()
    if check_distro() == "debian" or "ubuntu":
        basic_setup()
        fix_amdgpu_drivers()
        pulseAudio()
        brave_browser()
        vscode()
        spotify()
        configure_preload()
        nodejs_install()
        desnap()
    else:
        print("\033[91m {}\033[00m".format("Can't find your distribution type.. this is only for debian based distributions!."))