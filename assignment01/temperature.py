

temperature = float(input("Enter Temperature in celcius:"))

if temperature < 15:
    print(f"Temperature: {temperature:.2f}C -> Cold")
    
elif 15 <= temperature <=30: 
    print(f"Temperature: {temperature:.2f}C -> Warm")
    
else:
    print(f"Temperature: {temperature:.2f}C -> Hot") 
    