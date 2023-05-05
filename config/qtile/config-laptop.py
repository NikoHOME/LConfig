# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import os
import re
import socket
import subprocess
from libqtile import qtile
from libqtile.config import Click, Drag, Group, KeyChord, Key, Match, Screen, ScratchPad, DropDown
from libqtile.command import lazy
from libqtile import layout, bar, widget, hook
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
# logger
#from libqtile.log_utils import logger

mod = "mod4"
#terminal = alacritty
terminal = guess_terminal()

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "Left", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "Right", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "Down", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "Up", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(),
        desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "Left", lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod, "shift"], "Right", lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, "shift"], "Down", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "Up", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "mod1"], "Left", lazy.layout.grow_left(),
        desc="Grow window to the left"),
    Key([mod, "mod1"], "Right", lazy.layout.grow_right(),
        desc="Grow window to the right"),
    Key([mod, "mod1"], "Down", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "mod1"], "Up", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "q", lazy.reload_config(), desc="Reload the config"),

    Key([mod], "a",         lazy.spawn("rofi -show run"),),
    Key([mod], "s",         lazy.spawn("rofi -show drun"),),
    Key(["mod1"], "Tab",    lazy.spawn("rofi -show  window"),),
    Key([mod], "q",         lazy.spawn("/home/linus/.config/qtile/bin/rofi-close.sh"),),
    Key([mod], "d",         lazy.spawn("/home/linus/.config/qtile/bin/rofi-fav.sh"),),
    Key([mod], "o",         lazy.spawn("betterlockscreen -l dim"), ),
    Key(["control"], "2",   lazy.spawn("/home/linus/.config/qtile/bin/network-dmenu"),),

    Key([mod], "Print", lazy.spawn("scrot -s /home/linus/scrot/%Y-%m-%d_$wx$h.png")),

    Key([], "XF86AudioMute",            lazy.spawn("amixer -D pulse sset Master toggle"),),
    Key([], "XF86AudioLowerVolume",     lazy.spawn("amixer -c 1 sset Master 2- unmute") ),
    Key([], "XF86AudioRaiseVolume",     lazy.spawn("amixer -c 1 sset Master 2+ unmute")),
    Key([], "XF86MonBrightnessUp",      lazy.spawn("brightnessctl -s set +50")),
    Key([], "XF86MonBrightnessDown",    lazy.spawn("brightnessctl -s set 50-")),

    Key([mod,"control"], "KP_Insert", lazy.spawn("alacritty -e /home/linus/.config/qtile/bin/disableliveaudio.sh") ),
    Key([mod], "KP_Insert", lazy.spawn("/home/linus/.config/qtile/bin/goliveaudio.sh") ),

    Key([], "KP_End",       lazy.spawn("mpv --audio-device=pulse/VirtualOutput --volume=40 /home/linus/.config/qtile/audio/1/1vineboom.mp3") ),
    Key([], "KP_Down",      lazy.spawn("mpv --audio-device=pulse/VirtualOutput --volume=40 /home/linus/.config/qtile/audio/1/2bruh.mp3") ),
    Key([], "KP_Next",      lazy.spawn("mpv --audio-device=pulse/VirtualOutput --volume=40 /home/linus/.config/qtile/audio/1/3clashroyalelaugh.mp3") ),
    Key([], "KP_Left",      lazy.spawn("mpv --audio-device=pulse/VirtualOutput --volume=30 /home/linus/.config/qtile/audio/1/4alert.mp3") ),
    Key([], "KP_Begin",     lazy.spawn("mpv --audio-device=pulse/VirtualOutput --volume=50 /home/linus/.config/qtile/audio/6/steve.mp3") ),
    Key([], "KP_Right",     lazy.spawn("mpv --audio-device=pulse/VirtualOutput --volume=30 /home/linus/.config/qtile/audio/1/6ohmygod.mp3") ),
    Key([], "KP_Home",      lazy.spawn("mpv --audio-device=pulse/VirtualOutput --volume=50 /home/linus/.config/qtile/audio/1/7aaashort.mp3") ),
    Key([], "KP_Up",        lazy.spawn("mpv --audio-device=pulse/VirtualOutput --volume=35 /home/linus/.config/qtile/audio/1/8fart.mp3") ),
    Key([], "KP_Prior",     lazy.spawn("mpv --audio-device=pulse/VirtualOutput --volume=50 /home/linus/.config/qtile/audio/1/9uwu.mp3") ),
    Key([], "KP_Insert",    lazy.ungrab_all_chords() ),
    Key([], "KP_Enter",    lazy.spawn("killall mpv") ),

    KeyChord([mod], "KP_End", [
        Key([], "KP_End",       lazy.spawn("mpv --audio-device=pulse/VirtualOutput --volume=50 /home/linus/.config/qtile/audio/2/bonk.mp3") ),
        Key([], "KP_Down",      lazy.spawn("mpv --audio-device=pulse/VirtualOutput --volume=50 /home/linus/.config/qtile/audio/2/bruh.mp3") ),
        Key([], "KP_Next",      lazy.spawn("mpv --audio-device=pulse/VirtualOutput --volume=50 /home/linus/.config/qtile/audio/2/clashroyalelaugh.mp3") ),
        Key([], "KP_Left",      lazy.spawn("mpv --audio-device=pulse/VirtualOutput --volume=50 /home/linus/.config/qtile/audio/2/goddamn.mp3") ),
        Key([], "KP_Begin",     lazy.spawn("mpv --audio-device=pulse/VirtualOutput --volume=50 /home/linus/.config/qtile/audio/2/ohmygod.mp3") ),
        Key([], "KP_Right",     lazy.spawn("mpv --audio-device=pulse/VirtualOutput --volume=50 /home/linus/.config/qtile/audio/2/reload.mp3") ),
        Key([], "KP_Home",      lazy.spawn("mpv --audio-device=pulse/VirtualOutput --volume=50 /home/linus/.config/qtile/audio/2/vineboom.mp3") ),
        Key([], "KP_Up",        lazy.spawn("mpv --audio-device=pulse/VirtualOutput --volume=50 /home/linus/.config/qtile/audio/2/woah.mp3") ),
        Key([], "KP_Prior",     lazy.spawn("mpv --audio-device=pulse/VirtualOutput --volume=50 /home/linus/.config/qtile/audio/2/yeet.mp3") ),
        Key([], "KP_Insert",    lazy.ungrab_all_chords() ),
        Key([], "KP_Enter",    lazy.spawn("killall mpv") )],
        mode="Sound2"
    ),
    KeyChord([mod], "KP_Down", [
        Key([], "KP_End",       lazy.spawn("mpv --audio-device=pulse/VirtualOutput --volume=50 /home/linus/.config/qtile/audio/3/alert.mp3") ),
        Key([], "KP_Down",      lazy.spawn("mpv --audio-device=pulse/VirtualOutput --volume=50 /home/linus/.config/qtile/audio/3/fart.mp3") ),
        Key([], "KP_Next",      lazy.spawn("mpv --audio-device=pulse/VirtualOutput --volume=50 /home/linus/.config/qtile/audio/3/fartwet.mp3") ),
        Key([], "KP_Left",      lazy.spawn("mpv --audio-device=pulse/VirtualOutput --volume=50 /home/linus/.config/qtile/audio/3/moai.mp3") ),
        Key([], "KP_Begin",     lazy.spawn("mpv --audio-device=pulse/VirtualOutput --volume=50 /home/linus/.config/qtile/audio/3/oof.mp3") ),
        Key([], "KP_Right",     lazy.spawn("mpv --audio-device=pulse/VirtualOutput --volume=50 /home/linus/.config/qtile/audio/3/spongebob-fail.mp3") ),
        Key([], "KP_Home",      lazy.spawn("mpv --audio-device=pulse/VirtualOutput --volume=50 /home/linus/.config/qtile/audio/3/spongebob-womp.mp3") ),
        Key([], "KP_Up",        lazy.spawn("mpv --audio-device=pulse/VirtualOutput --volume=50 /home/linus/.config/qtile/audio/3/tyler1gun.mp3") ),
        Key([], "KP_Prior",     lazy.spawn("mpv --audio-device=pulse/VirtualOutput --volume=50 /home/linus/.config/qtile/audio/3/tyler1gun.mp3") ),
        Key([], "KP_Insert",    lazy.ungrab_all_chords() ),
        Key([], "KP_Enter",    lazy.spawn("killall mpv") )],  
        mode="Sound3"
    ),
    KeyChord([mod], "KP_Next", [
        Key([], "KP_End",       lazy.spawn("mpv --audio-device=pulse/VirtualOutput --volume=50 /home/linus/.config/qtile/audio/4/aaa.mp3") ),
        Key([], "KP_Down",      lazy.spawn("mpv --audio-device=pulse/VirtualOutput --volume=50 /home/linus/.config/qtile/audio/4/aaaloud.mp3") ),
        Key([], "KP_Next",      lazy.spawn("mpv --audio-device=pulse/VirtualOutput --volume=50 /home/linus/.config/qtile/audio/4/aaashort.mp3") ),
        Key([], "KP_Left",      lazy.spawn("mpv --audio-device=pulse/VirtualOutput --volume=50 /home/linus/.config/qtile/audio/4/amogus.mp3") ),
        Key([], "KP_Begin",     lazy.spawn("mpv --audio-device=pulse/VirtualOutput --volume=50 /home/linus/.config/qtile/audio/4/amongus.mp3") ),
        Key([], "KP_Right",     lazy.spawn("mpv --audio-device=pulse/VirtualOutput --volume=50 /home/linus/.config/qtile/audio/4/amongusemergency.mp3") ),
        Key([], "KP_Home",      lazy.spawn("mpv --audio-device=pulse/VirtualOutput --volume=50 /home/linus/.config/qtile/audio/4/amongusstart.mp3") ),
        Key([], "KP_Up",        lazy.spawn("mpv --audio-device=pulse/VirtualOutput --volume=50 /home/linus/.config/qtile/audio/4/siuu.mp3") ),
        Key([], "KP_Prior",     lazy.spawn("mpv --audio-device=pulse/VirtualOutput --volume=50 /home/linus/.config/qtile/audio/4/yoda.mp3") ),
        Key([], "KP_Insert",    lazy.ungrab_all_chords() ),
        Key([], "KP_Enter",    lazy.spawn("killall mpv") )],  
        mode="Sound4"
    ),
    KeyChord([mod], "KP_Left", [
        Key([], "KP_End",       lazy.spawn("mpv --audio-device=pulse/VirtualOutput --volume=50 /home/linus/.config/qtile/audio/5/applause.mp3") ),
        Key([], "KP_Down",      lazy.spawn("mpv --audio-device=pulse/VirtualOutput --volume=50 /home/linus/.config/qtile/audio/5/creeper.mp3") ),
        Key([], "KP_Next",      lazy.spawn("mpv --audio-device=pulse/VirtualOutput --volume=50 /home/linus/.config/qtile/audio/5/discordcall.mp3") ),
        Key([], "KP_Left",      lazy.spawn("mpv --audio-device=pulse/VirtualOutput --volume=50 /home/linus/.config/qtile/audio/5/discordping.mp3") ),
        Key([], "KP_Begin",     lazy.spawn("mpv --audio-device=pulse/VirtualOutput --volume=50 /home/linus/.config/qtile/audio/5/fnaf.mp3") ),
        Key([], "KP_Right",     lazy.spawn("mpv --audio-device=pulse/VirtualOutput --volume=50 /home/linus/.config/qtile/audio/5/gtasa.mp3") ),
        Key([], "KP_Home",      lazy.spawn("mpv --audio-device=pulse/VirtualOutput --volume=50 /home/linus/.config/qtile/audio/5/knock.mp3") ),
        Key([], "KP_Up",        lazy.spawn("mpv --audio-device=pulse/VirtualOutput --volume=50 /home/linus/.config/qtile/audio/5/laugh.mp3") ),
        Key([], "KP_Prior",     lazy.spawn("mpv --audio-device=pulse/VirtualOutput --volume=50 /home/linus/.config/qtile/audio/5/laugh.mp3") ),
        Key([], "KP_Insert",    lazy.ungrab_all_chords() ),
        Key([], "KP_Enter",    lazy.spawn("killall mpv") )],  
        mode="Sound5"
    ),
    KeyChord([mod], "KP_Begin", [
        Key([], "KP_End",       lazy.spawn("mpv --audio-device=pulse/VirtualOutput --volume=50 /home/linus/.config/qtile/audio/6/ben-no.mp3") ),
        Key([], "KP_Down",      lazy.spawn("mpv --audio-device=pulse/VirtualOutput --volume=50 /home/linus/.config/qtile/audio/6/ben-yes.mp3") ),
        Key([], "KP_Next",      lazy.spawn("mpv --audio-device=pulse/VirtualOutput --volume=50 /home/linus/.config/qtile/audio/6/burglecall.mp3") ),
        Key([], "KP_Left",      lazy.spawn("mpv --audio-device=pulse/VirtualOutput --volume=50 /home/linus/.config/qtile/audio/6/sadtrumpet.mp3") ),
        Key([], "KP_Begin",     lazy.spawn("mpv --audio-device=pulse/VirtualOutput --volume=50 /home/linus/.config/qtile/audio/6/sadtrumpet2.mp3") ),
        Key([], "KP_Right",     lazy.spawn("mpv --audio-device=pulse/VirtualOutput --volume=50 /home/linus/.config/qtile/audio/6/steve.mp3") ),
        Key([], "KP_Home",      lazy.spawn("mpv --audio-device=pulse/VirtualOutput --volume=50 /home/linus/.config/qtile/audio/6/uwu.mp3") ),
        Key([], "KP_Up",        lazy.spawn("mpv --audio-device=pulse/VirtualOutput --volume=50 /home/linus/.config/qtile/audio/6/uwu.mp3") ),
        Key([], "KP_Prior",     lazy.spawn("mpv --audio-device=pulse/VirtualOutput --volume=50 /home/linus/.config/qtile/audio/6/uwu.mp3") ),
        Key([], "KP_Insert",    lazy.ungrab_all_chords() ),
        Key([], "KP_Enter",    lazy.spawn("killall mpv") )],  
        mode="Sound6"
    ),
    KeyChord([mod], "KP_Right", [
        Key([], "KP_End",       lazy.spawn("mpv --audio-device=pulse/VirtualOutput --volume=50 /home/linus/.config/qtile/audio/7/dababy.mp3") ),
        Key([], "KP_Down",      lazy.spawn("mpv --audio-device=pulse/VirtualOutput --volume=50 /home/linus/.config/qtile/audio/7/phub.mp3") ),
        Key([], "KP_Next",      lazy.spawn("mpv --audio-device=pulse/VirtualOutput --volume=50 /home/linus/.config/qtile/audio/7/sickomode.mp3") ),
        Key([], "KP_Left",      lazy.spawn("mpv --audio-device=pulse/VirtualOutput --volume=50 /home/linus/.config/qtile/audio/7/wolveskanye.mp3") ),
        Key([], "KP_Begin",     lazy.spawn("mpv --audio-device=pulse/VirtualOutput --volume=50 /home/linus/.config/qtile/audio/7/wolveskanye.mp3") ),
        Key([], "KP_Right",     lazy.spawn("mpv --audio-device=pulse/VirtualOutput --volume=50 /home/linus/.config/qtile/audio/7/wolveskanye.mp3") ),
        Key([], "KP_Home",      lazy.spawn("mpv --audio-device=pulse/VirtualOutput --volume=50 /home/linus/.config/qtile/audio/7/wolveskanye.mp3") ),
        Key([], "KP_Up",        lazy.spawn("mpv --audio-device=pulse/VirtualOutput --volume=50 /home/linus/.config/qtile/audio/7/wolveskanye.mp3") ),
        Key([], "KP_Prior",     lazy.spawn("mpv --audio-device=pulse/VirtualOutput --volume=50 /home/linus/.config/qtile/audio/7/wolveskanye.mp3") ),
        Key([], "KP_Insert",    lazy.ungrab_all_chords() ),
        Key([], "KP_Enter",    lazy.spawn("killall mpv") )],  
        mode="Sound7"
    ),
    KeyChord([mod], "KP_Home", [
        Key([], "KP_End",       lazy.spawn("mpv --audio-device=pulse/VirtualOutput --volume=50 /home/linus/.config/qtile/audio/8/araara1.mp3") ),
        Key([], "KP_Down",      lazy.spawn("mpv --audio-device=pulse/VirtualOutput --volume=50 /home/linus/.config/qtile/audio/8/araara2.mp3") ),
        Key([], "KP_Next",      lazy.spawn("mpv --audio-device=pulse/VirtualOutput --volume=50 /home/linus/.config/qtile/audio/8/araara3.mp3") ),
        Key([], "KP_Left",      lazy.spawn("mpv --audio-device=pulse/VirtualOutput --volume=50 /home/linus/.config/qtile/audio/8/jojo.mp3") ),
        Key([], "KP_Begin",     lazy.spawn("mpv --audio-device=pulse/VirtualOutput --volume=50 /home/linus/.config/qtile/audio/8/necoarc.mp3") ),
        Key([], "KP_Right",     lazy.spawn("mpv --audio-device=pulse/VirtualOutput --volume=50 /home/linus/.config/qtile/audio/8/ora.mp3") ),
        Key([], "KP_Home",      lazy.spawn("mpv --audio-device=pulse/VirtualOutput --volume=50 /home/linus/.config/qtile/audio/8/oraora.mp3") ),
        Key([], "KP_Up",        lazy.spawn("mpv --audio-device=pulse/VirtualOutput --volume=50 /home/linus/.config/qtile/audio/8/rezero.mp3") ),
        Key([], "KP_Prior",     lazy.spawn("mpv --audio-device=pulse/VirtualOutput --volume=50 /home/linus/.config/qtile/audio/8/rezero.mp3") ),
        Key([], "KP_Insert",    lazy.ungrab_all_chords() ),
        Key([], "KP_Enter",    lazy.spawn("killall mpv") )],  
        mode="Sound8"
    )    
]

