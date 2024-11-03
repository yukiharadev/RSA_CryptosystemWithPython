import tkinter as tk

from .frames.decode_page import DecodePage
from .frames.home_page import HomePage
from .frames.encode_page import EncodePage

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("RSA Encryptor Decryptor")
        self.geometry("700x250")

        container = tk.Frame(self)
        container.pack(fill="both", expand=True)

        self.frames = {}
        for F in (HomePage, EncodePage, DecodePage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("HomePage")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()
