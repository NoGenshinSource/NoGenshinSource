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
from tkinter import ttk
from PIL import ImageTk, Image
from application_data.updaterData import localgithub_updater

class ManifestSettings:

    def __init__(self):
        self.window = Toplevel() # // Я и не думал, что решу проблему с картинками вот так вот..
        # // Tkinter, ты полная хуйня, уж извини. Может Python не для интерфейса сделан и бла-бла, но хоть что-то может.

    def close_settings(self):
        print("[INF] log: settings: destroying window settings.")
        self.window.destroy()

    def updaterScriptClick(self):
        master_update = localgithub_updater.UpdaterManifest()
        master_update.UpdaterManager()

    def set_settings_window(self):
        self.window.title("NoGenshinSource_settings")
        w = 800
        h = 600

        ws = self.window.winfo_screenwidth()
        hs = self.window.winfo_screenheight()

        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        self.window.geometry('%dx%d+%d+%d' % (w, h, x, y))
        self.window.resizable(False, False)
        self.window.wm_attributes("-transparentcolor")
        self.window.overrideredirect(1) # // Это нужно для того, чтобы не перемещали основное окно.
        canv_settings = Canvas(
            self.window,
            border=0,
            width=800,
            height=600,
            bg="#191919",
            highlightthickness=0
        )

        btn_update = ImageTk.PhotoImage(Image.open("noGenshinSource/application_image/btn_update.png"))
        print("[INF] log: loaded image 'btn_update'.")

        # // Кнопка для обновления скрипта.
        buttonUpdate = Button(
            self.window,
            text="update_btn",
            image=btn_update,
            bg="#191919",
            activebackground="#191919",
            bd=0,
            relief="sunken",
            command=self.updaterScriptClick
        )

        buttonSettings = Button(
            self.window,
            text="  ×  ", # // "x" или "×" этот символ.
            command=self.close_settings,
            bg="#191919",
            fg="grey",
            relief="sunken",
            bd=0,
            font=("calibri", 14),
            highlightthickness=0
        )

        comboboxLanguage = ttk.Combobox(
            self.window,
            foreground="black"
        )

        labelUpdateContext = Label(
            self.window,
            text="Check update for better using script and more tools.\n(It's not doing automaticaly so it's cool)",
            background="#191919",
            fg="grey",
            font=("calibri")
        )

        labelLanguageContext = Label(
            self.window,
            text="\tChoose language option here\n\t(Languages not finished as well..)",
            background="#191919",
            fg="grey",
            font=("calibri")
        )
        
        buttonSettings_window = canv_settings.create_window(
            760, # // __x
            8, # // __y
            anchor=NW,
            window=buttonSettings
        )
        print("[INF] log: created window with id 'buttonSettings_window'.")

        labelLanguageContext_window = canv_settings.create_window(
            20, # // __x
            95, # // __y
            anchor=NW,
            window=labelLanguageContext
        )
        print("[INF] log: created window with id 'labelLanguageContext_window'.")

        comboboxLanguage["values"] = ("English", "Russian")
        comboboxLanguage["state"] = "disabled"
        comboboxLanguage.current(0)
        comboboxLanguage_window = canv_settings.create_window(
            370, # // __x
            108, # // __y
            anchor=NW,
            window=comboboxLanguage
        )

        labelUpdateContext_window = canv_settings.create_window(
            20, # // __x
            30, # // __y
            anchor=NW,
            window=labelUpdateContext
        )
        print("[INF] log: created window with id 'labelUpdateContext_window'.")

        # // Обновление скрипта.
        buttonUpdate_window = canv_settings.create_window(
            380, # // __x
            30, # // __y
            anchor=NW,
            window=buttonUpdate
        )
        print("[INF] log: created window with id 'buttonUpdate_window'.")

        canv_settings.pack()
        self.window.mainloop()