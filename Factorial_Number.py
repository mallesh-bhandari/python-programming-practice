def Factorial_Number(Number):
#  Use Variable      
    Factorial = 1
# Use For loop     
    for i in range(1, Number +1):  
#  Factorial Logic               
        Factorial = Factorial * i
# Print final answer        
        print(Factorial)
      
# User input      
Value = int(input("Enter Any Number: "))   
# Function call     
Factorial_Number(Value)        