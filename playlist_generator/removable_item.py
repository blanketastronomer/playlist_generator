from tkinter import *

class RemovableItem(Frame):
    def __init__(self, parent, title='', url='', **options):
        Frame.__init__(self, parent, **options)

        lbl_name = Label(self, text='Track name:')
        lbl_url = Label(self, text='Youtube URL:')
        btn_destroy = Button(self, text='Remove item', command=self.destroy)

        # Text boxes.  Values can be accessed with get()
        self.name = Entry(self)
        self.url = Entry(self)

        if title != '':
            self.name.insert(0, title)

        if url != '':
            self.url.insert(0, url)

        lbl_name.grid(row=0, column=0)
        self.name.grid(row=0, column=1)
        lbl_url.grid(row=1, column=0)
        self.url.grid(row=1, column=1)

        btn_destroy.grid(row=0, column=2)
