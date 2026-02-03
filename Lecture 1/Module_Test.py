def average(array: list[float]) -> float:
    if not array:
        return 0
    else:
        return sum(array)/len(array)

