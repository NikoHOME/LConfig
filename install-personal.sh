Packages=(
    "gimp"
    "krita"
    "inkscape"
    "libreoffice-fresh"
    "qt"
    "discord"
    "kdenlive"
    "audacity"
    "breeze"
)

PackagesYay=(
    "visual-studio-code-bin"
    "onedrive-abraunegg"
    "onedrive_tray-git"
    "youtube-music-bin"
    "lightdm-settings"
    "lightdm-slick-greeter"
    "betterdiscord-installer"
    "sweet-gtk-theme-dark"
)

sudo pacman -Sy ${Packages[@]}

yay -Sy ${PackagesYay[@]}

betterdiscord-installer --no-sandbox

#keymap
localectl --no-convert set-x11-keymap pl

#root config
sudo cp -rf faillock.conf /etc/security/faillock.conf
#refind bootloader theme
sudo cp -rf refind/* /boot/EFI/refind/
#lighdm greeter
sudo cp -rf lightdm/* /etc/lightdm/


