import math
from datetime import datetime
arm_length = 1.5
target_angle_deg = 30.0
start = datetime.now()
target_angle_rad = math.radians(target_angle_deg)
y = arm_length*math.sin(target_angle_deg)
x = arm_length*math.cos(target_angle_deg)
duration = datetime.now() - start
print(f"x position: {x:.3f}")
print(f"y position: {y:.3f}")
print(f"Time to excute: {duration.total_seconds()}")