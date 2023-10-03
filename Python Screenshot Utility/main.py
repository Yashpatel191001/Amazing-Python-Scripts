from tkinter import *
from PIL import ImageGrab
import datetime, os

class SnippingTool:
    def __init__(self, master):
        self.master = master
        master.attributes('-topmost', True,'-alpha', 0.1)
        master.geometry(f"{master.winfo_screenwidth()}x{master.winfo_screenheight()}")
        master.overrideredirect(True)

        self.start_x, self.start_y, self.end_x, self.end_y = None, None, None, None
        self.snipping = False
        self.canvas = Canvas(master, cursor="cross",bg="black",highlightthickness=0 )
        self.canvas.pack(fill="both", expand=YES )

        self.canvas.bind("<ButtonPress-1>", self.on_mouse_down)
        self.canvas.bind("<B1-Motion>", self.on_mouse_move)
        self.canvas.bind("<ButtonRelease-1>", self.on_mouse_up)
        self.imageDir = "./images"  # add your preferred directory here
        self.imageType = '.png'  # change to '.jpg' if preferred or anyother
        master.bind("<Escape>", self.on_key_press)

    def on_mouse_down(self, event):
        self.snipping = True
        self.start_x, self.start_y = event.x, event.y
        self.end_x, self.end_y = event.x, event.y

    def on_mouse_move(self, event):
        if self.snipping:
            self.end_x, self.end_y = event.x, event.y
            self.draw_border()

    def on_mouse_up(self, event):
        self.snipping = False
        self.draw_border()
        self.capture_snip()

    def draw_border(self):
        self.canvas.delete("border")
        if self.start_x is not None and self.end_x is not None:
            self.canvas.create_rectangle(self.start_x, self.start_y, self.end_x, self.end_y, outline="white", width=0 ,tags="border",fill="white")

    def capture_snip(self):
        self.master.withdraw()
        x1, x2 = min(self.start_x, self.end_x), max(self.start_x, self.end_x)
        y1, y2 = min(self.start_y, self.end_y), max(self.start_y, self.end_y)
        screenshot = ImageGrab.grab(bbox=(x1, y1, x2, y2))
        filename = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S') + self.imageType
        screenshot.save(os.path.join(self.imageDir, filename))
        self.master.destroy()

    def on_key_press(self, event):
        if event.keysym == 'Escape':
            self.master.quit()

def main():
    root = Tk()
    app = SnippingTool(root)
    root.mainloop()

if __name__ == "__main__":
    main()