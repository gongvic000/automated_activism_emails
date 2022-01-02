# Activism Emails

In light the of China's treatment towards Uyghur Muslim, it is imperative that we push more more than a dimplomatic boycott, but a postponement, relocation or athlete boycott. 

The script sends a **unique message to each lawmaker** by varying sentence structures and switching out nouns, verbs, adverbs, and adjectives with synonyms. 

**This script only works for gmail accounts.** 

NOTE: there is a per-minute limit on SMTP messages sent via google's servers. to appease our corporate overlords, i've decreased the speed of our operations.


## Setup
1. Download the source code
	- Option 1: click the green "Clone or download" button on the upper-right, then "Download ZIP"
		- Then, decompress the files somewhere on your computer
	- Option 2: `git clone https://github.com/alandgton/activism-mail-bot.git`
		- Requires: a Github account, a terminal, and git installation

2. Temporarily grant mailbot permission to send emails on your behalf
	- Turn [_Allow less secure apps_  to  _ON_](https://myaccount.google.com/lesssecureapps) for your gmail account.
		- Be aware that this makes it easier for others to gain access to your account.
		- After running the script, you should switch this back OFF.
		- Your name, gmail, and password aren't being stored on a server anywhere, this script is run from your own computer!
	- If you have 2 Factor Authentication enabled on your gmail account:
		- [Follow these instructions](https://support.google.com/accounts/answer/185833)
	

## Running the script
- Option 1: Use Docker (**RECOMMENDED**)
	- Shoutout to Darry Balderas for setting this up!
	- Install docker-engine
    	- [Mac or Windows](https://docs.docker.com/engine/install/) (Catalina, Mojave, or High Sierra; Windows 10 Pro, Enterprise, or Education)
    	    - For older Mac and Windows systems install [Docker Toolbox](https://docs.docker.com/toolbox/toolbox_install_windows/)
   		- [Linux](https://docs.docker.com/engine/install/ubuntu/)

	- Run the command: `./exec-docker`
		- Make sure you're in the `automated_activism_emails/ directory
			- Use `cd automated_activism_emails/`
	- Run application: `python send.py`
	
- Option 2: Legacy Method
	- [Install python3](https://realpython.com/installing-python/)
	- Mac Users: you can double-click the `install-osx-python3` file instead
	- Windows Users: TBD

	- Mac Users: you may need to install certificates for SSL to work
		- ⌘ + space, search for a file named "Install Certificates.command"
		- double-click the resulting file
		- [Read more here](https://stackoverflow.com/questions/52805115/certificate-verify-failed-unable-to-get-local-issuer-certificate)

	- Run `python3 send.py`
		- Make sure you are in the `activism-mail-bot` directory
		- If you aren't, use the command `cd activism-mail-bot/`
		
## How to use mailbot

1. Choose which officials you would like to send emails to
	- Enter the number corresponding to the state/city/county of your choice
		- Enter 0 to Select All (current total: 542 recipients)
	- Enter blank (nothing) when finished selecting
	- NOTE: some city councilmembers may ask for your address to confirm that you are their constituent
	
2. Enter the subject (title) of your emails.
	- If blank, mailbot will randomly generate a spicy title for you

3. Would you like to write your own email or have mailbot do it for you?
	- If you want mailbot to write the emails, answer `y`.
	- Else if you have your own email message, answer `n`.
		- Mailbot will now read from a .txt file
		- Please write your own email in a .txt file
			- Easiest way: edit the contents of `example.txt`
			- Tell mailbot the name of your .txt file
			- Example: `example.txt`
			
4. Enter your full name

5. Enter your gmail

6. Enter your gmail password
	- i'm not logging this anywhere or anything, feel free to look at my code if you're paranoid
	
## Final Steps

- Please add more recipients!
	- [Use this Google Form](https://forms.gle/cm2Ayjs4mguQ77uK9) or add to `recipients.py` and submit a pull request
- thank you for your time, we did some good work :^)
- activism++
- **Please remember to switch `Allow less secure apps` to OFF.**


