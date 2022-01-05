import senators, smtplib, messages, ssl, states, sys, time
from email.message import EmailMessage
from getpass import getpass

def print_success():
    print("==================================================================")

def login():
    print_success()
    sender_name = ""
    while True:
        if not sender_name:
            sender_name = input("Type in your name then press enter: ")
        else:
            break
    email = input("Type in your gmail then press enter: ")
    password = getpass("Type in your password then press enter: ")
    print_success()
    return sender_name, email, password



def prepare_email():
    print_success()
    print("\nWhat would you like the subject (title) of your email to be?\n")
    title_subject = input("Type here and press enter (if blank, the program will generate one for you): ")
    print_success()
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


def select_recipients():
    receive = set()
    selected = set()

    # Choose a state
    while True:
        print_success()
        print("Select 0 to send your message to the state senators of your selected state")
        if selected: print(f'States chosen: {selected}\n')
        state_options = { v:k for v,k in enumerate(senators.get_states()) }
        for idx, opt in state_options.items():
            print(idx, "->", opt)
        print("Enter blank (nothing) when done.")
        
        state_idx = input("\nType the number corresponding to the state here: ")
        print_success()
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
                city_options = { v:k for v,k in enumerate(senators.get_cities(state)) }
                print_success()
                print("Which officials do you want to send emails to?")
                if subcart: print(f'Cities chosen: {subcart}\n')
                for idx, opt in city_options.items():
                    print(idx, "->", opt)
                print("Enter blank (nothing) when done.")
                city_idx = input("\nType the number corresponding to the state here: ")
        
                if not city_idx:
                    break
                elif int(city_idx) == 0:
                    subcart.update(senators.get_cities(state))
                    subcart.remove('Select All')
                    receive.update(senators.get_state(state))
                    break
                elif int(city_idx) in city_options.keys():
                    subcart.add(city_options[int(city_idx)])
                    receive.update(senators.get_city(state, city_options[int(city_idx)]))
                else:
                    print("Invalid index")
            for city in subcart:
                selected.add("%s, %s" % (city, states.abbreviate(state)))
            print_success()
        else:
            print("Invalid index")
    print_success()

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
        # create a secure SSL context
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

print_success()
print(f'\nSuccessfully sent {send} emails!\n')
print_success()
