'''
I wake up
If I am hungry:
    Then I'll have breakfast.
'''

is_male = True
is_tall = True

if is_male and is_tall:
    print("You are a male and tall.")
elif is_male and not(is_tall):
    print("You are a short male.")
elif not(is_male) and is_tall:
    print("You are not a male but are tall.")
else:
    print("You are not a male nor tall")

