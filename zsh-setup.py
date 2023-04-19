import os
import subprocess
import time

def install_zsh():
    current_sh = str(subprocess.check_output("echo $0",shell=True).decode("utf-8"))
    if current_sh == "bash":
        os.system("sudo apt install zsh -y")
        print("zsh installed sucessfully!..")
        time.sleep(0.3)
        os.system("sudo chsh -s /bin/zsh")
        print("Shell changed sucessfully!.")
    else:
        print("zsh already exists!..")

def oh_my_zsh():
    current_sh = str(subprocess.check_output("echo $0",shell=True).decode("utf-8"))
    if current_sh == "zsh":
        os.sytem('sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"')
        print("\n oh my zsh installed sucessfully!..\n")
        time.sleep(0.4)
        print("\n<<Theming zsh with powerlevel10k theme!>>\n")
        if os.path.exists("zsh-setup.zip"):
            os.system("unzip zsh-setup.zip")
            os.system("sudo cp .zshrc .zshrc.pre-oh-my-zsh .p10k.zsh ~/")
        os.system('git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/themes/powerlevel10k')
    else:
        print("\nCan't setup oh_my_zsh")