dest = []

print("Please enter your 5 travel destinations: ")

for i in range(5):
    place = input(f"Destination {i+1}: ")
    dest.append(place)

print("\nOriginal Travel Itinerary:")
for i in range(5):
    print(f"{i+1}. {dest[i]}")

print("\nLet's update your 2nd and 5th destinations.")

new_second = input("Enter a new destination for position 2: ")
dest[1] = new_second

new_fifth = input("Enter a new destination for position 5: ")
dest[4] = new_fifth

print("\nUpdated Travel Itinerary:")
for i in range(5):
    print(f"{i+1}. {dest[i]}")
    