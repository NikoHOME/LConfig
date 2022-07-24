Packages =(
    "firefox "
    "qtile "
    "lightdm "
    "thunar "
    "ranger "
    "git "
    "neofetch "
    "picom "
    "neovim "
    "lightdm-webkit2-greeter "
    "fish "
    "dmenu "
    "rofi "
    "python "
    "python-psutil "
    "python-iwlib "
    "alsa-utils "
    "ttf-ubuntu-font-family "
    "ttf-font-awesome "
    "noto-fonts-emoji "
    "udisks2 "
    "udiskie "
    "ntfs-3g " 
    "pavucontrol "
    "networkmanager "
    "eog "
    "mpv "
)

pacman -Sy $Packages

#yay
pacman -S --needed git base-devel && git clone https://aur.archlinux.org/yay.git && cd yay && makepkg -si

#fish
echo /usr/bin/fish | sudo tee -a /etc/shells
chsh -s /usr/bin/fish


curl https://raw.githubusercontent.com/oh-my-fish/oh-my-fish/master/bin/install | fish
fish
omf install slacker

#config

cp -rf config/* .config
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

#service
systenctl enable NetworkManager.service
systemctl enable lightdm.service



