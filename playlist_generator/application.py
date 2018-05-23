import json
import tkinter as tk
from tkinter import filedialog as fd
from playlist_generator.removable_item import RemovableItem
from playlist_generator.vertical_scrolled_frame import VerticalScrolledFrame

class Application():
    def __init__(self):
        """
        The main application.
        """
        self.main_window = tk.Tk()
        self.FILE_TYPES = (("json files", "*.json"), ("all files", "*.*"))

    def load_playlist(self):
        """
        Loads a playlist from a file.

        Returns:
            None

        Todo:
            * Implement this function.

        """
        print("Loading playlist...")
        self.item_frame.destroy()
        self.reset_item_frame()

        filename = fd.askopenfilename(initialdir='.', title='Select File', filetypes=self.FILE_TYPES)

        try:
            with open(filename, 'r') as read_file:
                data = json.load(read_file)

                for item in data['songs']:
                    removable_item = RemovableItem(self.item_frame.interior, title=item['title'], url=item['url'])
                    removable_item.pack()
        except FileNotFoundError:
            print(f"The system cannot find the specified file {filename}")

    def save_playlist(self):
        """
        Saves a playlist to a file.

        Returns:
            None

        Todo:
            * Implement this function.
        """
        print("Saving playlist...")
        data = dict(songs=[])
        filename = fd.asksaveasfilename(initialdir='.', title='Select File', filetypes=self.FILE_TYPES)

        elements = self.item_frame.interior.winfo_children()

        for element in elements:
            item = dict(title=element.name.get(), url=element.url.get())
            data['songs'].append(item)

        try:
            with open(filename, 'w') as write_file:
                json.dump(data, write_file, indent=True)
        except FileNotFoundError:
            print(f"The system cannot find the specified file at {filename}")

    def build_menu(self):
        """
        Builds the main menu for the application.

        Returns:
            None
        """
        menu = tk.Menu(self.main_window)
        self.main_window.config(menu=menu)

        file_menu = tk.Menu(menu)

        menu.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Load playlist", command=self.load_playlist)
        file_menu.add_command(label="Save playlist", command=self.save_playlist)

    def add_item(self):
        """
        Adds an item to the playlist.

        Each item is a RemovableItem, which contains two labels,
        two Entry() fields, and a button to destroy itself.

        Returns:
            None
        """
        print("Adding an item to the playlist...")
        item = RemovableItem(self.item_frame.interior)
        item.pack()

    def reset_item_frame(self):
        self.item_frame = VerticalScrolledFrame(self.main_window)
        self.item_frame.pack(side=tk.TOP)

    def build_ui(self):
        """
        Builds the application's user interface.

        Returns:
            None
        """
        self.build_menu()

        # Frames
        button_frame = tk.Frame(self.main_window)

        self.reset_item_frame()

        # Button
        btn = tk.Button(button_frame, text='Add playlist item', command=self.add_item)
        btn.pack()

        # Pack EVERYTHING
        button_frame.pack(side=tk.BOTTOM)

        # Ensure a playlist item is already in the window.
        self.add_item()

    def run(self):
        """
        Runs the application.

        Returns:
            None

        """
        self.build_ui()
        self.main_window.mainloop()
