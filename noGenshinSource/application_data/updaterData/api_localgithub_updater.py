import os
import zipfile
import requests
import json
import wget
from tkinter import messagebox

# // TODO: make updater class and etc.

os.system("del __pycache__\\api_localgithub_updater.cpython-310.pyc")
os.system("RMDIR __pycache__")

with open("noGenshinSource\\application_data\\updaterData\\api-localgithub-config.json", "r", encoding="utf-8") as updater_config:
    UpdaterManifestConfig = json.load(updater_config)

class UpdaterManifest:

    def __init__(self):
        self.updaterManifestPath = os.path.isdir("noGenshinSource\\updaterInstall")
        self.jsonGetVersionGitHub = json.loads(requests.get(UpdaterManifestConfig["api-updater"]["versionUpdaterCheck"]))
        self.versionApp = UpdaterManifestConfig["api-updater"]["version"]["version"]

    def UpdaterManager(self):
        if self.versionApp != self.jsonGetVersionGitHub:
            if self.updaterManifestPath == True:
                messagebox.showinfo(
                    title = "NoGenshinSource Updater",
                    message = "Founded new update!"
                )
                print(f"[INF] log: updater: founded new version NoGenshinSource: {self.jsonGetVersionGitHub}.")
                print("[INF] log: updater: In beta stade.\n[INF] log: updater: Downloading zip file...")
                downloadUrl = "https://github.com/ExtbhiteEAS/Genshin-Private-Start/archive/refs/heads/main.zip"
                wget.download(downloadUrl)
                print("\n[INF] log: updater: [INF] Downloaded zip file.")

                os.system("move ***.zip noGenshinSource\\updaterInstall")
                print("[INF] log: updater: Moved zip file to build...")
                zip_file = zipfile.ZipFile("noGenshinSource\\updaterInstall\\***.zip", "r")
                zip_file.extractall()
                zip_file.close()
                print("[INF] log: updater: Successfully updated script. Enjoy.")
            if self.updaterManifestPath == False:
                print("[INF] log: updater: can't find build folder.")
        else:
            messagebox.showinfo(
                title = "NoGenshinSource Updater",
                message = "Update don't founded..."
            )
            print("[INF] log: updater: didn't founded new version.")