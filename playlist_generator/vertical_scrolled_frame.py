import tkinter as tk

class VerticalScrolledFrame(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        """
        A pure tkinter scrollable form.

        Notes:
            * Only supports vertical scrolling.
        Args:
            parent (tk.Tk):
            *args:
            **kwargs:
        """
        tk.Frame.__init__(self, parent, *args, **kwargs)

        # Create a canvas and a vertical scrollbar for scrolling it.
        vert_scrollbar = tk.Scrollbar(self, orient=tk.VERTICAL)
        vert_scrollbar.pack(fill=tk.Y, side=tk.RIGHT, expand=tk.FALSE)
        canvas = tk.Canvas(self, bd=0, highlightthickness=0,
                           yscrollcommand=vert_scrollbar.set)
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=tk.TRUE)
        vert_scrollbar.config(command=canvas.yview)

        # Reset the canvas' view
        canvas.xview_moveto(0)
        canvas.yview_moveto(0)

        # Create a frame inside the canvas which will be scrolled with it.
        self.interior = interior = tk.Frame(canvas)
        interior_id = canvas.create_window(0, 0, window=interior, anchor=tk.NW)

        # Track changes to the canvas and frame width and sync them,
        # which updates the scrollbar.
        def _configure_interior(event):
            """
            Update the scrollbars to match the size of the inner frame.

            Args:
                event (Any): Event to bind to.

            Returns:
                None

            """
            size = (interior.winfo_reqwidth(), interior.winfo_reqheight())
            canvas.config(scrollregion="0 0 %s %s" % size)

            if interior.winfo_reqwidth() != canvas.winfo_reqwidth():
                # Update the canvas' width to fit the inner frame.
                canvas.config(width=interior.winfo_reqwidth())

        interior.bind('<Configure>', _configure_interior)

        def _configure_canvas(event):
            """
            Makes the canvas fill the width of the interior.
            Args:
                event (Any): Event to bind to.

            Returns:
                None

            """
            if interior.winfo_reqwidth() != interior.winfo_width():
                # Update inner frame's width to fill the canvas.
                canvas.itemconfigure(interior_id, width=canvas.winfo_width())

        canvas.bind('<Configure>', _configure_canvas)

        def _on_mousewheel(event):
            """
            Add mousewheel support to the scrollbar.

            tkinter doesn't have mousewheel support by default in Canvas.

            Args:
                event (Any): Event to bind to.

            Returns:
                None

            """
            shift = (event.state & 0x1) != 0
            scroll = -1 if event.delta > 0 else 1

            if shift:
                canvas.xview_scroll(scroll, 'units')
            else:
                canvas.yview_scroll(scroll, 'units')

        canvas.bind_all('<MouseWheel>', _on_mousewheel)
