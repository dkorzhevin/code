# sudo pip3.8 install pandas

import pandas

# Ammount of visitor during last 5 days

visitors = [ 232, 235, 564, 146, 543 ]

# Ammount of errors during last 5 days

errors = [ 12, 42, 22, 1, 23 ]

df = pandas.DataFrame( {"visitors": visitors, "errors": errors}, index=["Mon", "Tue", "Wed", "Thu", "Fri"])
print(df)

df["errors"].mean()