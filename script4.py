def greet_traveler(name, destination):
 # greeting = "Hello ", name,"enjoy your trip to", destination
 return f"Hello {name},enjoy your trip to, {destination}"
print(greet_traveler("Arjun", "Delhi"))
print(greet_traveler("Delhi", "Sam"))
print(greet_traveler("Toronto", ""))

def square_of_number(num):
 return num*num
print(square_of_number(5))

def palindrome(str):
 return  str == str[::-1]
print(palindrome("malayalam"))

def process_data