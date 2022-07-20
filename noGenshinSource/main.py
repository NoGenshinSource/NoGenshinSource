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
from tkinter import messagebox
from PIL import ImageTk, Image
import settings_manifest
import tkinter as tk
import webbrowser
import json
import os

# // Стоит не забывать, что это решение проблемы,
# // а также вот ссылка на его решение, чтобы не подумали обо мне плохом.
# // https://stackoverflow.com/questions/70996098/tkinter-button-over-transparent-background/71011331#71011331
# // Может я и глупый и плох, но искать нужно что-то для его исправления.
class CanvasButton:
    """ Create leftmost mouse button clickable canvas image object.

    The x, y coordinates are relative to the top-left corner of the canvas.
    """
    flash_delay = 100  # Milliseconds.

    def __init__(self, canvas, x, y, image_path, command, state=tk.NORMAL):
        self.canvas = canvas
        self.btn_image = tk.PhotoImage(file=image_path)
        self.canvas_btn_img_obj = canvas.create_image(x, y, anchor='nw', state=state,
                                                      image=self.btn_image)
        canvas.tag_bind(self.canvas_btn_img_obj, "<ButtonRelease-1>",
                        lambda event: (self.flash(), command()))
    def flash(self):
        self.set_state(tk.HIDDEN)
        self.canvas.after(self.flash_delay, self.set_state, tk.NORMAL)

    def set_state(self, state):
        """ Change canvas button image's state.

        Normally, image objects are created in state tk.NORMAL. Use value
        tk.DISABLED to make it unresponsive to the mouse, or use tk.HIDDEN to
        make it invisible.
        """
        self.canvas.itemconfigure(self.canvas_btn_img_obj, state=state)

