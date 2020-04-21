
first_name = input ( "What is your First Name?")
second_name = input ( "What is your Second Name?")
full_name=first_name + " " + second_name

a = int(len ( full_name))
b=round(a/2)
def remove_space(string):
    return string.replace(" ","")
split=list(full_name)


print ("Your name is ",full_name)
print ("Your name in reverse is ",full_name[::-1])
print ("First half of name is ",full_name[:b],"Last half of name is ",full_name[b:])
print ("After removing spaces name is",remove_space(full_name))
print ("characters used are",split)
print ("Full name after putting & after every letter","&".join(split))

import random
random.shuffle(split)
print("After mixing letters name is","".join(split))