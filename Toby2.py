import tkinter as tk
import random
import colorsys
import pygame
import os

# --- AUDIO SETUP ---
pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.mixer.init()
pygame.mixer.set_num_channels(8)

DEFAULT_DEATH = "roblox-oof.mp3"
PLACEHOLDER = "roblox-oof.mp3"
WARNING_SFX = "warning.mp3"
SIREN_SFX = "siren.mp3"

SPECIAL_DEATHS = {
    "minos": "minos-prime-death.mp3",
    "cat": "cat-death.mp3",
    "beast": "hollow-knight-death.mp3",
    "fnaf": "fnaf-power-out.mp3",
    "bummed": "falling.mp3",
    "loud": "explode.mp3",
}
BUTTON1_SFX = {
    "minos": "minos-punish.mp3",
    "cat": "cat.mp3",
    "beast": "beast-scream.mp3",
    "fnaf": "fnaf-beatbox.mp3",
    "bummed": "sad-spongebob.mp3",
    "loud": "chicken-loud.mp3",
}
BUTTON2_SFX = {
    "minos": "minos-crush.mp3",
    "cat": "cat.mp3",
    "beast": "trex-roar.mp3",
    "fnaf": "the-mimic.mp3",
    "bummed": "bruh.mp3",
    "loud": "wega.mp3",
}

# --- FACES ---
BASE_FACE_OPEN = "            █     \n            ██     \n             █    \n ████████    ██    \n ████████     ██    \n              ██    \n              ██    \n ████████     ██    \n ████████    ██    \n             █    \n            ██     \n            █     "
BASE_FACE_CLOSED = "             █     \n             ██     \n             ██    \n    ██       ██    \n    ██       ██    \n             ██    \n             ██    \n    ██       ██    \n    ██       ██    \n             ██    \n             ██     \n             █     "
BASE_FACE_SCARED = "                █████ \n              ██   ██ \n  ██████    ██     ██ \n █      █   ██     ██ \n  ██████    ██     ██ \n            ██     ██ \n  ██████    ██     ██ \n █      █   ██     ██ \n  ██████    ██     ██ \n              ██   ██ \n                █████"
BASE_FACE_DEAD = "  ██  ██        ██████▒   \n   ████         ███████▒  \n  ██  ██        ██   ▒██  \n                ██    ██  \n                ██   ▒██  \n                ███████▒  \n  ██  ██        ██████▒   \n   ████         ██        \n  ██  ██        ██        \n                ██        \n                ██        \n"
BASE_FACE_CURIOUS = "   ██                               \n    ██                              \n     ██                             \n      ██   ████████       ██        \n           ████████       ██        \n                          ██        \n                          ██        \n           ████████       ██        \n      ██   ████████       ██        \n      ██                  ██        \n      ██                  ██        \n                          ██        "

# --- UI SETUP ---
window = tk.Tk()
window.title("Pet Bot")
window.config(bg="black")
window.attributes("-topmost", True)

SIZE_W, SIZE_H = 450, 550
sw, sh = window.winfo_screenwidth(), window.winfo_screenheight()
window.geometry(f"{SIZE_W}x{SIZE_H}+{(sw//2)-(SIZE_W//2)}+{(sh//2)-(SIZE_H//2)}")

is_blinking = False
is_dying = False
is_hovering_x = False
is_hovering_help = False
is_meltdown = False
current_hue = 0.0
current_mode = "none"
last_dx, last_dy = 0, 0

# --- MELTDOWN COMPONENTS ---
countdown_win = None
countdown_label = None
time_left = 60

# --- COMPONENTS ---
rainbow_x = tk.Label(
    window, text="X", font=("Arial", 30, "bold"), bg="black", fg="white", cursor="hand2"
)
rainbow_x.place(x=20, y=20)

help_btn = tk.Label(
    window,
    text="?",
    font=("Arial", 20, "bold"),
    bg="black",
    fg="#555555",
    cursor="question_arrow",
)
help_btn.place(x=SIZE_W - 40, y=20)

label = tk.Label(
    window, text="", font=("Courier", 10), justify="left", bg="black", fg="#00FF00"
)
label.place(relx=0.5, rely=0.35, anchor="center")

mode_label = tk.Label(
    window, text="MODE: NONE", font=("Courier", 10, "bold"), bg="black", fg="#00FF00"
)
mode_label.place(relx=0.5, rely=0.58, anchor="center")

entry_label = tk.Label(
    window,
    text="TYPE KEYWORD + ENTER:",
    font=("Courier", 10, "bold"),
    bg="black",
    fg="#00FF00",
)
entry_label.place(relx=0.5, rely=0.65, anchor="center")

cmd_entry = tk.Entry(
    window,
    width=20,
    bg="#222222",
    fg="white",
    insertbackground="white",
    font=("Courier", 12, "bold"),
    bd=2,
    relief="sunken",
)
cmd_entry.place(relx=0.5, rely=0.72, anchor="center")

# --- FUNCTIONS ---


def force_focus():
    if not is_dying:
        cmd_entry.focus_force()


