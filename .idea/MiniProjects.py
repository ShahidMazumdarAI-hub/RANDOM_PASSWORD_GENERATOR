#RANDOM PASSWORD GENERATOR, like often chrome suggests strong Passwords when we make account anywhere, so kuch aisaa hi..
#lets generate a 12 length character, this may be of any lngth, password can have elements from A-Z, a-z, 0-9 or punctuators like ! / \ ? etc etc
#we will also use STRING module here by importing it

import random
import string

haha = random.choice([1,2,4,"good"]) #this will give any element from the list as o/p, but the o/p will keep on updating, we will need this func too in generating p/w, inside the brackets there can be anything like list or strings, numbers etc etc
print(haha)

val = string.ascii_letters
print(val)
val2 = string.digits
print(val2)
val3 = string.punctuation #prints allll the special characters which we shall be needing in generating a password
print(val3)

#u got the idea of modules and funcs which will be used here, lets start the project now:
char_values = string.ascii_letters+string.digits+string.punctuation
print(char_values)
pass_len = 12

password = "" #we took an empty string, kyu liya samjhogey wait:..see line 26 , taki randomly jo bhi values hum le rahe hain from char_values using choice func, un sab values ko main add kartaa rahu string Password me , so isiliye pehle isi line me humne empty string(Password) liyaa
for i in range(pass_len):
    print(random.choice(char_values)) #randomly from char values of line 19, elements will be printed and choice will return one element randomly from char_values at a time upto 12 characters length
    password+=random.choice(char_values)

print("ur random password is:", password)

