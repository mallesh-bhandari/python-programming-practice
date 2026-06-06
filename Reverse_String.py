def Reverse_String(Word):
    Result = ""
# Store original data in a temporary variable   
    Temp = Word
    for char in Word:
        Result = char + Result
    print(f"Reverse Of {Temp} Is = {Result} ")
            
Word = input("Enter Any Letters: ")
Reverse_String(Word)
        