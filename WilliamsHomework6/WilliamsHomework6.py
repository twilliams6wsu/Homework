



#Constants
##TODO: MAKE SURE THESE NAMES MATCH THE ONES YOU HAVE IN YOUR DIRECTORY
available_orders = [
    "order_one.txt",
    "order_two.txt",
]
last_receipt_file_name = "last_receipt.txt"
receipt_history_file_name = "receipt_history.txt"
sales_log_file_name = "sales_log.txt"
stock_file_name = "hw6_stock.txt"
restock_file_name = "restock_log.txt"
#=============================================================================
sales_tax = 0.0625
order_list = [
    #[Stapler,12.40,1]
]
stock_dictionary = {
    #"Stapler" : 3
}

stock_error_list = [
    #"Could noty sell <item> : <reason>"
]
restock_dictionary = {
    #"Stapler" : 6
}

# Lets the user input which order they want. Comment/uncomment the "raw_input" declarations to allow for easy testing and what not.
#TODO: PART 2 COMPLETE HERE
def userChooseOrderFile():
    while True:
        # raw_input = input("Order file (with .txt):").lower()
        raw_input = "order_one.txt"
        if raw_input in available_orders:
            break
        elif raw_input not in available_orders:
            print(f"Could not find {raw_input}. Try again.")

            continue
    return raw_input

#This variable needs to be declared before the definition of the other functions, so I don't need to pass the user's file as an arg every single call.
user_chosen_file = userChooseOrderFile()

def gatheringStockItems():
    with open(stock_file_name, "r") as file:
        for line in file.readlines():
            stocked_item, stocked_count = line.split(",")
            stock_dictionary[stocked_item] = int(stocked_count)
    print()
    print("Stocked items gathered.")



# DO NOT USE FOR STOCK... STOCK HAS A DIFFERENT FORMAT
def gatheringOrderItems():

    skipped_lines = []
    with open(user_chosen_file, "r") as file:
        for line in file:
            line.strip("\n")
            #TODO : PART 6 COMPLETE HERE
            if line.strip("") == "\n":
                continue
            elif line.startswith("#"):
                continue
            line = line.split(",")

            #TODO : PART 5 COMPLETE HERE

            try:


                if not stock_dictionary.get(line[0]):
                    stock_error_list.append(f"Could not sell '{line[0]}': not carried.")
                    continue

                elif stock_dictionary[line[0]] < int(line[2]):
                    stock_error_list.append(f"Could not sell '{line[0]}': only {stock_dictionary[line[0]]} in stock.")
                    #--EXTENSION--
                    #Appending to a new restock_log.txt file; one that reminds the store owner of the difference between what the
                    #customer wants and how much is in stock.
                    restock_dictionary[line[0]] = int(line[2]) - stock_dictionary[line[0]]
                    continue
                elif stock_dictionary[line[0]] >= int(line[2]):
                    order_list.append([
                        str(line[0]), #name
                        float(line[1]), #cost
                        int(line[2]), #count
                    ])
                    stock_dictionary[line[0]] -= int(line[2])
            except ValueError:
                skipped_lines.append(line)
            except IndexError:
                skipped_lines.append(line)
    print()
    print("Order items gathered, and put in the list.")
    if skipped_lines:
        print()
        # TODO: PART 2 COMPLETE HERE

        print(f"Skipped {len(skipped_lines)} bad order line(s):")
        print("=" * 30)
        for line in skipped_lines:
            print(line)

#This nice feature only works really well on monospace fonts. (I assume)
#Keeping the receipt lines all nice and pretty.
def returnPrettyReceiptLine(item_list) -> str:
    return f"{item_list[0]}{' ' * (30-len(item_list[0]))}|  ${format(item_list[1], '.2f')}{' ' * (5-len(format(item_list[1], '.2f')))}|  {item_list[2]}{' ' * (5-len(str(item_list[2])))}|  ${round(item_list[1] * item_list[2], 2):.2f}{' ' * (5-len(str(round(item_list[1] * item_list[2], 2))))}\n"

