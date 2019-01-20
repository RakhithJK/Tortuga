# Written by Metachar

import smtplib
import time as t
import colorama, Fore, init

init(convert=True)

class color:
	PURPLE = '\033[95m'
	CYAN = '\033[96m'
	DARKCYAN = '\033[36m'
	BLUE = '\033[94m'
	GREEN = '\033[92m'
	YELLOW = '\033[93m'
	RED = '\033[91m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'
	END = '\033[0m'
	CWHITE = '\33[37m'

logo = color.BOLD + '''{0}
 _______  _______  ______    _______  __   __  _______  _______ 
|       ||       ||    _ |  |       ||  | |  ||       ||   _   |
|_     _||   _   ||   | ||  |_     _||  | |  ||    ___||  |_|  |
  |   |  |  | |  ||   |_||_   |   |  |  |_|  ||   | __ |       |
  |   |  |  |_|  ||    __  |  |   |  |       ||   ||  ||       |
  |   |  |       ||   |  | |  |   |  |       ||   |_| ||   _   |
  |___|  |_______||___|  |_|  |___|  |_______||_______||__| |__|{4}

                {1}-- --{3}[{2}  Coded by {2}Metachar   {3}]{1}-- --
                {1}-- --{3}[{0}  Github{1}/{2}Metchar      {3}]{1}-- --
                {1}-- --{3}[{1}  Instagram @{2}zuccsss  {3}]{1}-- --
{1}=================================================================
Email info is {2}NEEDED{1} to send messages!\n 
'''.format(color.GREEN, color.CWHITE, Fore.RED,color.YELLOW,color.END)

def INFO(MESSAGE, CARRIER_MESSAGE, NUMBER,email_login,email_password):
    to_number = NUMBER+CARRIER_MESSAGE
    server = smtplib.SMTP( "smtp.gmail.com", 587 )
    server.starttls()           
    server.login(email_login, email_password)
    print '=================================='
    send(server, email_login,to_number,MESSAGE)

def send(server, email_login,to_number,MESSAGE):
    while True:
        try:
            server.sendmail(email_login, to_number, MESSAGE)
            print (color.GREEN+'[+]'+color.CWHITE+' Message has been sent')
        except KeyboardInterrupt:
            print '\n=================================='
            print (Fore.RED + '[!] '+color.CWHITE+' Exiting')
            exit()

def main():
    try:
        print logo
        t.sleep(1)
        email_login = raw_input(color.GREEN+'[~]'+color.CWHITE+' Enter your email address: ')
        t.sleep(.5)
        email_password = raw_input(color.GREEN+'[~]'+color.CWHITE+' Enter your email password: ')
        t.sleep(.5)
        NUMBER = raw_input(color.GREEN+'[~]'+color.CWHITE+' Enter a number to spam: ')
        t.sleep(.5)
        print ('\nCarriers: {0}att{4}, {1}tmobile{4}, {2}verizon {4}and {3}sprint' ).format(color.CYAN, color.PURPLE, Fore.RED,color.YELLOW, color.CWHITE)
        CARRIER = raw_input(color.GREEN+'[~]'+color.CWHITE+' Enter a carrier: ')
        t.sleep(.5)
        MESSAGE = raw_input(color.GREEN+'[~]'+color.CWHITE+' Enter a message to spam: ')
        if CARRIER == 'att':
            CARRIER_MESSAGE = '@mms.att.net'
        if CARRIER == 'tmobile':
            CARRIER_MESSAGE = '@tmomail.net'
        if CARRIER == 'verizon':
            CARRIER_MESSAGE = '@vtext.com'
        if CARRIER == 'sprint':
            CARRIER_MESSAGE = '@messaging.sprintpcs.com'
        INFO(MESSAGE,CARRIER_MESSAGE,NUMBER,email_login,email_password)
    except smtplib.SMTPAuthenticationError:
        print (Fore.RED + '[!] '+color.CWHITE+'Incorrect email information')
    except KeyboardInterrupt:
        print '\n'
        exit()

main()