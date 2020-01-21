def format_name(first_name, last_name):
	if len(first_name) and len(last_name) > 0:
	   format_name = "Name: " + last_name + ", " + first_name
	   
	elif len(first_name) == 0 and len(last_name) > 0:
	   format_name = "Name: " + last_name
	elif len(first_name) > 0 and len(last_name) == 0:
	   format_name = "Name: " + first_name
	else:
	   format_name = ""
	return format_name 

print(format_name("Ernest", "Hemingway"))
# Should be "Name: Hemingway, Ernest"

print(format_name("", "Madonna"))
# Should be "Name: Madonna"

print(format_name("Voltaire", ""))
# Should be "Name: Voltaire"

print(format_name("", ""))
# Should be ""