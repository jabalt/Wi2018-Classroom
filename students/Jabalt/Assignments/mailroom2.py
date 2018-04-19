#!/usr/bin/env python3


"""
It should have a data structure that holds a list of your donors and a history of the amounts they have donated. This structure should be populated at first with at least five donors, with between 1 and 3 donations each.
You can store that data structure in the global namespace.
The script should prompt the user (you) to choose from a menu of 3 actions: “Send a Thank You”, “Create a Report” or “quit”)
"""

import os


# Name of donor is key 
#Value is list 
#total amount donated (float)

donor_dict = {"Bill Gates":[5.85,3], "Paul Allen": [76.56,2], "Jeff Bezos": [29.30,3] , "Mark Zuckerberg": [15.76,1], "Warren Buffets": [445.75,1]}
donors = [donor for donor in donor_dict.keys()]


def mailroom():
    """ mail sending and report generation"""
    choice = " "
    arg_dict = {"1":send_thankyou, "2":generate_report, "3": send_letters, "4":quit}
    while choice != "4":
        choice = input("Please choose one : \n1. Send thank you \n2. Create report \n3. Send letters \n4. Quit\n")
        arg_dict.get(choice)()
            
def send_thankyou():
    """Prints out a thank you letter to specified person"""
    name = input("choose or add a name!\n")
    if name == "list":
        print("\n".join(donors))
        name = input("choose or add a name!")
    if name not in donors and (name !="list"):
        donor_dict[name] = [0,0]
        donation = input("How much is the donation?\n")
        donor_dict[name][0]+=float(donation)
        donor_dict[name][1]+=1
    print(thank_you_txt(name))


def thank_you_txt(name):
        return "Dear {0},\n\n \tThanks so much for the donation of ${1:.2f}.\n \tWe are grateful for your contribution. \n\n-Team".format(name, donor_dict[name][0])

def generate_report():
    print("{:16}|{:^13}|{:^11}|{:>13}".format("Donor Name", "Total Given", "Num Gifts", "Average Gift"))
    for name in donors:
        print("{:17}${:>12.2f} {:>11} ${:>12.2f}".format(name, donor_dict[name][0], donor_dict[name][1],(donor_dict[name][0]/donor_dict[name][1])))

def send_letters():
    for name in donors:
        output_dir = "letters"
        filename = output_dir+"/"+name+".txt"
        try:
            with open(filename, "w+") as f:
                f.write(thank_you_txt(name))
        except FileNotFoundError:
            os.mkdir(output_dir)
            with open(filename, "w+") as f:
                f.write(thank_you_txt(name))



if __name__ == "__main__":
    mailroom()