import pickle


class Contact(object):

    def __init__(self, first, last, email):
        self.first = first
        self.last = last
        self.email = email

    def getContactInfo(self):
        fs = "%-8s, %-8s %-20s" % (self.last, self.first, self.email)
        return fs


def addContact():
    contact_first = input("Please enter contacts first name: ")
    contacts_last = input("Please enter contacts last name: ")
    contacts_email = input("Please enter contacts email: ")
    contact_instance = Contact(contact_first, contacts_last, contacts_email)

    return contact_instance


def readData(f_hand):
    try:
        f = open(f_hand, 'rb')
        d = pickle.load(f)
        f.close()

    except IOError:
        d = []

    return d


def storeData(f_hand, f):
    fh = open(f_hand, 'wb')
    pickle.dump(f, fh)
    fh.close()


def displayData(my_contacts):
    if len(my_contacts) > 0:
        print()
        print("%-18s %-15s" % ("Name", "Email"))

        for c in my_contacts:
            print(c.getContactInfo())

    else:
        print("Sorry no data to display")


def main():
    f_hand = 'contacts.txt'
    my_contacts = readData(f_hand)

    while True:
        print("""
        Menu Options
        1.) Display all Contacts
        2.) Create a New Contact
        3.) Save and Exit
        """)

        opt = input("Enter a menu option 1, 2, or 3: ")

        if opt == '1':
            displayData(my_contacts)

        elif opt == '2':
            contact = addContact()
            my_contacts.append(contact)

        elif opt == '3':
            storeData(f_hand, my_contacts)
            print("Goodbye")
            print()
            break


if __name__ == '__main__':
    main()
