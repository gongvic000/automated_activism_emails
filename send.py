#!/usr/bin/env python3
import messages, senators, smtplib, ssl, states, sys, time
from getpass import getpass
from email.message import EmailMessage

def print_success():
    print("======================================================")

def prompt_login():
    print_success()
    name = ""
    # make sure name not blank
    while True:
        if not name:
            name = input("Type your name and press enter: ")
        else:
            break

    email = input("Type your gmail and press enter: ")
    password = getpass("Type your password and press enter: ")
    print_success()
    return name, email, password



def prompt_email():
    print_success()
    print("\nWhat would you like the subject (title) of your email to be?\n")
    subject = input("Type here and press enter (if blank, a random one will be generated): ")
    print_success()
    print("\nThis program creates unique and personalized emails to Senators.")
    print("However, if you would like to write your own message, please save it in a .txt file. The easiest way to do this is to just write your message in example.txt.\n")
    while True:
        response = input("Would you like mailbot to write emails for you? (y/n): ")
        if response == 'n':
            while True:
                filename = input("What is the name of your txt file?: ")
                with open(filename, 'r', encoding = 'utf-8-sig') as fd:
                    message = fd.read()
                break
            break
        elif response == 'y':
            message = ""
            break
        else:
            print("Please answer with y or n.")
    
    return subject, message


def prompt_recipients():
    recv = set()
    cart = set()

    # Choose a state
    while True:
        print_success()
        print("Which state senators do you want to send emails to?")
        if cart: print(f'States chosen: {cart}\n')
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
            recv.update(senators.get_all())
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
                city_idx = input("\nType the number corresponding to the city here: ")
        
                if not city_idx:
                    break
                elif int(city_idx) == 0:
                    subcart.update(senators.get_cities(state))
                    subcart.remove('Select All')
                    recv.update(senators.get_state(state))
                    break
                elif int(city_idx) in city_options.keys():
                    subcart.add(city_options[int(city_idx)])
                    recv.update(senators.get_city(state, city_options[int(city_idx)]))
                else:
                    print("Invalid index")
            # Add (city, state) to cart)
            for city in subcart:
                cart.add("%s, %s" % (city, states.abbreviate(state)))
            print_success()
        else:
            print("Invalid index")
    print_success()

    if not recv:
        sys.exit("ABORT: no recipients selected.")

    print(f'\n{len(recv)} recipients selected.\n')

    return recv


port = 465 # standard port for SMTP over SSL
smtp_server = "smtp.gmail.com"

send = 0
recv = prompt_recipients()
subject, message = prompt_email()
sender_name, sender_email, password = prompt_login()

while True:
    try:
        # create a secure SSL context
        context = ssl.create_default_context()

        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, password)
            while recv:
                recipient = recv.pop()
                senator_name = recipient[0]
                state = recipient[1]
                senator_email = recipient[2]

                msg = EmailMessage()

                msg['Subject'] = subject if subject else messages.line_subject()
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
