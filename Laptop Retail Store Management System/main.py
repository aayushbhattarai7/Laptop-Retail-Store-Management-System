#import date and time
import datetime
#create a function called shopdet
def shopdet():
    print("-------------------------------------------------------------")
    print("         -------------------Laptop Zone---------------")
    print("------------------Welcome to laptop zone----------------------")
    
#call shopdet function 
shopdet()
#create a function called laptopdict
def laptopdict():
    #print the topic for show available laptops
    print("Available Laptops:")
    #Reading laptop.txt file for details of laptop
    with open("laptop.txt", "r") as file:
        #create a list called lapt
        lapt = []
        #initialize Serial number to 0 
        idx = 0
        for line in file:
            name, brand, price, stock, processor, gpu = line.strip().split(",")
            # Fixed the print statement by using the correct variable name
          
            print(f"{idx+1}. {name} {brand} , Price: ${price}, Stock: {stock}   {processor} {gpu}")
            idx += 1
            l = {"id": idx, "name": name, "brand": brand, "price": int(price.replace("$", "")), "stock": int(stock), "processor": processor, "gpu": gpu}
            # Append the laptop dictionary to the list
            lapt.append(l)
    
    return lapt

# Call the function and print the output
laptop_list = laptopdict()

#Ask user to buy or sell
y = input("Do you want to 'buy' or 'sell': ")

while True:
    try:
        if y == 'buy':
            Cname = input("Enter the company Name: ")
            choice = int(input("Enter the laptop number you want to order: "))
            if choice < 1 or choice > len(laptop_list):
                raise ValueError
            select = laptop_list[choice - 1]
            item = select['stock']
            money = select['price']
            orders = int(input("Enter the quantity you want to order: "))
            if orders < 1 or orders > 100:
                raise ValueError
                
            # Update the stock in the laptop_list
            select['stock'] += orders
            
            # Update the "laptop.txt" file with the new stock
            with open("laptop.txt", "w") as file:
                for l in laptop_list:
                    file.write("{},{},${},{},{},{}\n".format(l['name'], l['brand'], l['price'], l['stock'], l['processor'], l['gpu']))
              #Write details in receipt.txt file      
            with open("receipt.txt", "w") as file:
                Vat=0.13
                cost = orders * money
                vat_price = cost * Vat
                total_price = cost + vat_price
                current_date_time = datetime.datetime.now()
               
                print("Purchased Successfully")
                file.write("-------------------------------------------\n")
                file.write(f"   ------{current_date_time}-------\n")
                file.write("------------Laptop Zone---------------------\n")
                file.write("     Company name: {}\n".format(Cname))
                file.write("      price per piece: {}\n".format(money))
                file.write("      Total price: {}\n".format(cost))
                file.write("     Value Added Tax: {}\n".format(Vat))
                file.write("     Total price: {}\n".format(total_price))
                
            break
        
        
        
    except ValueError:
       
           print("Please enter a number") 
        
    if y=='sell':
            name=input("Enter Customer Name:")
            choosing = int(input("Enter the laptop number you want to order: "))
            if choosing < 1 or choosing > len(laptop_list):
                raise ValueError

            select = laptop_list[choosing - 1]
            quantity = select['stock']
            order = int(input("Enter the quantity you want to buy (max " + str(quantity) + "): "))
            if order < 1 or order > quantity:
                raise ValueError
            

            shipping=input("Do you want shipping 'yes' or 'no'? ")
            if shipping=='yes':
                Address=input("Enter your shipping Address: ")
                #write in receipt.txt file
                with open("receipt.txt", "w") as file:      
                    scost=100
                    p=select['price']
                    price = order * p
                    totalprice = price+scost
                    
                   
                    print("Order placed Successfully!!Thank you for shopping us")
                    file.write("-------------------------------------\n")
                    file.write("----------Laptop Zone----------------\n")
                    importingDateTime = datetime.datetime.now()
                    file.write("---------{}---------------\n".format(importingDateTime))
                    file.write("-------------------------------------\n")
                    file.write("    Customer name: {}\n".format(name))
                    file.write("    Quantity: {}\n".format(order))
                    file.write("    Price per item: {}\n".format(p))
        
                    file.write("    Shipping Cost: {}\n".format(scost))
                    file.write("    Total price: {}\n".format(totalprice))   

            if shipping=='no':  
                print("Thank you for shopping with us")
                p=select['price']
                price = order * p
                #write in receipt.txt file
                with open("receipt.txt", "w") as file:
                    totalprice = order * price
                    print("Order placed Successfully")
                    file.write("-------------------------------------\n")
                    file.write("----------Laptop Zone----------------\n")
                    importingDateTime = datetime.datetime.now()
                    file.write("---------{}---------------\n".format(importingDateTime))
                    file.write("-------------------------------------\n")
                    file.write("    Customer name: {}\n".format(name))
                    file.write("    Quantity: {}\n".format(order))
                    file.write("    Price per item: {}\n".format(p))
                    file.write("    Total price: {}\n".format(totalprice))
                

            select['stock'] -= order

    # Update the "laptop.txt" file with the new stock
            with open("laptop.txt", "w") as file:
                    for l in laptop_list:
                        file.write("{},{},${},{},{},{}\n".format(l['name'], l['brand'], l['price'], l['stock'], l['processor'], l['gpu']))  
                    
    break   

