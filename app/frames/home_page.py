import tkinter as tk
from tkinter import ttk, messagebox  # Import thêm messagebox
import os
from app.controllers import home_controller
from app.app_logic import (
    generate_public_key, generate_private_key, generate_prime_number,
    convert_key_to_base64, write_to_file
)

class HomePage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        left_frame = tk.Frame(self)
        left_frame.grid(row=0, column=0, padx=10, pady=10, sticky='ns')

        label = tk.Label(left_frame, text="Trang chủ", font=("Arial", 16))
        label.pack(anchor='w', pady=(0, 10))

        encodeButton = tk.Button(
            left_frame, text="Encode",
            command=lambda: home_controller.go_to_encode(controller)
        )
        encodeButton.pack(fill='x', pady=5)

        decodeButton = tk.Button(
            left_frame, text="Decode",
            command=lambda: home_controller.go_to_decode(controller)
        )
        decodeButton.pack(fill='x', pady=5)

        separator = ttk.Separator(self, orient='vertical')
        separator.grid(row=0, column=1, sticky='ns', padx=5)

        right_frame = tk.Frame(self)
        right_frame.grid(row=0, column=2, padx=10, pady=10, sticky='nsew')

        self.generate_button = tk.Button(
            right_frame, text="Tạo keys", command=self.generate_keys
        )
        self.generate_button.pack(fill='x', pady=5)

        self.public_key_entry = tk.Text(right_frame, font=("Arial", 12), width=60, height=2, wrap="word")
        self.public_key_entry.pack(pady=5, fill='x')

        self.private_key_entry = tk.Text(right_frame, font=("Arial", 12),width=60, height=2, wrap="word")
        self.private_key_entry.pack(pady=5, fill='x')

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(2, weight=2)

    def generate_keys(self):
        public_key_path = "key/public_key.txt"
        private_key_path = "key/private_key.txt"
        p = generate_prime_number()
        q = generate_prime_number()
        if p == q:
            q = generate_prime_number()

        n = p * q
        phi_n = (p - 1) * (q - 1)
        e = generate_public_key(phi_n)
        d = generate_private_key(e, phi_n)
        public_key = e, n
        private_key = d, n
        base64_public_key = convert_key_to_base64(public_key)
        base64_private_key = convert_key_to_base64(private_key)
        self.public_key_entry.delete('1.0', tk.END)
        self.public_key_entry.insert('1.0', f"Public key: {base64_public_key}")
        self.private_key_entry.delete('1.0', tk.END)
        self.private_key_entry.insert('1.0', f"Private key: {base64_private_key}")
        write_to_file(public_key_path, base64_public_key)
        write_to_file(private_key_path, base64_private_key)
        messagebox.showinfo("Thông báo", f"Đã lưu khóa vào:\n {os.path.abspath(public_key_path)}\n{os.path.abspath(private_key_path)}")
