Packages=(
    "firefox"
    "qtile"
    "lightdm"
    "thunar"
    "ranger"
    "git"
    "neofetch"
    "picom"
    "neovim"
    "lightdm-webkit2-greeter"
    "fish"
    "dmenu"
    "rofi"
    "python"
    "python-psutil"
    "python-iwlib"
    "alsa-utils"
    "ttf-ubuntu-font-family"
    "ttf-font-awesome"
    "ttf-jetbrains-mono"
    "noto-fonts-emoji"
    "xorg-mkfontdir"
    "xorg"
    "udisks2"
    "udiskie"
    "ntfs-3g" 
    "pavucontrol"
    "networkmanager"
    "nm-connection-editor"
    "eog"
    "mpv"
    "inetutils"
    "unzip"
)

pacman -Sy ${Packages[@]}
#fonts reorganize
#mkdir /usr/share/fonts/TTF
#mkdir /usr/share/fonts/OTF
#cp -rf /usr/share/fonts/*/*.ttf /usr/share/fonts/TTF
#cp -rf /usr/share/fonts/*/*.otf /usr/share/fonts/OTF

#yay
pacman -S --needed git base-devel && git clone https://aur.archlinux.org/yay.git && cd yay && makepkg -si
cd ..
rm -rf yay
#fish
echo /usr/bin/fish | sudo tee -a /etc/shells
chsh -s /usr/bin/fish


curl https://raw.githubusercontent.com/oh-my-fish/oh-my-fish/master/bin/install | fish
fish
omf install slacker

#rofi
git clone https://github.com/catppuccin/rofi.git
chmod +x rofi/install.sh
cd rofi
./install.sh
cd ..
rm -rf rofi
#config

cp -rf config/* .config
mkdir /usr/share/fonts/jetbrains-nerd
cp -rf fonts/* /usr/share/fonts/jetbrains-nerd
cp -rf faillock.conf /etc/security/faillock.conf

#theme
cp -rf theme/Sweet-Dark-v40 /usr/share/themes
mkdir /usr/share/gtk-2.0
touch /usr/share/gtk-2.0/gtkrc
echo "gtk-icon-theme-name = \"Adwaita\"                                                                              
    gtk-theme-name = \"Sweet-Dark-v40\"
    gtk-font-name = \"Cantarell 11\"">/usr/share/gtk-2.0/gtkrc

mkdir /usr/share/gtk-3.0
touch /usr/share/gtk-3.0/settings.ini
echo "[Settings]
gtk-icon-theme-name = Adwaita
gtk-theme-name = Sweet-Dark-v40
gtk-font-name = Cantarell 11">/usr/share/gtk-3.0/settings.ini

#keymap
localectl --no-convert set-x11-keymap pl

#service
systenctl enable NetworkManager.service
systemctl enable lightdm.service


# Better lock screen


