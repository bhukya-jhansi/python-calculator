
print("Unit Converter")
print("1. Kilometers to Miles")
print("2. Miles to Kilometers")
print("3. Kilograms to Grams")
print("4. Meters to Kilometers")

choice = input("Enter your choice (1-4): ")
value = float(input("Enter value: "))

if choice == "1":
    print("Result:", value * 0.621371, "miles")
elif choice == "2":
    print("Result:", value * 1.60934, "kilometers")
elif choice == "3":
    print("Result:", value * 1000, "grams")
elif choice == "4":
    print("Result:", value / 1000, "kilometers")
else:
    print("Invalid choice")
  
