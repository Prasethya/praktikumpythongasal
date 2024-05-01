import subprocess
from pyfiglet import Figlet
import colorama

colorama.init()
f = Figlet(font='big')
print(colorama.Fore.GREEN + f.renderText('Tiyanmoe'))

profiles = subprocess.check_output(['netsh', 'wlan' ,'show', 'profiles']).decode('utf-8',errors="backslasherplace").split('\n')[1:]

profile_names = [i.split(':')[2][1:-1]for i in profiles if "All User Profile" in i]
print("{:<30}| {:<}".format("Wi-Fi Name", "Password"))
print("-----------------------------------------------")
for name in profile_names:
    try:
        results = subprocess.check_output(['netsh', 'waln', 'show', 'profile', name, 'key-clear']).decode('utf-8', errors="backslasherplace").split('\n')[1:]

        print("{:<30}| {:<}".format(name, ))

    except:
        print("{:<30}| {:<}".format(name, "not found"))
