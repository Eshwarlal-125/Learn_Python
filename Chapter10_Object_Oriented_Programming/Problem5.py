# Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats) and get
# fare information of train running under Indian Railways.

class Train:
    trainName = "Green Line Express"
    seats = 10
    def bookTicket(self):
        self.seats = self.seats-1
        print("Ticket Booked!")
    def getStatus(self):
        print("Remaining Seats: ",self.seats)
    def getInformation(self):
        print("Price of ticket: 500")

train = Train()
print("Name of Train: ", train.trainName)
print("No of Seats: ", train.seats)
train.getInformation()
train.bookTicket()
train.getStatus()

