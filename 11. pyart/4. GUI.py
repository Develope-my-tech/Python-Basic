'''
GUI 표준 라이브러리
- Tkinter
- Qt
- GTK+
- WxPython
- Kivy
'''

# 1. Tkinter
import tkinter
from PIL import Image, ImageTk

main = tkinter.Tk()
img = Image.open('sim.png')
tkimg = ImageTk.PhotoImage(img)
tkinter.Label(main, image=tkimg).pack()
main.mainloop()