groups = [Group("1", layout='columns', label="DEV"),
          Group("2", layout='columns', spawn='firefox', label="WWW"),
          Group("3", layout='columns', spawn='alacritty', label="SYS"),
          Group("4", layout='columns', spawn='alacritty -e ranger', label="SYS"),
          Group("5", layout='columns', matches=[Match(wm_class='-discord')], label="DIS"),
          Group("6", layout='floating', matches=[Match(wm_class='-steam')], label="STM"),
          Group("7", layout='monadtall', matches=[Match(wm_class='-minecraft')],label="VID"),
          Group("8", layout='monadtall', label="DOC"),
          Group("9", layout='floating', label="DOC")]


layout_theme = {"border_width": 2,
                "margin": 8,
                "border_focus": "800080",
                "border_normal": "625790"
                }

prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())


for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(
                    i.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

groups.append(ScratchPad('dropdown', [
    DropDown('mixer', 'pavucontrol', x=0.25, y=0.25, width=0.5,
             height=0.5, opacity=0.9, on_focus_lost_hide=False)
    #DropDown('wlan', 'nm-connection-editor', x=0.25, y=0.25, width=0.5,
    #         height=0.5, opacity=0.8, on_focus_lost_hide=False)
]))
keys.extend([
    Key(["control"], "1", lazy.group['dropdown'].dropdown_toggle('mixer'))
    #Key(["control"], "2", lazy.group['dropdown'].dropdown_toggle('wlan'))
])
layouts = [
    layout.Columns(
        border_width=2,
        border_focus="800080",
        border_normal="625790",
        margin=4,
        margin_on_single=2,
        border_on_single=1
    ),
    # layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    layout.MonadTall(
        border_width=2,
        border_focus="800080",
        border_normal="625790",
        margin=4,
        margin_on_single=2,
        border_on_single=1
    ),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    layout.Floating(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]
colors = [["#282c34", "#282c34"],
          ["#1c1f24", "#1c1f24"],
          ["#dfdfdf", "#dfdfdf"],
          ["#ff6c6b", "#ff6c6b"],
          ["#98be65", "#98be65"],
          ["#da8548", "#da8548"],
          ["#51afef", "#51afef"],
          ["#c678dd", "#c678dd"],
          ["#46d9ff", "#46d9ff"],
          ["#a9a1e1", "#a9a1e1"]]


widget_defaults = dict(
    font="Ubuntu Bold",
    fontsize=12,
    padding=2,
    background=colors[1]
)
extension_defaults = widget_defaults.copy()

widget_icon_size = 16

def init_widgets_list():
    widgets_list = [
        widget.Sep(
            linewidth=0,
            padding=6,
            foreground=colors[2],
            background=colors[0]
        ),
        widget.Image(
            filename="~/.config/qtile/img/cwz2.png",
            scale="False",
            background=colors[0],
            #mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(terminal)}
        ),
        widget.Sep(
            linewidth=0,
            padding=10,
            foreground=colors[2],
            background=colors[0]
        ),
        widget.GroupBox(
            font="Ubuntu Bold",
            fontsize=11,
            margin_y=3,
            margin_x=0,
            padding_y=5,
            padding_x=3,
            borderwidth=3,
            active=colors[2],
            inactive=colors[7],
            rounded=False,
            highlight_color=colors[1],
            highlight_method="line",
            this_current_screen_border=colors[6],
            this_screen_border=colors[4],
            other_current_screen_border=colors[6],
            other_screen_border=colors[4],
            foreground=colors[2],
            background=colors[0]
        ),
        widget.TextBox(
            text='|',
            font="Ubuntu Mono",
            background=colors[0],
            foreground='474747',
            padding=2,
            fontsize=14
        ),
        widget.CurrentLayoutIcon(
            custom_icon_paths=[os.path.expanduser("~/.config/qtile/icons")],
            foreground=colors[2],
            background=colors[0],
            padding=0,
            scale=0.9
        ),
        widget.CurrentLayout(
            foreground=colors[2],
            background=colors[0],
            padding=5
        ),
        widget.TextBox(
            text='|',
            font="Ubuntu Mono",
            background=colors[0],
            foreground='474747',
            padding=2,
            fontsize=14
        ),
        widget.WindowName(
            foreground=colors[6],
            background=colors[0],
            padding=0
        ),
        widget.Systray(
            background=colors[0],
            padding=5
        ),
        widget.Sep(
            linewidth=0,
            padding=6,
            foreground=colors[0],
            background=colors[0]
        ),
        widget.Image(
            filename='~/.config/qtile/img/arrow1.png',
            background=colors[0]
        ),
        widget.TextBox(
            text='',
            font="Font Awesome",
            foreground=colors[1],
            background=colors[3],
            padding=0,
            fontsize=widget_icon_size
        ),
        widget.Net(
            #interface = 'wlp0s20f0u1',
            format='Net:  {down} {up}',
            foreground=colors[1],
            background=colors[3],
            prefix='M',
            padding=5
        ),
        widget.Image(
            filename='~/.config/qtile/img/arrow2.png',
            background=colors[3]
        ),

#        widget.BatteryIcon(
#            foreground=colors[1],
#            background=colors[4],
#            theme_path='/home/linus/.config/qtile/theme',
#            scale = 1,
#            padding=0
#        ),
        widget.TextBox(
            text='',
            font="Font Awesome",
            foreground=colors[1],
            background=colors[4],
            padding=0,
            fontsize=widget_icon_size
        ),
        widget.Battery(
            foreground=colors[1],
            background=colors[4],
            charge_char='',
            discharge_char='',
            empty_char='',
            full_char='',
            low_percentage=0.2,
            format='Bat: {char} {percent:2.0%} {hour:d}:{min:02d}',
            notify_below=20,
            padding=5
        ),
        widget.Image(
            filename='~/.config/qtile/img/arrow3.png',
            background=colors[4]
        ),
        widget.Image(
            filename='~/.config/qtile/img/archicon.png',
            margin=2,
            background=colors[5]
        ),
        widget.CheckUpdates(
            update_interval = 1800,
            no_update_string="No Updates",
            colour_have_updates=colors[1],
            colour_no_updates=colors[1],
            foreground=colors[1],
            background=colors[5],
            padding=5,
            execute='exec alacritty -e sudo pacman -Syu'

        ),
        widget.Image(
            filename='~/.config/qtile/img/arrow4.png',
            background=colors[5]
        ),
        widget.TextBox(
            text='',
            font="Font Awesome",
            #font = "Ubuntu Mono",
            foreground=colors[1],
            background=colors[6],
            padding=0,
            fontsize=widget_icon_size
        ),
        widget.Memory(
            foreground=colors[1],
            background=colors[6],
            mouse_callbacks={'Button1': lambda: qtile.cmd_spawn(
                terminal + ' -e htop')},
            fmt='Mem: {}',
            padding=5
        ),
        widget.Image(
            filename='~/.config/qtile/img/arrow5.png',
            scale=1.5,
            background=colors[6]
        ),
        widget.TextBox(
            text='',
            font="Font Awesome",
            #text = '🔇',
            #text = '',
            foreground=colors[1],
            background=colors[7],
            padding=0,
            fontsize=widget_icon_size,
            mouse_callbacks={
                "Button1": lambda: qtile.cmd_simulate_keypress(["control"], "1")}
        ),
        widget.Volume(
            foreground=colors[1],
            background=colors[7],
            mute_command="amixer -D pulse sset Master toggle",
            fmt='Vol: {}',
            padding=5
        ),
        widget.Image(
            filename='~/.config/qtile/img/arrow6.png',
            scale=1.5,
            background=colors[7]
        ),
        widget.TextBox(
            text='',
            font="Font Awesome",
            #font = "Ubuntu Mono",
            foreground=colors[1],
            background=colors[8],
            padding=0,
            fontsize=widget_icon_size * 1.2,
            mouse_callbacks={
                "Button1": lambda: qtile.cmd_simulate_keypress(["control"], "2")}
            
        ),
        widget.Wlan(
            #interface = 'wlp0s20f0u1',
            disconnected_message="Disconnected",
            #format = 'Con: {quality}/70 {essid}',
            interface="wlan0",
            foreground=colors[1],
            background=colors[8],
            padding=5,
            mouse_callbacks={
                "Button1": lambda: qtile.cmd_simulate_keypress(["control"], "2")}
        ),
        widget.Image(
            filename='~/.config/qtile/img/arrow7.png',
            scale=1.5,
            background=colors[8]
        ),
        widget.TextBox(
            text='',
            font="Font Awesome",
            foreground=colors[1],
            background=colors[9],
            padding=0,
            # mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn("pavucontrol")},
            fontsize=widget_icon_size,
        ),
        widget.Clock(
            foreground=colors[1],
            background=colors[9],
            padding=5,
            markup=False,
            format="%A, %B %d - %H:%M "
        ),
    ]

    return widgets_list


def init_widgets_screen():
    widgets_screen = init_widgets_list()
    return widgets_screen


def init_screens():
    return [Screen(
        wallpaper='~/.config/qtile/img/background.jpg',
        wallpaper_mode='stretch',
        top=bar.Bar(widgets=init_widgets_screen(), opacity=1.0, size=24)
    )]


if __name__ in ["config", "__main__"]:
    screens = init_screens()
    widgets_list = init_widgets_list()
    widgets_screen = init_widgets_screen()

from floating_window_snapping import move_snap_window

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", 
        move_snap_window(snap_dist=30),
        start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.toggle_floating()),
    Click([mod], "Button1", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True


# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None


@hook.subscribe.startup
def autostartup():
    qtile.cmd_spawn("bash -c 'sleep 2; picom -b' &")


# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "qtile"
