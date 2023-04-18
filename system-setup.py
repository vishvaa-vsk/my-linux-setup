import subprocess
import os
import time

def basic_setup():
    os.system("sudo apt install git curl wget -y")

def pulseAudio():
    os.system("sudo apt install pulseaudio pavucontrol -y")
    print("\n\033[92m {}\033[00m".format("Pulse audio installed sucessfully\n"))
  
def configure_preload():
    sysmem = str(subprocess.check_output("grep MemTotal /proc/meminfo",shell=True).decode("utf-8")).split()
    if int(sysmem[1]) >= 4000000:
        os.system("sudo apt install preload -y")
        print("\n\033[91m {}\033[00m".format("Preload installed sucessfully\n"))
        print("\033[93m {}\033[00m".format("Check preload status by 'sudo systemctl status preload'\n"))
    else:
        print("\033[91m {}\033[00m".format("Preload is only advisable for 4GB+ installed RAM...\n"))

def fix_amdgpu_drivers():
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