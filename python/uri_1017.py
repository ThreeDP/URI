car_km_l = 12
hours = int(input())
km = int(input())

spent = km / car_km_l * hours
print("{:.3f}".format(spent))
