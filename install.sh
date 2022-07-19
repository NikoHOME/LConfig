#pacman -Sy firefox thunar ranger git neofetch picom neovim lightdm-webkit2-greeter fish dmenu rofi python python-psutil python-iwlib alsa-utils ttf-ubuntu-font-family ttf-font-awesome

git clone https://github.com/NikoHOME/dotfiles
cd dotfiles
cp -rf config/* ~/.config
cd ~/dotfiles/theme

cp -rf Sweet-Dark-v40 /usr/share/themes
echo "gtk-icon-theme-name = \"Adwaita\"                                                                              
    gtk-theme-name = \"Sweet-Dark-v40\"
    gtk-font-name = \"Cantarell 11\"">/usr/share/gtk-2.0/gtkrc

echo "[Settings]
gtk-icon-theme-name = Adwaita
gtk-theme-name = Sweet-Dark-v40
gtk-font-name = Cantarell 11">/usr/share/gtk-3.0/settings.ini

rm -rf Sweet-Dark-v40
cd ~
rm -rf dotfiles
