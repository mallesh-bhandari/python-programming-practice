def Check_String_Palindrome(Letter):
# Use Slicing Operation Here To Reverse String    
    Data = Letter[::-1]
    if Data == Letter:
        print("String Is Palindrome")
    else:
        print("String Is Not Palindrome")
        
# User Input         
Letter = input("Enter Any Word / Letter: ")

# Function Call
Check_String_Palindrome(Letter)            