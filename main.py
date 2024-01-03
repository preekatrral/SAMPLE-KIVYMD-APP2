import tkinter as tk

def get_screen_resolution():
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    return screen_width, screen_height

def display_resolution():
    resolution = get_screen_resolution()
    resolution_label.config(text=f"Screen Resolution: {resolution[0]} x {resolution[1]}")

# Create the main window
root = tk.Tk()
root.title("Screen Resolution Viewer")

# Create a label to display the resolution
resolution_label = tk.Label(root, text="")
resolution_label.pack(pady=20)

# Create a button to update and display the resolution
update_button = tk.Button(root, text="Update Resolution", command=display_resolution)
update_button.pack(pady=10)

# Display the initial resolution
display_resolution()

# Start the main loop
root.mainloop()
