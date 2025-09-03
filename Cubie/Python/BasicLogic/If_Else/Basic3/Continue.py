def multiples():
    for i in range(1,50):
        if i % 3 == 0 and i % 5 == 0:
            print(f"{i} KidoCode")
        elif i % 3 == 0:
            print (f"{i} Kido")
        elif i % 5 == 0:
            print(f"{i} Code")
        else:
            continue
        
multiples()
        