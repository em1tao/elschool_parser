import configparser

config = configparser.ConfigParser()
config.read("config.ini")
USERDATA = config['LOGIN']
USER = USERDATA['username']
PASSWORD = USERDATA['password']
