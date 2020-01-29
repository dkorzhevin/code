def validate_users(users):
  for user in users:
    if len(user) > 3:
      print(user + " is valid")
    else:
      print(user + " is invalid")

validate_users(['purplecat'])