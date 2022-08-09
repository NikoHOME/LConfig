Packages=(
    "gimp"
    "krita"
    "inkscape"
    "libreoffice-fresh"
    "qt"
    "discord"
)

pacman -Sy ${Packages[@]}

#lightdm theme
yay -S lightdm-webkit-theme-osmos

#vs code
yay -Suy visual-studio-code-bin

#onedrive
git clone https://aur.archlinux.org/onedrive-abraunegg.git
cd onedrive-abraunegg
makepkg -sci
cd ..
rm -rf onedrive-abraunegg

git clone https://github.com/DanielBorgesOliveira/onedrive_tray.git
cd onedrive_tray
mkdir build
cd build
qmake ../systray.pro
make install
cd ..
cd ..
rm -rf onedrive_tray

#better discord
git clone https://aur.archlinux.org/betterdiscord-installer.git
cd betterdiscord-installer
makepkg -sci
cd ..
rm -rf betterdiscord-installer

betterdiscord-installer --no-sandbox

#keymap
localectl --no-convert set-x11-keymap pl

#root config
cp -rf faillock.conf /etc/security/faillock.conf
cp -rf hosts /etc/hosts



