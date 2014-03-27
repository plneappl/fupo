#This programm is used to convert the .vcard from Nokias N900 to .csv format (for example Thunderbird)

#convert the .db into CSV tith all data in it *.csv
#from there you can transform it in a CSV for osmo called *_osmo.csv

import pexpect
child = pexpect.spawn("ls -1")

inn = open(child.readline(),'r')
out = open('/home/odonata/Projects/Address_Programm/Adressbuch.csv','w')
#all variables to find
out.write("forename,lastname,note,gender,company,ocupation,nickname,homepage,address_home,address_work,address_priv,bday,mail,mail_priv,mail_work,mobil_work,mobil_priv,mobil,phone_work,phone_priv,phone,fax,icq,skype,sip,photo" + '\n')

for line in inn.readlines():
    if 'NOTE:' in line:
        note = line[5:-2]
    if 'X-GENDER:' in line:
        gender = line[9:-2]
    if 'ORG:' in line:
        company = line[4:-2]
    if 'TITLE:' in line:
        ocupation = line[6:-2]
    if 'NICKNAME:' in line:
        nickname = line[9:-2]
    if 'URL:' in line:
        homepage = line[4:-2]
    if 'ADR;TYPE=WORK:' in line:
        address_work = line[14:-2]
    if 'ADR;TYPE=HOME:' in line:
        address_home = line[14:-2]
    if 'ADR:' in line:
        address_priv = line[4:-2]
    if 'BDAY:' in line:
        bday = line[5:-2]
    if 'EMAIL:' in line:
        mail = line[6:-2]
    if 'EMAIL;TYPE=HOME:' in line:
        mail_priv = line[16:-2]
    if 'EMAIL;TYPE=WORK:' in line:
        mail_work = line[16:-2]
    if 'TEL;TYPE=WORK,CELL:' in line:
        mobil_work = line[19:-2]
    if 'TEL;TYPE=HOME,CELL:' in line:
        mobil_priv = line[19:-2]
    if 'TEL;TYPE=CELL' in line:
        if 'VOICE' in line:
            mobil = line[20:-2]
        else:
            mobil = line[14:-2]
    if 'TEL;TYPE=WORK,VOICE:' in line:
        phone_work = line[20:-2]
    if 'TEL;TYPE=HOME,VOICE:' in line:
        phone_priv = line[20:-2]
    if 'TEL;TYPE=VOICE:' in line:
        phone = line[15:-2]
    if 'TEL;TYPE=FAX:' in line:
        fax = line[13:-2]
    if 'X-ICQ;TYPE=icq:' in line:
        icq = line[15:-2]
    if 'X-SKYPE;TYPE=skype:' in line:
        skype = line[19:-2]  
    if 'X-SIP;TYPE=sip:' in line:
        sip = line[15:-2] 
    if 'PHOTO;TYPE=png;ENCODING=b:' in line:
        photo = line[26:-2]                                                
    if 'FN:' in line:
        forename = str(line[3:-2].rsplit(' ')[0:]).rsplit(',')[0][2:-1]
        lastname = str(line[3:-2].rsplit(' ')[1:])[2:-2]
    if 'END:VCARD' in line:
        out.write((forename + ',' + lastname + ',' + note + ',' + gender + ',' + company + ',' + ocupation + ',' + nickname + ',' + homepage + ',' + 
              address_home + ',' +address_work + ',' + address_priv + ',' + bday + ',' + mail + ',' + mail_priv + ',' + mail_work + ',' + mobil_work + ',' +
              mobil_priv + ',' + mobil + ',' + phone_work + ',' + phone_priv + ',' + phone + ',' + fax + ',' + icq + ',' + skype + ',' + sip + ',' + photo + '\n').replace(';',' ').replace('\\', ''))
    if 'VERSION:' in line:
	forename = ''       #N:for;			##First name
	lastname = ''       #N:;last;			##Last name
	note = ''           #NOTE:			##Additional info
	gender = ''         #X-GENDER:			##Gender
	company = ''        #ORG:			##Organization
	ocupation = ''      #TITLE:			##Titel
	nickname = ''       #NICKNAME:			##Nickname
	homepage = ''       #URL:			##WWW
	address_work = ''   #ADR;TYPE=WORK:		
	address_priv = ''   #ADR:
	bday = ''           #BDAY:			##Birthday date
	mail = ''           #EMAIL:
	mail_priv = ''      #EMAIL;TYPE=HOME:		##E-Mail
	mail_work = ''      #EMAIL;TYPE=WORK:		##E-Mail 2
	mobil_work = ''     #TEL;TYPE=WORK,CELL:
	mobil_priv = ''     #TEL;TYPE=HOME,CELL:	##Cell phone
	mobil = ''          #TEL;TYPE=CELL:				###abfgnen von mobil und mobil_priv
	phone_work = ''     #TEL;TYPE=WORK,VOICE:	##Work phone
	phone_priv = ''     #TEL;TYPE=HOME,VOICE:	##Home phone
	phone = ''          #TEL;TYPE=VOICE:				###abfagnen von phone und phone_priv
	fax = ''            #TEL;TYPE=FAX:		##Fax
	icq = ''            #X-ICQ;TYPE=icq:		##IM ICQ
        skype = ''          #X-SKYPE;TYPE=skype: 	##IM Skype
        address_home = ''   #ADR;TYPE=HOME:             ##Address
        sip = ''            #X-SIP;TYPE=sip:            ##sip
        photo = ''          #PHOTO;TYPE=png;ENCODING=b:	##photo
inn.close()
out.close()
