import os


def RunTools():
	print("""
╔════════════════════════╗
║    Initialize Tools    ║
╚════════════════════════╝
""")
	os.system('''
        sudo apt install -y \
            git \
            curl \
            wget \
            snapd \
            gpg \
            htop \
            npm \
            nodejs \
            python3 \
            python3-pip
	''')
	
	
	
	#Claude Code
	os.system('sudo npm install -g @anthropic-ai/claude-code -y')



def RunApps():
	print("""
╔═════════════════════════╗
║     Initialize Apps     ║
╚═════════════════════════╝
""")
	#Brave
	os.system('curl -fsS https://dl.brave.com/install.sh | sh')
	
	
	
	#Spotify
	os.system('''
		curl -sS https://download.spotify.com/debian/pubkey_C85668DF69375001.gpg | sudo gpg --dearmor --yes -o /etc/apt/trusted.gpg.d/spotify.gpg
		echo "deb https://repository.spotify.com stable non-free" | sudo tee /etc/apt/sources.list.d/spotify.list
		sudo apt-get update && sudo apt-get install spotify-client
	''')
	
	
	
	#VSCode
	os.system('''
		wget -qO- https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > packages.microsoft.gpg
		sudo install -o root -g root -m 644 packages.microsoft.gpg /usr/share/keyrings/packages.microsoft.gpg
		sudo sh -c 'echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/packages.microsoft.gpg] https://packages.microsoft.com/repos/code stable main" > /etc/apt/sources.list.d/vscode.list'
		sudo apt update
		sudo apt install code -y
	''')
	
	
	
	#Virtual Box
	os.system('sudo apt install virtualbox virtualbox-ext-pack -y')
	
	
	
	#Obsidian
	os.system('wget https://github.com/obsidianmd/obsidian-releases/releases/download/v1.9.14/obsidian_1.9.14_amd64.deb && sudo dpkg -i obsidian_1.9.14_amd64.deb')



def RunConfig():
	print("""
╔═══════════════════════════╗
║     Initialize Config     ║
╚═══════════════════════════╝
""")
	#Remove Firefox
	os.system('sudo apt purge firefox -y && sudo snap remove firefox -y')



	#Fix apps
	os.system(''' 
        gsettings set org.gnome.shell favorite-apps "$(gsettings get org.gnome.shell favorite-apps | sed "s/]$/, 'brave-browser.desktop', 'spotify.desktop', 'code.desktop', 'virtualbox.desktop', 'obsidian.desktop']/")"
    ''')
	
	
	
	
	#Organize folders
	os.system('cd ~/Documents && mkdir projects vms scripts obsidian')
	


    #Set color theme
	os.system(""" 
        gsettings set org.gnome.desktop.interface color-scheme 'prefer-dark
        PROFILE_ID=$(gsettings get org.gnome.Terminal.ProfilesList list | tr -d "[],' ")
        gsettings set org.gnome.Terminal.Legacy.Profile:/org/gnome/terminal/legacy/profiles:/:$PROFILE_ID/ background-color '#000000'
        gsettings set org.gnome.Terminal.Legacy.Profile:/org/gnome/terminal/legacy/profiles:/:$PROFILE_ID/ foreground-color '#FFFFFF'
        gsettings set org.gnome.Terminal.Legacy.Profile:/org/gnome/terminal/legacy/profiles:/:$PROFILE_ID/ use-theme-colors false   
	""")

    #Config layout
	os.system("""
        gsettings set org.gnome.shell.extensions.dash-to-dock dock-position 'BOTTOM'
        gsettings set org.gnome.shell.extensions.dash-to-dock extend-height false	   
	""")

	#Config keyboard
	#Open terminal alt+x
	os.system("""
		gsettings set org.gnome.settings-daemon.plugins.media-keys custom-keybindings \
		"['/org/gnome/settings-daemon/plugins/media-keys/custom-keybindings/custom0/']"

		gsettings set org.gnome.settings-daemon.plugins.media-keys.custom-keybinding:/org/gnome/settings-daemon/plugins/media-keys/custom-keybindings/custom0/ name 'Abrir Terminal'
		gsettings set org.gnome.settings-daemon.plugins.media-keys.custom-keybinding:/org/gnome/settings-daemon/plugins/media-keys/custom-keybindings/custom0/ command 'gnome-terminal'
		gsettings set org.gnome.settings-daemon.plugins.media-keys.custom-keybinding:/org/gnome/settings-daemon/plugins/media-keys/custom-keybindings/custom0/ binding '<Alt>x'		   
	""")



	#Open folder Super+E
	os.system("""
		gsettings set org.gnome.settings-daemon.plugins.media-keys custom-keybindings \
		"['/org/gnome/settings-daemon/plugins/media-keys/custom-keybindings/custom0/', '/org/gnome/settings-daemon/plugins/media-keys/custom-keybindings/custom1/']"

		gsettings set org.gnome.settings-daemon.plugins.media-keys.custom-keybinding:/org/gnome/settings-daemon/plugins/media-keys/custom-keybindings/custom1/ name 'Abrir Arquivos'
		gsettings set org.gnome.settings-daemon.plugins.media-keys.custom-keybinding:/org/gnome/settings-daemon/plugins/media-keys/custom-keybindings/custom1/ command 'nautilus'
		gsettings set org.gnome.settings-daemon.plugins.media-keys.custom-keybinding:/org/gnome/settings-daemon/plugins/media-keys/custom-keybindings/custom1/ binding '<Super>e'   
	""")



	#Interactive Screenshot
	os.system("""
		gsettings set org.gnome.settings-daemon.plugins.media-keys custom-keybindings \
		"['/org/gnome/settings-daemon/plugins/media-keys/custom-keybindings/custom0/', '/org/gnome/settings-daemon/plugins/media-keys/custom-keybindings/custom1/', '/org/gnome/settings-daemon/plugins/media-keys/custom-keybindings/custom2/']"

		gsettings set org.gnome.settings-daemon.plugins.media-keys.custom-keybinding:/org/gnome/settings-daemon/plugins/media-keys/custom-keybindings/custom2/ name 'Captura de Tela'
		gsettings set org.gnome.settings-daemon.plugins.media-keys.custom-keybinding:/org/gnome/settings-daemon/plugins/media-keys/custom-keybindings/custom2/ command 'gnome-screenshot -i'
		gsettings set org.gnome.settings-daemon.plugins.media-keys.custom-keybinding:/org/gnome/settings-daemon/plugins/media-keys/custom-keybindings/custom2/ binding '<Alt>c'
	""")

	#Blacklist KVM
	os.system("""
		sudo modprobe -r kvm_intel
		sudo modprobe -r kvm
		sudo modprobe -r irqbypass
		echo 'blacklist kvm' | sudo tee -a /etc/modprobe.d/blacklist.conf
		echo 'blacklist kvm_amd' | sudo tee -a /etc/modprobe.d/blacklist.conf
		echo 'blacklist kvm_intel' | sudo tee -a /etc/modprobe.d/blacklist.conf
		sudo update-initramfs -u
	""")

	#Off blank screen
	os.system('''
	gsettings set org.gnome.desktop.session idle-delay 0
	gsettings set org.gnome.desktop.screensaver lock-enabled false
	''')

	#Disable mouse accel
	os.system('for id in $(xinput list --id-only | grep -v 2); do xinput set-prop $id "libinput Accel Profile Enabled" 0 1; done')

if __name__ == '__main__':
	RunTools()
	RunApps()
	RunConfig()