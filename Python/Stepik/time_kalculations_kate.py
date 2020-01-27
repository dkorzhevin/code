# put your python code here
kate_time = int(input())
kate_hours = int(input())
kate_minutes = int(input())

kate_time_minutes_total = int(((kate_hours*60)+kate_time+kate_minutes))

print(int(kate_time_minutes_total/60))
print(kate_time_minutes_total % 60)