import tkinter as tk
from tkinter import messagebox
from pypresence import Presence


def apply_settings():
    state = state_entry.get()
    details = details_entry.get()
    large_image_url = large_image_entry.get()

    if not state or not details or not large_image_url:
        messagebox.showwarning("Input Error", "Please fill out all fields!")
        return

    try:
        rpc.update(
            state=state,
            details=details,
            large_image=large_image_url
        )
        messagebox.showinfo("Success", "RPC updated successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to update RPC: {e}")

try:
    rpc = Presence(1309681652053708841)
    rpc.connect()
    rpc.update(
        state="state",
        details="details",
        large_image="https://sleepie.dev/boykisser.gif"
    )
except Exception as e:
    messagebox.showerror("Connection Error", f"Failed to connect to Discord: {e}")

root = tk.Tk()
root.title("Custom RPC Configurator")

tk.Label(root, text="State:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
state_entry = tk.Entry(root, width=40)
state_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Details:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
details_entry = tk.Entry(root, width=40)
details_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Large Image URL:").grid(row=2, column=0, padx=10, pady=5, sticky="e")
large_image_entry = tk.Entry(root, width=40)
large_image_entry.grid(row=2, column=1, padx=10, pady=5)

apply_button = tk.Button(root, text="Apply Settings", command=apply_settings)
apply_button.grid(row=5, column=0, columnspan=2, pady=10)

root.mainloop()
