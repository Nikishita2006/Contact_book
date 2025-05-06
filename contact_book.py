#contacts book
contacts=[]
def menu():
    while True:
        print("\nContacts book")
        print("1.To add a contact")
        print("2.To edit a contact")
        print("3.To delete a contact")
        print("4.To view contacts")
        print("5.Exit")
        n=input("Select the option you want to perform(1-5):")
        if(n=="1"):
            add()
        elif(n=="2"):
            edit()
        elif(n=="3"):
           delete()
        elif(n=="4"):
           view()
        else:
          exit_app()
def add():
    while True:
        r=input("Enter the name:")
        while not(r.isalpha()):
            print("Invalid")
            r=input("Enter the name again")
        p=input("Enter the phone number:")
        while not(p.isdigit()and len(p)==10):
            print("Invalid")
            p=input("Enter the phone number again")
        contact={"name":r,"phone":p}
        contacts.append(contact)
        print("Contacts saved successfully")
        t=input("Do you want to add more contacts?(yes/no)")
        if(t!="yes".lower()):
            break
def edit():
    while True:
        c=input("Enter the name you want to edit:")
        for contact in contacts:
            if(contact["name"]==c):
                print("Enter new name/same name or new number/same number")
                new_contact=input("Enter new name/same name:")
                while not(new_contact.isalpha()):
                    print("Invalid")
                    new_contact=input("Enter the name again:")
                new_phone=input("Enter new number/same  number:")
                while not(new_phone.isdigit() and len(new_phone)==10):
                    print("Invalid")
                    new_phone=input("Enter the number again:")
                if(new_contact):
                    contact["name"]=new_contact
                elif(new_phone):
                    contact["phone"]=new_phone
                print("contact edited successfully")
                break
        else:
            print("contact not found")
        a=input("Do you want to edit more contacts?(yes/no)")
        if(a!="yes".lower()):
                break
def delete():
    while True:
        b=input("Enter the name you want to delete:")
        for contact in contacts:
            if(b==contact["name"]):
                contacts.remove(contact)
                print("Contact deleted successfully")
            else:
                print("Contact not found")
        d=input("Do you want to delete more contacts?(yes/no)")
        if(d!="yes".lower):
            break
def view():
    print("View your contacts after adding the contacts:")
    print("\n Contacts:",contacts)
def exit_app():
    print("All your contacts are saved successfully,Exiting...")
    exit()
while True:
    menu()
        
                
            
    
