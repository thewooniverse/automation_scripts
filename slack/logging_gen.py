#! /usr/bin/python
#logging_gen.py - a script to generate and log productive hours for work at TU
#usage:
#python logging_gen.py on - to simply generate greeting string to paste to slack
#python logging_gen.py on add - to generate and add to database
#python logging_gen.py off
#python logging_gen.py off add





import datetime, pytz, sys, os, pyperclip, random, shutil, csv, shelve

# error logging
import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s -  %(levelname)s -  %(message)s')


# list of greetings
sign_on_ls = ['Hello, Woo signing on!!', 'Woo here for duty!', "I'm here n available!", 'Good morning team! I\'m is online']
sign_off_ls = ['Woo - out!', 'Signing off! Bye Folks!!', 'Signing off - see you all tomorrow!']


TU_specific_emoji =[':bling:', ':shimmy:', ':worm:', ':leftshark:', ':10-4:', ':robot:', ':ahhhh:']
TU_specific_emoji += [':surge:', ':meow_party:', ':tarmac:', ':wavey:', ':tmnt:', ':wild:']
random_emoji_seq = TU_specific_emoji[random.randint(0, len(TU_specific_emoji)-1)] * random.randint(1, 5)


# parse datetime now and other vars
now = datetime.datetime.now(tz=pytz.UTC)
slack_format = now.strftime('%H:%M %B %d, %Y %z %Z')
dmy_today = now.strftime('%d-%m-%Y')


# define random sign on / sign off generator
def str_gen(msg_type):
    result = ""

    if msg_type == "on":

        result += f'{random_emoji_seq} {sign_on_ls[random.randint(0, len(sign_on_ls)-1)]} {random_emoji_seq}\n'
        result += f"\nTime now is...\n{slack_format}\n"
        result += "\nPlease check this thread for things I'll be working on and updates!"


    elif msg_type == "off":

        result += f'{random_emoji_seq} {sign_off_ls[random.randint(0, len(sign_off_ls)-1)]} {random_emoji_seq}\n'
        result += f"\nTime now is...\n{slack_format}\n"
        result += f"\nPing me on Slack if urgent!!"

    return result




# read sys argv and call relevant
result = str_gen(sys.argv[1])
pyperclip.copy(result)





### logging to csv file ###
# detect filepath
cwd = os.getcwd()

# list directory to see if hours.csv exists or not;
# if it doesn't exist, it creates one.
ls_dir_result = os.listdir(cwd)

if 'hour_log.csv' not in ls_dir_result:
    with open('hour_log.csv', 'w') as output_csv:
        fields = ['date', 'start_time', 'end_time', 'total_hours']
        output_writer = csv.DictWriter(output_csv, fieldnames=fields)
        output_writer.writeheader()

else:
    pass

# open or create if it doesn't exist, a .db file with the filename of today's d-m-y where we will dump and read info from.
log_db = shelve.open(os.getcwd() + os.path.sep + 'logs' + os.path.sep + dmy_today)






def add_hours(msg_type):

    if msg_type == 'on':
        log_db['start_time'] = now
        # logging.debug('{0}'.format(log_db['start_time']))

    elif msg_type == 'off':
        log_db['end_time'] = now
        log_db['total_hours'] = ((log_db.get('end_time') - log_db.get('start_time')).total_seconds() / 3600) #gets the hours
        # logging.debug('{0}'.format(log_db['total_hours']))

        with open('hour_log.csv', 'a') as output_csv:
            fields = ['date', 'start_time', 'end_time', 'total_hours']
            output_writer = csv.DictWriter(output_csv, fieldnames=fields)
            items = {'date': dmy_today, 'start_time': log_db["start_time"], 'end_time': log_db["end_time"], 'total_hours': log_db["total_hours"]}
            output_writer.writerow(items)



if len(sys.argv) > 2:
    add_hours(sys.argv[1])
else:
    pass








# add gitignore.





