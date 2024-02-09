def about_me():
    me = {
        "first": "Darius",
        "last": "Ruckus",
        "age": 32,
        "address": {
            "street": "Grape",
            "number": "321",
            "city": "Los Santos",
            "zip": "12321"
        }
    }
    print(me)

    #read values
    print(me["first"] + " " + me["last"])
    print("I'm " + str(me["age"]) + " years old!")
    # using f-string
    print(f"I'm {me['age']} years old!")

    # print address details
    print(me["address"]["street"])

    address = me["address"]
    street = address["street"]
    num = address["number"]
    city = address["city"]
    zip = address["zip"]
    print(street)

    print(f"addy: {street} #{num}, {city}, {zip}.")
    
    address = me["address"]
    print(f"Address: {address['street']} #{address['number']}, {address['city']} {address['zip']}.")

    


# Function call
about_me()
