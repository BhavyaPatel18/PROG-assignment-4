import list
import random

class UI():

    def mainmenu(self):
        try:
            print("C:/Users/Bhavya/Downloads/Bhavya's Semester 2/PROG class/PROG assignment 4/Cineplex.csv","r")
            print("1: Enter the last_name and seat_no")
            print("2: enter the tickit_no")
            print("3: delete the ticket_no")
            Options = int(input("Please enter the your number:"))
            return Options
        except ValueError:
            print("Your statement was invalid, please try again.")
        except Exception as a:
                print("Your statement was invalid, please try again.")
                return (a)

    def run(self):
        Cineplex = list.List()
        while True:
            Option = self.mainmenu()
            if Option == 1:
                tickit_no = random.randint(100,200)
                last_name = input("Enter the Last name:")
                seat_no = int(input("Enter the seat_no:"))
                Cineplex.create(tickit_no, last_name, seat_no)
                Cineplex.write()
                print("Created a your cineplex booked list")
                continue
            
            elif Option == 2:
                seat_no = int(input("Enter the tickit_no to search:"))
                print(Cineplex.search(seat_no))
                continue
            
            elif Option == 3:
                seat_no = int(input("Enter the tickit_no to delete:"))
                Cineplex.delete(seat_no)
                Cineplex.write()
                continue

Book = UI()
Book.run()