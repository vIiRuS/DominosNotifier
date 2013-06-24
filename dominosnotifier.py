import urllib2
from HTMLParser import HTMLParser
from bs4 import BeautifulSoup
from gntp.notifier import mini
from time import sleep
import sys

appname = "Domino's notifier"
title = "Statusupdate"
current_step = 0
print("Tracking your status!")
while True:
	request = urllib2.Request(sys.argv[1])
	response = urllib2.urlopen(request)
	html = response.read()
	response.close()
	soup = BeautifulSoup(html)

	if soup.find(class_="step1-selected"):
		if current_step < 1:
			current_step = 1
			mini("Aktueller Status: Bestellung aufgenommen", applicationName=appname, title=title)
			print("Aktueller Status: Bestellung aufgenommen")
	elif soup.find(class_="step2-selected"):
		if current_step < 2:
			current_step = 2
			mini("Aktueller Status: Zubereitung", applicationName=appname, title=title)
			print("Aktueller Status: Zubereitung")
	elif soup.find(class_="step3-selected"):
		if current_step < 3:
			current_step = 3
			mini("Aktueller Status: Backen", applicationName=appname, title=title)
			print("Aktueller Status: Backen")
	elif soup.find(class_="step4-selected"):
		if current_step < 4:
			current_step = 4
			mini("Aktueller Status: Qualitaetskontrolle", applicationName=appname, title=title)
			print("Aktueller Status: Qualitaetskontrolle")
	elif soup.find(class_="step5-delivery-selected"):
		if current_step < 5:
			current_step = 5
			mini("Aktueller Status: Lieferung")
			print("Aktueller Status: Lieferung")
			break

	sleep(20)
