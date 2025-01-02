hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

# Write your code here.
dura_min = dura % 60
print("Duration in minutes: ",dura_min)
dura_hour = (dura - dura_min) // 60
print("Duration in hours: ", dura_hour)

end_min = (mins + dura_min) % 60
print("End Time minutes:",end_min)
end_hour = (hour + dura_hour) % 24
end_hour += ((mins % 60) + dura_min) // 60
print("End Time Hours: ",end_hour)

print(f"End Time: {end_hour}:{end_min}")