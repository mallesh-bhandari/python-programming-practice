# Use Function 
def check_even_odd(value):
# Check if the number is perfectly divisible by 2
    if value % 2 == 0:
        print("This is an Even Number")
    else:
        print("This is an Odd Number")

# Take User Input through Keyboard
num = int(input("Enter The Number: "))

# Function Call
check_even_odd(num)                       


# Variable (Value ) % 2 == 0 -- This Is Formula to Find Even Number 
# Variable (Value) % 2 != 0 -- This Is Find Odd Number