def play_audio(filename, loop=False):
    if os.path.exists(filename):
        try:
            pygame.mixer.Sound(filename).play(loops=-1 if loop else 0)
        except:
            pass


def trigger_meltdown(cmd_text):
    global is_meltdown, time_left, countdown_win, countdown_label
    if is_meltdown:
        return
    is_meltdown = True
    time_left = 60
    mode_label.config(text=f"{cmd_text.upper()}!")

    countdown_win = tk.Toplevel(window)
    countdown_win.overrideredirect(True)
    countdown_win.attributes("-topmost", True)
    countdown_win.config(bg="black")
    wx, wy = window.winfo_rootx(), window.winfo_rooty()
    countdown_win.geometry(f"200x60+{wx + (SIZE_W//2) - 100}+{wy - 70}")

    countdown_label = tk.Label(
        countdown_win, text="01:00", font=("Courier", 30, "bold"), bg="black", fg="red"
    )
    countdown_label.pack(expand=True)

    play_audio(WARNING_SFX, loop=True)
    play_audio(SIREN_SFX, loop=True)
    update_countdown()
    flash_red(True)
    open_minigame()


def update_countdown():
    global time_left, is_meltdown
    if not is_meltdown:
        return
    if time_left <= 0:
        on_x_click(None)
        return
    mins, secs = divmod(time_left, 60)
    countdown_label.config(text=f"{mins:02d}:{secs:02d}")
    time_left -= 1
    window.after(1000, update_countdown)


def flash_red(state):
    if not is_meltdown:
        return
    color = "red" if state else "yellow"
    for widget in [mode_label, entry_label, b1, b2, label]:
        widget.config(fg=color)
    window.after(3000, lambda: flash_red(not state))


def open_minigame():
    mg_win = tk.Toplevel(window)
    mg_win.overrideredirect(True)
    mg_win.attributes("-topmost", True)
    mg_win.config(bg="#111111", highlightbackground="red", highlightthickness=2)
    wx, wy = window.winfo_rootx(), window.winfo_rooty()
    mg_win.geometry(f"300x400+{wx - 310}+{wy}")

    tk.Label(
        mg_win,
        text="SEQUENCE OVERRIDE",
        bg="#111111",
        fg="red",
        font=("Courier", 12, "bold"),
    ).pack(pady=10)

    rounds_needed = 3
    current_round = 0
    sequence_clicked = 0
    buttons = []

    def press_logic(btn, val):
        nonlocal sequence_clicked, current_round
        if val == sequence_clicked + 1:
            sequence_clicked += 1
            btn.config(bg="green", fg="white", state="disabled")
            if sequence_clicked == 5:
                current_round += 1
                if current_round >= rounds_needed:
                    stop_meltdown(mg_win)
                else:
                    setup_round()
        else:
            sequence_clicked = 0
            for b in buttons:
                b.config(bg="white", fg="black", state="normal")

    def setup_round():
        nonlocal sequence_clicked, buttons
        sequence_clicked = 0
        for b in buttons:
            b.destroy()
        buttons.clear()
        order = list(range(1, 6))
        random.shuffle(order)
        for i in order:
            btn = tk.Button(mg_win, text=str(i), width=4, bg="white", fg="black")
            btn.config(command=lambda b=btn, val=i: press_logic(b, val))
            btn.place(x=random.randint(20, 240), y=random.randint(50, 330))
            buttons.append(btn)

    setup_round()


def stop_meltdown(mg_win):
    global is_meltdown
    is_meltdown = False
    mg_win.destroy()
    if countdown_win:
        countdown_win.destroy()
    for widget in [mode_label, entry_label, b1, b2, label]:
        widget.config(fg="#00FF00")
    mode_label.config(text="MODE: STABLE")
    pygame.mixer.stop()


def open_help(event=None):
    help_win = tk.Toplevel(window)
    help_win.overrideredirect(True)
    help_win.attributes("-topmost", True)
    help_win.config(bg="#111111", highlightbackground="#00FF00", highlightthickness=2)
    wx, wy = window.winfo_rootx(), window.winfo_rooty()
    screen_w = window.winfo_screenwidth()
    x_pos = wx + SIZE_W + 5
    if x_pos + 220 > screen_w:
        x_pos = wx - 225
    help_win.geometry(f"220x300+{x_pos}+{wy}")
    close_hitbox = tk.Frame(help_win, bg="#111111", cursor="hand2", width=40, height=40)
    close_hitbox.pack(anchor="ne")
    tk.Label(
        close_hitbox, text="X", bg="#111111", fg="#FF0000", font=("Arial", 12, "bold")
    ).place(relx=0.5, rely=0.5, anchor="center")
    close_hitbox.bind("<Button-1>", lambda e: help_win.destroy())
    tk.Label(
        help_win,
        text="--- COMMANDS ---",
        bg="#111111",
        fg="#00FF00",
        font=("Courier", 10, "bold"),
    ).pack(pady=(0, 5))
    tk.Label(
        help_win,
        text="\n".join(SPECIAL_DEATHS.keys()),
        bg="#111111",
        fg="white",
        font=("Courier", 12),
        justify="center",
    ).pack(expand=True, fill="both")
    help_win.focus_force()
    help_win.grab_set()


