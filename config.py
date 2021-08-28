from typing import List
from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
import os

mod = "mod4"

keys = [
    # Switch between windows
    Key([mod], "Left",             lazy.layout.left()),
    Key([mod], "Right",            lazy.layout.right()),
    Key([mod], "Down",             lazy.layout.down()),
    Key([mod], "Up",               lazy.layout.up()),
    Key([mod], "space",            lazy.layout.next()),

    Key([mod, "shift"], "Left",    lazy.layout.shuffle_left()),
    Key([mod, "shift"], "Right",   lazy.layout.shuffle_right()),
    Key([mod, "shift"], "Down",    lazy.layout.shuffle_down()),
    Key([mod, "shift"], "Up",      lazy.layout.shuffle_up()),

    Key([mod, "control"], "Left",  lazy.layout.grow_left()),
    Key([mod, "control"], "Right", lazy.layout.grow_right()),
    Key([mod, "control"], "Down",  lazy.layout.grow_down()),
    Key([mod, "control"], "Up",    lazy.layout.grow_up()),
    Key([mod], "n",                lazy.layout.normalize()),

    Key([mod, "shift"], "Return",  lazy.layout.toggle_split()),
    Key([mod], "Return",           lazy.spawn("kitty")),

    # Toggle between different layouts as defined below
    Key([mod], "Tab",              lazy.next_layout()),
    Key([mod], "q",                lazy.window.kill()),

    Key([mod, "shift"], "r",       lazy.restart()),
    Key([mod, "control"], "q",     lazy.shutdown()),
    Key([mod], "r",                lazy.spawncmd()),

    Key([mod], "d",                lazy.spawn("rofi -show drun -color-normal '#000,  #fff, #000, #090909, #C905EC' -color-active '#C905EC,  #fff,  #C905EC,  #C905EC,  #fff' -color-window '#000, #C905EC, #C905EC' -font 'mononoki NF 12'")),
    Key([mod], "F1",               lazy.spawn("qutebrowser")),
    Key([mod], "F2",               lazy.spawn("brightnessctl s 7-")),
    Key([mod], "F3",               lazy.spawn("brightnessctl s +7")),
    Key([mod], "s",                lazy.spawn("code-insiders")),
    Key([mod], "F4",               lazy.spawn("kitty nnn -d")),
    Key([mod], "Print",            lazy.spawn("xfce4-screenshooter")),
    Key([mod], "n",                lazy.spawn("picom -o 0.7 -D 3")),
    Key([mod], "c",                lazy.spawn("volumeicon")),
    Key([mod], "v",                lazy.spawn("nm-applet")),
    Key([mod], "b",                lazy.spawn("pamac-tray")),
    Key([mod], "z",                lazy.spawn("xfce4-power-manager")),
    Key([mod], "m",                lazy.spawn("kitty mocp")),
    Key([mod], "l",                lazy.spawn("kitty cmatrix -b  -r")),
    Key([mod], "w",                lazy.spawn("feh --bg-fill /home/martin/Downloads/52896-programacion.png")),

    # Tmux

	Key([mod, "control"],"t",      lazy.spawn("tmux new-session -s 'mySession' -d && tmux split-window -v && tmux split-window -h && tmux select-pane -t 0 && tmux split-window -h && tmux select-pane -t 1 && tmux -2 attach-session -d")),
    Key([mod, "control"],"1",          lazy.spawn("tmux select-pane -t 0")),
    Key([mod, "control"],"2",          lazy.spawn("tmux select-pane -t 1")),
    Key([mod, "control"],"3",          lazy.spawn("tmux select-pane -t 2")),
    Key([mod, "control"],"4",          lazy.spawn("tmux select-pane -t 3"))
]

__groups = {
    1: Group("  "),
    2: Group("  ", matches = [Match(wm_class = ["qutebrowser"])]),
    3: Group("  ", matches = [Match(wm_class = ["code-insiders", "subl"])]),
    4: Group("  ", matches = [Match(wm_class = ["virtualbox", "kitty mocp"])]), 
    5: Group("  "),
    6: Group("  ", matches = [Match(wm_class = ["zoom"])]),
}

groups = [__groups[i] for i in __groups]

def get_group_key(name):
    return [k for k, g in __groups.items() if g.name == name][0]

