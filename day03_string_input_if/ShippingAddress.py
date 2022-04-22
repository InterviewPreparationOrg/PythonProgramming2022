
full_name = input('Enter your full name: ')
building = input('Enter your building number: ')
street = input('Enter your street name: ')
city = input('Enter your city name: ')
state = input('Enter your state name: ')
zip_code = input('Enter your zip code: ')

print('\n\nYour shipping address is: ')
print(f'\t{full_name}')
print(f'\t{building} {street}')
print(f'\t{city}, {state} {zip_code}')


"""
1. Create a python file named ShippingAddress
            Ask the user to enter the following info, and display the shipping address of the user:
                    1. "Enter your full name"
                     2. "Enter your building number"
                     3. "Enter your street name"
                     4. "Enter your city name"
                     5. "Enter your state name"
                     6. "enter your zip code"

             Given data:
                name = "Aaron Kissinger"
                buildingNumber = 13621A
                streetName = "Legacy Circle"
                city = "Fairfax"
                state = "VA"
                zipCode = 22030

            Output:
                Your shipping addrrees is:
                        Aaron Kissinger
                        13621A Legacy Circle
                        Fairfax, VA 22030
"""
