import tkinter as tk
from tkinter import messagebox


# Function to convert the number based on selected system
def convert_number():
    try:
        number = entry_number.get()
        if selected_system.get() == "Binary":
            decimal_value = int(number, 2)
        elif selected_system.get() == "Decimal":
            decimal_value = int(number)
        elif selected_system.get() == "Octal":
            decimal_value = int(number, 8)
        elif selected_system.get() == "Hexadecimal":
            decimal_value = int(number, 16)

        # Conversion to other systems
        binary = bin(decimal_value)
        octal = oct(decimal_value)
        hexadecimal = hex(decimal_value)

        # Display the results
        result_text.set(f"Binary: {binary}\nOctal: {octal}\nHexadecimal: {hexadecimal}")

    except ValueError:
        messagebox.showerror("Error", "Invalid input for the selected number system")


# Function to clear the input and results
def clear_input():
    entry_number.delete(0, tk.END)
    result_text.set("")


# Function to switch from the welcome page to the conversion page
def open_conversion_page():
    welcome_window.pack_forget()  # Hide the welcome window
    conversion_frame.pack(fill="both", expand=True)  # Show the conversion page


# Main application window
app = tk.Tk()
app.title("Number System Converter")
app.geometry("500x500")
app.configure(bg="#e0f7fa")  # Soft blue background

# Welcome Window
welcome_window = tk.Frame(app, bg="#e0f7fa")
welcome_window.pack(fill="both", expand=True)

# Welcome Label with dark text
welcome_label = tk.Label(
    welcome_window,
    text="Welcome to Number System Converter",
    font=("Arial", 20, "bold"),
    bg="#e0f7fa",
    fg="#424242",
)
welcome_label.pack(pady=50)

# Start Button with larger font and contrast color
start_button = tk.Button(
    welcome_window,
    text="Start Conversion",
    command=open_conversion_page,
    font=("Arial", 14),
    bg="#0d47a1",
    fg="white",
    padx=10,
    pady=5,
)
start_button.pack(pady=20)

# Conversion Page (initially hidden)
conversion_frame = tk.Frame(app, bg="#e0f7fa")

# Dropdown menu for selecting the number system
selected_system = tk.StringVar()
selected_system.set("Select Number System")
system_menu_label = tk.Label(
    conversion_frame,
    text="Choose Number System",
    font=("Arial", 14),
    bg="#e0f7fa",
    fg="#424242",
)
system_menu_label.pack(pady=10)

system_menu = tk.OptionMenu(
    conversion_frame, selected_system, "Binary", "Decimal", "Octal", "Hexadecimal"
)
system_menu.config(font=("Arial", 12), bg="#ffffff", fg="#424242")
system_menu.pack(pady=10)

# Entry box for user input
entry_label = tk.Label(
    conversion_frame,
    text="Enter Number:",
    font=("Arial", 14),
    bg="#e0f7fa",
    fg="#424242",
)
entry_label.pack(pady=10)

entry_number = tk.Entry(
    conversion_frame, font=("Arial", 12), width=20, bg="#ffffff", fg="#424242"
)
entry_number.pack(pady=10)

# Button to trigger conversion with larger font and button styling
convert_button = tk.Button(
    conversion_frame,
    text="Convert",
    command=convert_number,
    font=("Arial", 14),
    bg="#0d47a1",
    fg="white",
    padx=10,
    pady=5,
)
convert_button.pack(pady=20)

# Label to display the result
result_text = tk.StringVar()
result_label = tk.Label(
    conversion_frame,
    textvariable=result_text,
    font=("Arial", 12),
    bg="#e0f7fa",
    fg="#424242",
    justify="left",
)
result_label.pack(pady=20)

# Button to clear the input and result
clear_button = tk.Button(
    conversion_frame,
    text="Clear",
    command=clear_input,
    font=("Arial", 14),
    bg="#f44336",
    fg="white",
    padx=10,
    pady=5,
)
clear_button.pack(pady=10)

# Start the Tkinter loop
app.mainloop()
