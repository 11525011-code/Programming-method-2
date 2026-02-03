voltages = [12.6, 12.5, 12.2, 11.8, 11.5, 10.8, 10.2]
for index, vol in enumerate(voltages):
    print(f"Minue {index}: Remain {vol} voltage")

v=12
while v >= 10.5:
    print(v)
    v -= 0.5

print("Warning low Battery")

for x in voltages:
    if x < 12.0:
        continue
    if x > 11.0:
        break
    print(x)