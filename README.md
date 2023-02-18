# Dotfiles
## Screenshot

![2022-07-25-193510_1920x1080_scrot](https://user-images.githubusercontent.com/88329920/180839591-112717c1-f1f3-44e7-9ee7-cc5350ea9651.png)

## Info
WM : Qtile <br>
DM : LightDM <br>
Dmenu : rofi <br>
Term : Alacitty <br>
Gtk Theme : Sweet-Dark <br>
Fonts : Awesome Ubuntu Jetbrains <br>
Text Editor : nvim <br>
File Explorer : ranger / thunar <br>
Image Viewer : Eye of Gnome <br>
Video Player : mpv <br>
Audio Player : cmus <br> 
## Warning
The personal installation script modifies root configuration files and changes keymap to polish
## Additional packages
gimp <br>
inkscape <br>
krita <br>
libreoffice <br>
vscode <br>
discord <br>
onedrive <br>
kdenlive <br>
audacity <br>
better-discord <br>

## Installation
```
git clone https://github.com/NikoHOME/dotfiles.git
cd dotfiles
chmod +x ./install-packages.sh
sudo ./install-packages.sh
chmod +x ./install-config.sh
sudo ./install-config.sh
```
One line version
```
git clone https://github.com/NikoHOME/dotfiles.git && cd dotfiles && chmod +x ./install-packages.sh && sudo ./install-packages.sh && chmod +x ./install-config.sh && sudo ./install-config.sh
```
For additional packages <br>
```
chmod +x ./install-personal.sh && ./install-personal.sh
```



