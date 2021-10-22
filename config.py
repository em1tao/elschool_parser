import configparser

config = configparser.ConfigParser()
config.read("config.ini")
USERDATA = config['LOGIN']
USER = USERDATA['User']
PASSWORD = USERDATA['Password']
