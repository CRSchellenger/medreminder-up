from datetime import datetime,timedelta
from operator import contains
import time
from colorama import Fore,Back,Style
from termcolor import colored,cprint
import requests, threading
from gtts import gTTS
from playsound import playsound
import os
import string
import random 
#def randfn(tk): #filename generation tts-mp3 and fn-t for text files. 
#    if tk == 'tts':
#        i = '_medreminder.mp3'
#
#        fd = 'tts'
#        frn = random.randint(999,10000)
#        fn = fd + str(frn) + i
#        fne = fn.encode('cp1258')
#        fnd = fne.decode('cp1258')
#        print(fne)
#        print(fnd)
#    elif tk == 'fn-t':
#        i = '_medreminder.txt'
#        fd = 'Txt'
#        rn = random.randint(999,10000)
#        fn = fd + str(rn) + i
#        fe = fn.encode('cp1258')
#        fnd = fe.decode('cp1258')
#        print(fn)
        
#randfn(tk)


def mrntta(i,tta,it,spd,stg): #tts system
    global an
    if stg == 'i':
        if spd == 'fast':
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
                an = input(it)
                print(an)
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
                an = input(it)
                print(an)
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



def mrn(): #email service not working
        ps = open('medschedule.txt', 'r')
        pi = ps.readlines()
        for i in pi:
            td = str(datetime.now())

            if td in i:
                timer = threading.Timer(1.0,mrn)
                timer.start()
                message = f'{i} is due to be administered please make sure you log this actvity in the medreminder system. \n If you get lost and need help please type help in medreminder to see all options'
                print(message)
                return requests.post(
                "https://api.mailgun.net/v3/sandbox167904bdf2224e25b135bd1143774c49.mailgun.org/messages",
                auth=("api", "43ddbc2130afdb049e91f373ab8ab01b-381f2624-f5e1b8d6"),
                data={"from": "Med reminder <postmaster@sandbox167904bdf2224e25b135bd1143774c49.mailgun.org>",
                "to": "christopher schellenger <schellengercrew@gmail.com>",
                "subject": "Hello christopher schellenger",
                "text": (message)})
            elif td not in i:
                pass
            else:
                print(Fore.WHITE + Back.RED+'Error reading file please contact support' + '\n' + '-error 2'+Style.RESET_ALL)
                timer.cancel()
    
#Global dec. 
global nm
global tta

