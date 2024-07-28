import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
import random

class RandomPicker:
    def __init__(self, root):
        self.root = root
        self.root.title("Random Picker")

        ctk.set_appearance_mode("System")  # Modes: "System" (default), "Dark", "Light"
        ctk.set_default_color_theme("blue")  # Themes: "blue" (default), "green", "dark-blue"

        self.label = ctk.CTkLabel(root, text="Enter items:")
        self.label.pack(pady=10)

        self.entries_frame = ctk.CTkFrame(root)
        self.entries_frame.pack(pady=5)

        self.entries = [self.create_entry()]

        self.add_button = ctk.CTkButton(root, text="Add Item", command=self.add_entry)
        self.add_button.pack(pady=5)

        self.pick_button = ctk.CTkButton(root, text="Pick Random Item", command=self.pick_random)
        self.pick_button.pack(pady=10)

        self.result_label = ctk.CTkLabel(root, text="", font=('Helvetica', 14, 'bold'))
        self.result_label.pack(pady=10)

    def create_entry(self):
        entry = ctk.CTkEntry(self.entries_frame, width=300)
        entry.pack(pady=2)
        return entry

    def add_entry(self):
        self.entries.append(self.create_entry())

    def pick_random(self):
        items = [entry.get().strip() for entry in self.entries if entry.get().strip()]
        if items:
            chosen_item = random.choice(items)
            self.result_label.configure(text=f"Chosen Item: {chosen_item}")
        else:
            CTkMessagebox(title="Warning", message="Please enter at least one item.")

if __name__ == "__main__":
    root = ctk.CTk()
    app = RandomPicker(root)
    root.mainloop()