#Creating a new receipt file; the single one that Part 1 specifies.
#TODO : PART 1 COMPLETE HERE
def producingReceiptFileShallow():
    subtotal = 0
    with open(last_receipt_file_name, "w") as file:
        file.write(f"Item{' ' * 26}| Cost   | Count | Total\n")
        file.write(f"{'-' * 60}\n")
        for item_list in order_list:
            file.write(returnPrettyReceiptLine(item_list))
            subtotal += item_list[2] * item_list[1]
        file.write(f"{'-' * 60}\n")


        file.write(f"Subtotal:{' ' * (47-len(format(subtotal, '.2f')))}${format(subtotal, '.2f')}\n")
        file.write(f"Sales Tax:{' ' * (46 - len(format(subtotal, '.2f')))}{sales_tax}\n")
        file.write(f"Total:{' ' * (50 - len(format(subtotal * (1 + sales_tax), '.2f')))}${format(subtotal * (1+sales_tax), '.2f')}\n")
    with open(last_receipt_file_name, "r") as file:
        print("Here's your receipt!!")
        #TODO : PART 1 COMPLETE HERE
        for line in file.readlines():
            print(line)
    #TODO : PART 5 DONE HERE
    if stock_error_list:
        print("SALE ERRORS:")
        for line in stock_error_list:
            print("     ",line)
    print()
    print("Receipt file created.")

#APPENDING to the full receipt history file.
def producingReceiptFileDeep():
    subtotal = 0
    with open(receipt_history_file_name, "a") as file:
        file.write('\n')
        file.write('\n')
        file.write(f"{'-' * 40}\n")
        file.write('\n')
        file.write('\n')

        file.write(f"Item{' ' * 26}| Cost   | Count | Total\n")
        file.write(f"{'-' * 60}\n")
        for item_list in order_list:
            file.write(returnPrettyReceiptLine(item_list))
            subtotal += round(item_list[2] * item_list[1],2)
        file.write(f"{'-' * 60}\n")

        file.write(f"Subtotal:{' ' * (47 - len(format(subtotal, '.2f')))}${format(subtotal, '.2f')}\n")
        file.write(f"Sales Tax:{' ' * (45 - len(format(subtotal, '.2f')))}{sales_tax}\n")
        file.write(f"Total:{' ' * (50 - len(format(subtotal * (1 + sales_tax), '.2f')))}${format(subtotal * (1 + sales_tax), '.2f')}\n")
    print()
    print("Receipt history file appended.")


#TODO : PART 3 COMPLETE HERE
def appendingSalesLogFile():

    #READ ONLY: converting each line with the format ITEM_NAME : ITEM_COUNT into a dictionary. Dictionary stored in mem
    with open(sales_log_file_name, "r") as file:
        bad_line_count = 0
        sales_log_dictionary = {}
        for log_line in file.readlines():
            #TODO : PART 6 COMPLETE HERE
            if log_line == "\n" or log_line.startswith("#"):
                continue
            try:
                item_name, item_count = log_line.strip('\n').split(" : ")[0], int(log_line.strip('\n').split(" : ")[1])
                sales_log_dictionary[item_name] = item_count
            except IndexError: #Might throw if some of the text in the log is invalid.
                bad_line_count += 1
                continue

        # TODO : PART 6 COMPLETE HERE
        print()
        print(f"Ignored {bad_line_count} bad line(s) in sales_log.txt")


    #WRITING NOW: Using the saved data from above, we will rewrite the whole sales_log.txt file, with the effect that it
    #looks like we're just updating the sale counts. Also adds new lines for previously unaccounted items.
    print()
    print()
    with open(sales_log_file_name, "w") as file:
        file.write("Items sold so far:\n")
        print("Items sold so far:")
        print("-" * 20)
        for item_list in order_list:
            if sales_log_dictionary.get(item_list[0]):
                sales_log_dictionary[item_list[0]] += item_list[2]
            else:
                sales_log_dictionary[item_list[0]] = item_list[2]
        for key,value in sales_log_dictionary.items():
            file.write(f"{key} : {value}\n")
            #TODO : PART 4 COMPLETE HERE
            print(f"{key} : {value}")
    print()
    print()
    print("Sales log file appended.")

def appendingStockFile():
    with open(stock_file_name,"w") as file:
        for item_name, item_count in stock_dictionary.items():
            file.write(f"{item_name},{item_count}\n")


#--EXTENSION--
#Using the data appended to restock_dictionary, make the file and add the necessary information.
def producingRestockFile():
    with open(restock_file_name, "w") as file:
        file.write("FORMAT: 'item to restock' : count\n")
        file.write("\n")
        for item_name, item_count in restock_dictionary.items():
            file.write(f"{item_name} : {item_count}\n")







#Seeing whats in stock, and storing the data
gatheringStockItems()

#Seeing what the user's order is, and storing the data if it's in stock!
gatheringOrderItems()

#Creating the "last_receipt.txt", that only has the most recent receipt on it.
producingReceiptFileShallow()

#Appending the full receipt history file with the most recent one.
producingReceiptFileDeep()

#Updating the "sales_log.txt" file to accurately match the sales.
appendingSalesLogFile()

#Updating the "hw6_stock.txt" file to accurately match the stock.
appendingStockFile()

#Making the restock_log file.
producingRestockFile()