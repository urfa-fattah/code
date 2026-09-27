"""
Fake "Hacking Environment" -> Syntax Error prank screen
--------------------------------------------------------
- Matrix-style green falling code background
- Fake terminal "hacking" log (typing effect)
- Shesh e ekta glowing red "SYNTAX ERROR" alert pop kore
- Puro screen ta trembling/shake hote thake

Run: python fake_hack_syntax_error.py
Bondho: ESC chapo, othoba error box e click koro
"""

import tkinter as tk
import random
import string

root = tk.Tk()
root.title("system32")
root.attributes("-fullscreen", True)
root.configure(bg="black")

WIDTH = root.winfo_screenwidth()
HEIGHT = root.winfo_screenheight()
base_x, base_y = 0, 0

canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="black", highlightthickness=0)
canvas.pack(fill="both", expand=True)

# ---------------- Matrix rain background ----------------
CHARS = string.ascii_uppercase + string.digits + "@#$%&01"
FONT_SIZE = 16
cols = WIDTH // FONT_SIZE
matrix_state = [random.randint(-30, 0) for _ in range(cols)]

def render_matrix_frame():
    canvas.delete("matrix")
    for i in range(cols):
        x = i * FONT_SIZE
        y = matrix_state[i] * FONT_SIZE
        ch = random.choice(CHARS)
        color = "#00FF41" if random.random() > 0.12 else "#D6FFD6"
        canvas.create_text(x, y, text=ch, fill=color, font=("Consolas", FONT_SIZE), anchor="nw", tags="matrix")
        matrix_state[i] += 1
        if y > HEIGHT and random.random() > 0.95:
            matrix_state[i] = random.randint(-10, 0)
    canvas.tag_lower("matrix")

# ---------------- Fake hacking terminal log ----------------
log_lines = [
    "> booting intrusion_module.py ...",
    "> connecting to target 192.168.1.10 ...",
    "> bypassing firewall [OK]",
    "> injecting payload ...",
    "> decrypting shell access ...",
    "> escalating privileges ... root@target",
    "> compiling exploit.py ...",
]

term_text = canvas.create_text(
    40, 40, text="", fill="#00FF41", font=("Consolas", 18, "bold"),
    anchor="nw", tags="term"
)

full_log = ""
line_idx = 0
char_idx = 0

def type_log():
    global full_log, line_idx, char_idx
    if line_idx < len(log_lines):
        line = log_lines[line_idx]
        if char_idx <= len(line):
            canvas.itemconfig(term_text, text=full_log + line[:char_idx])
            char_idx += 1
            root.after(25, type_log)
        else:
            full_log += line + "\n"
            line_idx += 1
            char_idx = 0
            root.after(300, type_log)
    else:
        root.after(400, show_error)

# ---------------- Glowing red SYNTAX ERROR alert ----------------
btn_w, btn_h = 420, 130
btn_x, btn_y = WIDTH // 2, HEIGHT // 2
error_items = []

def show_error():
    cx, cy = btn_x, btn_y
    for i in range(6, 0, -1):
        r = canvas.create_oval(
            cx - btn_w // 2 - i * 8, cy - btn_h // 2 - i * 8,
            cx + btn_w // 2 + i * 8, cy + btn_h // 2 + i * 8,
            fill="", outline="#ff0000", width=2, tags="err"
        )
        error_items.append(r)
    box = canvas.create_rectangle(
        cx - btn_w // 2, cy - btn_h // 2,
        cx + btn_w // 2, cy + btn_h // 2,
        fill="#1a0000", outline="#ff2222", width=3, tags="err"
    )
    title = canvas.create_text(
        cx, cy - 25, text="SYNTAX ERROR",
        fill="#ff3333", font=("Consolas", 30, "bold"), tags="err"
    )
    sub = canvas.create_text(
        cx, cy + 25, text="line 42: unexpected token — access denied",
        fill="#ff8888", font=("Consolas", 13), tags="err"
    )
    for item in (box, title, sub):
        canvas.tag_bind(item, "<Button-1>", close_app)
    error_items.extend([box, title, sub])
    pulse_glow()

def close_app(event=None):
    root.destroy()

root.bind("<Escape>", close_app)

glow_colors = ["#ff0000", "#ff3333", "#ff6666", "#ff9999", "#ff3333"]
glow_step = 0

def pulse_glow():
    global glow_step
    if not error_items:
        return
    color = glow_colors[glow_step % len(glow_colors)]
    for r in error_items[:6]:
        canvas.itemconfig(r, outline=color)
    glow_step += 1
    canvas.tag_raise("err")
    root.after(120, pulse_glow)

# ---------------- Screen shake ----------------
def shake_screen():
    dx = random.randint(-8, 8)
    dy = random.randint(-8, 8)
    root.geometry(f"+{base_x + dx}+{base_y + dy}")
    root.after(50, shake_screen)

# ---------------- Main animation loop ----------------
def animate():
    render_matrix_frame()
    canvas.tag_raise("term")
    canvas.tag_raise("err")
    root.after(70, animate)

animate()
shake_screen()
root.after(500, type_log)

root.mainloop()
