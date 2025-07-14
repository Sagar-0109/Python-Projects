while True:
    print("Welcome to Online Store")
    print("Select\n1 for Fashion\n2 for Electronics\n3 for Food")
    userinput1=int(input("Enter the Choice: "))
    if userinput1 <= 0 or userinput1 >3:
        print("Enter a valid input")  
    if userinput1==1:
        print("You have selected Fashion")
        print("Select\n1 for Men\n2 for Women")
        userinput2=int(input("Enter the number: "))
        if userinput2 <= 0 or userinput2 >2:
                print("Enter a valid input") 

        if userinput2==1:
            print("You have Selected Men Fashion")
            print("Select\n1 for Shirts\n2 for trousers")
            userinput3=int(input("Enter the number: "))
            if userinput3 <= 0 or userinput3 >2:
                print("Enter a valid input")
            if userinput3==1:
                print("You have Selected Shirts")
                print("Select\n1 for Size S\n2 for Size M\n3 for Size L")
                userinput4=int(input("Enter the number: "))
                if userinput4 <= 0 or userinput4 >3:
                    print("Enter a valid input")
                if userinput4 == 1:
                    print("You have Selected Size S shirt")
                elif userinput4 == 2:
                    print("You have Selected Size M shirt")
                elif userinput4 == 3:
                    print("You have Selected Size L shirt")
                print("Shirt Purchased")

            elif userinput3==2:
                print("You have Selected Trousers")
                print("Select\n1 for Size 30\n2 for Size 34\n3 for Size 38")
                userinput5=int(input("Enter the number: "))
                if userinput5 <= 0 or userinput5 >3:
                    print("Enter a valid input")
                if userinput5 == 1:
                    print("You have Selected Size 30 trouser")
                elif userinput5 == 2:
                    print("You have Selected Size 34 trouser")
                elif userinput5 == 3:
                    print("You have Selected Size 38 trouser")
                print("Trouser Purchased")
        
        if userinput2==2:
            print("You have Selected Women Fashion")
            print("Select\n1 for Tops\n2 for Geans")
            userinput6=int(input("Enter the number: "))
            if userinput6 <= 0 or userinput6 >2:
                print("Enter a valid input")
            if userinput6==1:
                print("You have Selected Tops")
                print("Select\n1 for Size S\n2 for Size M\n3 for Size L")
                userinput7=int(input("Enter the number: "))
                if userinput7 <= 0 or userinput7 >3:
                    print("Enter a valid input")
                elif userinput7 == 1:
                    print("You have Selected Size S Top")
                elif userinput7 == 2:
                    print("You have Selected Size M Top")
                elif userinput7 == 3:
                    print("You have Selected Size L Top")
                print("Top Purchased")

            elif userinput6==2:
                print("You have Selected Trousers")
                print("Select\n1 for Size 30\n2 for Size 34\n3 for Size 38")
                userinput8=int(input("Enter the number: "))
                if userinput8 <= 0 or userinput8 >2:
                    print("Enter a valid input")
                if userinput8 == 1:
                    print("You have Selected Size 30 trouser")
                elif userinput8 == 2:
                    print("You have Selected Size 34 trouser")
                elif userinput8 == 3:
                    print("You have Selected Size 38 trouser")
                print("Trouser Purchased")

    if userinput1==2:
        print("You have selected Electronics")
        print("Select\n1 for Mobiles\n2 for Laptops")
        userinput9=int(input("Enter the number: "))
        if userinput1 <= 0 or userinput1 >2:
            print("Enter a valid input")

        if userinput9==1:
            print("You have Selected Mobiles")
            print("Select\n1 for Samsung\n2 for Oneplus\n3 for Nokia")
            userinput10=int(input("Enter the number: "))
            if userinput10 <= 0 or userinput10 >3:
                print("Enter a valid input")
            if userinput10==1:
                print("You have Selected Samsung")
                print("Select\n1 for 4GB Ram\n2 for 8GB Ram\n3 for 16GB Ram")
                userinput11=int(input("Enter the number: "))
                if userinput11 <= 0 or userinput11 >3:
                    print("Enter a valid input")
                print("Select\n1 for 64GB Storage\n2 for 128GB Storage\n3 for 256GB Storage")
                userinput12=int(input("Enter the number: "))
                if userinput12 <= 0 or userinput12 >3:
                    print("Enter a valid input")
                elif userinput11 == 1 and userinput12 == 1:
                    print("You have Selected 4GB Ram and 64GB Storage")
                elif userinput11 == 1 and userinput12 == 2:
                    print("You have Selected 4GB Ram and 128GB Storage")
                elif userinput11 == 1 and userinput12 == 3:
                    print("You have Selected 4GB Ram and 256GB Storage")
                elif userinput11 == 2 and userinput12 == 1:
                    print("You have Selected 6GB Ram and 64GB Storage")
                elif userinput11 == 2 and userinput12 == 2:
                    print("You have Selected 8GB Ram and 128GB Storage")
                elif userinput11 == 2 and userinput12 == 3:
                    print("You have Selected 16GB Ram and 256GB Storage")
                elif userinput11 == 3 and userinput12 == 1:
                    print("You have Selected 16GB Ram and 64GB Storage")
                elif userinput11 == 3 and userinput12 == 2:
                    print("You have Selected 16GB Ram and 256GB Storage")
                elif userinput11 == 3 and userinput12 == 3:
                    print("You have Selected 16GB Ram and 256GB Storage")
                print("You have Purchased Samsung Mobile")
            
            if userinput10==2:
                print("You have Selected Oneplus Mobiles")
                print("Select\n1 for 4GB Ram\n2 for 8GB Ram\n3 for 16GB Ram")
                userinput13=int(input("Enter the number: "))
                if userinput13 <= 0 or userinput13 >3:
                    print("Enter a valid input")
                print("Select\n1 for 64GB Storage\n2 for 128GB Storage\n3 for 256GB Storage")
                userinput14=int(input("Enter the number: "))
                if userinput14 <= 0 or userinput14 >3:
                    print("Enter a valid input")
                elif userinput13 == 1 and userinput14 == 1:
                    print("You have Selected 4GB Ram and 64GB Storage")
                elif userinput13 == 1 and userinput14 == 2:
                    print("You have Selected 4GB Ram and 128GB Storage")
                elif userinput13 == 1 and userinput14 == 3:
                    print("You have Selected 4GB Ram and 256GB Storage")
                elif userinput13 == 2 and userinput14 == 1:
                    print("You have Selected 6GB Ram and 64GB Storage")
                elif userinput13 == 2 and userinput14 == 2:
                    print("You have Selected 8GB Ram and 128GB Storage")
                elif userinput13 == 2 and userinput14 == 3:
                    print("You have Selected 16GB Ram and 256GB Storage")
                elif userinput13 == 3 and userinput14 == 1:
                    print("You have Selected 16GB Ram and 64GB Storage")
                elif userinput13 == 3 and userinput14 == 2:
                    print("You have Selected 16GB Ram and 256GB Storage")
                elif userinput13 == 3 and userinput14 == 3:
                    print("You have Selected 16GB Ram and 256GB Storage")
                print("Oneplus Mobile Purchased")
            
            if userinput10==3:
                print("You have Selected Nokia Mobiles")
                print("Select\n1 for 4GB Ram\n2 for 8GB Ram\n3 for 16GB Ram")
                userinput15=int(input("Enter the number: "))
                if userinput15 <= 0 or userinput15 >3:
                    print("Enter a valid input")
                print("Select\n1 for 64GB Storage\n2 for 128GB Storage\n3 for 256GB Storage")
                userinput16=int(input("Enter the number: "))
                if userinput16 <= 0 or userinput16 >3:
                    print("Enter a valid input")
                elif userinput15 == 1 and userinput16 == 1:
                    print("You have Selected 4GB Ram and 64GB Storage ")
                elif userinput15 == 1 and userinput16 == 2:
                    print("You have Selected 4GB Ram and 128GB Storage ")
                elif userinput15 == 1 and userinput16 == 3:
                    print("You have Selected 4GB Ram and 256GB Storage")
                elif userinput15 == 2 and userinput16 == 1:
                    print("You have Selected 6GB Ram and 64GB Storage ")
                elif userinput15 == 2 and userinput16 == 2:
                    print("You have Selected 8GB Ram and 128GB Storage ")
                elif userinput15 == 2 and userinput16 == 3:
                    print("You have Selected 16GB Ram and 256GB Storage ")
                elif userinput15 == 3 and userinput16 == 1:
                    print("You have Selected 16GB Ram and 64GB Storage")
                elif userinput15 == 3 and userinput16 == 2:
                    print("You have Selected 16GB Ram and 256GB Storage")
                elif userinput15 == 3 and userinput16 == 3:
                    print("You have Selected 16GB Ram and 256GB Storage")
                print("Nokia Mobile Purchased")

        if userinput9==2:
            print("You have Selected Laptops")
            print("Select\n1 for Samsung\n2 for Dell\n3 for MacBook")
            userinput17=int(input("Enter the number: "))
            if userinput17 <= 0 or userinput17 >3:
                print("Enter a valid input")
            if userinput17==1:
                print("You have Selected Samsung Laptops")
                print("Select\n1 for 4GB Ram\n2 for 8GB Ram\n3 for 16GB Ram")
                userinput18=int(input("Enter the number: "))
                if userinput18 <= 0 or userinput18 >3:
                    print("Enter a valid input")
                print("Select\n1 for 64GB Storage\n2 for 128GB Storage\n3 for 256GB Storage")
                userinput19=int(input("Enter the number: "))
                if userinput19 <= 0 or userinput19 >3:
                    print("Enter a valid input")
                print("Select the Processor\n1 for Intel i3 Core\n2 for Intel i5 Core\n3 for Intel i8 Core")
                userinput20=int(input("Enter the number: "))
                if userinput20 <= 0 or userinput20 >3:
                    print("Enter a valid input")
                elif userinput18 == 1 and userinput19 == 1 and userinput20 == 1:
                    print("You have Selected 4GB Ram and 64GB Storage and Intel i3 Core Processor ")
                elif userinput18 == 1 and userinput19 == 2 and userinput20 == 1:
                    print("You have Selected 4GB Ram and 128GB Storage and Intel i3 Core Processor ")
                elif userinput18 == 1 and userinput19 == 3 and userinput20 == 1:
                    print("You have Selected 4GB Ram and 256GB Storage and Intel i3 Core Processor ")
                elif userinput18 == 2 and userinput19 == 1 and userinput20 == 2:
                    print("You have Selected 6GB Ram and 64GB Storage and Intel i5 Core Processor ")
                elif userinput11 == 2 and userinput19 == 2 and userinput20 == 2:
                    print("You have Selected 8GB Ram and 128GB Storage and Intel i5 Core Processor ")
                elif userinput18 == 2 and userinput19 == 3 and userinput20 == 2:
                    print("You have Selected 16GB Ram and 256GB Storage and Intel i5 Core Processor ")
                elif userinput18 == 3 and userinput19 == 1 and userinput20 == 3:
                    print("You have Selected 16GB Ram and 64GB Storage and Intel i8 Core Processor ")
                elif userinput18 == 3 and userinput19 == 2 and userinput20 == 3:
                    print("You have Selected 16GB Ram and 256GB Storage and Intel i8 Core Processor ")
                elif userinput18 == 3 and userinput19 == 3 and userinput20 == 3:
                    print("You have Selected 16GB Ram and 256GB Storage and Intel i8 core processor")
                print("Samsung laptop Purchased")
            
            if userinput17==2:
                print("You have Selected Dell Laptops")
                print("Select\n1 for 4GB Ram\n2 for 8GB Ram\n3 for 16GB Ram")
                userinput21=int(input("Enter the number: "))
                if userinput21 <= 0 or userinput21 >3:
                    print("Enter a valid input")
                print("Select\n1 for 64GB Storage\n2 for 128GB Storage\n3 for 256GB Storage")
                userinput22=int(input("Enter the number: "))
                if userinput22 <= 0 or userinput22 >3:
                    print("Enter a valid input")
                print("Select the Processor\n1 for Intel i3 Core\n2 for Intel i5 Core\n3 for Intel i8 Core")
                userinput23=int(input("Enter the number: "))
                if userinput23 <= 0 or userinput23 >3:
                    print("Enter a valid input")
                elif userinput21 == 1 and userinput22 == 1 and userinput23 == 1:
                    print("You have Selected 4GB Ram and 64GB Storage and Intel i3 Core Processor ")
                elif userinput21 == 1 and userinput22 == 2 and userinput23 == 1:
                    print("You have Selected 4GB Ram and 128GB Storage and Intel i3 Core Processor ")
                elif userinput21 == 1 and userinput22 == 3 and userinput23 == 1:
                    print("You have Selected 4GB Ram and 256GB Storage and Intel i3 Core Processor ")
                elif userinput21 == 2 and userinput22 == 1 and userinput23 == 2:
                    print("You have Selected 6GB Ram and 64GB Storage and Intel i5 Core Processor ")
                elif userinput21 == 2 and userinput22 == 2 and userinput23 == 2:
                    print("You have Selected 8GB Ram and 128GB Storage and Intel i5 Core Processor ")
                elif userinput21 == 2 and userinput22 == 3 and userinput23 == 2:
                    print("You have Selected 16GB Ram and 256GB Storage and Intel i5 Core Processor ")
                elif userinput21 == 3 and userinput22 == 1 and userinput23 == 3:
                    print("You have Selected 16GB Ram and 64GB Storage and Intel i8 Core Processor ")
                elif userinput21 == 3 and userinput22 == 2 and userinput23 == 3:
                    print("You have Selected 16GB Ram and 256GB Storage and Intel i8 Core Processor ")
                elif userinput21 == 3 and userinput22 == 3 and userinput23 == 3:
                    print("You have Selected 16GB Ram and 256GB Storage and Intel i8 core processor")
                print("Dell laptop Purchased")
            
            if userinput17==3:
                print("You have Selected MacBook  Laptops")
                print("Select\n1 for 4GB Ram\n2 for 8GB Ram\n3 for 16GB Ram")
                userinput24=int(input("Enter the number: "))
                if userinput24 <= 0 or userinput24 >3:
                    print("Enter a valid input")
                print("Select\n1 for 64GB Storage\n2 for 128GB Storage\n3 for 256GB Storage")
                userinput25=int(input("Enter the number: "))
                if userinput25 <= 0 or userinput25 >3:
                    print("Enter a valid input")
                print("Select the Processor\n1 for Intel i3 Core\n2 for Intel i5 Core\n3 for Intel i8 Core")
                userinput26=int(input("Enter the number: "))
                if userinput26 <= 0 or userinput26 >3:
                    print("Enter a valid input")
                elif userinput24 == 1 and userinput25 == 1 and userinput26 == 1:
                    print("You have Selected 4GB Ram and 64GB Storage and Intel i3 Core Processor ")
                elif userinput24 == 1 and userinput25 == 2 and userinput26 == 1:
                    print("You have Selected 4GB Ram and 128GB Storage and Intel i3 Core Processor ")
                elif userinput24 == 1 and userinput25 == 3 and userinput26 == 1:
                    print("You have Selected 4GB Ram and 256GB Storage and Intel i3 Core Processor ")
                elif userinput24 == 2 and userinput25 == 1 and userinput26 == 2:
                    print("You have Selected 6GB Ram and 64GB Storage and Intel i5 Core Processor ")
                elif userinput24 == 2 and userinput25 == 2 and userinput26 == 2:
                    print("You have Selected 8GB Ram and 128GB Storage and Intel i5 Core Processor ")
                elif userinput24 == 2 and userinput25 == 3 and userinput26 == 2:
                    print("You have Selected 16GB Ram and 256GB Storage and Intel i5 Core Processor ")
                elif userinput24 == 3 and userinput25 == 1 and userinput26 == 3:
                    print("You have Selected 16GB Ram and 64GB Storage and Intel i8 Core Processor ")
                elif userinput24 == 3 and userinput25 == 2 and userinput26 == 3:
                    print("You have Selected 16GB Ram and 256GB Storage and Intel i8 Core Processor ")
                elif userinput24 == 3 and userinput25 == 3 and userinput26 == 3:
                    print("You have Selected 16GB Ram and 256GB Storage and Intel i8 core processor")
                print("Dell laptop Purchased")

    if userinput1==3:
        print("You have selected Food")
        print("Select\n1 for Pizza\n2 for Burger")
        userinput27=int(input("Enter the number: "))
        if userinput27 <= 0 or userinput27 >2:
                print("Enter a valid input") 
        if userinput27==1:
                print("You have Selected Pizzas")
                print("Select\n1 for Veg Pizza\n2 for Non-veg pizza\n3 for Baby Corn Pizza")
                userinput28=int(input("Enter the number: "))
                if userinput28 <= 0 or userinput28 >3:
                    print("Enter a valid input")
                elif userinput28 == 1:
                    print("You have Selected Veg Pizza")
                elif userinput28 == 2:
                    print("You have Selected Non-veg Pizza")
                elif userinput28 == 3:
                    print("You have Selected Baby Corn Pizza")
                print("Pizza Purchased")

        elif userinput27==2:
            print("You have Selected Burgers")
            print("Select\n1 for Veg Burger\n2 for Non-Veg Burger\n3 for Special Burger(Non veg)")
            userinput28=int(input("Enter the number: "))
            if userinput28 <= 0 or userinput28 >3:
                print("Enter a valid input")
            if userinput28 == 1:
                print("You have Selected Veg Burger")
            elif userinput28 == 2:
                print("You have Selected Non Burger")
            elif userinput28 == 3:
                print("You have Selected Special Burger(Non-veg)")
            print("Burger Purchased")
    print("Select\n1 for Shop More\n2 for Exit")
    userinput29=int(input("Enter Your Choice:"))
    if userinput29 <= 0 or userinput29 >2:
        print("Enter a valid input")
    if userinput29 == 2:
        print("Thanks for Visiting!")
        break
