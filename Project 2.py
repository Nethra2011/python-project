#Trafic Light Simulator
trafficlight = input("Enter the color")
trafficlight = trafficlight.lower()
if trafficlight == "red":
     print("stop")
elif trafficlight == "yellow":
    print("get ready")
elif trafficlight == "green":
    print("go")
else :
    print("chose red,green or yellow")

