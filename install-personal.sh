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
    "lightdm-webkit-theme-osmos"
    "visual-studio-code-bin"
    "onedrive-abraunegg"
    "onedrive_tray.git"
    "betterdiscord-installer"
)

pacman --needed -Sy ${Packages[@]}

betterdiscord-installer --no-sandbox

#keymap
localectl --no-convert set-x11-keymap pl

#root config
cp -rf faillock.conf /etc/security/faillock.conf
cp -rf hosts /etc/hosts



