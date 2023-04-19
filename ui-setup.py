import subprocess
import os
import time

from linux_setup import Red,Green,Yellow,Purple,Cyan

def theme_setup():
    if os.path.exists("theme-setup.zip"):
        os.system("sudo unzip theme-setup.zip")
        os.system("sudo mv .icons .themes ~/")
        os.system("clear")
        print(Purple("Applying Theme!😀...\n"))
        os.system("gsettings set org.gnome.desktop.interface gtk-theme Orchis-Dark-Dracula")
        os.system("gsettings set org.gnome.desktop.interface icon-theme WhiteSur-dark")
        os.system("gsettings set org.gnome.desktop.wm.preferences theme Orchis-Dark-Dracula")
        os.system("gsettings set org.gnome.desktop.interface cursor-theme Bibata-Original-Classic")
        print(Green("<<< Theme Applied succesfully >>>\n"))
    else:
        print(Red("theme-setup.zip not found!.."))

def dynamic_wallpaper():
    current_dir = os.getcwd()
    if os.path.exists("Dynamic-Wallpapers.zip"):
        os.system("unzip Dynamic-Wallpapers.zip")
        os.system("clear")
        os.chdir("Linux_Dynamic_Wallpapers/")
        os.system("./install.sh")
        os.chdir(current_dir)
        print(Green("Dynamic Wallpapers installed Suceesfully!.."))
        print(Cyan("Go to apperence settings to apply it."))
    else:
        print(Red("Dynamic-Wallpapers.zip not found!.."))

def grub_theme():
    current_dir = os.getcwd()
    if os.path.exists("grub-theme.zip"):
        os.system("unzip grub-theme.zip")
        os.system("clear")
        os.chdir("darkmatter-grub-theme/")
        os.system("sudo python3 darkmatter-theme.py -i")
        time.sleep(0.2)
        os.chdir(current_dir)
    else:
        print(Red("grub-theme.zip not found!.."))