def med_reminder(): # main program
    tta =0 #tta service call- if 0 tts off and if 1 tts service will engage 
    while True:
        
        if tta == 0: # first itiration w/o tts
            import os
            mrn()
            cprint('\n-----MED REMINDER-----','blue')
            ad = input('What would you like to do? ')

            if ad.lower() == 'admin meds':
                fr = open('medlist.txt', 'r')
                content = fr.read()
                print ('------Med list -------- \n '+ content)
                fr.close()
                i = input('Please enter a med name: ')
                
                if i == 'xanax':
                    x = input('Please enter your name: ')
                    ct = time.strftime('%Y-%m-%d %H:%M:%S')
                    mt = time.strftime('%H:%m')
                    xtt = datetime.now() + timedelta(hours=5)
                    r = '-----------------' + '\n' + x +' has administered '+ i +' at '+ ct + '-----------------' 

                    medfile = open('medfile.txt', 'a')
                    medfile.writelines(r)
                    medfile.close()
                    medfile = open('medfile.txt','r+')

                    print(Fore.WHITE+ Back.GREEN+'Xanax has been administered'+Style.RESET_ALL)
                    print(Fore.WHITE+ Back.YELLOW+'next pill to be administered at '+ str(xtt) + Style.RESET_ALL)

                    xsr = '\n' + str(xtt) +' xanax'
                    xs = open('medschedule.txt', 'a')
                    xs.writelines(xsr)
                    xs.close()
                    xs = open('medschedule.txt', 'r+')
                    mrn()
                elif i == 'oxycodone':
                    o = input('Please enter your name: ')
                    rt = time.strftime('%Y-%m-%d %H:%M:%S')
                    ot = time.strftime('%H:%m')
                    ott = datetime.now() + timedelta(hours=4)

                    oi = '-----------------' + '\n' + o +' has administered '+ i +' at '+ rt + '-----------------' 

                    medfile = open('medfile', 'a')
                    medfile.writelines(oi)
                    medfile.close()
                    medfile = open('medfile.txt','r+')

                    print(Fore.WHITE + Back.GREEN +'oxycodone has been administered'+Style.RESET_ALL)
                    print(Fore.WHITE + Back.YELLOW +'next pill to be administered at '+ str(ott)+Style.RESET_ALL)

                    osr = '\n' + str(ott) + ' oxycodone'
                    os = open('medschedule.txt', 'a')
                    os.writelines(str(osr))
                    os.close()
                    os = open('medschedule.txt', 'r+')
                    mrn()
                elif i == 'loratadine':
                    ln = input('Please enter your name: ')
                    lt = time.strftime('%Y-%m-%d %H:%M:%S')
                    ltq = time.strftime('%H:%m')
                    ltt = datetime.now() + timedelta(hours=24)

                    li = '-----------------' +  '\n' + ln +' has administered '+ i +' at '+ lt + '-----------------' 

                    medfile = open('medfile.txt', 'a')
                    medfile.writelines(li)
                    medfile.close()
                    medfile = open('medfile.txt','r+')

                    print(Fore.WHITE + Back.GREEN + 'oxycodone has been administered'+Style.RESET_ALL)
                    print(Fore.WHITE + Back.YELLOW +'next pill to be administered at '+ str(ltt)+Style.RESET_ALL)

                    lsr = '\n' + str(ltt) + ' loratadine'
                    ls = open('medschedule.txt', 'a')
                    ls.writelines(str(lsr))
                    ls.close()
                    ls = open('medschedule.txt', 'r+')
                    mrn()
                elif i == 'tramadol':
                    tn = input('Please enter your name: ')
                    tt = time.strftime('%Y-%m-%d %H:%M:%S')
                    ttq = time.strftime('%H:%m')
                    ttt = datetime.now() + timedelta(hours=6)

                    ti = '-----------------'  + '\n' + tn +' has administered '+ i +' at '+ tt + '-----------------' 

                    medfile = open('medfile.txt', 'a')
                    medfile.writelines(ti)
                    medfile.close()
                    medfile = open('medfile.txt','r+')

                    print(Fore.WHITE + Back.GREEN+ 'Tramadol has been administered'+Style.RESET_ALL)
                    print(Fore.WHITE + Back.YELLOW+ 'next pill to be administered at '+ str(ttt)+Style.RESET_ALL)

                    tsr = '\n' + str(ttt) + ' tramadol'
                    ts = open('medschedule.txt', 'a')
                    ts.writelines(str(tsr))
                    ts.close()
                    ts = open('medschedule.txt', 'r+')
                    mrn()

                elif i == 'temazepam':
                        ten = input('Please enter your name: ')
                        tet = time.strftime('%Y-%m-%d %H:%M:%S')
                        tte = time.strftime('%H:%m')
                        tte = datetime.now() + timedelta(hours=24)

                        te = '-----------------' +'\n' + ten +' has administered '+ i +' at '+ tet + '-----------------'

                        medfile = open('medfile.txt', 'a')
                        medfile.writelines(te)
                        medfile.close()
                        medfile = open('medfile.txt','r+')

                        print(Fore.WHITE + Back.GREEN +'temazepam has been administered'+Style.RESET_ALL)
                        print(Fore.WHITE + Back.YELLOW +'next pill to be administered at '+ str(tte)+Style.RESET_ALL)

                        tse = '\n' + str(tte) + ' temazepam'
                        te = open('medschedule.txt', 'a')
                        te.writelines(str(tse))
                        te.close()
                        te = open('medschedule.txt', 'r+')

                        mrn()

                elif i == 'senokot':
                        sen = input('Please enter your name: ')
                        set = time.strftime('%Y-%m-%d %H:%M:%S')
                        ste = time.strftime('%H:%m')
                        ste = datetime.now() + timedelta(hours=12)

                        se = '-----------------' +'\n' + sen +' has administered '+ i +' at '+ set + '-----------------'

                        medfile = open('medfile.txt', 'a')
                        medfile.writelines(se)
                        medfile.close()
                        medfile = open('medfile.txt','r+')

                        print(Fore.WHITE + Back.GREEN+'Senokot has been administered'+Style.RESET_ALL)
                        print(Fore.WHITE + Back.YELLOW+'next pill to be administered at '+ str(ste)+Style.RESET_ALL)

                        sse = '\n' + str(ste) + ' senokot'
                        se = open('medschedule.txt', 'a')
                        se.writelines(str(sse))
                        se.close()
                        se = open('medschedule.txt', 'r+')

                        mrn()

                elif i == 'fentanyl':
                        fen = input('Please enter your name: ')
                        fet = time.strftime('%Y-%m-%d %H:%M:%S')
                        fte = time.strftime('%H:%m')
                        fre = datetime.now() + timedelta(hours=24)

                        fe = '-----------------' + '\n' + fen +' has administered '+ i +' at '+ fet + '-----------------' 

                        medfile = open('medfile.txt', 'a')
                        medfile.writelines(fe)
                        medfile.close()
                        medfile = open('medfile.txt','r+')

                        print(Fore.WHITE + Back.GREEN+'oxycodone has been administered'+Style.RESET_ALL)
                        print(Fore.WHITE + Back.YELLOW+'next pill to be administered at '+ str(fre)+Style.RESET_ALL)

                        fse = '\n' + str(fre) + ' fentanyl'
                        fe = open('medschedule.txt', 'a')
                        fe.writelines(str(fse))
                        fe.close()
                        fe = open('medschedule.txt', 'r+')

                        mrn()

                elif i == 'test':
                    fen = input('Please enter your name: ')
                    fet = time.strftime('%Y-%m-%d %H:%M')
                    fte = time.strftime('%H:%m')
                    fre = datetime.now() + timedelta(hours=0)
                    
                    fse = '\n' + str(fre) + ' test'
                    
                    fe = open('medschedule.txt', 'a')
                    fe.writelines(str(fse))
                    fe.close()
                    fe = open('medschedule.txt', 'r+')

                    mrn()
                else:
                    print(Fore.WHITE + Back.RED+'Please enter med name' + '\n' + '-error 1'+Style.RESET_ALL)
                    mrn()
            elif ad.lower() == 'add meds':
                cprint('\n-----Add new meds-----','blue',attrs=['blink'])
                nm= input('Please enter med name that you would like to add to the system: ')
                medlist =open('medlist.txt', 'a')
                medlist.writelines('\n' + nm)
                medlist.close()
                medlist = open('medlist.txt','r+')

            elif ad.lower() == 'med info':
                print('welcome to the med information section')
                di = input('Please enter med name that you would like to learn about: ')
                di.lower()
                if di == 'xanax' or di == 'alprazolam':
                    xi = open('xanax drug info', 'r')
                    xc = xi.read()
                    print(xc)
                    xi.close()

                elif di == 'oxycodone':
                    oi = open('oi.text', 'r')
                    oc = oi.read()
                    print(oc)
                    oi.close()

                elif di == 'loratadine':
                    li = open('li.txt', 'r')
                    lc = li.read()
                    print(lc)
                    li.close()

                elif di == 'tramadol':
                    ti = open('ti.txt', 'r')
                    tc = ti.read()
                    print(tc)
                    ti.close()

                elif di == 'temazepam':
                    te = open('te.txt', 'r')
                    tc = te.read()
                    print(tc)
                    te.close()


                elif di == 'senokot':
                    si = open('si.txt', 'r')
                    sc = si.read()
                    print(sc)
                    si.close()


                elif di == 'fentanyl':
                    fi = open('fi.txt', 'r')
                    fc = fi.read()
                    print(fc)
                    fi.close()


            elif ad.lower() == 'note':
                ntd = time.strftime('%Y-%m-%d %H:%M:%S')
                nt = input('Title: ')
                ntb = input('Note: ')

                n = '\n-------------------------------------------' +'\n'+ ntd + '\n' + nt + '\n' + ntb +'\n-------------------------------------------'

                note = open('notes.txt', 'a')
                note.writelines(n)
                note.close()
                note = open('notes.txt','r+')


            elif ad.lower() == 'print notes':
                ni = open('Documents/med-reminder/notes.txt', 'r')
                nc = ni.read()
                print(nc)
                ni.close()

            elif ad.lower() == 'vitials':
                bp = input('Enter Blood pressure: ')
                hr = input('Enter heart rate: ')
                sp = input('Enter SP02 rate: ')
                ctd = time.strftime('%Y-%m-%d %H:%M:%S')

                v = '\n-------------------------------------------'+'\n' +ctd +'\nBlood Pressure: '+ bp + '\nHeart Rate: '+hr + '\nSP02: ' + sp +'\n-------------------------------------------'

                note = open('vitals.txt', 'a')
                note.writelines(v)
                note.close()
                note = open('vitals.txt','r+')
            elif ad.lower() == 'print vitals':
                vi = open('vitals.txt', 'r')
                vc = vi.read()
                print(vc)
                vi.close()
            
            
            elif ad.lower() == 'nurse':
                ny = input('Please enter your name: ')
                ni = input('Would you like to add any notes about todays visit?: (yes/no) ')
                td = time.strftime('%Y-%m-%d %H:%M:%S')
                if ni == 'yes':
                    nn = input('Enter your notes now: ')
                    d= '\n-------------------------------------------'+'\n' +td +'\nNurse Name: '+ ny + '\nNurse Notes: '+ nn + '\n-------------------------------------------'
                    nv = open('nurse.txt', 'a')
                    nv.writelines(d)
                    nv.close()
                    nv = open('nurse.txt','r+')
                else:
                    e = '\n-------------------------------------------'+'\n' +td +'\nNurse Name: '+ ny + '\nNurse did not enter any notes'+'\n-------------------------------------------'
                    nv1 = open('nurse.txt', 'a')
                    nv1.writelines(e)
                    nv1.close()
                    nv1 = open('nurse.txt','r+')
                    print('No notes added.' + e)
            


            elif ad.lower() == 'covid test':
                print('Types of tests are Anitgen and PCR')
                pn = input('Please enter the name of the person this test was performed on: ')
                ctt = input ('Please enter the the type of test you have taken: ')
                print('--------------------------------')
                print('pos,neg')
                ttr = input('Please enter the result of the test: ')
                if ttr == 'pos':
                    print(Fore.WHITE + Back.RED +'\nPlease isolate for 5 days to ensure the virus does not spread' + Style.RESET_ALL)
                else:
                    pass
                tdd = time.strftime('%Y-%m-%d %H:%M:%S')

                cttr = '\n-------------------------------------------'+'\n' +tdd +'\nName of the person this test was performed on: ' + pn +'\ntype of test taken: ' + ctt + '\nResult of the test: ' + ttr +'\n-------------------------------------------'

                covid = open('ct.txt', 'a')
                covid.writelines(cttr)
                covid.close()
                covid = open('ct.txt','r+')

            elif ad.lower() == 'print meds':
                ml = open('medlist.txt', 'r')
                mi = ml.read()
                print(mi)
                ml.close()

            elif ad.lower() == 'print schedule':
                ps = open('medschedule.txt', 'r')
                pi = ps.read()
                print(pi)
                ps.close()
            elif ad.lower() == 'print activity':
                at = open('Documents/med-reminder/medfile.txt', 'r')
                ai = at.read()
                print(ai)
                at.close()
            elif ad.lower() == 'print covid test':
                ct = open('ct.txt', 'r')
                ci = ct.read()
                print(ci)
                ct.close()
            elif ad.lower() == 'quit':
                print('Closing system...')
                time.sleep(0.5)
                break
            elif ad.lower() == 'nurse report':
                nr = open('Documents/med-reminder/nurse.txt', 'r')
                ns = nr.read()
                print (ns)
                nr.close()
            elif ad.lower() == 'help':
                print('------ Terms within the system ------')
                print('\n Admin meds - To log when you administered medication \n Med info - To get information about a specific medication \n Note - To log any notes \n Nurse - For a nurse to be able to log any notes about a specific visit \n Vitials - To log patient vitals \n Covid test - To log a covid test and what type was taken \n Print notes - Shows all notes in the system \n Print meds - Shows all meds in the system \n Print schedule - Shows a current and past schedule for the meds in the system \n Print activity - Shows all activity within a system and also shows who did a certain task and at which time \n Print covid test - Shows all past covid tests that have been logged into the system \n Read - To enable or disable TTS service \n Quit - To exit the system')
            elif ad.lower() == 'read':
                import os
                tta = 0
                it = input('To enable TTS please type enable or to disable type disable then after finished press enter. ')
                if it == 'enable':    

                    
                    tta +=1
                    print(tta)
                    
                    
                elif it.lower() == 'test': 
                    fns = []
                    i = 'This is a sample of the TTS service in medreminder'
                    language = 'en-US'
                    myobj = gTTS(text=i , lang=language, slow= False)

                    fn = random.choice(string.ascii_lowercase) 
                    fns.append(fn)
                    qw = f'{fn}_medreminder.mp3'
                    myobj.save(qw)
                    
                    print(Fore.WHITE + Back.GREEN +'-TTS service running-'+ Style.RESET_ALL)
                    print(Fore.BLACK + Back.YELLOW +'-Please wait until the input is available again-' + Style.RESET_ALL)
                    playsound(qw)

                    os.remove(qw)

                elif it == 'disable':
                    tta -=1
                    continue
                else:
                    print(Fore.BLACK + Back.RED + 'Please enter a vaild option. Exiting to main menu. -ERROR 6' + Style.RESET_ALL)

        elif tta == 1:
            while tta ==1:
                from colorama import Fore,Back,Style
                i = 'What would you like to do?'
                it = 'What would you like to do? '
                spd = 'fast'
                stg = 'i'
                mrntta(i,tta,it,spd,stg)
                
                if an.lower() == 'admin meds':
                    #TTS #it is input text
                    i = 'Administer medications.'
                    it= 0
                    spd = 'fast'
                    stg = 'ni'
                    mrntta(i,tta,it,spd,stg)

                    #End TTS

                    fr = open('medlist.txt', 'r')
                    content = fr.read()
                    time.sleep(0.8)
                    print ('------Med list -------- \n '+ content)
                    fr.close()
                    i = 'Medication list: ' + content
                    it= 0
                    spd = 'slow'
                    stg = 'ni'
                    mrntta(i,tta,it,spd,stg)
                    #get input from user
                    i = 'Please enter a medication name'
                    it= 'Plese enter med name'
                    spd = 'fast'
                    stg = 'i'
                    mrntta(i,tta,it,spd,stg)
                    #end tts input from user
                    it = an
                    if it == 'xanax':
                        x = input('Please enter your name: ')


                        ct = time.strftime('%Y-%m-%d %H:%M:%S')
                        mt = time.strftime('%H:%m')
                        xtt = datetime.now() + timedelta(hours=5)
                        xtt1 = xtt.strftime('%Y-%m-%d %H:%m')
                        r = '-----------------' + '\n' + x +' has administered '+ i +' at '+ ct + '-----------------' 

                        medfile = open('medfile.txt', 'a')

                        medfile.writelines(r)
                        medfile.close()
                        medfile = open('medfile.txt','r+')

                        print(Fore.WHITE+ Back.GREEN+'Xanax has been administered'+Style.RESET_ALL)
                        txt = ('next pill to be administered on '+ str(xtt1))
                        txt1 = ('next pill to be administered on '+ str(xtt1)+Style.RESET_ALL)

                        #start tts 
                        i = txt
                        it= 0
                        spd = 'fast'
                        stg = 'ni'
                        mrntta(i,tta,it,spd,stg)
                        #end tts 
                        print(txt1) #show user the next time to take medication

                        xsr = '\n' + str(xtt) +' xanax'
                        xs = open('medschedule.txt', 'a')
                        xs.writelines(xsr)
                        xs.close()
                        xs = open('medschedule.txt', 'r+')
                        mrn()
                    elif i == 'oxycodone':
                        o = input('Please enter your name: ')
                        rt = time.strftime('%Y-%m-%d %H:%M:%S')
                        ot = time.strftime('%H:%m')
                        ott = datetime.now() + timedelta(hours=4)

                        oi = '-----------------' + '\n' + o +' has administered '+ i +' at '+ rt + '-----------------' 

                        medfile = open('medfile', 'a')
                        medfile.writelines(oi)
                        medfile.close()
                        medfile = open('medfile.txt','r+')

                        print(Fore.WHITE + Back.GREEN +'oxycodone has been administered'+Style.RESET_ALL)
                        txt = (Fore.WHITE + Back.YELLOW +'next pill to be administered at '+ str(ott)+Style.RESET_ALL)
                        i = txt
                        it= 0
                        spd = 'fast'
                        stg = 'ni'
                        mrntta(i,tta,it,spd,stg)
                        print(txt)

                        osr = '\n' + str(ott) + ' oxycodone'
                        os = open('medschedule.txt', 'a')
                        os.writelines(str(osr))
                        os.close()
                        os = open('medschedule.txt', 'r+')
                        mrn()
                    elif i == 'loratadine':
                        ln = input('Please enter your name: ')
                        lt = time.strftime('%Y-%m-%d %H:%M:%S')
                        ltq = time.strftime('%H:%m')
                        ltt = datetime.now() + timedelta(hours=24)

                        li = '-----------------' +  '\n' + ln +' has administered '+ i +' at '+ lt + '-----------------' 

                        medfile = open('medfile.txt', 'a')
                        medfile.writelines(li)
                        medfile.close()
                        medfile = open('medfile.txt','r+')

                        print(Fore.WHITE + Back.GREEN + 'oxycodone has been administered'+Style.RESET_ALL)
                        print(Fore.WHITE + Back.YELLOW +'next pill to be administered at '+ str(ltt)+Style.RESET_ALL)

                        lsr = '\n' + str(ltt) + ' loratadine'
                        ls = open('medschedule.txt', 'a')
                        ls.writelines(str(lsr))
                        ls.close()
                        ls = open('medschedule.txt', 'r+')
                        mrn()
                    elif i == 'tramadol':
                        tn = input('Please enter your name: ')
                        tt = time.strftime('%Y-%m-%d %H:%M:%S')
                        ttq = time.strftime('%H:%m')
                        ttt = datetime.now() + timedelta(hours=6)

                        ti = '-----------------'  + '\n' + tn +' has administered '+ i +' at '+ tt + '-----------------' 

                        medfile = open('medfile.txt', 'a')
                        medfile.writelines(ti)
                        medfile.close()
                        medfile = open('medfile.txt','r+')

                        print(Fore.WHITE + Back.GREEN+ 'Tramadol has been administered'+Style.RESET_ALL)
                        print(Fore.WHITE + Back.YELLOW+ 'next pill to be administered at '+ str(ttt)+Style.RESET_ALL)

                        tsr = '\n' + str(ttt) + ' tramadol'
                        ts = open('medschedule.txt', 'a')
                        ts.writelines(str(tsr))
                        ts.close()
                        ts = open('medschedule.txt', 'r+')
                        mrn()

                    elif i == 'temazepam':
                            ten = input('Please enter your name: ')
                            tet = time.strftime('%Y-%m-%d %H:%M:%S')
                            tte = time.strftime('%H:%m')
                            tte = datetime.now() + timedelta(hours=24)

                            te = '-----------------' +'\n' + ten +' has administered '+ i +' at '+ tet + '-----------------'

                            medfile = open('medfile.txt', 'a')
                            medfile.writelines(te)
                            medfile.close()
                            medfile = open('medfile.txt','r+')

                            print(Fore.WHITE + Back.GREEN +'temazepam has been administered'+Style.RESET_ALL)
                            print(Fore.WHITE + Back.YELLOW +'next pill to be administered at '+ str(tte)+Style.RESET_ALL)

                            tse = '\n' + str(tte) + ' temazepam'
                            te = open('medschedule.txt', 'a')
                            te.writelines(str(tse))
                            te.close()
                            te = open('medschedule.txt', 'r+')

                            mrn()

                    elif i == 'senokot':
                            sen = input('Please enter your name: ')
                            set = time.strftime('%Y-%m-%d %H:%M:%S')
                            ste = time.strftime('%H:%m')
                            ste = datetime.now() + timedelta(hours=12)

                            se = '-----------------' +'\n' + sen +' has administered '+ i +' at '+ set + '-----------------'

                            medfile = open('medfile.txt', 'a')
                            medfile.writelines(se)
                            medfile.close()
                            medfile = open('medfile.txt','r+')

                            print(Fore.WHITE + Back.GREEN+'Senokot has been administered'+Style.RESET_ALL)
                            print(Fore.WHITE + Back.YELLOW+'next pill to be administered at '+ str(ste)+Style.RESET_ALL)

                            sse = '\n' + str(ste) + ' senokot'
                            se = open('medschedule.txt', 'a')
                            se.writelines(str(sse))
                            se.close()
                            se = open('medschedule.txt', 'r+')

                            mrn()

                    elif i == 'fentanyl':
                            fen = input('Please enter your name: ')
                            fet = time.strftime('%Y-%m-%d %H:%M:%S')
                            fte = time.strftime('%H:%m')
                            fre = datetime.now() + timedelta(hours=24)

                            fe = '-----------------' + '\n' + fen +' has administered '+ i +' at '+ fet + '-----------------' 

                            medfile = open('medfile.txt', 'a')
                            medfile.writelines(fe)
                            medfile.close()
                            medfile = open('medfile.txt','r+')

                            print(Fore.WHITE + Back.GREEN+'oxycodone has been administered'+Style.RESET_ALL)
                            print(Fore.WHITE + Back.YELLOW+'next pill to be administered at '+ str(fre)+Style.RESET_ALL)

                            fse = '\n' + str(fre) + ' fentanyl'
                            fe = open('medschedule.txt', 'a')
                            fe.writelines(str(fse))
                            fe.close()
                            fe = open('medschedule.txt', 'r+')

                            mrn()
                elif an.lower() == 'add meds':
                    cprint('\n-----Add new meds-----','blue',attrs=['blink'])
                    nm= input('Please enter med name that you would like to add to the system: ')
                    medlist =open('medlist.txt', 'a')
                    medlist.writelines('\n' + nm)
                    medlist.close()
                    medlist = open('medlist.txt','r+')

                elif an.lower() == 'med info':
                    print('welcome to the med information section')
                    di = input('Please enter med name that you would like to learn about: ')
                    di.lower()
                    if di == 'xanax' or di == 'alprazolam':
                        xi = open('xanax drug info', 'r')
                        xc = xi.read()
                        print(xc)
                        xi.close()

                    elif di == 'oxycodone':
                        oi = open('oi.text', 'r')
                        oc = oi.read()
                        print(oc)
                        oi.close()

                    elif di == 'loratadine':
                        li = open('li.txt', 'r')
                        lc = li.read()
                        print(lc)
                        li.close()

                    elif di == 'tramadol':
                        ti = open('ti.txt', 'r')
                        tc = ti.read()
                        print(tc)
                        ti.close()

                    elif di == 'temazepam':
                        te = open('te.txt', 'r')
                        tc = te.read()
                        print(tc)
                        te.close()


                    elif di == 'senokot':
                        si = open('si.txt', 'r')
                        sc = si.read()
                        print(sc)
                        si.close()


                    elif di == 'fentanyl':
                        fi = open('fi.txt', 'r')
                        fc = fi.read()
                        print(fc)
                        fi.close()


                elif an.lower() == 'note':
                    ntd = time.strftime('%Y-%m-%d %H:%M:%S')
                    nt = input('Title: ')
                    ntb = input('Note: ')

                    n = '\n-------------------------------------------' +'\n'+ ntd + '\n' + nt + '\n' + ntb +'\n-------------------------------------------'

                    note = open('notes.txt', 'a')
                    note.writelines(n)
                    note.close()
                    note = open('notes.txt','r+')


                elif an.lower() == 'print notes':
                    ni = open('Documents/med-reminder/notes.txt', 'r')
                    nc = ni.read()
                    print(nc)
                    ni.close()

                elif an.lower() == 'vitials':
                    bp = input('Enter Blood pressure: ')
                    hr = input('Enter heart rate: ')
                    sp = input('Enter SP02 rate: ')
                    ctd = time.strftime('%Y-%m-%d %H:%M:%S')

                    v = '\n-------------------------------------------'+'\n' +ctd +'\nBlood Pressure: '+ bp + '\nHeart Rate: '+hr + '\nSP02: ' + sp +'\n-------------------------------------------'

                    note = open('vitals.txt', 'a')
                    note.writelines(v)
                    note.close()
                    note = open('vitals.txt','r+')
                elif an.lower() == 'print vitals':
                    vi = open('vitals.txt', 'r')
                    vc = vi.read()
                    print(vc)
                    vi.close()
                
                
                elif an.lower() == 'nurse':
                    ny = input('Please enter your name: ')
                    ni = input('Would you like to add any notes about todays visit?: (yes/no) ')
                    td = time.strftime('%Y-%m-%d %H:%M:%S')
                    if ni == 'yes':
                        nn = input('Enter your notes now: ')
                        d= '\n-------------------------------------------'+'\n' +td +'\nNurse Name: '+ ny + '\nNurse Notes: '+ nn + '\n-------------------------------------------'
                        nv = open('nurse.txt', 'a')
                        nv.writelines(d)
                        nv.close()
                        nv = open('nurse.txt','r+')
                    else:
                        e = '\n-------------------------------------------'+'\n' +td +'\nNurse Name: '+ ny + '\nNurse did not enter any notes'+'\n-------------------------------------------'
                        nv1 = open('nurse.txt', 'a')
                        nv1.writelines(e)
                        nv1.close()
                        nv1 = open('nurse.txt','r+')
                        print('No notes added.' + e)
                


                elif an.lower() == 'covid test':
                    print('Types of tests are Anitgen and PCR')
                    pn = input('Please enter the name of the person this test was performed on: ')
                    ctt = input ('Please enter the the type of test you have taken: ')
                    print('--------------------------------')
                    print('pos,neg')
                    ttr = input('Please enter the result of the test: ')
                    if ttr == 'pos':
                        print(Fore.WHITE + Back.RED +'\nPlease isolate for 5 days to ensure the virus does not spread' + Style.RESET_ALL)
                    else:
                        pass
                    tdd = time.strftime('%Y-%m-%d %H:%M:%S')

                    cttr = '\n-------------------------------------------'+'\n' +tdd +'\nName of the person this test was performed on: ' + pn +'\ntype of test taken: ' + ctt + '\nResult of the test: ' + ttr +'\n-------------------------------------------'

                    covid = open('ct.txt', 'a')
                    covid.writelines(cttr)
                    covid.close()
                    covid = open('ct.txt','r+')

                elif an.lower() == 'print meds':
                    ml = open('medlist.txt', 'r')
                    mi = ml.read()
                    print(mi)
                    ml.close()

                elif an.lower() == 'print schedule':
                    ps = open('medschedule.txt', 'r')
                    pi = ps.read()
                    print(pi)
                    ps.close()
                elif an.lower() == 'print activity':
                    at = open('Documents/med-reminder/medfile.txt', 'r')
                    ai = at.read()
                    print(ai)
                    at.close()
                elif an.lower() == 'print covid test':
                    ct = open('ct.txt', 'r')
                    ci = ct.read()
                    print(ci)
                    ct.close()
                elif an.lower() == 'quit':
                    print('Closing system...')
                    time.sleep(0.5)
                    break
                elif an.lower() == 'nurse report':
                    nr = open('Documents/med-reminder/nurse.txt', 'r')
                    ns = nr.read()
                    print (ns)
                    nr.close()
                elif an.lower() == 'help':
                    print('------ Terms within the system ------')
                    print('\n Admin meds - To log when you administered medication \n Med info - To get information about a specific medication \n Note - To log any notes \n Nurse - For a nurse to be able to log any notes about a specific visit \n Vitials - To log patient vitals \n Covid test - To log a covid test and what type was taken \n Print notes - Shows all notes in the system \n Print meds - Shows all meds in the system \n Print schedule - Shows a current and past schedule for the meds in the system \n Print activity - Shows all activity within a system and also shows who did a certain task and at which time \n Print covid test - Shows all past covid tests that have been logged into the system \n Read - To enable or disable TTS service \n Quit - To exit the system')
                elif an.lower() == 'read':
                    import os
                    tta = 0
                    it = input('To enable TTS please type enable or to disable type disable then after finished press enter. ')
                    if it == 'enable':    

                        
                        tta +=1
                        print(tta)
                        
                        
                    elif it.lower() == 'test': 
                        fns = []
                        i = 'This is a sample of the TTS service in medreminder'
                        language = 'en-US'
                        myobj = gTTS(text=i , lang=language, slow= False)

                        fn = random.choice(string.ascii_lowercase) 
                        fns.append(fn)
                        qw = f'{fn}_medreminder.mp3'
                        myobj.save(qw)
                        
                        print(Fore.WHITE + Back.GREEN +'-TTS service running-'+ Style.RESET_ALL)
                        print(Fore.BLACK + Back.YELLOW +'-Please wait until the input is available again-' + Style.RESET_ALL)
                        playsound(qw)

                        os.remove(qw)

                    elif it == 'disable':
                        tta -=1
                        #continue
                    else:
                        print(Fore.BLACK + Back.RED + 'Please enter a vaild option. Exiting to main menu. -ERROR 6' + Style.RESET_ALL)
                else:
                    break
        else:
            break 
    

            
            
                
            

           
            
                    



        




#texttospeech() https://towardsdatascience.com/easy-text-to-speech-with-python-bfb34250036e
med_reminder()
    
mrntta(i,tta,it)


            