class ManifestApplication:
    """Создаёт само приложение и его структуру, но функции не стоит трогать - может повлиять на нестабильность.\n
Ниже буду приведены функции, которые находятся в скрипте:
- `self.closeApplicationClick` - закрывает процесс самого приложения, а также сам консоль в котором и работает наш GUI.
- `self.settingsOptionClick` - открывает настройки самой программы, настройки расположены в другом системном файле, а к чему я клоню?
К тому, что не нужно трогать папку `noGenshinSource\*` - на памятку. С остальными функциями настроек можно познакомиться наведя на `ManifestSettings`
или открыть файл под названием `settings_manifest.py`, только **НИЧЕГО НЕ ТРОГАЙТЕ ЕСЛИ НЕ ЗНАЕТЕ ПРОГРАММИРОВАНИЕ!**
- `self.launchServerClick` - запускает сервер, но только это приложение, а jar файл как известно - через саму консоль. Консоль сама не закроется,
если вы не закроете его сами после запуска.
- `self.informationAppClick` - тут описывать нечего, показывает информацию о скрипте.
- `self.start_application` - запускает само окно приложение, а если его завершить то и сама консоль закроется. :)
    """

    def __init__(self):
        self.window = tk.Tk()
        self.title = "NoGenshinSource"

    # // Закрывает приложение и саму консоль.
    def closeApplicationClick(self):
        print("[INF] log: ending application, please wait...")
        self.window.destroy()
    
    # // Открывает настройки.
    def settingsOptionClick(self):
        print("[INF] log: settings: set new window")
        master = settings_manifest.ManifestSettings()
        master.set_settings_window()

    # // Запускает сам сервер, но позже переделаю его в запуск Геншина.
    def launchServerClick(self):
        print("[INF] log: launching private server.")
        #self.window.destroy()
        os.system("start cmd.exe /C noGenshinSource\\localserver-start.bat")

    def launchGenshinClick(self):
        print("[INF] log: launching genshin impact client.")
        self.window.destroy()
        os.system("start noGenshinSource\\NoGenshinSource.lnk")

    # // Открывает GitHub проект самого приложения.
    def githubOpenBrowser(self):
        webbrowser.open_new_tab("https://github.com/NoGenshinSource/NoGenshinSource")

    # // Открывает Telegram для связи.
    def telegramOpenBrowser(self):
        webbrowser.open_new_tab("https://t.me/Extbhite")

    # // Показывает информацию о приложении.
    def informationAppClick(self): # // id: message_box_info
        with open("noGenshinSource\\application_data\\updaterData\\localgithub-config.json", "r", encoding="utf-8") as info_config:
            InfoManifestConfig = json.load(info_config)
        versionApp = InfoManifestConfig["api-updater"]["version"]["version"]
        authorApp = InfoManifestConfig["api-updater"]["version"]["author"]
        print("[INF] log: showing messagebox with type 'showinfo' while id 'message_box_info'.")
        messagebox.showinfo(
            title="Info",
            message=f"Application version: {versionApp}\nAuthor: {authorApp}\nGithub: https://github.com/NoGenshinSource/NoGenshinSource"
        )

    def start_application(self):
        # // Configuration for application.
        # // Решение вопроса по поводу background и белых линий в программе: https://stackoverflow.com/questions/47357090/
        # // --                                                              https://stackoverflow.com/questions/71551729/
        # // Решил проблему по поводу перемещения окна здесь:                https://stackoverflow.com/questions/14910858/
        try:
            with open("noGenshinSource\\application_data\\settings.json", "r", encoding="utf-8") as config_json:
                config = json.load(config_json)
            pycache_clear = config["main-application"]["pycache-clear"]

            # // Очищает кеш от автоматического создания при запуске приложении.
            if pycache_clear == True:
                print("[INF] log: deleting cache...")
                os.system("del noGenshinSource\\__pycache__\\settings_manifest.cpython-310.pyc && RMDIR noGenshinSource\\__pycache__")
                os.system("del noGenshinSource\\application_data\\updaterData\\__pycache__\\localgithub_updater.cpython-310.pyc")
                os.system("RMDIR noGenshinSource\\application_data\\updaterData\\__pycache__")
                print("[INF] log: deleted cache.")
            if pycache_clear == False:
                print("[INF] log: cache clear is disabled...")
                pass
            
            # // Сама структура приложении.
            w = 1280
            h = 768

            ws = self.window.winfo_screenwidth()
            hs = self.window.winfo_screenheight()

            x = (ws/2) - (w/2)
            y = (hs/2) - (h/2)
            
            self.window.title(self.title)
            self.window.geometry('%dx%d+%d+%d' % (w, h, x, y))
            self.window.iconbitmap("noGenshinSource/application_image/icon.ico")
            self.window.resizable(False, False)
            self.window.wm_attributes("-transparentcolor")
            self.window.overrideredirect(1) # // Это нужно для того, чтобы не перемещали основное окно.

            canv = tk.Canvas(
                self.window,
                border=0,
                width=1280,
                height=768,
                relief="raised",
                bd=0,
                bg="#191919",
                highlightthickness=0
            )
            title_bar = tk.Frame(
                self.window,
                bg="#111111",
                relief="raised",
                bd=0
            )

            # // Фальшивая строка заголовка.
            # // Но перемещать его не будет. :)
            title_label = tk.Label(
                title_bar,
                text="    NoGenshinSource",
                bg="#111111",
                fg="grey",
                highlightthickness=0
            )
            close_button = tk.Button(
                title_bar,
                text="  ×  ", # // "x" или "×" этот символ.
                command=self.closeApplicationClick,
                bg="#111111",
                fg="grey",
                relief="sunken",
                bd=0,
                font=("calibri", 14),
                highlightthickness=0
            )

            title_label.pack(
                side=tk.LEFT,
                pady=4
            )
            close_button.pack(
                side=tk.RIGHT,
                padx=5
            )
            title_bar.pack(expand=1, fill=tk.X) # // Пакует сам заголовок
            title_bar.bind("<B1-Motion>") # // Отображает сам заголовок.
            print("[INF] log: loaded configuration.")

            # // Загружает кнопки и задний фон. Да и остальное понятно, то что это капец какой=то...
            img = ImageTk.PhotoImage(Image.open("noGenshinSource/application_image/background.jpg"))
            btn_launch = "noGenshinSource/application_image/btn_launchserver.png"
            btn_launch_local = "noGenshinSource/application_image/btn_launch.png"
            btn_img_github = "noGenshinSource/application_image/launcher_sm_img/github_icon.png"
            btn_img_telegram = "noGenshinSource/application_image/launcher_sm_img/telegram_icon.png"
            btn_settings = ImageTk.PhotoImage(Image.open("noGenshinSource/application_image/btn_settings.png"))
            btn_info = ImageTk.PhotoImage(Image.open("noGenshinSource/application_image/btn_info.png"))
            
            canv.create_image(0, 0, anchor=tk.NW, image=img)
            print("[INF] log: created background image.")

            # // Кнопка для открытия настроек.
            buttonSettings = tk.Button(
                self.window,
                text="settings_btn",
                image=btn_settings,
                bg="#212121",
                activebackground="#212121",
                bd=0,
                relief="sunken",
                command=self.settingsOptionClick
            )

            # // Кнопка для открытия информации о приложении.
            buttonInfo = tk.Button(
                self.window,
                text="info_application_btn",
                image=btn_info,
                bg="#212121",
                activebackground="#212121",
                bd=0,
                relief="sunken",
                command=self.informationAppClick
            )

            # // Создаёт окно, в котором и будут наши кнопки.
            # // Запуск Геншина.
            canvas_buttonLaunch = CanvasButton(
                canv,
                1014,
                638,
                btn_launch,
                self.launchGenshinClick
            )

            # // Запуск сервера.
            canvas_buttonLaunchLocal = CanvasButton(
                canv,
                920,
                638,
                btn_launch_local,
                self.launchServerClick
            )

            # // Соц. сети и прочее.
            # // Github.
            canvas_buttonGithub = CanvasButton(
                canv,
                1225,
                60,
                btn_img_github,
                self.githubOpenBrowser
            )
            
            # // Telegram
            canvas_buttonTelegram = CanvasButton(
                canv,
                1225,
                125,
                btn_img_telegram,
                self.telegramOpenBrowser
            )

            # // Настройки.
            buttonSettings_window = canv.create_window(
                14, # // __x
                5, # // __y
                anchor=tk.NW,
                window=buttonSettings
            )

            # // Информация.
            buttonInformation_window = canv.create_window(
                61, # // __x
                5, # // __y
                anchor=tk.NW,
                window=buttonInfo
            )

            print("[INF] log: successfully started application.") # // Просто уведомляет о завершении
                                                                  # // успешного построение самого приложения.

            # // А это упаковывает и заставляет работать это всё.
            # // И тут ещё присутствует функция показа окна с информацией при запуске программы.
            canv.pack()
            print("[INF] log: showing messagebox with type 'showinfo'.")
            messagebox.showinfo(
                title="Благодарю за установку",
                message="Хоть это программа сделана на коленях и БЕЗ всякого труда, то оно практически в плане использование. Но с полным ознакомлением вам стоит прочитать README_noGenshinSource.md после скачивание Server.zip, но лучше всего вам стоит использовать Cultivation который намного лучше этой программы."
            )

            # // Заставляет работать само приложение.
            self.window.mainloop()
            print("[INF] log: ended application...")
            os._exit(0)
        except Exception as e:
            print(f"[INF] log: {e}")

if __name__ == "__main__":
    root_application = ManifestApplication()
    root_application.start_application()