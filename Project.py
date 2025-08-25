Appointments = []
def add():
    name = input("Enter the name:")
    date = input("Enter the date:")
    time = input("Enter the time:")
    for appt in Appointments:
        if appt[1] == date and appt[2] == time:
            print("This appointment conflicts with an existing one!") 
            return
    Appointments.append([name, date, time])
    print("Appointment added successfully!")
def show():
    if not Appointments:
        print("No appointments yet!!")
    else:
        i = 1
        for app in Appointments:
            print(i,": ", app)
            i += 1
def delete():
    try: 
        number = int (input("Enter the number of appointment:"))
        del Appointments[number - 1]
        print("Appointment deleted successfully.")
    except Exception: 
        if not Appointments:
            print("No appointments to delete!!")
        elif number - 1 < 0 or number - 1 >= len(Appointments):
            print("Index out of range!!")
while True:
    print("----------------\n1. Add a new appointment.\n2. Show all appointments.\n3. Delete an appointment.\n4. Exit.\n----------------")
    number = int (input("Enter a number: "))
    if number == 1:
        add()
    elif number == 2:
        show()
    elif number == 3:
        delete()
    elif number == 4:
        break           