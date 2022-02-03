# If you would like to add to this list, please let me know at victoriagong22@gmail.com
# Every Senator
#used for testing
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

def get_states():
    lst = ["Select All"]
    lst.extend(mailing_list.keys())
    return lst


