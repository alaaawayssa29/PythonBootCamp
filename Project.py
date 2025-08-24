Appointments = []
def add(name, date, time):
    Appointments.append([name, date, time])
    print("Appointment added successfully!")
def show():
    if not Appointments:
        print("No appointments yet!!")
    else:
        i = 0
        for app in Appointments:
            print(i,": ", app, "\n")
            i += 1
def delete(number):
    del Appointments[number]
    print("Appointment deleted successfully.")
while True:
    print("----------------\n1. Add a new appointment.\n2. Show all appointments.\n3. Delete an appointment.\n4. Exit.\n----------------")
    number = int (input("Enter a number: "))
    if number == 1:
        n = input("Enter the name:")
        d = input("Enter the date:")
        t = input("Enter the time:")
        add(n, d, t)
    elif number == 2:
        show()
    elif number == 3:
        try: 
            n = int (input("Enter the number of appointment:"))
            delete(n)
        except Exception as e: 
            print(e)
    elif number == 4:
        break           