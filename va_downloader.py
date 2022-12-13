from pytube import YouTube
import os


def video_downloader(xpath_def, xlist_def):
    for url in xlist_def:
        print('\nLoading....')
        vid = YouTube(url)

        video = vid.streams.filter().get_highest_resolution()

        if xpath_def != 'n':
            destination = xpath_def
        else:
            destination = os.getcwd()

        out_file = video.download(output_path=destination)

        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp4'
        os.rename(out_file, new_file)

        print(f'\n{vid.title}')
        print('\nhas been downloaded.')


def audio_downloader(xpath_def, xlist_def):
    for url in xlist_def:
        print('\nLoading....')
        aud = YouTube(url)

        audio = aud.streams.filter(only_audio=True).first()

        if xpath_def != 'n':
            destination = xpath_def
        else:
            destination = os.getcwd()

        out_file = audio.download(output_path=destination)

        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)

        print(f'\n{aud.title}')
        print('\nhas been downloaded.')

# URLS list
xlist = []

print(
'''

                DD
                DD
                DD
                DD
                DDDDDDDDDDDDDDDDDD
                DD              DD
                DD          DD  DD  DD
                DD           DD DD DD
                DD            DDDDDD
                DD              DD
                DD
                DD

'''
)

print('\n       1. Video Downloud')
print('\n       2. Audio Downloud')
xtypeoption = input('\nEnter a Option: ')

while True:
    try:
        xtypeoption = int(xtypeoption)
        if xtypeoption == 1 or xtypeoption == 2:
            break
        else:
            xtypeoption = input('\n  Please Enter Option 1 or 2: ')
    except:
        print('\nPlease Enter a Number!')
        print('\n1. Video Downloud')
        print('\n2. Audio Downloud')
        xtypeoption = input('\nEnter a Option: ')


print(
'''

                FFFFFFFFFFFFFFFFFFFFFFF
                FF                    FF
                FF                     FFFFFFFFFFF
                FF                              FF
                FF           FOLDER             FF
                FF                              FF
                FF                              FF
                FF                              FF
                FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF
            
'''
)

print(f'\nDownload location is "{os.getcwd()}"')
print('\nDo you want to change it? ( for Yes > y and for No > n )')
xpath = input('\n=> ')
while True:
    try:
        xpath = str(xpath)
        if xpath == 'y':
            xpath = input('\nEnter the Path => ')
            break
        elif xpath == 'n':
            break
        else:
            xpath = input('\nPlease Enter Option y or n: ')
    except:
        print(f'\nDownload location is "{os.getcwd()}"')
        print('\nDo you want to change it? ( for Yes > y and for No > n )')
        print('\nPlease type one of the following options')
        xpath = input('\n => ')


print(
'''

                LL            LL   LLLL       LL   LL    LL
                LL            LL   LL LL      LL   LL   LL
                LL            LL   LL  LL     LL   LL  LL
                LL            LL   LL   LL    LL   LL LL
                LL            LL   LL    LL   LL   LLLL
                LL            LL   LL     LL  LL   LL LL
                LL            LL   LL      LL LL   LL  LL
                LL            LL   LL       LLLL   LL   LL
                LLLLLLLLLLL   LL   LL        LLL   LL    LL
            
'''
)

print('\nIf you are done, leave the field blank, then press Enter')
xurl = input('\nURLS => ')

while True:
    try:
        xurl = str(xurl)
        if xurl != '':
            xlist.append(xurl)
            xurl = input('\nURLS => ')
        else:
            break
    except:
        print('\nIf you are done, leave the field blank, then press Enter')
        xurl = input('\nURLS => ')


if xtypeoption == 1:
    video_downloader(xpath, xlist)
elif xtypeoption == 2:
    audio_downloader(xpath, xlist)
else:
    print('You have a Problem')































