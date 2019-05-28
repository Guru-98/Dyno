import configparser

config = configparser.ConfigParser()
config.read('settings.ini')

DC1 = config.get('devices','DC1',fallback="COM1")
DC2 = config.get('devices','DC2',fallback="COM1")
DC3 = config.get('devices','DC3',fallback="COM1")
DC4 = config.get('devices','DC4',fallback="COM1")
DC5 = config.get('devices','DC5',fallback="COM1")
DCS = [DC1,DC2,DC3,DC4,DC5]

VFD = config.get("devices","VFD",fallback="COM1")
OSC = config.get("devices","OSC",fallback="COM1")