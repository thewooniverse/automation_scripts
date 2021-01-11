#! /usr/bin/python
#logging_gen.py - a script to generate

import datetime, pytz, sys, os, pyperclip, random, shutil


# list of greetings
sign_on_ls = ['Hello, Woo signing on!!', 'The Wooniverse is here for duty!', "I'm here n available!", 'Good morning team, Woo is online', 'Its Woo time!']
sign_off_ls = ['Woo - out!', 'Woo signing off!! Bye Folks!!', 'Signing off - see you all tomorrow!']

# parse datetime now
now = datetime.datetime.now()
format_now = now.strftime('%H:%M %B %d, %Y -- GMT+0')
# print(format_now)


# define random sign on / sign off generator
def str_gen(msg_type):
    result = ""

    if msg_type == "on":

        result += f'{sign_on_ls[random.randint(0, len(sign_on_ls)-1)]}'
        result += f"\nTime now is...{format_now}"
        result += "\nPlease check this thread for things I'll be working on and updates!"

    elif msg_type == "off":

        result += f'{sign_off_ls[random.randint(0, len(sign_off_ls)-1)]}'
        result += f"\nTime now is...{format_now}"
        result += f"\nPing me on Slack still if urgent!!"

    return result


# read sys argv and call relevant
result = str_gen(sys.argv[1])
pyperclip.copy(result)


# detect filepath


# log total hours... probably work with a .csv file.



# TODO: Add support for emoji
