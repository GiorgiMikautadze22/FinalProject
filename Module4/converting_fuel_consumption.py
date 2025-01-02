def liters_100km_to_miles_gallon(liters):
#
# Write your code here.
#
    one_km_litres = liters / 100
    mile_gallon = one_km_litres * 3.785411784

    return mile_gallon

def miles_gallon_to_liters_100km(miles):
#
# Write your code here
    meters = miles * 1609.344
    return meters
#

print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))
