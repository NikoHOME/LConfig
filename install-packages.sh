Packages=(
    "linux-headers"
    "pulseaudio"
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
    "imagemagick"
    "bc"
    "alsa-utils"
    "ttf-ubuntu-font-family"
    "ttf-font-awesome"
    "ttf-jetbrains-mono"
    "noto-fonts"
    "noto-fonts-emoji"
    "noto-fonts-cjk"
    "noto-fonts-extra"
    "xorg-mkfontdir"
    "xorg"
    "htop"
    "scrot"
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
    "galculator"
    "gparted"
    "pacseek"
)

pacman --needed -Sy ${Packages[@]}

pacman -S --needed git base-devel
git clone https://aur.archlinux.org/yay.git
cd yay-bin
makepkg -si
cd ..
rm -rf yay-bin

PackagesYay=(
    "betterlockscreen"
    "i3lock-color"
    "sweet-dark-theme"
)

yay --needed -S ${PackagesYay[@]}

#service
systemctl enable NetworkManager.service
systemctl enable lightdm.service
systemctl enable betterlockscreen@$USER




