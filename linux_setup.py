import subprocess
import os
import time

def Red(msg): print("\033[91m {}\033[00m" .format("\n"+msg))
def Green(msg): print("\033[92m {}\033[00m" .format('\n'+msg))
def Yellow(msg): print("\033[93m {}\033[00m" .format('\n'+msg))
def Purple(msg): print("\033[95m {}\033[00m" .format('\n'+msg)) 
def Cyan(msg): print("\033[96m {}\033[00m" .format('\n'+msg))


class system_setup:
    def basic_setup():
        os.system("sudo apt update")
        os.system("sudo apt install git curl ssh wget -y")
    
    def pulseAudio():
        os.system("sudo apt install pulseaudio pavucontrol -y")
        print(Green("Pulse audio installed sucessfully\n"))

    def configure_preload():
        sysmem = str(subprocess.check_output("grep MemTotal /proc/meminfo",shell=True).decode("utf-8")).split()[1]
        if int(sysmem) >= 4000000:
            os.system("sudo apt install preload -y")
            print(Green("Preload installed sucessfully\n"))
            print(Yellow("Check preload status by 'sudo systemctl status preload'\n"))
        else:
            print(Red("Preload is only advisable for 4GB+ installed RAM...\n"))

    def fix_amdgpu_drivers():
            os.system("sudo apt purge *nvidia*")
            print(Cyan("\nRemoved proprietary nvidia drivers!..\n"))
            os.system("echo 'deb http://deb.debian.org/debian buster main contrib non-free' | sudo tee -a /etc/apt/sources.list")
            print(Cyan("\nUpdating packages and repo!..\n"))
            os.system("sudo apt update")
            print(Yellow("\nFixing AMD GPU drivers!...\n"))
            os.system("sudo apt-get install firmware-amd-graphics libgl1-mesa-dri libglx-mesa0 mesa-vulkan-drivers xserver-xorg-video-all firmware-linux firmware-linux-nonfree libdrm-amdgpu1 xserver-xorg-video-amdgpu -y")
            print(Green("AMD GPU drivers installed sucessfully!..\nReboot to see changes\n"))

class softwares:
    def brave_browser():
        os.system("sudo apt install apt-transport-https curl -y")
        time.sleep(0.2)
            
        os.system("sudo curl -fsSLo /usr/share/keyrings/brave-browser-archive-keyring.gpg https://brave-browser-apt-release.s3.brave.com/brave-browser-archive-keyring.gpg")
        time.sleep(0.2)
            
        print(Cyan("Wait.. Adding brave-browser repository to system!\n"))
        os.system('echo "deb [signed-by=/usr/share/keyrings/brave-browser-archive-keyring.gpg arch=amd64] https://brave-browser-apt-release.s3.brave.com/ stable main"|sudo tee /etc/apt/sources.list.d/brave-browser-release.list')
        os.system('sudo apt update')
        time.sleep(0.2)

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

class desnap_ubuntu:
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

    def remove_snap():
        current_path = os.getcwd()+"/Files/"
        packages_name = open(f"{current_path}snap-list.txt","r+")
        snap_list = packages_name.readlines()
        if snap_list != None or []:
            for package in snap_list:
                os.system(f"sudo snap remove --purge {package}")#removing each snap packages
                os.system("sudo apt remove --autoremove snapd -y")#removing snap itself!
                break
            print(Cyan("Wait ..."))
            time.sleep(0.3)
            desnap_ubuntu.nosnap()# calling nosnap preference 

            print(Yellow("Snap removed from system!.."))
            print(Cyan("Updating system one last time!.."))

            os.system("sudo apt update")#updating system

            print(Cyan("Installing software-store without snap!.."))
            os.system("sudo apt install --install-suggests gnome-software -y")#Installing gnome-software-store without snap
            
            ff_confirm = input(Purple("\nNow firefox has removed from system. Do you want to install it again? [Y/n]"))#asking about firefox reinstallation!
            if ff_confirm.lower() == "y":
                    desnap_ubuntu.firefox_deb()#installing firefox as non snap package
            else:
                print(Green("Script sucessful \n Happy coding!.."))
        else:
            print(Red("Unexpeted error in removing snap! try again.."))

