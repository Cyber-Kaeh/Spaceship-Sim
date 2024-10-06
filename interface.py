from gui_components import *
from functions import *

if __name__ == "__main__":
    display = Window()
    btn = Buttons(150, 150, "Clicker!", command=hello_tk())
    display.mainloop()
