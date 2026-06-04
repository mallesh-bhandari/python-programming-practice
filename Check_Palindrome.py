def Check_Palindrome(Number):
# put original value in temp variable    
    temp = Number
    reverse = 0
    
    while Number> 0:
        digit = Number % 10 
        reverse =(reverse*10) + digit
        Number = Number // 10
# use conditional statement         
    if temp == reverse:
       print("This Is Palindrome Number")   
    
    else:
        print("This Is Not Palindrome")         

# user input        
Number =int(input("Enter Any Number: "))
# function call
Check_Palindrome(Number)            