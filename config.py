import configparser

config = configparser.ConfigParser()
config.read("config.ini")
USERDATA = config['LOGIN']
USERNAME = USERDATA['username']
PASSWORD = USERDATA['password']
