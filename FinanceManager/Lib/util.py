import json
import pathlib
from os import system

def get_data_dir():
    if system() == "Windows":
        data_dir = pathlib.Path(os.path.expandvars("%LOCALAPPDATA%")) / "Finance-Manager"
    else:
        data_dir = pathlib.Path.home() / ".config" / "Finance-Manager"
    if not data_dir.exists():
        data_dir.mkdir(parents=True, exist_ok=True)
    return(data_dir)

def checkIsInitialized():
    dataDir = get_data_dir()
    configFile = dataDir / 'config.json'
    if configFile.exists():
        with open(configFile, 'rt') as readConfig:
            configData = json.loads(configFile.read())
            if configData['initialized'] == True:
                return True
            else:
                return False
    else:
        return False