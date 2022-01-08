import os
print(os.getcwd())
# os.chdir("./sets")
os.getcwd()
print(os.getcwd())
os.system('ls -l')
os.system('ls -a')
os.system("echo Hello from the other side! >> tex")

a = []
b = []
a.append('[diego]')
b.append(str(os.system(''' GHUSER=diegodila; curl https://api.github.com/users/$GHUSER/repos?per_page=100 | grep -o 'git@[^"]*' ''')))
print(len(b))

#Calling multiple commands using os.system in Python
os.system(" ls -l; <some command>; launchMyApp")
os.system('''
ls -l
<some command>
launchMyApp
''')