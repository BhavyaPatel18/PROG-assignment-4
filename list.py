import csv

class List:
    def __init__(self):
        self.Cineplex = []
        self.read()
        
    def read(self):
        with open("Cineplex.csv",'r') as csv_file:
            reader = csv.DictReader(csv_file, delimiter=',')
            for line in reader:
                Cineplex = list(line.values())
                self.Cineplex.append(Cineplex)
       
    def write(self):
        with open('Cineplex.csv','w') as csv_file:
            field_names = ['tickit_no','last_name','seat_no']
            writer = csv.DictWriter(csv_file, fieldnames=field_names, delimiter = ",")
            writer.writeheader()
            for line in self.Cineplex:
                writer.writerow({'tickit_no':line[0], 'last_name':line[1], 'seat_no':line[2]})
       
    def create(self, tickit_no, last_name, seat_no):
        self.Cineplex.append((tickit_no, last_name, seat_no))
        
    def search(self,tickit_no):   
        for line in self.Cineplex:
            if line[0] == str(tickit_no):
                return line
       
    def delete(self,tickit_no):
        new_list = self.search(tickit_no)
        if new_list:
            self.Cineplex.remove(new_list)
            print("Deleted the tickit_no successfully")

    def edit(self, tickit_no):
        new_list = self.search(tickit_no)
        if new_list:
            self.Cineplex.remove(new_list)
            last_name = input("Enter the last_name:")
            seat_no = int(input("Enter the seat_no:"))
            self.Cineplex.append((tickit_no,last_name,seat_no))
            
    print("Successfully Updated.")