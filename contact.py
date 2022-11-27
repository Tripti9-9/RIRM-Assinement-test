import re
number = input("Enter your mobile number:")
pattern = re.compile("(0|91)?[-/s]?[0-2][0-9]{9}")
if pattern.match(number):
    print(f"{number}is Valid Number")  
          
else:
    print(f"{number} is Invalid Number")
