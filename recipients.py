# If you would like to add to this list, please let me know at victoriagong22@gmail.com
# Every Senator
# Credit - http://hrlibrary.umn.edu/peace/senate.html

# a dictionary that maps states to dictionaries that map states to contacts
# contacts are tuples (name, state, email)
mailing_list = {
    "Alaska" : {
            "Alaska" : [
                ( "Senator Stevens", "Alaska", "victoriagong22@gmail.com"),
                ( "Senator Murkowski", "Alaska", "vicvictoria100@gmail.com"),
            ]
    },
   
}

def get_all():
    recv = []
    for state in mailing_list:
        for county in mailing_list[state]:
            recv.extend(mailing_list[state][county])
    return recv

def get_state(state):
    recv = []
    for county in mailing_list[state]:
        recv.extend(mailing_list[state][county])
    return recv

def get_city(state, county):
    return mailing_list[state][county]

def get_states():
    lst = ["Select All"]
    lst.extend(mailing_list.keys())
    return lst

def get_cities(state):
    lst = ["Select All"]
    lst.extend(mailing_list[state].keys())
    return lst

"""
prints a javascript dictionary of the form
...
{
    label: "San Antonio",
    name: "Councilmember Roberto C. Trevino",
    email: "district1@sanantonio.gov"
},
{
    label: "San Antonio",
    name: "Councilmember Jada Andrews-Sullivan",
    email: "district2@sanantonio.gov"
}
...
"""
def convert_to_js_dict():
    for state in mailing_list:
        for county in mailing_list[state]:
            people = mailing_list[state][county]
            for p in people:
                print('{\n\tlabel: "%s",\n\tname: "%s",\n\temail: "%s",\n},' % (p[1], p[0], p[2]))

def convert_to_js_dict_and_save_to(filename):
    import sys
    sys.stdout = open(filename, 'w')
    convert_to_js_dict()
