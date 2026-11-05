




available_orders = [
    "order_one.txt",
    "order_two.txt",
]
receipt_file_name = "last_receipt.txt"
sales_log_file_name = "sales_log.txt"


sales_tax = 0.0625
order_list = []

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


user_chosen_file = userChooseOrderFile()




def gatheringOrderItems():
    #DO NOT USE FOR STOCK... STOCK HAS A DIFFERENT FORMAT
    skipped_lines = []
    with open(user_chosen_file, "r") as file:
        for line in file:
            line.strip("\n")
            line = line.split(",")
            try:
                order_list.append([
                    str(line[0]), #name
                    float(line[1]), #cost
                    int(line[2]), #count
                ])
            except ValueError:
                skipped_lines.append(line)
            except IndexError:
                skipped_lines.append(line)
    print("Order items gathered, and put in the list.")
    if skipped_lines:
        print(f"Skipped {len(skipped_lines)} bad line(s):")
        print("=" * 30)
        for line in skipped_lines:
            print(line)

#This nice feature only works really well on monospace fonts.
def returnPrettyReceiptLine(item_list) -> str:
    return f"{item_list[0]}{' ' * (30-len(item_list[0]))}|  ${item_list[1]}{' ' * (5-len(str(item_list[1])))}|  {item_list[2]}{' ' * (5-len(str(item_list[2])))}|  ${round(item_list[1] * item_list[2], 2)}{' ' * (5-len(str(round(item_list[1] * item_list[2], 2))))}\n"

#Creating a new receipt file everytime this runs.
def producingReceiptFileShallow():
    subtotal = 0
    with open("last_receipt.txt", "w") as file:
        file.write(f"Item{' ' * 26}| Cost   | Count | Total\n")
        file.write(f"{'-' * 40}\n")
        for item_list in order_list:
            file.write(returnPrettyReceiptLine(item_list))
            subtotal += round(item_list[2] * item_list[1],2)
        file.write(f"{'-' * 40}\n")

        file.write(f"""
        Subtotal: ${round(subtotal,2)}
        Sales Tax: (6.25%) ${round(subtotal * sales_tax, 2)}
        Total: ${round(subtotal * (float(1) + sales_tax), 2)}""")
    print("Receipt file created.")

#APPENDING to the receipt history file.
def producingReceiptFileDeep():
    subtotal = 0
    with open("receipt_history.txt", "a") as file:
        file.write(f"{'#' * 40}\n")

        file.write(f"Item{' ' * 26}| Cost   | Count | Total\n")
        file.write(f"{'-' * 40}\n")
        for item_list in order_list:
            file.write(returnPrettyReceiptLine(item_list))
            subtotal += round(item_list[2] * item_list[1],2)
        file.write(f"{'-' * 40}\n")

        file.write(f"""
        Subtotal: ${round(subtotal,2)}
        Sales Tax: (6.25%) ${round(subtotal * sales_tax, 2)}
        Total: ${round(subtotal * (float(1) + sales_tax), 2)}\n

""")
    print("Receipt history file appended.")



def appendingSalesLogFile():

    #READ ONLY: converting each line with the format ITEM_NAME : ITEM_COUNT into a dictionary. Dictionary stored in mem
    with open("sales_log.txt", "r") as file:
        sales_log_dictionary = {}
        for log_line in file.readlines():
            try:
                item_name, item_count = log_line.strip('\n').split(" : ")[0], int(log_line.strip('\n').split(" : ")[1])
                sales_log_dictionary[item_name] = item_count
            except IndexError: #Might throw if some of the text in the log is invalid.
                continue



    #WRITING NOW: Using the saved data from above, we will rewrite the whole sales_log.txt file, with the effect that it
    #looks like we're just updating the sale counts. Also adds new lines for previously unaccounted items.
    #Seriously, this was a breath of fresh air. Much more stimulating with open-ended prompts, rather than a single file
    #holding your hand through the whole thing.
    with open("sales_log.txt", "w") as file:
        file.write("Items sold so far:\n")
        for item_list in order_list:
            if sales_log_dictionary.get(item_list[0]):
                sales_log_dictionary[item_list[0]] += item_list[2]
            else:
                sales_log_dictionary[item_list[0]] = item_list[2]
        for key,value in sales_log_dictionary.items():
            file.write(f"{key} : {value}\n")
    print("Sales log file appended.")


#TODO: Add stock function, need to copy from assignment

gatheringOrderItems()
producingReceiptFileShallow()
producingReceiptFileDeep()
appendingSalesLogFile()
