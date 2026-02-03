def Motor_Control(rpm: float, motor_id: int):
    if rpm > 1000:
        raise ValueError("Safety Limit Excess")

try:
    motor = Motor_Control(1001, 10)
except ValueError as err:
    print(err)

