
import yaml
def readConf(filePath):

    with open(filePath, 'r') as stream:
        return yaml.load(stream)