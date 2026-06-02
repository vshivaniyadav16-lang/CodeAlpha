import tkinter as tk
from tkinter import ttk, messagebox
from deep_translator import GoogleTranslator

# Translate function
def translate_text():
    try:
        text = input_text.get("1.0", tk.END).strip()

        if not text:
            messagebox.showwarning("Warning", "Please enter some text")
            return

        source_lang = source_var.get()
        target_lang = target_var.get()

        translated = GoogleTranslator(
            source=source_lang,
            target=target_lang
        ).translate(text)

        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, translated)

    except Exception as e:
        messagebox.showerror("Error", str(e))

# Copy function
def copy_text():
    translated = output_text.get("1.0", tk.END).strip()

    if translated:
        root.clipboard_clear()
        root.clipboard_append(translated)
        messagebox.showinfo("Success", "Text copied!")

# Main Window
root = tk.Tk()
root.title("Language Translation Tool")
root.geometry("700x500")

# Input
tk.Label(root, text="Enter Text", font=("Arial", 12)).pack()

input_text = tk.Text(root, height=6, width=70)
input_text.pack(pady=5)

# Languages
languages = {
    "English": "en",
    "Hindi": "hi",
    "French": "fr",
    "German": "de",
    "Spanish": "es",
    "Telugu": "te",
    "Tamil": "ta"
}

frame = tk.Frame(root)
frame.pack(pady=10)

# Source Language
tk.Label(frame, text="Source Language").grid(row=0, column=0)

source_var = tk.StringVar(value="en")

source_menu = ttk.Combobox(
    frame,
    values=list(languages.keys()),
    state="readonly"
)
source_menu.current(0)
source_menu.grid(row=1, column=0)

# Target Language
tk.Label(frame, text="Target Language").grid(row=0, column=1)

target_var = tk.StringVar(value="hi")

target_menu = ttk.Combobox(
    frame,
    values=list(languages.keys()),
    state="readonly"
)
target_menu.current(1)
target_menu.grid(row=1, column=1)

def update_source(event):
    source_var.set(languages[source_menu.get()])

def update_target(event):
    target_var.set(languages[target_menu.get()])

source_menu.bind("<<ComboboxSelected>>", update_source)
target_menu.bind("<<ComboboxSelected>>", update_target)

# Translate Button
tk.Button(
    root,
    text="Translate",
    command=translate_text,
    bg="lightblue"
).pack(pady=10)

# Output
tk.Label(root, text="Translated Text", font=("Arial", 12)).pack()

output_text = tk.Text(root, height=6, width=70)
output_text.pack(pady=5)

# Copy Button
tk.Button(
    root,
    text="Copy Text",
    command=copy_text,
    bg="lightgreen"
).pack(pady=10)

root.mainloop()
      