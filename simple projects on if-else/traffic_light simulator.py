traffic_light=input("Enter the traffic light colour(red/yellow/green): ").lower()
if traffic_light=="red":
    print("STOP!")
elif traffic_light=="yellow":
    print("GET READY!")
elif traffic_light=="green":
    print("GO!")
else:
    print("invalid!please enter the correct one")