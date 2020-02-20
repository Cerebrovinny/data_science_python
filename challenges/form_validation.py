name_form = input('Enter your name ' )
if len(name_form) <=2:
    print('name must be at least 3 characters')
elif len(name_form) >=51:
    print('name can be maximum of 50 characters')
else:
    print('name looks good!')