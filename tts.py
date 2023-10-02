import random 
from gtts import gTTS
from colorama import Fore,Back,Style
from playsound import playsound
import os
import string
import random
from plyer import notification
import time
from datetime import datetime,timedelta
from dateutil import parser
"""
tta =1
i = 'this is a test?'
it = 'this is a test '
spd = 'fast'
stg = 'ni'

def mrntta(i,tta,it,spd,stg):
    if stg == 'i':
        if spd =='fast':
            if tta !=0:
                language = 'en-US'
                tns = []
                myobj = gTTS(text=i , lang=language, slow= False)

                qn = random.choice(string.ascii_lowercase) 
                tns.append(qn)
                qw = f'{qn}_medreminder.mp3'
                myobj.save(qw)
                        
                print(Fore.WHITE + Back.GREEN +'-TTS service running-'+ Style.RESET_ALL)
                print(Fore.BLACK + Back.YELLOW +'-Please wait until the input is available again-' + Style.RESET_ALL)
                playsound(qw)

                os.remove(qw)
                ad = input(it)
                for i in ad:
                    return i
                
                print (ad)

            else:
                pass
        elif spd == 'slow':
                language = 'en-US'
                tns = []
                myobj = gTTS(text=i , lang=language, slow= True)

                qn = random.choice(string.ascii_lowercase) 
                tns.append(qn)
                qw = f'{qn}_medreminder.mp3'
                myobj.save(qw)
                        
                print(Fore.WHITE + Back.GREEN +'-TTS service running-'+ Style.RESET_ALL)
                print(Fore.BLACK + Back.YELLOW +'-Please wait until the input is available again-' + Style.RESET_ALL)
                playsound(qw)

                os.remove(qw)
                ad = input(it)
                for i in ad:
                    return i
                
                print (ad)
        else:
            print('Error')
    elif stg == 'ni':
        if spd =='fast':
            if tta !=0:
                language = 'en-US'
                tns = []
                myobj = gTTS(text=i , lang=language, slow= False)

                qn = random.choice(string.ascii_lowercase) 
                tns.append(qn)
                qw = f'{qn}_medreminder.mp3'
                myobj.save(qw)
                        
                print(Fore.WHITE + Back.GREEN +'-TTS service running-'+ Style.RESET_ALL)
                print(Fore.BLACK + Back.YELLOW +'-Please wait until the input is available again-' + Style.RESET_ALL)
                playsound(qw)

                os.remove(qw)

            else:
                pass
        elif spd == 'slow':
                language = 'en-US'
                tns = []
                myobj = gTTS(text=i , lang=language, slow= True)

                qn = random.choice(string.ascii_lowercase) 
                tns.append(qn)
                qw = f'{qn}_medreminder.mp3'
                myobj.save(qw)
                        
                print(Fore.WHITE + Back.GREEN +'-TTS service running-'+ Style.RESET_ALL)
                print(Fore.BLACK + Back.YELLOW +'-Please wait until the input is available again-' + Style.RESET_ALL)
                playsound(qw)

                os.remove(qw)
        else:
            print('Error')
mrntta(i,tta,it,spd)


tk = 'fn-t'

def randfn(tk):
    if tk == 'tts':
        i = '_medreminder.mp3'

        fd = 'tts'
        frn = random.randint(999,10000)
        fn = fd + str(frn) + i
        fne = fn.encode('cp1258')
        return fne
        
    elif tk == 'fn-t':
        i = '_medreminder.txt'
        fd = 'Txt'
        rn = random.randint(999,10000)
        fn = fd + str(rn) + i
        fe = fn.encode('cp1258')
        return fe
        
randfn(tk)
"""
    
from notifypy import Notify
import re

"""notification = Notify( default_notification_application_name= 'Med reminder')
notification.title = "this is a test"
notification.message = "test"
notification.send()"""




def wt(): #notifacation engine
    print(Fore.BLACK + Back.LIGHTGREEN_EX + '-Notification engine running-' + Style.BRIGHT +Style.RESET_ALL)
    ld = [0]
    c= 0
    global l
    while True:
        
        ml = open('medschedule.txt', 'r')
        content = ml.readlines()
        lcd = len(content)
        ld.append(lcd)
        for l in ld:
            l = l
        if l == lcd:
            td = datetime.now()
            #print(content)
            o = len(content)
            if c == 0:
                ml = open('medschedule.txt', 'r')
                content = ml.readlines()
                td = datetime.now()
                for i in content:
                    if i == '\n':
                        i.replace(i,'')
                    elif i != '\n':                        
                        date = parser.parse(i,fuzzy=True)
                        #print(f' this is the date from doc : {date}')
                        t =datetime.now()
                        ts = t.strftime('%Y-%m-%d %H:%M:%S')
                        #print(f' this is the strftime output {ts}')
                        tst = str(ts)
                        dtt = str(date)
                        if tst == dtt:
                            notification = Notify( default_notification_application_name= 'Med reminder', default_notification_icon='icon.png')
                            notification.title = "this is a test"
                            notification.message = "test"
                            notification.send()
                            print(f'{i} is due')
                            ml = open('medschedule.txt', 'r')
                            c += 1
                            print(c)
                            pass
            elif c ==1:
                td = datetime.now()
                for i in content:
                    if i == '\n':
                        i.replace(i,'')
                    elif i != '\n':
                        date = parser.parse(i,fuzzy=True)
                        #print(f' this is the date from doc : {date}')
                        t =datetime.now()
                        ts = t.strftime('%Y-%m-%d %H:%M:%S')
                        #print(f' this is the strftime output {ts}')
                        tst = str(ts)
                        dtt = str(date)
                        if tst == dtt:
                            notification = Notify( default_notification_application_name= 'Med reminder')
                            notification.title = "this is a test"
                            notification.message = "test"
                            notification.send()
                            ml = open('medschedule.txt', 'r')
                            c += 1
                            wt()
        elif l < lcd:
            print(Fore.BLACK + Back.YELLOW + 'switch program' + Style.RESET_ALL)
            ml = open('medschedule.txt', 'r')
            content = ml.readlines()
            lcd = len(content)
            ld.append(lcd)
            if lcd == l:
                td = datetime.now()
                #print(content)
                o = len(content)
                if c == 0:
                    ml = open('medschedule.txt', 'r')
                    content = ml.readlines()
                    td = datetime.now()
                    for i in content:
                        if i == '\n':
                            i.replace(i,'')
                        elif i != '\n':
                            date = parser.parse(i,fuzzy=True)
                            #print(f' this is the date from doc : {date}')
                            t =datetime.now()
                            ts = t.strftime('%Y-%m-%d %H:%M:%S')
                            #print(f' this is the strftime output {ts}')
                            tst = str(ts)
                            dtt = str(date)
                            if tst == dtt:
                                notification = Notify( default_notification_application_name= 'Med reminder')
                                notification.title = "this is a test"
                                notification.message = "test"
                                notification.send()
                                ml = open('medschedule.txt', 'r')
                                c += 1
                                print(c)
                                wt()

                    
        


wt()



#time isloater
"""str1 = 'my date of b is 12-23-1997'

date = parser.parse(str1,fuzzy=True)
print(f'Date found: {date}')"""