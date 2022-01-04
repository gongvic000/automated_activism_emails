# Make a Difference Today!

In light the of China's treatment towards Uyghur Muslim, it is imperative that we push more more than a diplomatic boycott, but genuine intervention. 

The script sends a **unique message to each lawmaker** by varying sentence structures and switching out nouns, verbs, adverbs, and adjectives with synonyms. 

**This script only works for gmail accounts.** 

## Setup the program
1. Download the source code
	- Click the green "Clone or download" button on the upper-right, then "Download ZIP"
	- Unzip the files on your computer 

2. Grant the program permission to send emails
	- Turn [_Allow less secure apps_  to  _ON_](https://myaccount.google.com/lesssecureapps) for your gmail account.
		- Be aware that this makes it easier for others to gain access to your account.
		- After running the script, you should switch this back OFF.
		- Your name, gmail, and password aren't being stored on a server anywhere, this script is run from your own computer!
	- If you have 2 Factor Authentication enabled on your gmail account:
		- [Follow these instructions](https://support.google.com/accounts/answer/185833)
	

## Running the script
Shoutout to Darry for helping me set this up!
	- Install docker-engine
    		- [Mac or Windows](https://docs.docker.com/engine/install/) (Catalina, Mojave, or High Sierra; Windows 10 Pro, Enterprise, or Education)
	- Run application: `python send.py`

## How to use my program

1. Choose which state senators you would like to send emails to
	- Enter the number corresponding to the state of your choice
		- Enter 0 to select all 100 senators
	- Enter blank (nothing) when finished selecting if you choose to select individual states

2. Enter the subject (title) of your emails.
	- If you leave it blank, the script wil automatically create one 

3. Would you like to write your own email or have the program do it for you?
	- If you want program to write the emails, answer `y`.
	- Else if you have your own email message, answer `n`.
		- Mailbot will now read from a .txt file
		- Please write your own email in a .txt file
			- Easiest way: edit the contents of `example.txt`
			- Tell mailbot the name of your .txt file
			- Example: `example.txt`
			
4. Enter your full name

5. Enter your gmail

6. Enter your gmail password
	- This code will not save your information! Do not worry!!
	
## Notes

- I will be in the process of updating the recipients list to one day include representatives as well
	- [Use this Google Form](https://forms.gle/cm2Ayjs4mguQ77uK9) or add to `recipients.py` and submit a pull request
- **Please remember to switch `Allow less secure apps` to OFF.**


