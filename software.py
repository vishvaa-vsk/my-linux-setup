import subprocess
import os
import time

def brave_browser():
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

def spotify():
    os.system("curl -sS https://download.spotify.com/debian/pubkey_7A3A762FAFD4A51F.gpg | sudo gpg --dearmor --yes -o /etc/apt/trusted.gpg.d/spotify.gpg")
    os.system('echo "deb http://repository.spotify.com stable non-free" | sudo tee /etc/apt/sources.list.d/spotify.list')
    
    print("\n\033[96m {}\033[00m" .format("Updating packages & installing spotify\n"))
    time.sleep(0.2)
    
    os.system("sudo apt-get update && sudo apt-get install spotify-client -y")
    print("\n\033[92m {}\033[00m".format("Spotify installed sucessfully!..\n"))
    
def vscode():
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

def nodejs_install():
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
        print("\033[91m {}\033[00m".format("Enter a valid option!...\n"))