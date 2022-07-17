## Copyright [2022-2024] [Extbite]
##
## Licensed under the Apache License, Version 2.0 (the "License");
## you may not use this file except in compliance with the License.
## You may obtain a copy of the License at
##
##   http://www.apache.org/licenses/LICENSE-2.0
##
## Unless required by applicable law or agreed to in writing, software
## distributed under the License is distributed on an "AS IS" BASIS,
## WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
## See the License for the specific language governing permissions and
## limitations under the License.

from tkinter import *
from PIL import ImageTk, Image

class ManifestSettings:

    def __init__(self):
        self.window = Tk()

    def close_settings(self):
        self.window.destroy()

    def set_settings_window(self):
        self.window.title("NoGenshinSource_settings")
        w = 600
        h = 400

        ws = self.window.winfo_screenwidth()
        hs = self.window.winfo_screenheight()

        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        self.window.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.window.resizable(False, False)
        self.window.wm_attributes("-transparentcolor")
        self.window.overrideredirect(1) # // Это нужно для того, чтобы не перемещали основное окно.
        canv_settings = Canvas(self.window, border=0, width=600, height=400, bg="#191919", highlightthickness=0)

        #img_bg = ImageTk.PhotoImage(Image.open("noGenshinSource/application_image/bg_settings.png"))
        #canv_settings.create_image(0, 0, anchor=NW, image=img_bg)

        #btn_settings = ImageTk.PhotoImage(Image.open("noGenshinSource/application_image/btn_settings.png"))
        buttonSettings = Button(
            self.window,
            text="Close",
            bg="#353535",
            activebackground="#353535",
            bd=0,
            relief="sunken",
            command=self.close_settings
        )
        
        buttonSettings_window = canv_settings.create_window(
            550, # // __x
            10, # // __y
            anchor=NW,
            window=buttonSettings
        )
        canv_settings.pack()
        self.window.mainloop()