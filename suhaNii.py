












import os, platform

try:

    import requests

except:

    os.system('xdg-open https://youtube.com/channel/UCbT--Z1XzQpSUgjD6bfzzUA')

import requests

bit = platform.architecture()[0]

if bit == '64bit':

    from SUHANII import ud

    ud()

elif bit == '32bit':

    from SUHANII32 import ud

    ud()

else:

    print('\n YOUR DEVICE IS NOT SUPPORT THIS COMMAND')

    os.system('exit')
