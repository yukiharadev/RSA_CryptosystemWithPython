import tkinter as tk
from tkinter import ttk

from app.app_logic import read_from_file, convert_base64_to_key, encrypt_message
from app.controllers import encode_controller

class EncodePage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        left_frame = tk.Frame(self)
        left_frame.grid(row=0, column=0, padx=10, pady=10, sticky='ns')

        label = tk.Label(left_frame, text="Mã Hoá", font=("Arial", 16))  # Sửa "Decode" thành "Encode"
        label.pack(anchor='w', pady=(0, 10))

        homeButton = tk.Button(
            left_frame, text="Home",
            command=lambda: encode_controller.go_back_to_home(controller)
        )
        homeButton.pack(fill='x', pady=5)

        decodeButton = tk.Button(
            left_frame, text="Decode",
            command=lambda: encode_controller.go_to_decode(controller)
        )
        decodeButton.pack(fill='x', pady=5)

        separator = ttk.Separator(self, orient='vertical')
        separator.grid(row=0, column=1, sticky='ns', padx=5)
        right_frame = tk.Frame(self)
        right_frame.grid(row=0, column=2, padx=10, pady=10, sticky='nsew')

        message_label = tk.Label(right_frame, text="Nhập tin nhắn:", font=("Arial", 12))
        message_label.pack(anchor='w', pady=5)
        self.message_entry = tk.Text(right_frame, width=60, height=2, wrap="word", font=("Arial", 12))
        self.message_entry.pack(fill='x', pady=5)

        message_label_encode = tk.Label(right_frame, text="Tin nhắn mã hoá:", font=("Arial", 12))
        message_label_encode.pack(anchor='w', pady=5)
        self.message_encode = tk.Text(right_frame, width=60, height=2, wrap="word", font=("Arial", 12))
        self.message_encode.pack(fill='x', pady=5)

        encode_button = tk.Button(
            right_frame, text="Encode Message", command=self.encode
        )
        encode_button.pack(fill='x', pady=10)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(2, weight=2)

    def encode(self):
        message = self.message_entry.get("1.0", tk.END).strip()
        public_key = read_from_file("key/public_key.txt")
        decoded_public_key = convert_base64_to_key(public_key)
        print(decoded_public_key)
        if message:
            encode_message = encrypt_message(message, decoded_public_key)
            self.message_encode.delete('1.0', tk.END)
            self.message_encode.insert('1.0', encode_message)

        else:
            print("No message entered.")
