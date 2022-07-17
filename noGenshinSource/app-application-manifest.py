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

# // Импорт всяких библиотек.
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from application_data import systemapp_package
from application_data.updaterData import api_localgithub_updater
import app_application_settings
import json
import time
import os

class ManifestApplication:

    def __init__(self):
        self.window = Tk()
        self.systemTemp = systemapp_package.FunctionsSystem(language="local_russian")
        self.title = "NoGenshinSource"
        self.title_2 = "NoGenshinSource_settings"

    # // Закрывает приложение и саму консоль.
    def closeApplicationClick(self):
        print("[INF] log: ending application, please wait...")
        time.sleep(1.6)
        os._exit(0)
    
    # // Открывает настройки.
    def settingsOptionClick(self):
        master = app_application_settings.ManifestSettings()
        master.set_settings_window()

    def updaterScriptClick(self):
        master_update = api_localgithub_updater.UpdaterManifest()
        master_update.UpdaterManager()

    # // Запускает сам сервер, но позже переделаю его в запуск Геншина.
    def launchServerClick(self):
        print("[INF] log: launching private server.")
        self.window.destroy()
        self.systemTemp.ServerStart()

    # // Показывает информацию о приложении.
    def informationAppClick(self): # // id: message_box_info
        print("[INF] log: showing messagebox with type 'showinfo' while id 'message_box_info'.")
        messagebox.showinfo(
            title="Info",
            message="Application version: 0.2.8_beta\nAuthor: Extbhite\nGithub: https://github.com/ExtbhiteEAS"
        )

    # // Коротко, данная функция отвечает за то, чтобы передвигало окно.
    # // Но это всё происходит через левый угол.. Я не могу разобраться в этом, так что, вот так вот..)
    # // def move_application_root(self, e):
    # //    self.window.geometry(f"+{e.x_root}+{e.y_root}")

    def start_application(self):
        # // Configuration for application.
        # // Решение вопроса по поводу background и белых линий в программе: https://stackoverflow.com/questions/47357090/
        # // --                                                              https://stackoverflow.com/questions/71551729/
        # // Решил проблему по поводу перемещения окна здесь:                https://stackoverflow.com/questions/14910858/
        try:
            with open("noGenshinSource\\application_data\\app-settings.json", "r", encoding="utf-8") as config_json:
                config = json.load(config_json)
            pycache_clear = config["main-application"]["pycache-clear"]

            # // Очищает кеш от автоматического создания при запуске приложении.
            if pycache_clear == True:
                print("[INF] log: deleting cache...")
                os.system("del noGenshinSource\\application_data\__pycache__\systemapp_package.cpython-310.pyc")
                os.system("del noGenshinSource\\__pycache__\\app_application_settings.cpython-310.pyc")
                os.system("del __pycache__\\api_localgithub_updater.cpython-310.pyc")
                os.system("RMDIR __pycache__")
                os.system("RMDIR noGenshinSource\\application_data\__pycache__ && RMDIR noGenshinSource\\__pycache__")
                print("[INF] log: deleted cache.")
            if pycache_clear == False:
                print("[INF] log: cache clear is disabled...")
                pass
            
            # // Сама структура приложении.
            
            self.window.title(self.title)
            w = 800
            h = 500

            ws = self.window.winfo_screenwidth()
            hs = self.window.winfo_screenheight()

            x = (ws/2) - (w/2)
            y = (hs/2) - (h/2)
            self.window.geometry('%dx%d+%d+%d' % (w, h, x, y))
            self.window.resizable(False, False)
            self.window.wm_attributes("-transparentcolor")
            self.window.overrideredirect(1) # // Это нужно для того, чтобы не перемещали основное окно.
            canv = Canvas(self.window, border=0, width=800, height=500, bg="#191919", highlightthickness=0)
            print("[INF] log: loaded configuration.")

            # // Загружает кнопки и задний фон. Да и остальное понятно, то что это капец какой=то...
            img = ImageTk.PhotoImage(Image.open("noGenshinSource/application_image/background.jpg"))
            print("[INF] log: loaded image 'background'.")
            btn_img = ImageTk.PhotoImage(Image.open("noGenshinSource/application_image/btn_launchserver.png"))
            print("[INF] log: loaded image 'btn_launchserver'.")
            btn_settings = ImageTk.PhotoImage(Image.open("noGenshinSource/application_image/btn_settings.png"))
            print("[INF] log: loaded image 'btn_settings'.")
            btn_info = ImageTk.PhotoImage(Image.open("noGenshinSource/application_image/btn_info.png"))
            print("[INF] log: loaded image 'btn_info'.")
            btn_update = ImageTk.PhotoImage(Image.open("noGenshinSource/application_image/btn_update.png"))
            print("[INF] log: loaded image 'btn_update'.")

            canv.bind("<B1-Motion>")
            canv.create_image(0, 0, anchor=NW, image=img)
            print("[INF] log: Created background image.")

            # // Кнопка для старта сервера(опять же, сделаю под запуск Геншина.)
            buttonStart = Button(
                self.window,
                text="launch_btn",
                image=btn_img,
                bg="#353535",
                activebackground="#353535",
                bd=0,
                relief="sunken",
                command=self.launchServerClick
            )

            # // Кнопка для открытия настроек.
            buttonSettings = Button(
                self.window,
                text="settings_btn",
                image=btn_settings,
                bg="#353535",
                activebackground="#353535",
                bd=0,
                relief="sunken",
                command=self.settingsOptionClick
            )

            # // Кнопка для открытия информации о приложении.
            buttonInfo = Button(
                self.window,
                text="info_application_btn",
                image=btn_info,
                bg="#353535",
                activebackground="#353535",
                bd=0,
                relief="sunken",
                command=self.informationAppClick
            )

            # // Кнопка для обновления скрипта.
            buttonUpdate = Button(
                self.window,
                text="update_btn",
                image=btn_update,
                bg="#353535",
                activebackground="#353535",
                bd=0,
                relief="sunken",
                command=self.updaterScriptClick
            )

            # // Создаёт окно, в котором и будут наши кнопки.
            # // Запуск сервера.
            buttonStart_window = canv.create_window(
                647, # // __x
                389, # // __y
                anchor=NW,
                window=buttonStart
            )
            print("[INF] log: created window with id 'buttonStart_window'.")

            # // Обновление скрипта.
            buttonUpdate_window = canv.create_window(
                647, # // __x
                320, # // __y
                anchor=NW,
                window=buttonUpdate
            )
            print("[INF] log: created window with id 'buttonUpdate_window'.")

            # // Настройки.
            buttonSettings_window = canv.create_window(
                741, # // __x
                20, # // __y
                anchor=NW,
                window=buttonSettings
            )
            print("[INF] log: created window with id 'buttonSettings_window '.")

            # // Информация.
            buttonInformation_window = canv.create_window(
                643, # // __x
                20, # // __y
                anchor=NW,
                window=buttonInfo
            )
            print("[INF] log: created window with id 'buttonInformation_window '.")

            print("[INF] log: successfully started application.") # // Просто уведомляет о завершении
                                                                  # // успешного построение самого приложения.

            # // А это упаковывает и заставляет работать это всё.
            # // И тут ещё присутствует функция показа окна с информацией при запуске программы.
            canv.pack()
            messagebox.showinfo(
                title="Благодарю за установку",
                message="Хоть это программа сделана на коленях и всякого труда, то оно практически в плане использование. Но с полным ознакомлением вам стоит прочитать README.md, но лучше всего вам стоит использовать Cultivation который намного лучше этой программы."
            )
            print("[INF] log: showing messagebox with type 'showinfo'.")

            # // Заставляет работать само приложение.
            self.window.mainloop()
            print("[INF] log: ended application...")
            time.sleep(1)
        except Exception as e:
            print(f"[INF] log: {e}")

root_application = ManifestApplication()
root_application.start_application()