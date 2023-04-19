import subprocess
import os
import time
from linux_setup import Red,Green,Yellow,Purple,Cyan

def basic_setup():
    os.system("sudo apt updateinstall ")
    os.system("sudo apt install git curl ssh wget -y")

def pulseAudio():
    os.system("sudo apt install pulseaudio pavucontrol -y")
    print(Green("Pulse audio installed sucessfully\n"))
  
def configure_preload():
    sysmem = str(subprocess.check_output("grep MemTotal /proc/meminfo",shell=True).decode("utf-8")).split()
    if int(sysmem[1]) >= 4000000:
        os.system("sudo apt install preload -y")
        print(Green("Preload installed sucessfully\n"))
        print(Yellow("Check preload status by 'sudo systemctl status preload'\n"))
    else:
        print(Red("Preload is only advisable for 4GB+ installed RAM...\n"))

def fix_amdgpu_drivers():
    lspci = str(subprocess.check_output("lspci -nn | grep VGA", shell=True).decode("utf-8"))
    if lspci.find("AMD")!= -1:
        os.system("sudo apt purge *nvidia*")
        print(Cyan("\nRemoved proprietary nvidia drivers!..\n"))
        os.system("echo 'deb http://deb.debian.org/debian buster main contrib non-free' | sudo tee -a /etc/apt/sources.list")
        print(Cyan("\nUpdating packages and repo!..\n"))
        os.system("sudo apt update")
        print(Yellow("\nFixing AMD GPU drivers!...\n"))
        os.system("sudo apt-get install firmware-amd-graphics libgl1-mesa-dri libglx-mesa0 mesa-vulkan-drivers xserver-xorg-video-all firmware-linux firmware-linux-nonfree libdrm-amdgpu1 xserver-xorg-video-amdgpu -y")
        print(Green("AMD GPU drivers installed sucessfully!..\nReboot to see changes\n"))
    else:
        print(Red("This is only for AMD GPUs/APUs!..\n"))