import subprocess
import os
import time
from linux_setup import Red,Green,Yellow,Purple,Cyan

def brave_browser():
    os.system("sudo apt install apt-transport-https curl -y")
    time.sleep(0.3)
        
    os.system("sudo curl -fsSLo /usr/share/keyrings/brave-browser-archive-keyring.gpg https://brave-browser-apt-release.s3.brave.com/brave-browser-archive-keyring.gpg")
    time.sleep(0.3)
        
    print(Cyan("Wait.. Adding brave-browser repository to system!\n"))
    os.system('echo "deb [signed-by=/usr/share/keyrings/brave-browser-archive-keyring.gpg arch=amd64] https://brave-browser-apt-release.s3.brave.com/ stable main"|sudo tee /etc/apt/sources.list.d/brave-browser-release.list')
    os.system('sudo apt update')
    time.sleep(0.3)
        
    print(Yellow("Installing Brave-Browser\n"))
    os.system("sudo apt install brave-browser -y")
        
    print(Green("Brave Browser installed sucessfully!..\n"))

def spotify():
    os.system("curl -sS https://download.spotify.com/debian/pubkey_7A3A762FAFD4A51F.gpg | sudo gpg --dearmor --yes -o /etc/apt/trusted.gpg.d/spotify.gpg")
    os.system('echo "deb http://repository.spotify.com stable non-free" | sudo tee /etc/apt/sources.list.d/spotify.list')
    
    print(Yellow("Updating packages & installing spotify\n"))
    time.sleep(0.2)
    
    os.system("sudo apt-get update && sudo apt-get install spotify-client -y")
    print(Green("Spotify installed sucessfully!..\n"))
    
def vscode():
    os.system("sudo apt install apt-transport-https curl")
    print(Cyan("Wait.. Adding vscode repo!..\n"))
    time.sleep(0.3)
    
    os.system("curl https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > microsoft.gpg")
    time.sleep(0.1)
    os.system("sudo install -o root -g root -m 644 microsoft.gpg /usr/share/keyrings/microsoft-archive-keyring.gpg")
    os.system("sudo touch /etc/apt/sources.list.d/vscode.list")
    os.system("echo 'deb [arch=amd64,arm64,armhf signed-by=/usr/share/keyrings/microsoft-archive-keyring.gpg] https://packages.microsoft.com/repos/vscode stable main' | sudo tee -a /etc/apt/sources.list.d/vscode.list")
    
    print(Yellow("Added vscode repo to system!..\n"))
    time.sleep(0.2)
        
    os.system("sudo apt-get install apt-transport-https")
    os.system("sudo apt-get update")
        
    print(Purple("Installing vscode!..\n"))
    os.system("sudo apt-get install code -y")
    os.system("sudo rm microsoft.gpg")
    print(Green("VScode installed sucessfully!..\n"))

def nodejs_install():
    choice = int(input(Cyan("Choose one below:\n 1. Install Node.js LTS\n 2. Install Latest Version of Node.js\nEnter choice: ")))
    if choice ==1:
        os.system("curl -fsSL https://deb.nodesource.com/setup_lts.x | sudo -E bash -")
        print(Purple("Installing node.js!..."))
        time.sleep(0.2)
        os.system("sudo apt install nodejs")
        print(Green("node.js LTS version installed sucessfully\n"))
    elif choice==2:
        os.system("curl -fsSL https://deb.nodesource.com/setup_current.x | sudo -E bash -")
        print(Purple("Installing node.js!..."))
        time.sleep(0.2)
        os.system("sudo apt install nodejs")
        print(Green("Latest version of node.js installed sucessfully\n"))
    else:
        print(Red("Enter a valid option!...\n"))