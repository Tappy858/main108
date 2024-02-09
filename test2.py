def students():
    names = ["Dave", "Jazper",  "Andy", "Corey", "Samuel", "Cesar", "Darius",  "Demetri", "Janaye", "Donald", "Marco"]

    print(names)

    #add elements
    names.append("Darius")

    #travel the list
    for name in names:
        print(name)

    #A) how many names are there?
        print (len(names))


def products():
    prices = [23,35,56,85,420,500,600,675,700,30,200,4,234,43,565,69]

    #A) print every price
    #B sum of all prices
    #c hpw many prices are lower than 500
    #d) how many are greater or equal to 500 

    total = 0
    count = 0
    expensive = 0

    for price in prices:
        print(price)
        #total= total + price
        total += price

        if price < 500:
            #count = count + 1
            count += 1
        
        if price >= 500:
            expensive += 1

    print(total)
    print(count)
    print(expensive)


def art():
    colors = ["red", "blue", "pink", "blue", "white", "blak", "green", "blak", "red", "white", "blue", "yellow"]

    #a) how many colors are ther in  the list 
    print(len(colors))

    #b how many are blue


    #c) how many are white and black
    blue = 0
    black_white = 0

    for color in colors:
        if color == "blue":
            blue += 1

        if color == "white" or color == "black":
            black_white += 1

    print("blues " + str(blue))
    print("whites or blacks " + str(black_white))

#calls
#students()
#products()
art()