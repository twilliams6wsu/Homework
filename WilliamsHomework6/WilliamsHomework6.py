available_orders = [
    "hw6_order.txt",
    "hw6_order2.txt",
]
receipt_file_name = "receipt.txt"
sales_log_file_name = "sales_log.txt"


sales_tax = 0.00625
order_list = []

def userChooseOrderFile():
    raw_input = input("Order file:").lower()
    while raw_input not in available_orders:
        print(f"Could not find {raw_input}. Try again.")
        raw_input = input("Order file:").lower()
    open(raw_input, "r")
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
    if skipped_lines:
        print(f"Skipped {len(skipped_lines)} bad line(s).")
        for line in skipped_lines:
            print(f"'{line}'")
    print("Order items gathered, and put in the list.")

def producingReceiptFile():
    subtotal = 0
    total = 0
    with open("receipt.txt", "w") as file:
        file.write("Item        Unit  Cost Count Line Total\n")
        file.write("---------------------------------------\n")
        for item_list in order_list:
            file.write(f"{item_list[0]}   {item_list[1]}   {item_list[2]}\n")
            subtotal += round(item_list[2] * item_list[1],2)
        file.write("---------------------------------------\n")
        file.write(f"""
        Subtotal: ${subtotal}
        Sales Tax: (6.25%) ${round(subtotal * sales_tax, 2)}
        Total: ${round(subtotal * (float(1) + sales_tax), 2)}""")
    print("Receipt file created.")



def appendingSalesLogFile():
    with open("sales_log.txt", "a") as file:
        for item_list in order_list:
            file.write("\n")
            file.write(f"{item_list[0]}:{item_list[2]}")
    print("Sales log file appended.")



userChooseOrderFile()
gatheringOrderItems()
