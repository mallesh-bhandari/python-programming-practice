def Sum_Of_Digits(Number):
    # Copy original number to print it at the end
    Temp = Number
    Sum = 0
    
    # Loop runs until the number becomes 0
    while Number > 0:
        # Get the last digit of the number
        Digit = Number % 10
        
        # Add the digit to the total sum
        Sum = Sum + Digit 
        
        # Remove the last digit from the number
        Number = Number // 10
        
    print(f"Sum OF Digit {Temp} is = {Sum} ")
        
# Get number from the user
Value = int(input("Enter Any Number: "))

# Run the function
Sum_Of_Digits(Value)