for i in groups:
    keys.extend([
        # mod1 + letter of group = switch to group
        Key([mod], str(get_group_key(i.name)), lazy.group[i.name].toscreen(), desc="Switch to group {}".format(i.name)),

        # mod1+shift+letter of group = switch to & move focused window to group
        Key([mod, "shift"], str(get_group_key(i.name)), lazy.window.togroup(i.name, switch_group=True), desc="Switch to & move focused window to group {}".format(i.name)),
    ])

layouts = [
    layout.Columns(
        border_focus = '#C905EC',
        border_normal = "#000000",
        border_width = 1,
        margin = 3
    ),

    layout.Max(),
]

widget_defaults = dict(
    font = 'mononoki Nerd Font Bold',
    fontsize = 13,
    padding = 2,
    background = "#000000"
)

extension_defaults = widget_defaults.copy()

def back():
    "#000"

screens = [
    Screen(
        top = bar.Bar([
                widget.GroupBox(
                    highlight_color = "#250100",
                    highlight_method = "line",
                    background = "#000000",
                    fontsize = 16,
                    active = "#C905EC",
                    spacing = 0,
                    block_highlight_text_color="#ffffff"
                ),

		        widget.Sep(
                    background = back(),
                    foreground = "#C905EC"
                ),

                widget.Prompt(),

                widget.WindowName(
                    max_chars = 20,
                    foreground = "#C905EC"
                ),

                widget.Chord(
                    chords_colors = {
                        'launch': (
                            "#C905EC",
                            "#ffffff"
                        ),
                    },

                    name_transform = lambda name: name.upper(),
                ),

                widget.Sep(
                    background = "#000000",
                    foreground = "#C905EC"
                ),

                widget.Moc(max_chars=1,
                    background = "#000000",
                    play_color = "#C905EC",
                    noplay_color = "#ffffff"
                ),

                widget.Sep(
                    background = "#000000",
                    foreground = "#C905EC"
                ),
                
                widget.TextBox(
                    "",
                    background = "#000000"
                ),

                widget.ThermalSensor(
                    background = "#000000"
                ),

                widget.Sep(
                    background = "#000000",
                    foreground = "#C905EC"
                ),

				widget.TextBox(
                    " ",
                    background = "#000000"
                ),

                widget.NetGraph(
                    border_color = "#000000",
                    fill_color = "#C905EC",
                    graph_color = "#C905EC"
                ),
				
                widget.Sep(
                    background = "#000000",
                    foreground = "#C905EC"
                ),
				
                widget.TextBox(
                    " ",
                    background = "#000000"
                ),
				
                widget.CPUGraph(
                    border_color = "#000000",
                    fill_color = "#C905EC",
                    graph_color = "#C905EC"
                ),

                widget.Sep(
                    background = "#000000",
                    foreground = "#C905EC"
                ),
                
#                widget.TextBox(
#                    "",
#                    background = "#000000"
#                ),
                
#                widget.Battery(
#                    background = "#000000",
#                    foreground = "#ffffff",
#                    format = '{char} {percent:2.0%}'
#                ),

                
                widget.TextBox(
                    " ",
                    background = "#000000"
                ),
                
                widget.Clock(
                    format = '%d-%m-%Y %a %I:%M %p',
                    background = "#000000"
                ),
                
                widget.Sep(
                    background = "#000000",
                    foreground = "#C905EC"
                ),
                
                widget.Systray(
                    background = "#000000"
                ),
            ],
            24,
            margin = 0,
            opacity = 0.91
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1",  lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3",  lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None

dgroups_app_rules = []  # type: List

main = None  # WARNING: this is deprecated and will be removed soon

follow_mouse_focus = True

bring_front_click = False

cursor_warp = False

floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    
    Match(wm_class = 'confirmreset'),  # gitk

    Match(wm_class = 'makebranch'),  # gitk
    
    Match(wm_class = 'maketag'),  # gitk
    
    Match(wm_class = 'ssh-askpass'),  # ssh-askpass
    
    Match(title    = 'branchdialog'),  # gitk
    
    Match(title    = 'pinentry'),  # GPG key password entry
])

auto_fullscreen = True

focus_on_window_activation = "smart"

wmname = "LG3D"

autostart = [
    "feh --bg-fill /home/martin/Downloads/407941.png",
    "setxkbmap es"
]

for x in autostart:
    os.system(x)
