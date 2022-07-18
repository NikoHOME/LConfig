if status is-interactive
    # Commands to run in interactive sessions can go here
    neofetch
    function fish_greeting
	set -l cyan (set_color -i cyan)
	echo "$fish$cyan"Linus Rules"$fish"
    end
    fish_vi_key_bindings
end
