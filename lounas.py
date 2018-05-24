import json
import requests
import datetime

class Lounas:
	def __init__(self):
        self.commands = { 'lounas': self.getLounas, 'ruoka': self.getRuoka, 'fusari': self.getFusari }
        self.lounasUrl = 'http://api.ruoka.xyz/' + datetime.datetime.today().strftime('%Y-%m-%d')


    def getCommands(self):
        return self.commands

    def getJson(self):
    	r = requests.get(self.lounasUrl)
    	return r.json()

    def getLounas(self, bot, update, args=''):
    	j = getJson()
    	j['restaurants'][0]['menus'][1]['meals'][1]['contents'][0]['name']

