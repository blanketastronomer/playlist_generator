from tkinter import *

class Application():
    def __init__(self):
        self.main_window = Tk()

    def load_playlist(self):
        print("Loading playlist...")

    def save_playlist(self):
        print("Saving playlist...")

    def build_menu(self):
        menu = Menu(self.main_window)
        self.main_window.config(menu=menu)

        file_menu = Menu(menu)

        menu.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Load playlist", command=self.load_playlist)
        file_menu.add_command(label="Save playlist", command=self.save_playlist)

    def build_ui(self):
        self.build_menu()

    def run(self):
        self.build_ui()
        self.main_window.mainloop()
