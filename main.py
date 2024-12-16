"""
QR-Code Generator with python
"""
import tkinter as tk


class qrCode(tk.Tk):
    def __init__(self, size):
        super().__init__()
        self.title('QR-Code Generator')
        self.size = size
        self.sqrsize = 5

        self.canvas = tk.Canvas(self, bg='blue', height=5*self.size, width=5*self.size)
        self.canvas.pack()


code = qrCode(100)
code.mainloop()


        
