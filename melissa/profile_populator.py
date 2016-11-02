import os
import sys
import subprocess
import json
from getpass import getpass
import pywapi


def tts_local(message):
    if sys.platform == 'darwin':
        tts_engine = 'say'
        return subprocess.call([tts_engine, message])
    elif sys.platform.startswith('linux') or sys.platform == 'win32':
        tts_engine = 'espeak'
        speed = '-s170'
        return subprocess.call([tts_engine, speed, message])


def profile_populator():
    def empty(variable):
        if variable:
            return False
        else:
            return True

    tts_local('Welcome to Melissa. Let us generate your profile!')
    print('Welcome to Melissa. Let us generate your profile!')
    print('Press Enter for using default values.')

    va_name = raw_input('What would you like to name me?: ')
    if empty(va_name):
        va_name = 'Melissa'

    while(True):
        va_gender = raw_input('What is my gender ((m)ale/(f)emale)?: ')
        if va_gender in ('male', 'm', 'female', 'f', ''):
            if empty(va_gender):
                va_gender = 'female'
            elif va_gender == 'm':
                va_gender = 'male'
            elif va_gender == 'f':
                va_gender = 'female'
            break
        print('Invalid input, please enter male, female or <ENTER>.')

    name = raw_input('Your name: ')
    if empty(name):
        name = 'Tanay'

    sun_signs = {1: 'Aquarius',
                 2: 'Pisces',
                 3: 'Aries',
                 4: 'Taurus',
                 5: 'Gemini',
                 6: 'Cancer',
                 7: 'Leo',
                 8: 'Virgo',
                 9: 'Libra',
                 10: 'Scorpio',
                 11: 'Sagittarius',
                 12: 'Capricorn'}
    print 'What is your sun sign?'
    for sign in sun_signs.keys():
        print str(sign) + '. ' + sun_signs[sign]
    sun_sign = raw_input('Enter the serial number of the sign: ')
    while (not sun_sign.isdigit() or not 1 <= int(sun_sign) <= 12):
        sun_sign = raw_input('You did not enter a number between 1\
                 and 12,press <Enter> without an entry to select the\
                default of Aquarius')
        if empty(sun_sign):
            sun_sign = '1'
            break
    sun_sign = sun_signs[int(sun_sign)]

    while(True):
        stt = raw_input(
            'STT Engine ((g)oogle/(s)phinx/(t)elegram/(k)eyboard): ').lower()
        if stt in ('g', 'google', 's', 'sphinx', 'k',
                   'keyboard', 't', 'telegram', ''):
            if empty(stt) or stt == 'g':
                stt = 'google'
            elif stt == 's':
                stt = 'sphinx'
            elif stt == 't':
                stt = 'telegram'
            elif stt == 'k':
                stt = 'keyboard'
            break
        print('Invalid input, please enter(g)oogle, (s)phinx, (t)elegram,' +
              '(k)eyboard or < ENTER > .')

    telegram_username = raw_input('Your username at Telegram: ')
    if empty(telegram_username):
        telegram_username = 'tanay1337'

    while(True):
        music_path = raw_input('Path to your music directory: ')
        if empty(music_path):
            music_path = '.'
            break
        if os.path.isdir(music_path):
            break
        print('Invalid input, please enter a valid directory path or <ENTER>.')

    while(True):
        images_path = raw_input('Path to your images directory: ')
        if empty(images_path):
            images_path = '.'
            break
        if os.path.isdir(images_path):
            break
        print('Invalid input, please enter a valid directory path or <ENTER>.')

    city_name = raw_input('Name of city where you live: ')
    if empty(city_name):
        city_name = 'New Delhi'

    city_code = raw_input('Code of city from weather.com\
 or <ENTER> for a search based on the name\
 of the city you live in: ')
    if empty(city_code):
        city_list = pywapi.get_loc_id_from_weather_com(unicode(city_name))
        if city_list['count'] == 0:
            print 'Sorry, search results were empty.'
            city_code = 'INXX0096'
        else:
            print 'Cities returned are: '
            for city_list_i in range(city_list['count']):
                print str(city_list_i+1) + ": " + city_list[city_list_i][1]
            while(True):
                city_choice_i = ''
                city_choice_i = raw_input('Enter the index of \
the city of your choice: ')
                if empty(city_choice_i):
                    city_code = 'INXX0096'
                    break
                city_choice_i = int(city_choice_i)
                if 1 <= city_choice_i <= city_list['count']:
                    city_code = city_list[city_choice_i-1][0]
                    break
                else:
                    print 'Enter an index from one of the choices.\
 Try again!'

    while(True):
        degrees = raw_input('(c)elsius/(f)ahrenheit): ').lower()
        if degrees in ('c', 'celsius', 'f', 'fahrenheit', ''):
            if empty(degrees) or degrees == 'c':
                degrees = 'celsius'
            elif degrees == 'f':
                degrees = 'fahrenheit'
            break
        print('Invalid input, please enter(c)elsius, (f)ahrenheit) or' +
              '<ENTER > .')

    gmail_address = raw_input('Enter your gmail address (???@gmail.com): ')
    gmail_password = ''
    if len(gmail_address) > 0:
        gmail_password = getpass()

    icloud_username = raw_input(
        'Enter your icloud username/address (???@???.com): ')
    icloud_password = ''
    if len(icloud_username) > 0:
        icloud_password = getpass()

    tts = 'xxxx'

    hotword_detection = 'on'

    access_key = 'xxxx'
    secret_key = 'xxxx'

    access_token = 'xxxx'
    access_token_secret = 'xxxx'
    consumer_key = 'xxxx'
    consumer_secret = 'xxxx'

    client_id = 'xxxx'
    client_secret = 'xxxx'

    telegram_token = 'xxxx'

    modeldir = './data/model/'
    hmm = 'hmm/en_us/hub4wsj_sc_8k'
    lm = 'lm/sphinx.lm'
    dic = 'lm/sphinx.dic'

    modules = 'melissa.actions'
    actions_db_file = ':memory:'
    memory_db = './data/memory.db'

    profile_data = {
        'va_name': va_name,
        'va_gender': va_gender,
        'name': name,
        'sun_sign': sun_sign,
        'stt': stt,
        'tts': tts,
        'hotword_detection': hotword_detection,
        'telegram_username': telegram_username,
        'telegram_token': telegram_token,
        'music_path': music_path,
        'images_path': images_path,
        'city_name': city_name,
        'city_code': city_code,
        'degrees': degrees,
        'pocketsphinx': {
            'modeldir': modeldir,
            'hmm': hmm,
            'lm': lm,
            'dic': dic
        },
        'twitter': {
            'access_token': access_token,
            'access_token_secret': access_token_secret,
            'consumer_key': consumer_key,
            'consumer_secret': consumer_secret
        },
        'imgur': {
            'client_id': client_id,
            'client_secret': client_secret
        },
        'ivona': {
            'access_key': access_key,
            'secret_key': secret_key
        },
        'gmail': {
            'address': gmail_address,
            'password': gmail_password
        },
        'icloud': {
            'username': icloud_username,
            'password': icloud_password
        },
        'modules': modules,
        'actions_db_file': actions_db_file,
        'memory_db': memory_db
    }

    with open('profile.json', 'w') as outfile:
        json.dump(profile_data, outfile, indent=4)