def clean_keyword(text):
    return "".join(filter(str.isalpha, text.lower()))


def get_keyword():
    raw = clean_keyword(cmd_entry.get())
    for key in SPECIAL_DEATHS:
        if key in raw:
            return key
    return raw


def set_mode(event=None):
    global current_mode
    val = cmd_entry.get().strip().lower()
    if val in ["self destruct", "explode", "times up"]:
        trigger_meltdown(val)
        cmd_entry.delete(0, tk.END)
        return
    kw = get_keyword()
    current_mode = kw if kw else "none"
    mode_label.config(text=f"MODE: {current_mode.upper()}")
    cmd_entry.delete(0, tk.END)


def update_face(dx, dy, closed=False):
    global last_dx, last_dy
    if not closed:
        last_dx, last_dy = dx, dy
    else:
        dx, dy = last_dx, last_dy
    if is_dying:
        face = BASE_FACE_DEAD
    elif is_hovering_help:
        face = BASE_FACE_CURIOUS
    elif is_hovering_x:
        face = BASE_FACE_SCARED
    elif closed:
        face = BASE_FACE_CLOSED
    else:
        face = BASE_FACE_OPEN
    lines = face.split("\n")
    padding = "\n" * max(0, 2 + int(dy))
    content = padding + "".join(
        [" " * max(0, 10 + int(dx)) + line + "\n" for line in lines]
    )
    label.config(text=content)


def global_track():
    if not is_dying and not is_blinking:
        mx, my = window.winfo_pointerxy()
        wx, wy = window.winfo_rootx() + (SIZE_W // 2), window.winfo_rooty() + (
            SIZE_H // 3
        )
        dx = int(max(-15, min(15, (mx - wx) / 60)))
        dy = int(max(-8, min(8, (my - wy) / 90)))
        update_face(dx, dy)
    window.after(30, global_track)


def btn_action(mode):
    mapping = BUTTON1_SFX if mode == 1 else BUTTON2_SFX
    play_audio(mapping.get(current_mode, PLACEHOLDER))


def on_x_click(event):
    global is_dying
    if is_dying:
        return
    is_dying = True
    update_face(0, 0)
    play_audio(SPECIAL_DEATHS.get(current_mode, DEFAULT_DEATH))
    window.after(3000, lambda: window.destroy())


# --- BUTTONS ---
btn_frame = tk.Frame(window, bg="black")
btn_frame.place(relx=0.5, rely=0.85, anchor="center")
b1 = tk.Button(
    btn_frame,
    text="ACTION 1",
    bg="black",
    fg="#00FF00",
    font=("Arial", 10, "bold"),
    command=lambda: btn_action(1),
    width=10,
    relief="flat",
    bd=0,
)
b1.pack(side="left", padx=10)
b2 = tk.Button(
    btn_frame,
    text="ACTION 2",
    bg="black",
    fg="#00FF00",
    font=("Arial", 10, "bold"),
    command=lambda: btn_action(2),
    width=10,
    relief="flat",
    bd=0,
)
b2.pack(side="left", padx=10)


def start_move(event):
    window.x, window.y = event.x, event.y


def do_move(event):
    window.geometry(f"+{event.x_root - window.x}+{event.y_root - window.y}")


label.bind("<Button-1>", start_move)
label.bind("<B1-Motion>", do_move)
rainbow_x.bind("<Button-1>", on_x_click)
rainbow_x.bind("<Enter>", lambda e: set_hovering(True))
rainbow_x.bind("<Leave>", lambda e: set_hovering(False))
help_btn.bind("<Button-1>", open_help)
help_btn.bind("<Enter>", lambda e: set_help_hovering(True))
help_btn.bind("<Leave>", lambda e: set_help_hovering(False))
cmd_entry.bind("<Return>", set_mode)
window.bind("<Button-1>", lambda e: force_focus())
window.bind("<Escape>", lambda e: window.destroy())


def shift_rainbow():
    global current_hue
    rgb = [int(x * 255) for x in colorsys.hls_to_rgb(current_hue, 0.5, 1.0)]
    rainbow_x.config(fg=f"#{rgb[0]:02x}{rgb[1]:02x}{rgb[2]:02x}")
    current_hue = (current_hue + 0.02) % 1.0
    window.after(50, shift_rainbow)


def set_hovering(state):
    global is_hovering_x
    is_hovering_x = state


def set_help_hovering(state):
    global is_hovering_help
    is_hovering_help = state


def idle_blink():
    global is_blinking
    if not is_dying and not is_hovering_x and not is_hovering_help:
        is_blinking = True
        update_face(0, 0, closed=True)
        window.after(150, stop_blink)
    window.after(random.randint(3000, 6000), idle_blink)


def stop_blink():
    global is_blinking
    is_blinking = False


# --- FINAL START ---
window.after(100, force_focus)
shift_rainbow()
global_track()
idle_blink()
cmd_entry.focus_set()
window.mainloop()
