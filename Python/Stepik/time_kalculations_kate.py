kate_time = int(input("Total minutes: "))
kate_hours = int(input("Hours : "))
kate_minutes = int(input("Minutes: "))

kate_time_minutes_total = int(((kate_hours*60)+kate_time+kate_minutes))

print("Alarm should be set on:", int(kate_time_minutes_total/60), "hours")
print("And", int(kate_time_minutes_total % 60), "minutes")