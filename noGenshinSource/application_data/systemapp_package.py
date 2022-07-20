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

import json
import time
import os

with open("noGenshinSource\\application_data\\configuration.json", "r", encoding="utf-8") as config:
    app_config = json.load(config)

with open("noGenshinSource\\application_data\localisation\local_russian.json", "r", encoding="utf-8") as russian_json:
    russian_lang = json.load(russian_json)

with open("noGenshinSource\\application_data\localisation\local_english.json", "r", encoding="utf-8") as english_json:
    english_lang = json.load(english_json)

class FunctionsSystem:

    def __init__(self, language: str):
        self.language = language

    def ServerStart(self):

        if self.language == "local_russian":
            print(russian_lang["2_starting_fiddler"])
            os.system(app_config["main-application-settings"]["config-startup-command"]["config-start-fiddler"])
            time.sleep(1.0)
            print(russian_lang["3_started_fiddler"])

            jar_file_name = app_config["main-application-settings"]["config-grasscutter-start-patcher"]
            print(russian_lang["5_starting_jar_package"])
            os.system(f"java -jar {jar_file_name}")
            
        if self.language == "local_english":
            print(english_lang["2_starting_fiddler"])
            os.system(app_config["main-application-settings"]["config-startup-command"]["config-start-fiddler"])
            time.sleep(1.0)
            print(english_lang["3_started_fiddler"])

            jar_file_name = app_config["main-application-settings"]["config-grasscutter-start-patcher"]
            print(english_lang["5_starting_jar_package"])
            os.system(f"cd {jar_file_name} && java -jar grasscutter-1.2.2-dev.jar")

root_system = FunctionsSystem(language="local_english")
root_system.ServerStart()