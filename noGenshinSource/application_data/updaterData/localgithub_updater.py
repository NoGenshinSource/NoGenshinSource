import os
import zipfile
import requests
import json
import wget
from tkinter import messagebox

# // TODO: make updater class and etc.

with open("noGenshinSource\\application_data\\updaterData\\localgithub-config.json", "r", encoding="utf-8") as updater_config:
    UpdaterManifestConfig = json.load(updater_config)

class UpdaterManifest:

    def __init__(self):
        self.updaterManifestPath = os.path.isdir("noGenshinSource\\updaterInstall")
        self.versionApp = UpdaterManifestConfig["api-updater"]["version"]["version"]
        self.jsonGetVersionGitHub = json.loads(requests.get("https://raw.githubusercontent.com/NoGenshinSource/NoGenshinSource/stable/noGenshinSource/application_data/updaterData/localgithub-config.json").text)
        self.versionUpdateGet = self.jsonGetVersionGitHub["api-updater"]["version"]["version"]

    def UpdaterManager(self):
        try:
            print("[INF] log: updater: finding update on github...")
            if self.versionApp != self.versionUpdateGet:
                if self.updaterManifestPath == True:
                    messagebox.showinfo(
                        title = "NoGenshinSource Updater",
                        message = "Founded new update!"
                    )
                    print(f"[INF] log: updater: founded new version NoGenshinSource: {self.versionUpdateGet}.")
                    print("[INF] log: updater: In beta stade.\n[INF] log: updater: Downloading zip file...")
                    downloadUrl = f"https://github.com/NoGenshinSource/NoGenshinSource/releases/download/{self.versionUpdateGet}/NoGenshinSource.zip"
                    wget.download(downloadUrl)
                    print("\n[INF] log: updater: [INF] Downloaded zip file.")

                    os.system("move Server.zip noGenshinSource\\updaterInstall")
                    print("[INF] log: updater: Moved zip file to build...")
                    zip_file = zipfile.ZipFile("noGenshinSource\\updaterInstall\\Server.zip", "r")
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
        except Exception as e:
            print(f"[INF] log: updater: updater got error how - {e}")