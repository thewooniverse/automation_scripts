#! /usr/bin/python
#logging_gen.py - a script to generate

import datetime, pytz, sys, os, pyperclip, random, shutil


# list of greetings
sign_on_ls = ['Hello, Woo signing on!!', 'The Wooniverse is here for duty!', "I'm here n available!", 'Good morning team, Woo is online', 'Its Woo time!']
sign_off_ls = ['Woo - out!', 'Woo signing off!! Bye Folks!!', 'Signing off - see you all tomorrow!']
TU_specific_emoji =[':bling:', ':shimmy:', ':worm:', ':leftshark:', ':10-4:', ':robot:', ':ahhhh:']
TU_specific_emoji += [':surge:', ':meow_party:', ':tarmac:', ':wavey:', ':tmnt:', ':wild:']

# parse datetime now and other vars
now = datetime.datetime.now()
format_now = now.strftime('%H:%M %B %d, %Y -- GMT+0')
random_emoji_seq = TU_specific_emoji[random.randint(0, len(TU_specific_emoji)-1)] * random.randint(1, 5)

# define random sign on / sign off generator
def str_gen(msg_type):
    result = ""

    if msg_type == "on":

        result += f'{random_emoji_seq} {sign_on_ls[random.randint(0, len(sign_on_ls)-1)]} {random_emoji_seq}\n'
        result += f"\nTime now is...\n{format_now}\n"
        result += "\nPlease check this thread for things I'll be working on and updates!"

    elif msg_type == "off":

        result += f'{random_emoji_seq} {sign_off_ls[random.randint(0, len(sign_off_ls)-1)]} {random_emoji_seq}'
        result += f"\nTime now is...{format_now}"
        result += f"\nPing me on Slack still if urgent!!"

    return result


# read sys argv and call relevant
result = str_gen(sys.argv[1])
pyperclip.copy(result)


# detect filepath


# log total hours... probably work with a .csv file locally



# add gitignore.





