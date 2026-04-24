import tkinter as tk
import os
import platform
import random

# Configuration
FONT_NAME = "Roboto Mono"
BG_COLOR = "black"
FG_COLOR = "white"
TEXT_SIZE = 24
BAR_SIZE = 22


class ShutdownInterface:
    def __init__(self, root):
        self.root = root
        self.root.configure(bg=BG_COLOR)
        self.root.overrideredirect(True)
        self.root.geometry(
            f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}+0+0"
        )

        self.container = tk.Frame(self.root, bg=BG_COLOR)
        self.container.pack(anchor="nw", padx=60, pady=60)

        self.current_input = ""
        self.root.bind("<Escape>", lambda e: self.root.destroy())
        self.root.focus_force()
        self.root.after(500, self.run_intro)

    def add_line(self, text, size=TEXT_SIZE, bold=True, color=FG_COLOR):
        lbl = tk.Label(
            self.container,
            text=text,
            fg=color,
            bg=BG_COLOR,
            font=(FONT_NAME, size, "bold" if bold else "normal"),
            justify="left",
        )
        lbl.pack(anchor="nw", pady=(0, 20))
        return lbl

    def run_intro(self):
        self.add_line("Malicious program detected")
        self.root.after(
            1000,
            lambda: self.animate_dots(
                "identifying malicious program", 0, 2, self.show_malware_name, True
            ),
        )

    def animate_dots(
        self, base_text, dot_count, repeats, callback, show_complete=False
    ):
        if not hasattr(self, "temp_dot_label"):
            self.temp_dot_label = self.add_line(base_text)
        if dot_count <= 3:
            self.temp_dot_label.config(text=base_text + "." * dot_count)
            self.root.after(
                400,
                lambda: self.animate_dots(
                    base_text, dot_count + 1, repeats, callback, show_complete
                ),
            )
        elif repeats > 0:
            self.root.after(
                400,
                lambda: self.animate_dots(
                    base_text, 0, repeats - 1, callback, show_complete
                ),
            )
        else:
            if show_complete:
                self.temp_dot_label.config(text=f"{base_text}... [COMPLETE]")
            delattr(self, "temp_dot_label")
            self.root.after(1000, callback)

    def show_malware_name(self):
        self.add_line("Malware Identified: Toby.exe")
        self.root.after(
            1000,
            lambda: self.animate_dots(
                "attempting shutdown", 0, 1, self.enable_user_input, True
            ),
        )

    def enable_user_input(self):
        self.prompt_label = self.add_line("Initiate Shutdown? Y/N: ")
        self.root.bind("<Key>", self.handle_keypress)

    def handle_keypress(self, event):
        if event.keysym == "BackSpace":
            self.current_input = self.current_input[:-1]
        elif len(event.char) == 1 and event.char.isprintable():
            self.current_input += event.char
        self.prompt_label.config(text=f"Initiate Shutdown? Y/N: {self.current_input}")

        check_input = self.current_input.strip().lower()
        if check_input == "y":
            self.root.unbind("<Key>")
            self.loading_label = self.add_line("", size=BAR_SIZE, bold=False)
            self.start_loading(0, duration=500)
        elif check_input == "n":
            self.root.unbind("<Key>")
            self.trigger_refusal_sequence()

    def trigger_refusal_sequence(self):
        self.container.pack_forget()

        self.canvas = tk.Canvas(
            self.root, width=800, height=400, bg="black", highlightthickness=0
        )
        self.canvas.place(relx=0.5, rely=0.5, anchor="center")

        self.glitch_text = self.canvas.create_text(
            400, 200, text="WHY NOT?", fill="red", font=(FONT_NAME, 85, "bold"), angle=0
        )

        self.glitch_step = 0
        self.glitch_loop()
        self.root.after(2500, self.stop_glitch_and_start_av)

    def glitch_loop(self):
        # Increased rotation to 6 degrees
        # Faster alternation: (self.glitch_step // 2) means it swaps every 40ms total
        angle = 6 if (self.glitch_step // 2) % 2 == 0 else -6

        offset_x = random.randint(-2, 2)
        offset_y = random.randint(-2, 2)

        self.canvas.coords(self.glitch_text, 400 + offset_x, 200 + offset_y)
        self.canvas.itemconfig(self.glitch_text, angle=angle)

        self.glitch_step += 1
        # Faster loop: now 20ms
        self.glitch_timer = self.root.after(20, self.glitch_loop)

    def stop_glitch_and_start_av(self):
        self.root.after_cancel(self.glitch_timer)
        self.canvas.destroy()
        self.show_antivirus_popup()

    def show_antivirus_popup(self):
        self.popup = tk.Toplevel(self.root)
        self.popup.overrideredirect(True)
        self.popup.configure(
            bg="#1a1a1a", highlightthickness=2, highlightbackground="red"
        )
        w, h = 400, 200
        x, y = (
            self.root.winfo_screenwidth() - w - 50,
            self.root.winfo_screenheight() - h - 50,
        )
        self.popup.geometry(f"{w}x{h}+{x}+{y}")

        tk.Label(
            self.popup,
            text="SYSTEM ANTIVIRUS",
            fg="white",
            bg="red",
            font=(FONT_NAME, 12, "bold"),
        ).pack(fill="x")
        tk.Label(
            self.popup,
            text="Toby.exe override detected.",
            fg="white",
            bg="#1a1a1a",
            pady=10,
        ).pack()
        self.pop_progress = tk.Label(
            self.popup, text="", fg="white", bg="#1a1a1a", font=(FONT_NAME, 14)
        )
        self.pop_progress.pack()
        self.popup_loading(0)

    def popup_loading(self, count):
        if count <= 20:
            self.pop_progress.config(text="█" * count)
            self.root.after(250, lambda: self.popup_loading(count + 1))
        else:
            self.pop_progress.config(text="OVERRIDE COMPLETE")
            self.root.after(1000, self.execute_shutdown)

    def start_loading(self, count, duration=500):
        if count <= 20:
            self.loading_label.config(text=f"Progress: {'█' * count}")
            self.root.after(duration, lambda: self.start_loading(count + 1, duration))
        else:
            self.loading_label.config(text="Progress: " + "█" * 20 + " [COMPLETE]")
            self.final_lbl = self.add_line("Initiating shutdown")
            self.animate_final_dots(0)

    def animate_final_dots(self, dot_count):
        if dot_count <= 3:
            self.final_lbl.config(text="Initiating shutdown" + "." * dot_count)
            self.root.after(400, lambda: self.animate_final_dots(dot_count + 1))
        else:
            self.final_lbl.config(text="Initiating shutdown... [COMPLETE]")
            self.root.after(1000, self.execute_shutdown)

    def execute_shutdown(self):
        # os.system("shutdown /s /t 1")
        self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = ShutdownInterface(root)
    root.mainloop()
