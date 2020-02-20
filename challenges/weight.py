weight_user = int(input('Please enter you weight ' ))
unit = input('(L)bs or (K)g: ')
if unit.upper() == "L":
    converted = weight_user * 0.45
    print(f"You are {converted} kilos")
else:
    converted = weight_user / 0.45
    print(f"You are {converted} pounds")