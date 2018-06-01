from bs4 import BeautifulSoup
import urllib.request

TARGET = "https://support.fire-emblem-heroes.com/voting_gauntlet/tournaments/13"


class CharaInfo:
		def __init__(self):
				name = ""
				point_str = "" 
				point = 0
		def setData(self, name, point_str):
				self.name = name
				self.point_str = point_str
				self.point = int(point_str.replace(',', ''))

def getinfo():
		string = ""
		html = urllib.request.urlopen(TARGET)
		soup = BeautifulSoup(html, 'lxml')
		articles = soup.findAll('article', class_='body-section-tournament')

		for li in articles[1].findAll('li'):
				p = li.findAll('p')

				left = CharaInfo()
				left.setData(p[0].text, p[1].text)
				right = CharaInfo()
				right.setData(p[2].text, p[3].text)

		#		print("{0}:{1}".format(left.name, left.point_str))
		#		print("{0}:{1}".format(right.name, right.point_str))
				string+=left.name+":"+left.point_str+"VS"+right.point_str+":"+right.name+"\n"
		return string

print(getinfo())
