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

#connect with github api 
USER='AUSER'
API_TOKEN='ATOKEN'
GIT_API_URL='https://api.github.com'

def get_api(url):
    try:
        request = urllib2.Request(GIT_API_URL + url)
        base64string = base64.encodestring('%s/token:%s' % (USER, API_TOKEN)).replace('\n', '')
        request.add_header("Authorization", "Basic %s" % base64string)
        result = urllib2.urlopen(request)
        result.close()
    except:
        print 'Failed to get api request from %s' % url


#commands return github repos
#The following curl command to list the repositories:
GHUSER=CHANGEME; curl "https://api.github.com/users/$GHUSER/repos?per_page=100" | grep -o 'git@[^"]*'

#List cloned URLs, run:
GHUSER=CHANGEME; curl -s "https://api.github.com/users/$GHUSER/repos?per_page=1000" | grep -w clone_url | grep -o '[^"]\+://.\+.git'

#If it's private, you need to add your API key (access_token=GITHUB_API_TOKEN), for example:
curl "https://api.github.com/users/$GHUSER/repos?access_token=$GITHUB_API_TOKEN" | grep -w clone_url