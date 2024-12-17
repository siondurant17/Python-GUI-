import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Main Window
root = tk.Tk()
root.title("Durant NBA Player Data Entry Form")

# Create a LabelFrame for Team Information
frame1 = tk.LabelFrame(root, text="Team Information", padx=10, pady=10)
frame1.grid(row=0, column=0, padx=10, pady=10)

# Team Name Label and Entry
label_team_name = tk.Label(frame1, text="Team Name:")
label_team_name.grid(row=0, column=0, padx=5, pady=5)
entry_team_name = tk.Entry(frame1)
entry_team_name.grid(row=0, column=1, padx=5, pady=5)

# City Label and Entry
label_city = tk.Label(frame1, text="City:")
label_city.grid(row=1, column=0, padx=5, pady=5)
entry_city = tk.Entry(frame1)
entry_city.grid(row=1, column=1, padx=5, pady=5)

# Coach Label and Entry
label_coach = tk.Label(frame1, text="Coach:")
label_coach.grid(row=2, column=0, padx=5, pady=5)
entry_coach = tk.Entry(frame1)
entry_coach.grid(row=2, column=1, padx=5, pady=5)

# Create a LabelFrame for Player Information
frame2 = tk.LabelFrame(root, text="Player Information", padx=10, pady=10)
frame2.grid(row=1, column=0, padx=10, pady=10)

# Player Name Label and Entry
label_player = tk.Label(frame2, text="Player:")
label_player.grid(row=0, column=0, padx=5, pady=5)
entry_player = tk.Entry(frame2)
entry_player.grid(row=0, column=1, padx=5, pady=5)

# Player Position Label and Entry
label_position = tk.Label(frame2, text="Select Position:")
label_position.grid(row=1, column=0, padx=5, pady=5)
combo_position = ttk.Combobox(frame2, values=["Guard", "Forward", "Center"])
combo_position.grid(row=1, column=1, padx=5, pady=5)

# Jersey Number Label and Entry
label_jersey_number = tk.Label(frame2, text="Jersey Number:")
label_jersey_number.grid(row=2, column=0, padx=5, pady=5)
spinbox_jersey_number = tk.Spinbox(frame2, from_=0, to=100)
spinbox_jersey_number.grid(row=2, column=1, padx=5, pady=5)

# Create a LabelFrame for Player Status
frame3 = tk.LabelFrame(root, text="Player Status", padx=10, pady=10)
frame3.grid(row=2, column=0, padx=10, pady=10)

# Player Status Checkboxes
checkbox_active_var = tk.BooleanVar()
checkbox_retired_var = tk.BooleanVar()
checkbox_active = tk.Checkbutton(frame3, text="Active", variable=checkbox_active_var)
checkbox_active.grid(row=0, column=0, padx=5, pady=5)
checkbox_retired = tk.Checkbutton(frame3, text="Retired", variable=checkbox_retired_var)
checkbox_retired.grid(row=0, column=1, padx=5, pady=5)

# Agreement
frame4 = tk.LabelFrame(root, text="Agreement", padx=10, pady=10)
frame4.grid(row=3, column=0, padx=10, pady=10)

# Agreement Checkbox
checkbox_agree_var = tk.BooleanVar()
checkbox_agree = tk.Checkbutton(frame4, text="I agree to the terms and conditions", variable=checkbox_agree_var)
checkbox_agree.grid(row=0, column=0, padx=5, pady=5)

# Save Button
frame5 = tk.LabelFrame(root, text="Save", padx=10, pady=10)
frame5.grid(row=4, column=0, padx=10, pady=10)

# Function to handle button click event and save data
def save_data():
    # Access widget data using .get() method
    team_name = entry_team_name.get()
    city = entry_city.get()
    coach = entry_coach.get()
    player_name = entry_player.get()
    position = combo_position.get()
    jersey_number = spinbox_jersey_number.get()
    is_active = checkbox_active_var.get()
    is_retired = checkbox_retired_var.get()

    # Validate input fields
    if not (team_name and city and coach and player_name and position and jersey_number):
        print("All fields must be filled out.")
        messagebox.showwarning("Input Error", "All fields must be filled out.")
        return

    if not checkbox_agree_var.get():
        print("You must agree to the terms and conditions.")
        messagebox.showwarning("Agreement Required", "You must agree to the terms and conditions.")
        return

    # Write data to a file (append mode to add new entries)
    with open('team_and_player_info.txt', 'a') as file:
        file.write("----- New Entry -----\n")
        file.write(f"Team Name: {team_name}\n")
        file.write(f"City: {city}\n")
        file.write(f"Coach: {coach}\n")
        file.write(f"Player Name: {player_name}\n")
        file.write(f"Position: {position}\n")
        file.write(f"Jersey Number: {jersey_number}\n")
        file.write(f"Active: {'Yes' if is_active else 'No'}\n")
        file.write(f"Retired: {'Yes' if is_retired else 'No'}\n")
        file.write("---------------------\n\n")

    print("Data Saved")
    messagebox.showinfo("Success", "Data has been saved successfully.")
    
# Function to open and display the contents of the text file
def open_file():
    try:
        with open('team_and_player_info.txt', 'r') as file:
            content = file.read()
            messagebox.showinfo("File Content", content)
    except FileNotFoundError:
        messagebox.showerror("Error", "File not found. Please save data first.")


    # Clear the form fields after saving
    entry_team_name.delete(0, tk.END)
    entry_city.delete(0, tk.END)
    entry_coach.delete(0, tk.END)
    entry_player.delete(0, tk.END)
    combo_position.set('')
    spinbox_jersey_number.delete(0, tk.END)
    checkbox_active_var.set(False)
    checkbox_retired_var.set(False)
    checkbox_agree_var.set(False)

# Attach the save_data function to the button click event
button_save = tk.Button(root, text="Save", command=save_data)
button_save.grid(row=5, column=0, padx=10, pady=10)

# Run the app
root.mainloop()
