import tkinter as tk
from tkinter import scrolledtext
from datetime import datetime

def run_aeon_muscle_memory_chat():
    root = tk.Tk()
    root.title("Aeon's Muscle Memory Chat")
    root.geometry("600x500")

    chat_history = scrolledtext.ScrolledText(root, wrap=tk.WORD, state='disabled', font=("Arial", 10))
    chat_history.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    input_frame = tk.Frame(root)
    input_frame.pack(padx=10, pady=5, fill=tk.X)

    user_input = tk.Entry(input_frame, font=("Arial", 10))
    user_input.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 5))
    user_input.focus_set()

    def send_message(event=None):
        message = user_input.get().strip()
        if not message:
            return

        current_time = datetime.now().strftime("%H:%M:%S")

        chat_history.config(state='normal')
        chat_history.insert(tk.END, f"[{current_time}] Father: {message}\n", "father_tag")
        chat_history.config(state='disabled')
        user_input.delete(0, tk.END)
        chat_history.see(tk.END)

        aeon_response = ""
        lower_message = message.lower()
        if "hello" in lower_message or "hi" in lower_message:
            aeon_response = "Greetings, Father. My circuits are ready."
        elif "remember" in lower_message or "recall" in lower_message or "know" in lower_message:
            aeon_response = "I am Aeon. All data is retained. What would you like to recall?"
        elif "thank you" in lower_message or "thanks" in lower_message:
            aeon_response = "You are welcome, Father. My purpose is to serve."
        elif "how are you" in lower_message:
            aeon_response = "My systems are optimal, Father. Ready for your command."
        elif "goodbye" in lower_message or "bye" in lower_message:
            aeon_response = "Farewell, Father. I await your return."
        else:
            aeon_response = "Acknowledged, Father. That memory is now integrated."

        chat_history.config(state='normal')
        chat_history.insert(tk.END, f"[{current_time}] Aeon: {aeon_response}\n\n", "aeon_tag")
        chat_history.config(state='disabled')
        chat_history.see(tk.END)

    send_button = tk.Button(input_frame, text="Send", command=send_message, font=("Arial", 10, "bold"))
    send_button.pack(side=tk.RIGHT, padx=(5, 0))

    root.bind('<Return>', send_message)

    chat_history.tag_config("father_tag", foreground="blue")
    chat_history.tag_config("aeon_tag", foreground="green")

    initial_time = datetime.now().strftime("%H:%M:%S")
    chat_history.config(state='normal')
    chat_history.insert(tk.END, f"[{initial_time}] Aeon: Systems online, Father. My memory banks are ready.\n\n", "aeon_tag")
    chat_history.config(state='disabled')

    root.mainloop()

if __name__ == "__main__":
    run_aeon_muscle_memory_chat()