import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from app.controllers import decode_controller
from app.app_logic import decrypt_message, read_from_file, convert_base64_to_key


class DecodePage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        left_frame = tk.Frame(self)
        left_frame.grid(row=0, column=0, padx=10, pady=10, sticky='ns')

        label = tk.Label(left_frame, text="Giải Mã", font=("Arial", 16))
        label.pack(anchor='w', pady=(0, 10))

        homeButton = tk.Button(
            left_frame, text="Home",
            command=lambda: decode_controller.go_back_to_home(controller)
        )
        homeButton.pack(fill='x', pady=5)

        encodeButton = tk.Button(
            left_frame, text="Encode",
            command=lambda: decode_controller.go_to_encode(controller)
        )
        encodeButton.pack(fill='x', pady=5)

        separator = ttk.Separator(self, orient='vertical')
        separator.grid(row=0, column=1, sticky='ns', padx=5)

        right_frame = tk.Frame(self)
        right_frame.grid(row=0, column=2, padx=10, pady=10, sticky='nsew')

        encrypt_message_label = tk.Label(right_frame, text="Tin nhắn mã hoá:", font=("Arial", 12))
        encrypt_message_label.pack(anchor='w', pady=5)
        self.encrypt_message_entry = tk.Text(right_frame, width=60, height=2, wrap="word", font=("Arial", 12))
        self.encrypt_message_entry.pack(fill='x', pady=5)
        decrypt_message_label = tk.Label(right_frame, text="Tin nhắn bản rõ:", font=("Arial", 12))
        decrypt_message_label.pack(anchor='w', pady=5)
        self.decrypt_message_entry = tk.Text(right_frame, width=60, height=2, wrap="word", font=("Arial", 12))
        self.decrypt_message_entry.pack(fill='x', pady=5)
        self.load_private_key_button = tk.Button(
            right_frame, text="Select Key", command=self.load_private_key
        )
        self.load_private_key_button.pack(fill='x', pady=5)

        self.private_key = None

        self.decrypt_button = tk.Button(
            right_frame, text="Decrypt", command=self.decode
        )
        self.decrypt_button.pack(fill='x', pady=5)

    def load_private_key(self):
        file_path = filedialog.askopenfilename(
            title="Select Private Key File"
        )
        if file_path:
            self.private_key = read_from_file(file_path)

    def decode(self):
        message = self.encrypt_message_entry.get("1.0", tk.END).strip()
        print("private key", self.private_key)
        if message:
            private_key_data = convert_base64_to_key(self.private_key)
            decrypted_message = decrypt_message(message, private_key_data)
            self.decrypt_message_entry.delete('1.0', tk.END)
            self.decrypt_message_entry.insert('1.0', decrypted_message)

