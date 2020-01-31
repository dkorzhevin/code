def find_item(list, item):
  #Returns True if the item is in the list, False if not.
  if len(list) == 0:
    return False
  #print(len(list))

  #Is the item in the center of the list?
  middle = len(list)//2
  if list[middle] == item:
    return True
  
  #print(middle)

  #Is the item in the first half of the list? 
  if item < list[middle]:
    #Call the function with the first half of the list
    return find_item(list[:middle], item)
  else:
    #Call the function with the second half of the list
    return find_item(list[middle+1:], item)

  return False

list_of_names = sorted(["Parker", "Drew", "Cameron", "Logan", "Alex", "Chris", "Terry", "Jamie", "Jordan", "Taylor"])

print(find_item(list_of_names, "Alex")) # True
print(find_item(list_of_names, "Andrew")) # False
print(find_item(list_of_names, "Drew")) # True
print(find_item(list_of_names, "Jared")) # False