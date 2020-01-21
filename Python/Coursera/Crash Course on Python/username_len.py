def hint_username(username):
    if len(username) < 6:
        print("Invalid username. Username must be at least 6 characters long")
    else:
        print("Username valid")

hint_username("dkorzhevin")