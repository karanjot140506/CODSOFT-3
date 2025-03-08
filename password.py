import random
import string

def password(length,uppercase,lowercase,digit,special_char):
    characters_set = ""
    if uppercase:
        characters_set += string.ascii_uppercase
    if lowercase:
        characters_set += string.ascii_lowercase
    if digit:
        characters_set += string.digits
    if special_char:
        characters_set += string.punctuation
         
    if characters_set =="":
        print("Select atleast one character type.")
        return None
    
    password=''
    for i in range(length):
        password=password+random.choice(characters_set)
    return password
   
def main():
  try:
    length=int(input("Enter the length of password: "))
    uppercase=input("1.uppercase letter? (y/n):").lower()=='y'  
    lowercase=input("2.lowercase letter? (y/n):").lower()=='y'
    digits=input("3.digits? (y/n):").lower()=='y'
    special_char=input("4.special_char? (y/n):").lower()=='y'
    
    gen_pass = password(length,uppercase,lowercase,digits,special_char)
    print("Generated Password:",gen_pass)
  except ValueError:
      print("Please Enter a valid integer for the length of the password:")
      
if __name__=="__main__": 
    main()       
    