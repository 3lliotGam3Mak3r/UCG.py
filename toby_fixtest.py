import tkinter as tk
import random

window = tk.Tk()
window.title("Toby.Launch")
window.config(bg="black")
power_on = True

# --- SETTINGS ---
WIDTH, HEIGHT = 400, 450

# --- CENTER MAIN WINDOW ---
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x_c = int((screen_width / 2) - (WIDTH / 2))
y_c = int((screen_height / 2) - (HEIGHT / 2))
window.geometry(f"{WIDTH}x{HEIGHT}+{x_c}+{y_c}")

# --- YOUR ORIGINAL ASCII FACES ---
face_open = (
    "\n\n\n\n"
    "            █     \n"
    "            ██     \n"
    "             █    \n"
    " ████████    ██    \n"
    " ████████     ██    \n"
    "              ██    \n"
    "              ██    \n"
    " ████████     ██    \n"
    " ████████    ██    \n"
    "             █    \n"
    "            ██     \n"
    "            █     \n"
)

face_open_sad = (
    "\n\n\n\n"
    "               █     \n"
    "              ██     \n"
    "              █    \n"
    " ████████    ██    \n"
    " ████████   ██    \n"
    "            ██    \n"
    "            ██    \n"
    " ████████   ██    \n"
    " ████████    ██    \n"
    "              █    \n"
    "              ██     \n"
    "               █     \n"
)

face_talking = (
    "\n\n\n\n"
    """           █████   
           ███████  
           ██   ██ 
 ████████  ██    ██ 
 ████████  ██    ██ 
           ██    ██ 
           ██    ██ 
 ████████  ██    ██ 
 ████████  ██    ██ 
           ██   ██
           ███████  
           █████     
"""
)

# Your original glitch list
faces_glitch = [
    "\n              █\n          ██\n              █\n ███▒▒▒██    ██\n ████████   ██\n            ██\n     ░      ██\n ████████   ██\n ████████    ██\n              █   ~\n          ██\n               █",
    "\n            █    ░\n              ██  ▒\n          █  ▓\n ████████    ██  !\n █████▒▒▒   ██  _\n        ▒   ██\n            ██  ░\n ████████   ██\n ████████    ██   ▒\n          _   █\n              ██\n               █  ▚",
    "\n           █\n      ▚       ██  ▒\n   ░          █\n ████████  ░ ██  /\n ████████   ██  _\n      ░     ██    ░\n  _   _     ██\n ████████   ██  \\\n ████████    ██  ░\n       ░      █\n   ▒          ██\n               █   ░",
    "\n             █   ̷ ̷ ̷ ̷ ̷ ̷ ̷ ̷ ̷ ̷\n              ██      ░░▒▒\n     ҂         █\n ████████    ██   [ERROR]\n █████▓▒░   ██\n       ▗▟█████████▟▙\n            ██\n ████████   ██  ▓▓▓▓▓\n ███   ██    ██   █\n      █ █     █\n     █  ██    ██  ☠️\n        █      █",
]


# --- REFINED GLITCH SPAWN ---
def spawn_glitch_clones():
    if not power_on:
        return

    toby_x = window.winfo_x()
    toby_y = window.winfo_y()

    glitch_windows = []

    for _ in range(15):
        clone = tk.Toplevel(window)
        clone.overrideredirect(True)
        clone.config(bg="black")
        clone.attributes("-topmost", True)

        # Offset logic: popups stay within 350px of Toby
        offset_x = random.randint(-350, 350)
        offset_y = random.randint(-350, 350)

        # Ensure they don't cover the main window center immediately
        if -120 < offset_x < 120:
            offset_x += 160 * (1 if offset_x > 0 else -1)

        c_x = toby_x + (WIDTH // 2) + offset_x
        c_y = toby_y + (HEIGHT // 2) + offset_y

        clone.geometry(f"150x100+{c_x}+{c_y}")

        msg = tk.Label(
            clone, text="WHY NOT?", font=("Courier", 14, "bold"), bg="black", fg="red"
        )
        msg.pack(expand=True)
        # Store initial offsets to keep them moving WITH the main window
        glitch_windows.append(
            {"win": clone, "label": msg, "ox": offset_x, "oy": offset_y}
        )

    animate_glitch_windows(glitch_windows)


def animate_glitch_windows(glitch_windows):
    if not power_on:
        for g in glitch_windows:
            g["win"].destroy()
        return

    # Tracking main window movement (shakes)
    toby_x = window.winfo_x()
    toby_y = window.winfo_y()

    for g in glitch_windows:
        jitter_x = random.randint(-4, 4)
        jitter_y = random.randint(-4, 4)

        new_x = toby_x + (WIDTH // 2) + g["ox"] + jitter_x
        new_y = toby_y + (HEIGHT // 2) + g["oy"] + jitter_y

        g["win"].geometry(f"+{new_x}+{new_y}")

        if random.random() < 0.1:
            g["label"].config(text=random.choice(["WHY NOT?", "HELP", "SORRY", "???"]))

    window.after(40, lambda: animate_glitch_windows(glitch_windows))


def Glitch_out():
    if not power_on:
        return

    # Violence level of the shake
    shake_intensity = 12
    sx = x_c + random.randint(-shake_intensity, shake_intensity)
    sy = y_c + random.randint(-shake_intensity, shake_intensity)
    window.geometry(f"+{sx}+{sy}")

    # Use your original glitch faces
    label.config(text=random.choice(faces_glitch), fg="red")

    chars = "░▒▓█▟▙▀▄▘▝"
    glitch_txt = "".join(random.choice(chars) for _ in range(12))
    dialogue_label.config(text=glitch_txt, fg="red")

    window.after(60, Glitch_out)


# --- UI SETUP ---
label = tk.Label(
    window, text=face_open, font=("Courier", 10), justify="left", bg="black", fg="white"
)
label.pack(pady=10)

dialogue_label = tk.Label(
    window, text="Hi! I'm Toby.", font=("Arial", 16, "bold"), bg="black", fg="white"
)
dialogue_label.pack(pady=10)

frame = tk.Frame(window, bg="black")
frame.pack(expand=True)


def toby_talk(text):
    dialogue_label.config(text=text)
    label.config(text=face_talking)
    window.after(800, lambda: label.config(text=face_open))


def handle_rejection():
    for widget in frame.winfo_children():
        widget.destroy()
    dialogue_label.config(text="W-Why not?", fg="red")
    label.config(text=face_open_sad)
    # Delay the glitch for dramatic effect
    window.after(2000, lambda: [Glitch_out(), spawn_glitch_clones()])


# --- BUTTONS ---
btn_yes = tk.Button(
    frame,
    text="Be Friends",
    font=("Arial", 10, "bold"),
    command=lambda: window.destroy(),
)
btn_yes.pack(side="left", padx=10)

btn_no = tk.Button(
    frame, text="I dunno.", font=("Arial", 10, "bold"), command=handle_rejection
)
btn_no.pack(side="left", padx=10)

window.mainloop()
