


# -*- coding: utf-8 -*-

import random

"""

"""



# Randomly generates the subject header of the email
def line_subject(): #note can this function be used later if its part of the app route? (im very new to flask)
	s = ["Human Rights Inquiry","Thoughts of a Concerned Citizen","In Light of Recent Human Rights Abuses", "A Genocide Unraveling", "Time for Change", "Boycott is the First Step", "Stand up for Uyghur", "Take a Stand Against Human Genocide", "A Second Holocaust", "Ethnic Cleansing"]
	return random.choice(s)

# Randomly cretes mail content follwing a template with different phrases
def body_text(sender_name, senator_name, state):
	return f'{recipiant_greeting(senator_name)}\t{introduction(state)}\n\t{gen_curiosity()}\n\t{gen_conclusion(sender_name)}'

# Generates the greeting to the recipient of the email
def recipiant_greeting(person):
	s = ["Dear", "Hello", "Greetings", "Hi"]
	return f'{random.choice(s)} {person},\n\n'

# # Greeting statement to whom the email is directed to
# def member_greeting(person, body):
# 	s = ["Dear", "Hello", "Greetings", "Hi"]
# 	return f'{random.choice(s)} {person},\n\n{body}'

# First sentence in email.
def introduction(state):
	disaster = ["a catastrophe" "an inconceivable mess" "in shambles", "horrific" "a horrific siutation" "disgusting", "a disaster", "a mess"]
	subject = ["As a human", "I beleive that everyon deserve to be treated as an equal","As a concerned American,"]
	contact = ["getting in touch", "reaching out to you", "contacting you", "sending you this message"]
	adverb = ["deeply", "very", "greatly", "extremely", "especially", "immensely"]
	concern = ["troubled", "concerned", "disturbed", "distressed", "distraught", "worried", "devastated"]
	explanation = ["occuring genoicde", "unfair treatment of Uyghurs", "blatant acts of human rights violations", "unjust treatment of Uyghurs", "violence against Uyghurs", "atrocities against Uyghurs"]
	location = ["in China", "taking place in China", "on our top trading partner's soil" "in the coutry hosting the 2020 Olympics"]

	r = random.randint(0,100)
	if r < 33:
		return f'The current acts agisnt Uyghurs is {random.choice(disaster)}. I am {random.choice(contact)} because I am {random.choice(adverb)} {random.choice(concern)} by the {random.choice(explanation)} by officials {random.choice(location)}.\n'
	elif r < 66:
		return f'I am {random.choice(contact)} because of the {random.choice(adverb)} disturbing cases of {random.choice(explanation)} by the government {random.choice(location)}.\n'
	else:
		return f'{random.choice(subject)} I am {random.choice(contact)} because I am {random.choice(adverb)} {random.choice(concern)} by what I have seen recently regarding the {random.choice(explanation)} by the government {random.choice(location)}.\n'

# Expose truth with a question
def gen_curiosity():
	verb = ["know", "inquire", "ask"]
	noun = ["safeguards", "policies", "provisions"]
	work = ["commitments", "efforts", "actions"]
	crime = ["distrubing violations of human rights", "violations of human rights", "restricions of freedom", "exploitations of human rights" "a mondern genocide"]

	if random.randint(0,100) % 2:
		return f'As a public servant, what {random.choice(work)} will you make to protect an entire ethnic group? In addition, what {random.choice(noun)} are in place to prevent {random.choice(crime)} from continuing to occur? {gen_rhetorical_questions()}\n'
	else:
		return f'I would like to {random.choice(verb)} what {random.choice(noun)} our government have in place to prevent {random.choice(crime)}, and what {random.choice(work)} you will make to protect Uyghur lives. {gen_rhetorical_questions()}\n'

# Emotional rhetorical questions
def gen_rhetorical_questions():
	q1 = [
			"What message does America send when they do not make a stand agaisnt China?",
			"Will you allow another Holocaust to unfold in front of our eyes?",
			"How can we call America a stronghold of Democracy?",
			"When will the human rights violations end if we do not take a stand today? Never?",
	]
	q2 = [
			"Will we set a precendent that genocide is acceptable? Will our children read history books of the violece and cowardice of America?",
			"Can you continue to call America the land of the free if you do not fight for other's freedoms?",
			"What have you done to stand up for Uyghurs today? Will you contiue to ignore their suffering?",
			"How many more violations do we have to report for you to step in and protect an entire ethnic group?",
	]
	
	return f"{' '.join(random.sample(q1,k=len(q1)))} {' '.join(random.sample(q2,k=len(q2)))}"

def gen_conclusion(name):
	noun = ["safeguards", "policies", "plans", "intervention policies"]
	adverb = ['certainly', 'definitely', 'absolutely', 'undoubtedly']
	verb = ["support", "want", "approve of"]
	place = ["law enforcement agencies", "a military", "government institutions", "a Navy", "troops"]

	r = random.randint(0,100)
	if r % 2:
		return f'If these {random.choice(noun)} are not in place, then they {random.choice(adverb)} should be. {gen_action()} I do not {random.choice(verb)} my taxes going to {random.choice(place)} that is scared of protecing human rights. {gen_interests()}\n\n\t{recipiant_gratitude()}\n{gen_closing(name)}'
	else:
		return f'These {random.choice(noun)} must be put into place to protect Uyghur rights and lives. As a taxpayer, I do not {random.choice(verb)} my taxes being used to fund {random.choice(place)} that fails to interfere when necessary. {gen_interests()}\n\n\t{recipiant_gratitude()}\n{gen_closing(name)}'

def gen_action():
	bank = [
		"The status quo is failing us. We must take a stand agaisnt China's treatment today.",
		"The current system isn't working and we need more than a Diplomatic Boycott of the Beijing Olympics.",
		"This issue will not disappear on its own. The American Government cannot stand by the actions of China.",
	]

	return random.choice(bank)

def gen_interests():
	noun = [ 'Changes', 'Government policies']
	preamble = [
			f'{random.choice(noun)} that need to be implemented include: ',
			'The American Government should implement',
	]
	return f'{random.choice(preamble)} {gen_services()} to name only a few.'

def gen_services():
	i = [
			"an embargo,",
			"a trading ban,",
			"a boycott on the Beijing Olympics,",
			"raised public awareness,",
			"human-aid intervention,",
	]
	return ' '.join(random.sample(i, k=len(i)))

def recipiant_gratitude():
	clauses = [
			"Thank you for your attention to my concerns.",
			"Thanks for taking the time to read my message.",
			"Your attention to my concerns is very appreciated.",
	]
	finale = [
			"I hope to hear back from you soon.",
			"I'm hoping to hear back from you soon.",
			"I look forward to hearing back from you.",
	]

	return f'{random.choice(clauses)} {random.choice(finale)}'

def gen_closing(name):
	c = [
			"Signed",
			"Sincerely",
			"From",
			"Regards",
			"Best",
	]
	return f'\n{random.choice(c)},\n{name}'
