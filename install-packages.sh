Packages=(
    "linux-headers"
    "pipewire-pulse"
    "firefox"
    "qtile"
    "lightdm"
    "thunar"
    "ranger"
    "git"
    "neofetch"
    "picom"
    "neovim"
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
    "ttf-linux-libertine"
    "ttf-dejavu"
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
    "refind"
    "efibootmgr"
    "ttf-font-awesome"
    "ttf-jetbrains-mono-nerd"
)

sudo pacman --needed -Sy ${Packages[@]}

sudo pacman -S --needed git base-devel
git clone https://aur.archlinux.org/yay.git
cd yay
makepkg -si
cd ..
rm -rf yay

PackagesYay=(
    "betterlockscreen"
    "i3lock-color"
    "pacseek"
    "downgrade"
)

yay -Sy ${PackagesYay[@]}


#service
sudo systemctl enable NetworkManager.service
sudo systemctl enable lightdm.service
sudo systemctl enable betterlockscreen@$USER




