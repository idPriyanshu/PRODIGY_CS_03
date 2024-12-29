import math
import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def password_strength(password):
    criteria = {
        "length": len(password) >= 8,
        "uppercase": any(char.isupper() for char in password),
        "lowercase": any(char.islower() for char in password),
        "number": any(char.isdigit() for char in password),
        "special_char": any(not char.isalnum() for char in password)
    }

    feedback = []
    if not criteria["length"]:
        feedback.append("Password should be at least 8 characters long.")
    if not criteria["uppercase"]:
        feedback.append("Password should contain at least one uppercase letter.")
    if not criteria["lowercase"]:
        feedback.append("Password should contain at least one lowercase letter.")
    if not criteria["number"]:
        feedback.append("Password should contain at least one number.")
    if not criteria["special_char"]:
        feedback.append("Password should contain at least one special character.")

    entropy = calculate_entropy(password)
    strength_levels = ["Very Weak", "Weak", "Moderate", "Strong", "Very Strong"]
    entropy_thresholds = [0, 30, 45, 65, 90] 
    for i, threshold in enumerate(entropy_thresholds):
        if entropy < threshold:
            strength = strength_levels[i]
            break
    else:
        strength = strength_levels[-1]

    return strength, feedback, criteria

def calculate_entropy(password):
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digits = "0123456789"
    special = "!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~"

    pool = 0
    if any(char in lower for char in password):
        pool += len(lower)
    if any(char in upper for char in password):
        pool += len(upper)
    if any(char in digits for char in password):
        pool += len(digits)
    if any(char in special for char in password):
        pool += len(special)

    entropy = len(password) * math.log2(pool) if pool > 0 else 0

    return entropy

def time_to_crack(entropy):
    guesses_per_second = 1e10
    seconds = 2 ** entropy / guesses_per_second
    return seconds

def format_time(seconds):
    intervals = (
        ('centuries', 100 * 365 * 24 * 3600),
        ('years', 365 * 24 * 3600),
        ('months', 30 * 24 * 3600),
        ('days', 24 * 3600),
        ('hours', 3600),
        ('minutes', 60),
        ('seconds', 1),
    )
    result = []
    for name, count in intervals:
        value = seconds // count
        if value:
            seconds -= value * count
            result.append(f"{int(value)} {name}")
    if len(result) == 0:
        result.append("<1 second")
    return ', '.join(result)

def check_password():
    password = entry.get().strip()
    if not password:
        result_label.config(text="No password entered.")
        result_label.pack_propagate(True)
        return
    if password.isspace():
        result_label.config(text="Password cannot be all spaces.")
        result_label.pack_propagate(True)
        return
    strength, feedback, criteria = password_strength(password)
    entropy = calculate_entropy(password)
    crack_time_seconds = time_to_crack(entropy)

    feedback_text = "\n".join(f"- {item}" for item in feedback) if feedback else ""
    result_text = (
        f"Password strength: {strength}\n"
        f"Feedback:\n{feedback_text}\n"
        f"Estimated time to crack: {format_time(crack_time_seconds)}"
    )

    result_label.config(text=result_text)
    result_label.pack_propagate(True)
    plot_chart(entropy)

def plot_chart(entropy):
    if not hasattr(plot_chart, "canvas"):
        fig = Figure(figsize=(5, 4), dpi=100)
        plot_chart.ax = fig.add_subplot(111)
        plot_chart.canvas = FigureCanvasTkAgg(fig, master=chart_frame)
        plot_chart.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        chart_frame.pack_propagate(True)

    colors = ["red", "orange", "yellow", "lightgreen", "green"]
    entropy_thresholds = [0, 30, 45, 65, 90]
    strength = sum(entropy >= threshold for threshold in entropy_thresholds)
    color = colors[min(max(1, strength), 5) - 1]

    plot_chart.ax.clear()
    plot_chart.ax.bar(["Password Strength"], [strength], color=color)
    plot_chart.ax.set_ylim(0, 5)
    plot_chart.ax.set_ylabel('Strength Level')
    plot_chart.canvas.draw()
    chart_frame.pack_propagate(True)

def toggle_password():
    if show_password_var.get():
        entry.config(show="")
    else:
        entry.config(show="*")

root = tk.Tk()
root.title("Password Checker")

root.geometry("600x600")

label = tk.Label(root, text="Enter your password:")
label.pack(pady=10)

entry = tk.Entry(root, width=30, show="*")
entry.pack(pady=10)

show_password_var = tk.BooleanVar()
show_password_check = tk.Checkbutton(root, text="Show Password", variable=show_password_var, command=toggle_password)
show_password_check.pack(pady=5)

button = tk.Button(root, text="Check Password", command=check_password)
button.pack(pady=10)

result_label = tk.Label(root, text="", justify=tk.LEFT, anchor="w")
result_label.pack(pady=10, fill=tk.BOTH, expand=1)

chart_frame = tk.Frame(root)
chart_frame.pack(pady=10, fill=tk.BOTH, expand=1)

root.pack_propagate(True)
root.update_idletasks()
root.minsize(root.winfo_width(), root.winfo_height())

root.mainloop()
