# Make sure requests module is installed
# In Ubuntu 19.10 'sudo pip install requests'

import requests
response = requests.get("http://www.google.com")
print(len(response.text))
print(response.content)