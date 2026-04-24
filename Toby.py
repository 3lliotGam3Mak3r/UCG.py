import tkinter as tk
import os
import platform
import random


# --- SHUTDOWN WINDOW LOGIC ---
# This class handles the "Antivirus" popup that appears when Toby gets upset.
class ShutdownWindow:
    def __init__(self, master):
        # Create a new window on top of the main one
        self.top = tk.Toplevel(master)
        self.top.title("Antivirus.log")
        self.top.geometry("400x450")
        self.top.configure(bg="black")
        self.top.attributes(
            "-topmost", True
        )  # Make sure it stays in front of everything

        # Disable the "X" button so the user can't just close the window
        self.top.protocol("WM_DELETE_WINDOW", lambda: None)
        # Safe exit for the developer: Pressing Escape kills the whole app
        self.top.bind("<Escape>", lambda e: master.destroy())

        # Container for the 'terminal' text lines
        self.container = tk.Frame(self.top, bg="black")
        self.container.pack(anchor="nw", padx=20, pady=20, fill="both", expand=True)

        self.current_input = ""
        self.prompt_label = None

        # Start the "fake" system scan sequence
        self.add_line("Malicious Program Detected")
        self.animate_dots("Identifying Malicious Program", 0, 2, self.show_malware_name)

    # Helper function to add a line of text to the screen
    def add_line(self, text, size=14, color="white"):
        lbl = tk.Label(
            self.container,
            text=text,
            fg=color,
            bg="black",
            font=("Courier", size, "bold"),  # Changed to Courier to prevent font errors
            justify="left",
        )
        lbl.pack(anchor="nw", pady=(0, 10))
        return lbl

    # Logic for that classic "Scanning..." dot animation
    def animate_dots(self, base_text, dot_count, repeats, callback):
        if not hasattr(self, "temp_dot_label"):
            self.temp_dot_label = self.add_line(base_text)

        if dot_count <= 3:
            self.temp_dot_label.config(text=base_text + "." * dot_count)
            self.top.after(
                400,
                lambda: self.animate_dots(base_text, dot_count + 1, repeats, callback),
            )
        elif repeats > 0:
            # If we finish 3 dots, reset and do it again for the number of 'repeats'
            self.top.after(
                400, lambda: self.animate_dots(base_text, 0, repeats - 1, callback)
            )
        else:
            # Animation finished, move on to the next function
            delattr(self, "temp_dot_label")
            self.top.after(1000, callback)

    def show_malware_name(self):
        self.add_line("Malware Identified: Toby.exe")
        self.animate_dots(
            "Attempting to Initiate Shutdown", 0, 1, self.enable_user_input
        )

    # Allow the user to actually type into the terminal
    def enable_user_input(self):
        self.prompt_label = self.add_line("Initiate Shutdown? Y/N: ")
        self.top.bind("<Key>", self.handle_keypress)
        self.top.focus_force()

    def handle_keypress(self, event):
        # Handle backspacing
        if event.keysym == "BackSpace":
            self.current_input = self.current_input[:-1]
        # Handle normal characters
        elif len(event.char) == 1 and event.char.isprintable():
            self.current_input += event.char

        # Update the text on screen as the user types
        if self.prompt_label:
            self.prompt_label.config(
                text=f"Initiate Shutdown? Y/N: {self.current_input}"
            )

        check_input = self.current_input.strip().lower()
        if check_input == "y":
            self.top.unbind("<Key>")
            # Show a progress bar and then shut down the program
            self.loading_label = self.add_line("Progress: ")
            self.start_loading(0)
        elif check_input == "n":
            self.top.unbind("<Key>")
            # This is where the spooky stuff happens if they refuse
            self.trigger_refusal_sequence()

    def start_loading(self, count):
        if count <= 20:
            self.loading_label.config(text=f"Progress: {'█' * count}")
            self.top.after(200, lambda: self.start_loading(count + 1))
        else:
            self.add_line("SYSTEM SHUTDOWN INITIATED")
            self.top.after(1000, lambda: os._exit(0))

    def trigger_refusal_sequence(self):
        # Wipe the terminal and show the "WHY NOT?" text
        self.container.pack_forget()
        canvas = tk.Canvas(
            self.top, width=400, height=450, bg="black", highlightthickness=0
        )
        canvas.place(relx=0.5, rely=0.5, anchor="center")
        txt = canvas.create_text(
            200, 225, text="WHY NOT?", fill="red", font=("Courier", 40, "bold")
        )

        # Loop to make the text jitter and rotate slightly (glitch effect)
        def loop(step):
            angle = 6 if (step // 2) % 2 == 0 else -6
            canvas.coords(txt, 200 + random.randint(-2, 2), 225 + random.randint(-2, 2))
            canvas.itemconfig(txt, angle=angle)
            self.top.after(20, lambda: loop(step + 1))

        loop(0)

        # After 2.5 seconds of jittering, show the final system error
        self.top.after(2500, self.show_antivirus_popup)

    def show_antivirus_popup(self):
        # Create a stylized notification window in the corner of the screen
        self.popup = tk.Toplevel(self.top)
        self.popup.overrideredirect(True)
        self.popup.configure(
            bg="#1a1a1a", highlightthickness=2, highlightbackground="red"
        )

        # Calculate position to put it in the bottom right
        w, h = 400, 200
        x = self.top.winfo_screenwidth() - w - 50
        y = self.top.winfo_screenheight() - h - 50
        self.popup.geometry(f"{w}x{h}+{x}+{y}")
        self.popup.attributes("-topmost", True)

        tk.Label(
            self.popup,
            text="SYSTEM ANTIVIRUS",
            fg="white",
            bg="red",
            font=("Courier", 12, "bold"),
        ).pack(fill="x")
        tk.Label(
            self.popup,
            text="\nToby.exe override detected.",
            fg="white",
            bg="#1a1a1a",
            pady=10,
        ).pack()

        self.pop_progress = tk.Label(
            self.popup, text="", fg="white", bg="#1a1a1a", font=("Courier", 14)
        )
        self.pop_progress.pack()
        self.popup_loading(0)

    # Final "loading" bar before the app closes
    def popup_loading(self, count):
        if count <= 20:
            self.pop_progress.config(text="█" * count)
            self.top.after(250, lambda: self.popup_loading(count + 1))
        else:
            self.pop_progress.config(text="OVERRIDE COMPLETE")
            self.top.after(1000, lambda: os._exit(0))


# --- YOUR FULL ORIGINAL SCRIPT STARTS HERE ---
# Setting up the main Toby interaction window
window = tk.Tk()
window.title("Toby.Launch")
window.geometry("400x450")
window.config(bg="black")
power_on = True

# Safety features: unclosable window + dev escape key
window.protocol("WM_DELETE_WINDOW", lambda: None)
window.bind("<Escape>", lambda e: window.destroy())
# Dev shortcut: press '6' to jump straight to the friendship question
window.bind("6", lambda e: show_final_choices())

WIDTH = 400
HEIGHT = 450

# --- ASCII FACES ---
# These strings store the different "frames" of Toby's face
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

face_closed = (
    "\n\n\n\n"
    "             █     \n"
    "             ██     \n"
    "             ██    \n"
    "    ██       ██    \n"
    "    ██       ██    \n"
    "             ██    \n"
    "             ██    \n"
    "    ██       ██    \n"
    "    ██       ██    \n"
    "             ██    \n"
    "             ██     \n"
    "             █     \n"
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

face_closed_sad = (
    "\n\n\n\n"
    "               █     \n"
    "              ██     \n"
    "              █    \n"
    "    ██       ██    \n"
    "    ██      ██    \n"
    "            ██    \n"
    "            ██    \n"
    "    ██      ██    \n"
    "    ██       ██    \n"
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

face_talk_sad = (
    "\n\n\n\n"
    """              █████   
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

# Lists used for the startup and shutdown animations
faces_startup = [
    "\n\n\n\n        ██    \n        ██    \n        ██    \n     ████████ \n     ████████ \n        ██    \n        ██    \n        ██    \n",
    "     ██▓  ▓██ \n     ▒██  ██▒ \n      ██▓▓██  \n      ▒████▒  \n       ████   \n       ▒██▒   \n       ▒██▒   \n       ████   \n      ▒████▒  \n      ██▒▒██  \n     ▒██  ██▒ \n     ██▓  ▓██ ",
    "\n\n        ██    \n        ██    \n        ██    \n        ██    \n        ██    \n        ██    \n        ██    \n        ██    \n        ██    \n        ██    \n        ██    \n        ██    \n        ██    \n        ██    ",
    "\n\n██        ██    \n██        ██    \n██        ██    \n██        ██    \n██        ██    \n██        ██    \n██        ██    \n██        ██    \n██        ██    \n██        ██    \n██        ██    \n██        ██    \n██        ██    \n██        ██    ",
    "\n\n\n    ██                  ██    \n    ██                  ██    \n    ██                  ██    \n    ██                  ██    \n    ██        ██        ██    \n    ██        ██        ██    \n    ██        ██        ██    \n    ██                  ██    \n    ██                  ██    \n    ██        ██        ██    \n    ██        ██        ██    \n    ██        ██        ██    \n    ██                  ██    \n    ██                  ██    \n    ██                  ██    ",
    "\n\n\n\n              █     \n              ██     \n              ██    \n ████████     ██    \n ████████     ██    \n              ██    \n              ██    \n ████████     ██    \n ████████     ██    \n              ██    \n              ██     \n              █     \n",
    face_open,
    face_closed,
]

faces_shutdown = [
    "\n\n\n\n              █     \n              ██     \n              ██    \n ████████     ██    \n ████████     ██    \n              ██    \n              ██    \n ████████     ██    \n ████████     ██    \n              ██    \n              ██     \n              █     \n",
    "\n\n\n    ██                  ██    \n    ██                  ██    \n    ██                  ██    \n    ██                  ██    \n    ██        ██        ██    \n    ██        ██        ██    \n    ██        ██        ██    \n    ██                  ██    \n    ██                  ██    \n    ██        ██        ██    \n    ██        ██        ██    \n    ██        ██        ██    \n    ██                  ██    \n    ██                  ██    \n    ██                  ██    ",
    "\n\n██        ██    \n██        ██    \n██        ██    \n██        ██    \n██        ██    \n██        ██    \n██        ██    \n██        ██    \n██        ██    \n██        ██    \n██        ██    \n██        ██    \n██        ██    \n██        ██    \n██        ██    ",
    "\n\n        ██    \n        ██    \n        ██    \n        ██    \n        ██    \n        ██    \n        ██    \n        ██    \n        ██    \n        ██    \n        ██    \n        ██    \n        ██    \n        ██    ",
    "     ██▓  ▓██ \n     ▒██  ██▒ \n      ██▓▓██  \n      ▒████▒  \n       ████   \n       ▒██▒   \n       ▒██▒   \n       ████   \n      ▒████▒  \n      ██▒▒██  \n     ▒██  ██▒ \n     ██▓  ▓██ ",
    "\n\n\n\n        ██    \n        ██    \n        ██    \n     ████████ \n     ████████ \n        ██    \n        ██    \n        ██    \n",
]

# Spooky glitch faces for when the app breaks
glitch_severity = 0
faces_glitch = [
    "\n              █\n          ██\n              █\n ███▒▒▒██    ██\n ████████   ██\n            ██\n     ░      ██\n ████████   ██\n ████████    ██\n              █   ~\n          ██\n               █",
    "\n            █    ░\n              ██  ▒\n          █  ▓\n ████████    ██  !\n █████▒▒▒   ██  _\n        ▒   ██\n            ██  ░\n ████████   ██\n ████████    ██   ▒\n          _   █\n              ██\n               █  ▚",
    "\n           █\n      ▚       ██  ▒\n   ░          █\n ████████  ░ ██  /\n ████████   ██  _\n      ░     ██    ░\n  _   _     ██\n ████████   ██  \\\n ████████    ██  ░\n       ░      █\n   ▒          ██\n               █   ░",
    "\n             █   ̷ ̷ ̷ ̷ ̷ ̷ ̷ ̷ ̷ ̷\n              ██      ░░▒▒\n     ҂         █\n ████████    ██   [ERROR]\n █████▓▒░   ██\n       ▗▟█████████▟▙\n            ██\n ████████   ██  ▓▓▓▓▓\n ███   ██    ██   █\n      █ █     █\n     █  ██    ██  ☠️\n        █      █",
    "\n          █      ███▙\n          █      █▘  ▘▞\n ▒▓▒░▒▓░▒▟██████░   ▐ ▒▓▒░▗\n ████████ █████▄   ▟  █▓░\n  ▝▀█████████████▟▙▒▓\n         █▀█  █▄█▓░\n █▄▄████▓  ████▓ ░▒\n ███  ███   ███▀▀  ▒░\n        ▀    ▀     ▐\n   ▟           ▟ ▓░\n  ███         ███\n  ▝▀▘░▒▓      ▝▀▘",
    "\n                █\n   [VOID]      ███▙   ░▒\n           ▗▄▄▄█   ▐\n █▓▒░▒▓▒▟███████░░   ░▒▓\n ████████ █████▄    ▟  ▓\n  ▝▀█████████████▟▙\n         █▀█  █▄█▓░\n [REDACTED]   ████▓ ░▒\n ███  ███     ███▀\n    █▀      █   █\n   ▟       ██   ██   ▒░\n  ███     ████  ███  ☠️\n  ▝▀▘     ▝▀▘▀  ▝▀▘",
]

# --- UI SETUP ---
# The main ASCII display label
label = tk.Label(
    window, text="", font=("Courier", 12), justify="left", bg="black", fg="white"
)
label.pack(pady=10)

# The text box for Toby's dialogue
dialogue_label = tk.Label(
    window, text="", font=("Arial", 18, "bold"), wraplength=350, bg="black", fg="white"
)
dialogue_label.pack(pady=10)

# Container for the interaction buttons
frame = tk.Frame(window, bg="black")
frame.pack(expand=True)
choice = tk.StringVar(value="C")

# --- CORE LOGIC & ANIMATION ---
startup_index = 0
startup_blink_count = 0
max_startup_blinks = 3
shutdown_index = 0


# Function to update dialogue and swap face to 'talking'
def toby_talk(text):
    dialogue_label.config(text=text)
    label.config(text=face_talking)
    window.after(750, lambda: label.config(text=face_open))


# Same as above but for sad dialogue
def toby_talk_sad(text):
    dialogue_label.config(text=text)
    label.config(text=face_talk_sad)
    window.after(750, lambda: label.config(text=face_open_sad))


# Iterates through the startup animation frames
def startup_cycle_faces():
    global startup_index
    if startup_index < len(faces_startup):
        label.config(text=faces_startup[startup_index])
        startup_index += 1
        window.after(300, startup_cycle_faces)
    else:
        quick_blink()
        window.after(
            2000, lambda: [toby_talk("Hey there! I'm Toby."), show_initial_greeting()]
        )


# Iterates through the shutdown animation frames
def shutdown_cycle_faces():
    global shutdown_index
    if power_on == False:
        if shutdown_index < len(faces_shutdown):
            label.config(text=faces_shutdown[shutdown_index])
            shutdown_index += 1
            window.after(300, shutdown_cycle_faces)
        else:
            window.destroy()


# Spawns small popup windows across the screen for the glitch effect
def spawn_glitch_clones():
    if not power_on:
        return
    toby_x, toby_y = window.winfo_x(), window.winfo_y()
    glitch_windows = []
    for _ in range(15):
        clone = tk.Toplevel(window)
        clone.overrideredirect(True)  # Removes the title bar
        clone.config(bg="black")
        clone.attributes("-topmost", True)

        # Randomly position windows around the center
        offset_x = random.randint(-500, 500)
        offset_y = random.randint(-500, 500)
        if -120 < offset_x < 120:
            offset_x += 160 * (1 if offset_x > 0 else -1)

        c_x, c_y = toby_x + (WIDTH // 2) + offset_x, toby_y + (HEIGHT // 2) + offset_y
        clone.geometry(f"150x100+{c_x}+{c_y}")

        msg = tk.Label(
            clone, text="WHY NOT?", font=("Courier", 14, "bold"), bg="black", fg="red"
        )
        msg.pack(expand=True)
        glitch_windows.append(
            {"win": clone, "label": msg, "ox": offset_x, "oy": offset_y}
        )
    animate_glitch_windows(glitch_windows)


# Makes the cloned windows jitter and change text randomly
def animate_glitch_windows(glitch_windows):
    if not power_on:
        for g in glitch_windows:
            g["win"].destroy()
        return
    toby_x, toby_y = window.winfo_x(), window.winfo_y()
    for g in glitch_windows:
        jx, jy = random.randint(-4, 4), random.randint(-4, 4)
        g["win"].geometry(
            f"+{toby_x + (WIDTH // 2) + g['ox'] + jx}+{toby_y + (HEIGHT // 2) + g['oy'] + jy}"
        )
        if random.random() < 0.1:
            g["label"].config(text=random.choice(["WHY NOT?", "HELP", "SORRY", "???"]))
    window.after(40, lambda: animate_glitch_windows(glitch_windows))


# Main glitch logic: shakes the main window and cycles creepy faces
def Glitch_out():
    global glitch_severity
    if power_on:
        if glitch_severity == 0:
            # Reorganize the screen layouts when glitching starts
            label.pack_forget()
            dialogue_label.pack_forget()
            label.pack(expand=True, fill="both")
            dialogue_label.pack(expand=True, fill="x")
            label.config(justify="center", anchor="center")
            spawn_glitch_clones()

        if glitch_severity < len(faces_glitch) - 1:
            glitch_severity += 0.04  # Slowly increase the intensity

        c_idx = int(glitch_severity)
        curr_face = random.choice(faces_glitch[max(0, c_idx - 2) : c_idx + 1])

        # Make the main window grow and shake
        new_dim = 400 + int(glitch_severity * 30)
        shake = int(glitch_severity * 3)
        window.geometry(
            f"{new_dim}x{new_dim}+{int(window.winfo_screenwidth()/2-new_dim/2)+random.randint(-shake,shake)}+{int(window.winfo_screenheight()/2-new_dim/2)+random.randint(-shake,shake)}"
        )

        label.config(text=curr_face, fg="red", font=("Courier", 12))
        # Turn dialogue into random scary characters
        dialogue_label.config(
            text="".join(random.choice("░▒▓█/?!_@#$%^&*") for _ in range(15)), fg="red"
        )
        window.after(max(40, 90 - int(glitch_severity * 10)), Glitch_out)


# --- IDLE BLINKING LOGIC ---
def quick_blink():
    global startup_blink_count
    if startup_blink_count < max_startup_blinks:
        label.config(text=face_closed)
        window.after(150, quick_open)
    else:
        label.config(text=face_open)
        window.after(random.randint(1000, 5000), blink)


def quick_open():
    global startup_blink_count
    label.config(text=face_open)
    startup_blink_count += 1
    window.after(150, quick_blink)


def blink():
    label.config(text=face_closed)
    window.after(200, open_eyes)


def open_eyes():
    label.config(text=face_open)
    window.after(random.randint(1000, 5000), blink)


# --- FLOW CONTROL ---
def clear_action_frame():
    # Remove all current buttons to make room for new ones
    for widget in frame.winfo_children():
        widget.destroy()


def handle_greeting_response():
    clear_action_frame()
    toby_talk("How was your day?")
    window.after(2000, show_mood_options)


def handle_positive_mood():
    clear_action_frame()
    toby_talk("Awesome!")
    window.after(2000, show_reciprocal_questions)


def handle_negative_mood():
    clear_action_frame()
    toby_talk_sad("Oh, sorry about that.")
    window.after(2000, show_reciprocal_questions)


def handle_toby_status_query():
    clear_action_frame()
    toby_talk("It was pretty average, to be honest.")
    window.after(2000, show_acknowledgment_options)


def handle_friendship_request():
    clear_action_frame()
    toby_talk("Totally! \n Want to be friends?")
    window.after(2000, show_final_choices)


def handle_awkward_friendship_request():
    clear_action_frame()
    toby_talk("So... want to be friends?")
    window.after(2000, show_final_choices)


def handle_final_shutdown():
    global power_on
    clear_action_frame()
    toby_talk("All Right! Oh, gotta go!\n   See you later!")
    power_on = False
    window.after(2000, shutdown_cycle_faces)


def handle_rejection():
    # Triggered if user clicks "I dunno"
    clear_action_frame()
    toby_talk_sad("Huh? W-Why not?")
    # Start the glitching effect
    window.after(1000, Glitch_out)
    # After 4 seconds of glitching, pop up the log window
    window.after(4000, lambda: ShutdownWindow(window))


# --- UI BUTTONS ---
def create_button(text, val, cmd):
    # Style the buttons to look like a clean terminal UI
    return tk.Radiobutton(
        frame,
        text=text,
        variable=choice,
        value=val,
        indicatoron=0,
        command=cmd,
        bg="#eeeeee",
        fg="black",
        selectcolor="#bbbbbb",
        font=("Arial", 10, "bold"),
        padx=10,
        pady=5,
    )


def show_initial_greeting():
    create_button("Hi Toby!", "A", handle_greeting_response).pack(side="left", padx=5)
    create_button("Sup Dude.", "B", handle_greeting_response).pack(side="left", padx=5)


def show_mood_options():
    create_button("Pretty Good!", "1", handle_positive_mood).pack(side="left", padx=5)
    create_button("Not that great.", "2", handle_negative_mood).pack(
        side="left", padx=5
    )


def show_reciprocal_questions():
    create_button("What about You?", "X", handle_toby_status_query).pack(
        side="left", padx=5
    )
    create_button("How was your day Toby?", "Y", handle_toby_status_query).pack(
        side="left", padx=5
    )


def show_acknowledgment_options():
    create_button("Oh... Okay!", "9", handle_awkward_friendship_request).pack(
        side="left", padx=5
    )
    create_button("I Know Right?", "0", handle_friendship_request).pack(
        side="left", padx=5
    )


def show_final_choices():
    clear_action_frame()
    toby_talk("So... want to be friends?")
    create_button("Sure!", "Q", handle_final_shutdown).pack(side="left", padx=5)
    create_button("I dunno.", "W", handle_rejection).pack(side="left", padx=5)


# Entry point for the program
startup_cycle_faces()
window.mainloop()
