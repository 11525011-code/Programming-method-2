dist = 0.8
emergency_stop = False
safety_mode = ""
if emergency_stop == True:
    safety_mode = "ESTOP"
elif dist < 0.5:
    safety_mode = "COLLISION"
elif 0.5 < dist < 1.5:
    safety_mode = "WARNING"
else:
    safety_mode = "NORMAL"