import tkinter as tk
import pywhatkit

# Function to send the WhatsApp message
def send_whatsapp_message():
    phone_number = phone_number_entry.get()
    message = message_text.get("1.0", "end-1c")  # Get message text from Text widget
    try:
        # Sending message
        pywhatkit.sendwhatmsg(phone_number, message, int(hours_entry.get()), int(minutes_entry.get()))
        status_label.config(text="Message sent successfully!", fg="green")
    except Exception as e:
        status_label.config(text=f"Error sending message: {str(e)}", fg="red")

# Function to clear the input fields
def clear_input_fields():
    phone_number_entry.delete(0, "end")
    message_text.delete("1.0", "end")
    hours_entry.delete(0, "end")
    minutes_entry.delete(0, "end")
    status_label.config(text="")

# Create the main window
root = tk.Tk()
root.title("Auto WhatsApp Message Sender using tkinter by Arnab")
root.geometry("600x500")

# Set dark mode background color
root.configure(bg="#333")

# Create and pack labels and entry fields with white text and bold font
phone_label = tk.Label(root, text="Enter WhatsApp Number:", bg="#333", fg="white", font=("Helvetica", 10, "bold"))
phone_label.place(x=40, y=60)

phone_number_entry = tk.Entry(root)
phone_number_entry.place(x=252, y=60)

message_label = tk.Label(root, text="Enter Message:", bg="#333", fg="white", font=("Helvetica", 10, "bold"))
message_label.place(x=40, y=120)

message_text = tk.Text(root, height=5, width=40)
message_text.place(x=40, y=170)

time_label = tk.Label(root, text="Enter Scheduled Time (HH:MM):", bg="#333", fg="white", font=("Helvetica", 10, "bold"))
time_label.place(x=40, y=285)

hours_entry = tk.Entry(root, width=2)
hours_entry.place(x=300, y=285)
tk.Label(root, text=":", bg="#333", fg="white", font=("Helvetica", 10, "bold")).place(x=320, y=285)
minutes_entry = tk.Entry(root, width=2)
minutes_entry.place(x=340, y=285)

# Create buttons with white text and bold font
send_button = tk.Button(root, text="Send Message", command=send_whatsapp_message, bg="#444", fg="white", font=("Helvetica", 12, "bold"))
clear_button = tk.Button(root, text="Clear", command=clear_input_fields, bg="#444", fg="white", font=("Helvetica", 12, "bold"))

send_button.place(x=150, y=400)
clear_button.place(x=320, y=400)

# Create and pack a status label
status_label = tk.Label(root, text="", fg="green", bg="#333", font=("Helvetica", 10, "bold"))
status_label.place(x=40, y=450)

root.mainloop()
