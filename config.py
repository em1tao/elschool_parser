import configparser

config = configparser.ConfigParser()
config.read("config.ini")
USERDATA = config['LOGIN']
USER = config['user']
PASSWORD = config['password']
