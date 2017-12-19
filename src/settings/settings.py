"""
Log
+--------------------------+------------+----------------------------------+
| Who                      | When       | What                             |
+--------------------------+------------+----------------------------------+
| Wesley Ameling           | 17-12-2017 | Create this file, setting up the |
|                          |            | skeleton of this application     |
+--------------------------+------------+----------------------------------+

"""
import json
import os


DEFAULT_SETTINGS = {

}

SETTINGS_FILE_PATH = os.path.join(os.path.dirname(__file__), '.settings.json')


class Settings(object):
    instance = None

    @staticmethod
    def getInstance():
        if Settings.instance is None:
            Settings.instance = Settings()
            Settings.instance.loadFromFile()
        return Settings.instance

    def __init__(self):
        self.loadedFromFile = False
        self.settings = {}

    def loadFromFile(self):
        if not self.loadedFromFile:
            if os.path.isfile(SETTINGS_FILE_PATH):
                with open(SETTINGS_FILE_PATH, 'r') as inFile:
                    self.settings = json.load(inFile)
            self.loadedFromFile = True

    def writeToFile(self):
        with open(SETTINGS_FILE_PATH, 'w') as outFile:
            json.dump(self.settings, outFile)

    def getSetting(self, settingName):
        value = self.settings.get(settingName, None)
        if value is None:
            value = DEFAULT_SETTINGS.get(settingName)
        return value

    def setSetting(self, settingName, settingValue):
        self.settings[settingName] = settingValue