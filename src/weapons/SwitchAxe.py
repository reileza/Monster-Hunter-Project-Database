#imports and libraries
import requests
import csv
from bs4 import BeautifulSoup

#site of weapon info
swAxeURL = "https://monsterhunterrise.wiki.fextralife.com/Switch_Axe_Weapon_Tree"
repSwAxe = requests.get(swAxeURL)

swAxeData = BeautifulSoup(repSwAxe.text, 'html.parser')
