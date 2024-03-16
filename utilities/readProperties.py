import configparser

config = configparser.RawConfigParser()
config.read(".\\configurations\\config.ini")


class ReadConfig():
    def getApplicationURL():
        url = config.get("common info", "baseURl")
        return url


    def getUseremail():
        username = config.get("common info", "useremail")
        return username


    def getPassword():
        password = config.get("common info", "password")
        return password