class ui_setup:
    def theme_setup():
        current_path = os.getcwd()
        if os.path.exists(f"{current_path}/Files/theme-setup.zip"):
            os.chdir(f"{current_path}/Files/")
            os.system("sudo unzip -q theme-setup.zip")
            os.system("sudo mv .icons .themes ~/")
            print(Purple("Applying Theme!😀...\n"))
            os.chdir(f"{current_path}/")
            os.system("gsettings set org.gnome.desktop.interface gtk-theme Orchis-Dark-Dracula")
            os.system("gsettings set org.gnome.desktop.interface icon-theme WhiteSur-dark")
            os.system("gsettings set org.gnome.desktop.wm.preferences theme Orchis-Dark-Dracula")
            os.system("gsettings set org.gnome.desktop.interface cursor-theme Bibata-Original-Classic")
            print(Green("<<< Theme Applied succesfully >>>\n"))
        else:
            print(Red("theme-setup.zip not found!.."))

    def dynamic_wallpaper():
        current_dir = os.getcwd()
        if os.path.exists(f"{current_dir}/Files/Dynamic-Wallpapers.zip"):
            os.system("unzip -q Dynamic-Wallpapers.zip")
            os.chdir("Linux_Dynamic_Wallpapers/")
            os.system("./install.sh")
            os.chdir(f"{current_dir}/")
            print(Green("Dynamic Wallpapers installed Suceesfully!.."))
            print(Cyan("Go to apperence settings to apply it."))
        else:
            print(Red("Dynamic-Wallpapers.zip not found!.."))

    def grub_theme():
        current_dir = os.getcwd()
        if os.path.exists(f"{current_dir}/Files/grub-theme.zip"):
            os.system("unzip -q grub-theme.zip")
            os.chdir("darkmatter-grub-theme/")
            os.system("sudo python3 darkmatter-theme.py -i")
            time.sleep(0.2)
            os.chdir(f"{current_dir}/")
        else:
            print(Red("grub-theme.zip not found!.."))

class zsh_setup:
    def oh_my_zsh():
        current_sh = str(subprocess.check_output("echo $0",shell=True).decode("utf-8"))
        if current_sh == "zsh":
            os.sytem('sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"')
            print(Green("oh my zsh installed sucessfully!..\n"))
            time.sleep(0.4)
            print(Cyan("<<Theming zsh with powerlevel10k theme!>>\n"))
            if os.path.exists("zsh-setup.zip"):
                os.system("unzip zsh-setup.zip")
                os.system("sudo cp .zshrc .zshrc.pre-oh-my-zsh .p10k.zsh ~/")
            os.system('git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/themes/powerlevel10k')
        else:
            print(Red("Can't setup oh_my_zsh \n Try this script alone.."))

    def install_zsh():
        current_sh = str(subprocess.check_output("echo $0",shell=True).decode("utf-8"))
        if current_sh == "bash":
            os.system("sudo apt install zsh -y")
            print(Yellow("zsh installed sucessfully!..\n"))
            time.sleep(0.3)
            os.system("sudo chsh -s /bin/zsh")
            print(Green("Shell changed sucessfully!..\n Logout current session if dosen't work!.."))
            zsh_setup.oh_my_zsh()
        else:
            print(Red("zsh already exists!.."))



def check_root():# checking 
    if os.geteuid() != 0:
        exit(Red("You need to have root privileges to run this script.\n try running with sudo!"))

def check_distro():
    try:
        lsb_id = subprocess.check_output("lsb_release -i", shell=True).decode("utf-8")
        id = lsb_id.split(":")[-1].lower().strip()
    except Exception:
        id = ""
    return id

if __name__ == "__main__":
    check_root()
    if check_distro() == "debian" or "ubuntu":
        print(Cyan("\nStarting basic system setup!.. ⏳\n"))
        system_setup.basic_setup()
        lspci = str(subprocess.check_output("lspci -nn | grep VGA", shell=True).decode("utf-8"))
        if lspci.find("AMD")!= -1:
            system_setup.fix_amdgpu_drivers()
        system_setup.pulseAudio()
        system_setup.configure_preload()

        print(Purple("\nInstalling necessary softwares!..⌛️\n"))
        softwares.brave_browser()
        softwares.spotify()
        softwares.vscode()
        softwares.nodejs_install()
        
        if check_distro() == "ubuntu":
           ch=input(Purple("Iam not hater of Snap & Snap store\nBut its packages are too slow!\n Hence removing it makes sense!..\n Do you want to remove snap from ubuntu [Y/n]?")).lower()
           if ch == 'y':
               desnap_ubuntu.remove_snap()
        else:
            pass
        
        print(Yellow("\n Theming your Linux desktop!..🖌️ \n"))
        desk_env = subprocess.check_output("echo $XDG_CURRENT_DESKTOP",shell=True).decode("utf-8").strip()
        if desk_env == "GNOME":
            ui_setup.theme_setup()
            ui_setup.dynamic_wallpaper()
        ui_setup.grub_theme()

        print(Green("\n Theming your terminal!..🖌️ \n"))
        zsh_setup.install_zsh()

        print(Green(f"\n The script setted up the {check_distro()} desktop sucessfully"))
        d_ch=input(Yellow("Do you want to remove the files extracted/downloaded during this setup? [Y/n]")).lower()
        if d_ch=="y":
            curr_dir = os.getcwd()
            os.system(f"sudo rm -r {curr_dir}/Files")
        else:
            print(Green("Thank you for using the script.\n Check out me on https://github.com/vishvaa-vsk \n\n Happy Computing!..😀" ))      

    else:
        print(Red("Can't find your distribution type.. this is only for debian based distributions!."))