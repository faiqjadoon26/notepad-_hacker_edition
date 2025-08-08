import tkinter as tk
from tkinter import filedialog, messagebox, font

# ---------- MAIN APP ----------
class HackerNotepad:
    def __init__(self, root):
        self.root = root
        self.root.title("Hacker Edition Notepad")
        self.root.geometry("900x600")
        self.file_path = None

        # Set hacker style colors
        self.bg_color = "black"
        self.text_color = "#00FF00"  # neon green
        self.font_family = "Courier New"
        self.font_size = 14

        # Create text widget
        self.text_area = tk.Text(
            self.root,
            wrap="word",
            undo=True,
            bg=self.bg_color,
            fg=self.text_color,
            insertbackground=self.text_color,
            font=(self.font_family, self.font_size)
        )
        self.text_area.pack(fill=tk.BOTH, expand=True)

        # Status bar
        self.status_bar = tk.Label(self.root, text="Words: 0  Characters: 0", anchor="w", bg=self.bg_color, fg=self.text_color)
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)

        # Menu bar
        self.menu_bar = tk.Menu(self.root, bg=self.bg_color, fg=self.text_color, tearoff=False)
        self.root.config(menu=self.menu_bar)

        # File menu
        file_menu = tk.Menu(self.menu_bar, tearoff=False, bg=self.bg_color, fg=self.text_color)
        file_menu.add_command(label="New", command=self.new_file)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_command(label="Save As", command=self.save_file_as)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit)
        self.menu_bar.add_cascade(label="File", menu=file_menu)

        # View menu
        view_menu = tk.Menu(self.menu_bar, tearoff=False, bg=self.bg_color, fg=self.text_color)
        view_menu.add_command(label="Toggle Fullscreen", command=self.toggle_fullscreen)
        self.menu_bar.add_cascade(label="View", menu=view_menu)

        # Bind events
        self.text_area.bind("<KeyRelease>", self.update_status_bar)
        self.root.bind("<F11>", lambda e: self.toggle_fullscreen())

    # ---------- FUNCTIONS ----------
    def new_file(self):
        self.text_area.delete(1.0, tk.END)
        self.file_path = None
        self.root.title("Hacker Edition Notepad - New File")
        self.update_status_bar()

    def open_file(self):
        path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if path:
            with open(path, "r", encoding="utf-8") as file:
                self.text_area.delete(1.0, tk.END)
                self.text_area.insert(tk.END, file.read())
            self.file_path = path
            self.root.title(f"Hacker Edition Notepad - {path}")
            self.update_status_bar()

    def save_file(self):
        if self.file_path:
            with open(self.file_path, "w", encoding="utf-8") as file:
                file.write(self.text_area.get(1.0, tk.END))
        else:
            self.save_file_as()

    def save_file_as(self):
        path = filedialog.asksaveasfilename(defaultextension=".txt",
                                            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if path:
            with open(path, "w", encoding="utf-8") as file:
                file.write(self.text_area.get(1.0, tk.END))
            self.file_path = path
            self.root.title(f"Hacker Edition Notepad - {path}")

    def toggle_fullscreen(self):
        is_fullscreen = self.root.attributes("-fullscreen")
        self.root.attributes("-fullscreen", not is_fullscreen)

    def update_status_bar(self, event=None):
        text = self.text_area.get(1.0, tk.END).strip()
        words = len(text.split())
        chars = len(text)
        self.status_bar.config(text=f"Words: {words}  Characters: {chars}")

# ---------- RUN APP ----------
if __name__ == "__main__":
    root = tk.Tk()
    app = HackerNotepad(root)
    root.mainloop()
