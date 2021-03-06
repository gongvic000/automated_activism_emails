import senators, smtplib, messages, ssl, states, sys, time
from email.message import EmailMessage
from getpass import getpass

def boundary():
    print("==================================================================")

def prepare_email():
    boundary()
    print("\nWhat would you like the subject (title) of your email to be?\n")
    title_subject = input("Type here and press enter (if blank, the program will generate one for you): ")
    boundary()
    print("\nThis program creates unique and personalized emails to Senators.")
    print("However, if you would like to write your own message, please save it in a .txt file. The easiest way to do this is to just write your message in example.txt.\n")
    while True:
        response = input("Would you like the program to write emails for you? Each email will be unique. (y/n): ")
        if response == 'n':
            while True:
                file = input("What is the name of your txt file?: ")
                with open(file, 'r', encoding = 'utf-8-sig') as fd:
                    message = fd.read()
                break
            break
        elif response == 'y':
            message = ""
            break
        else:
            print("Please answer with y or n.")
    
    return title_subject, message


def login():
    boundary()
    sender_name = ""
    while True:
        if not sender_name:
            sender_name = input("Type in your name then press enter: ")
        else:
            break
    email = input("Type in your gmail then press enter: ")
    password = getpass("Type in your password then press enter: ")
    boundary()
    return sender_name, email, password


def select_recipients():
    receive = set()
    selected = set()

    # Choose a state
    while True:
        boundary()
        print("Select 0 to send your message to the state senators of your selected state")
        if selected: print(f'States chosen: {selected}\n')
        state_options = { v:k for v,k in enumerate(senators.get_states()) }
        for idx, opt in state_options.items():
            print(idx, "->", opt)
        print("Enter blank (nothing) when done.")
        
        state_idx = input("\nType the number corresponding to the state here: ")
        boundary()
        # Blank -> Done
        if not state_idx:
            break
        # 0 -> All States
        elif int(state_idx) == 0:
            receive.update(senators.get_all())
            break
        # (1 to N) -> Individual States
        elif int(state_idx) in state_options.keys():
            state = state_options[int(state_idx)]
            subcart = set()
        # Choose a senator
            while True:
                state_confirmation = { v:k for v,k in enumerate(senators.confirm(state)) }
                boundary()
                print("If the state selected is correct, press 0 to cofirm your selection")
                if subcart: print(f'States chosen: {subcart}\n')
                for idx, opt in state_confirmation.items():
                    print(idx, "->", opt)
                print("Enter blank (nothing) when done.")
                choose_state = input("\nType the number corresponding to the state here: ")
        
                if not choose_state:
                    break
                elif int(choose_state) == 0:
                    subcart.update(senators.confirm(state))
                    subcart.remove('Select All')
                    receive.update(senators.get_state(state))
                    break
                elif int(choose_state) in state_confirmation.keys():
                    subcart.add(state_confirmation[int(choose_state)])
                    receive.update(senators.confirm_mail_list(state, state_confirmation[int(choose_state)]))
                else:
                    print("Invalid index")
            for city in subcart:
                selected.add("%s, %s" % (city, states.abbreviate(state)))
            boundary()
        else:
            print("Invalid index")
    boundary()

    if not receive:
        sys.exit("ABORT: no recipients selected.")

    print(f'\n{len(receive)} recipients selected.\n')
    
    return receive


port = 465 # standard port for SMTP over SSL
smtp_server = "smtp.gmail.com"

send = 0
receive = select_recipients()
title_subject, message = prepare_email()
sender_name, sender_email, password = login()
while True:
    try:
        context = ssl.create_default_context()

        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, password)
            while receive:
                recipient = receive.pop()
                senator_name = recipient[0]
                state = recipient[1]
                senator_email = recipient[2]

                msg = EmailMessage()

                msg['Subject'] = title_subject if title_subject else messages.line_subject()
                msg['From'] = sender_email
                msg['To'] = senator_email

                body = messages.attach_greeting(senator_name, message) if message else messages.body_text(sender_name, senator_name, state)
                msg.set_content(body)
                print(msg.as_string())

                server.send_message(msg)
                send += 1
        break
    except smtplib.SMTPException:


        print("Unexpected error... trying again in 10 seconds.")
        time.sleep(10)

boundary()
print(f'\nSuccessfully sent {send} emails!\n')
boundary()
