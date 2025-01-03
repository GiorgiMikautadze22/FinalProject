def liters_100km_to_miles_gallon(liters):
#
# Write your code here.
    km = 100
    one_litre_in_gallon = 3.785411784
    one_km_in_miles = 1.609344

    return (km * one_litre_in_gallon) / (liters * one_km_in_miles)

def miles_gallon_to_liters_100km(miles):
#
# Write your code here
    km = 100
    one_litre_in_gallon = 3.785411784
    one_km_in_miles = 1.609344

    return (km * one_litre_in_gallon) / (miles * one_km_in_miles)
#

print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))
