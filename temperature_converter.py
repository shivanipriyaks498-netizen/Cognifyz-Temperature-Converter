
print("===================================")
print("       TEMPERATURE CONVERTER")
print("===================================")

print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")

choice = input("Choose conversion (1 or 2): ")

temperature = float(input("Enter temperature: "))

if choice == "1":
    fahrenheit = (temperature * 9/5) + 32
    print("Temperature in Fahrenheit:", round(fahrenheit, 2), "°F")

elif choice == "2":
    celsius = (temperature - 32) * 5/9
    print("Temperature in Celsius:", round(celsius, 2), "°C")

else:
    print("Invalid choice! Please select 1 or 2.")

print("Thank you for using Temperature Converter!")

