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

class account:
    def __init__(self):
        self.accountFilePath = get_data_dir() / 'bank.json'
        self.spendable = None

    def getBalance(self):
        with open(self.accountFilePath, 'rt') as readBank:
            data = json.loads(readBank.read())

    def addStatement(self):
        with open(self.accountFilePath, 'rt') as readBank:
            data = json.loads(readBank.read())
        statements = data['history']
        statements.append(newStatement)
        data['history'] = statements
        with open(self.accountFilePath, 'wt') as writeBank:
            writeBank.write(json.dumps(data, indent=2))
