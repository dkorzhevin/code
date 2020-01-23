# Make sure arrow module is installed
# In Ubuntu 19.10 'sudo pip3.8 install arrow'

import arrow
date = arrow.get('2020-01-23', 'YYYY-MM-DD')
print(date.shift(weeks=+4).format('MMM DD YYYY'))