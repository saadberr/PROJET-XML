import requests
from bs4 import BeautifulSoup
import os
from itertools import zip_longest

##########ORGANIGRAMME##################
page_link = "http://www.odco.gov.ma/fr/content/organigramme"
result = requests.get(page_link)
src = result.content
soup = BeautifulSoup(src, "lxml")


f=open("odco.txt","w")
f.write('<?xml version="1.0" encoding="ISO-8859-1"?>\n')
f.write("<ODCO>\n")

f.write("<Responsables>\n")
f.write("\t<directeur>Youssef Hosni</directeur>\n")
inc=0
chefs = soup.find_all("a", {"class":"lg"})
niv3 = soup.find_all("a", {"class":"niveau3"})

for i in chefs[1:]:
	f.write("\t<responsabilite>\n")
	f.write("\t\t<chef>"+i['title'][23:-6]+"</chef>\n")
	f.write("\t\t<metier>"+i.text+"</metier>\n")
	for j in niv3[0+inc:2+inc]:
		f.write("\t\t<sous-responsabilite>\n")
		f.write("\t\t\t<chef>"+j['title'][23:-6]+"</chef>\n")
		f.write("\t\t\t<metier>"+j.text+"</metier>\n")
		f.write("\t\t</sous-responsabilite>\n")
	inc+=2
	f.write("\t</responsabilite>\n")

delreg = soup.find_all("a", {"class":"special-blue delegation"})
f.write("\t<delegationsregional>\n")
for i in delreg:
	ch=str(i['title'])
	f.write("\t\t<ville>\n")
	f.write("\t\t\t<nom>"+i.text+"</nom>\n")
	f.write("\t\t\t<responsable>"+ch[36:-6]+"</responsable>\n")
	f.write("\t\t</ville>\n")
f.write("\t</delegationsregional>\n")
f.write("\t<InspecteurGeneral></InspecteurGeneral>\n")
f.write("</Responsables>\n")

###############Missions#################

page_link = "http://www.odco.gov.ma/fr/blog/missions"
result = requests.get(page_link)
src = result.content
soup = BeautifulSoup(src, "lxml")

miss = soup.find_all("div", {"class":"field-item even"})
H = str(miss[1].text).split("SERVICE")
H.pop(0)
B=[]
for i in H:
	i = "SERVICE "+i
	t=i.split("\n")
	B.append(t)

f.write("<Missions>\n")
for i in B:
	f.write("\t<service>\n")
	f.write("\t\t<nom>"+i[0]+"</nom>\n")
	for j in range(1,len(i)-1):
		f.write("\t\t<mission>"+i[j]+"</mission>\n")
	f.write("\t</service>\n")

f.write("</Missions>\n")

#############CooperativesParSecteur##################

page_link = "http://www.odco.gov.ma/fr/content/situation-au-31-d%C3%A9cembre-2020"
result = requests.get(page_link)
src = result.content
soup = BeautifulSoup(src, "lxml")

mytable = soup.find_all("table", {"align":"center"})
L = mytable[0].text.split("\n\n\n")
L.pop(0)
L.pop(0)
L.pop()
T=[]
for i in L:
	t=i.split("\n")
	T.append(t)

f.write("<Cooperatives-par-secteur-2020>\n")
for i in T:
	f.write("\t<secteur>\n")
	f.write("\t\t<nom>"+i[0]+"</nom>\n")
	f.write("\t\t<nbrCooperatives>"+str(i[1]).replace(" ","")+"</nbrCooperatives>\n")
	f.write("\t\t<nbrAdherants>"+str(i[2]).replace(" ","")+"</nbrAdherants>\n")
	f.write("\t</secteur>\n")

f.write("</Cooperatives-par-secteur-2020>\n")

#############CooperativesParRegion##################
page_link = "http://www.odco.gov.ma/fr/content/situation-au-fin-2020"
result = requests.get(page_link)
src = result.content
soup = BeautifulSoup(src, "lxml")

mytable = soup.find_all("table", {"align":"center"})
L = mytable[0].text.split("\n\n\n")
L.pop(0)
L.pop(0)
L.pop()
T=[]
for i in L:
	t=i.split("\n")
	T.append(t)

f.write("<Cooperatives-par-region-2020>\n")
for i in T:
	f.write("\t<region>\n")
	f.write("\t\t<nom>"+i[0]+"</nom>\n")
	f.write("\t\t<nbrCooperatives>"+str(i[1]).replace(" ","")+"</nbrCooperatives>\n")
	f.write("\t\t<nbrAdherants>"+str(i[2]).replace(" ","")+"</nbrAdherants>\n")
	f.write("\t</region>\n")

f.write("</Cooperatives-par-region-2020>\n")
f.write("</ODCO>\n")
f.close()