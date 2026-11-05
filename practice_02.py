def liters_per_trip(liters, trips):
    if trips == 0:
        return "На ноль делить нельзя"
    return liters / trips

assert liters_per_trip(24, 3) == 8.0
assert liters_per_trip(10, 0) == "На ноль делить нельзя"
assert liters_per_trip(75, 5) == 15.0

words = ["дом", "улица", "общежитие"]
by_length = sorted(words, key=lambda word: len(word))
print(by_length)