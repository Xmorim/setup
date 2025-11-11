#libs
import os

#==============#
# Dependencies #
#==============#

def RunDependencies():
    print('''
╔═══════════════════════════════════════════════╗
║              Initialize Updates               ║
╚═══════════════════════════════════════════════╝
    ''')
    #Docker Dependencies
    def DockerDependencies():
        os.system(''' 
            sudo apt update && sudo apt upgrade -y
            sudo apt install -y ca-certificates curl gnupg lsb-release
            sudo install -m 0755 -d /etc/apt/keyrings
            curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
            sudo chmod a+r /etc/apt/keyrings/docker.gpg
            echo \
            "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
            $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
            sudo apt update && sudo apt upgrade -y
        ''')
    DockerDependencies()

    #VSCode Dependencies
    def VScodeDependencies():
            os.system('''
                sudo apt install -y wget gpg
                wget -qO- https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > packages.microsoft.gpg
                sudo install -D -o root -g root -m 644 packages.microsoft.gpg /etc/apt/keyrings/packages.microsoft.gpg
                echo "deb [arch=amd64,arm64,armhf signed-by=/etc/apt/keyrings/packages.microsoft.gpg] https://packages.microsoft.com/repos/code stable main" | sudo tee /etc/apt/sources.list.d/vscode.list > /dev/null
                sudo apt update -y
            ''')
    VScodeDependencies()

    #Spotify Dependencies
    def SpotifyDependencies():
        os.system('''
            curl -sS https://download.spotify.com/debian/pubkey_C85668DF69375001.gpg | sudo gpg --dearmor --yes -o /etc/apt/trusted.gpg.d/spotify.gpg
            echo "deb https://repository.spotify.com stable non-free" | sudo tee /etc/apt/sources.list.d/spotify.list
            sudo apt-get update -y
        ''')
    SpotifyDependencies()



#=============#
#    Tools    #
#=============#

def RunTools():
    print('''
╔═══════════════════════════════════════════════╗
║               Initialize Tools                ║
╚═══════════════════════════════════════════════╝
''')
    def brave():
        os.system('curl -fsS https://dl.brave.com/install.sh | sh')
    brave()
    
    def docker():
        os.system('sudo apt install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin')
    docker()

    def npm():
        os.system('sudo apt install npm -y')
    npm()

    def git():
        os.system('sudo apt install git -y')
    git()

    def nodejs():
        os.system('sudo apt install nodejs -y')
    nodejs()

    def claudecode():
        os.system('sudo npm install -g @anthropic-ai/claude-code -y')
    claudecode()



#=============#
#     Apps    #
#=============#

def RunApps():
    print('''
╔═══════════════════════════════════════════════╗
║               Initialize Apps                 ║
╚═══════════════════════════════════════════════╝
''')
    def vscode():
        os.system('sudo apt install code -y')
    vscode()

    def spotify():
        os.system('sudo apt install spotify-client -y')
    spotify()

    def obsidian():
        os.system('''
            wget https://github.com/obsidianmd/obsidian-releases/releases/download/v1.9.14/obsidian_1.9.14_amd64.deb
            sudo dpkg -i obsidian_1.9.14_amd64.deb
        ''')
    obsidian()

    def virtualbox():
        os.system('sudo apt install -y virtualbox virtualbox-ext-pack')
    virtualbox()



#=============#
#    Config   #
#=============#

def RunConfig():
    print('''
╔═══════════════════════════════════════════════╗
║              Initialize Config                ║
╚═══════════════════════════════════════════════╝
''')
    #Apply Dark Theme
    os.system("gsettings set org.gnome.desktop.interface color-scheme 'prefer-dark'")

    #Open interactive screencshot in alt+c
    os.system("gsettings set org.gnome.shell.keybindings show-screenshot-ui \"['<Alt>c']\"")

    #Open new terminal window in alt+x
    os.system("gsettings set org.gnome.settings-daemon.plugins.media-keys terminal \"['<Alt>x']\"")

    #Open folders in super+e
    os.system("gsettings set org.gnome.settings-daemon.plugins.media-keys home \"['<super>e']\"")

    #Create organized folders
    os.system('''
        cd ~/Documents
        mkdir obsidian projects vms
        cd obsidian && mkdir vaults
    ''')

    #Pin apps
    os.system('gsettings set org.gnome.shell favorite-apps "[\'code.desktop\', \'virtualbox.desktop\', \'spotify.desktop\', \'obsidian.desktop\', \'brave-browser.desktop\']"')



if __name__ == '__main__':
    RunDependencies()
    RunTools()
    RunApps()
    RunConfig()