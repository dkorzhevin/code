def convert_distance(miles):
  kilometers = miles * 1.6  # approximately 1.6 km in 1 mile
  return kilometers

distance = convert_distance(55)
round_trip = distance*2

print("The distance in kilometers is " + str(distance))
print("The round-trip in kilometers is " + str(round_trip))