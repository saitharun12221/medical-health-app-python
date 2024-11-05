
import os
import time

class AppointmentBooking:
    def __init__(self):
        self.doctor_name = []
        self.doctor_qualification = []
        self.doctor_gender = []
        self.doctor_password = []
        self.doctor_age = []
        self.doctor_mobile_number = []
        self.doctor_city = []

        self.patient_age = []
        self.patient_name = []
        self.patient_gender = []
        self.patient_password = []
        self.patient_mobile_number = []

        self.patient_age_booking = []
        self.patient_name_booking = []
        self.patient_gender_booking = []
        self.doctor_id = []

    def data_add(self):
        """Method for creating default doctor list."""
        self.doctor_name = ["Nagarjun Raut", "Ankush Nag", "Prashant Jha", 
                            "Ashish Gadpayle", "Sandip Paul", "Himanshu Pokhle", "Amit Mule"]
        self.doctor_qualification = ["MBBS", "Er, MBBS", "MBBS, MD", "MBBS,MD", 
                                     "BAMS", "MBBS, MD, Surgeon", "BAMS"]
        self.doctor_gender = ["M", "M", "M", "M", "M", "M", "M"]
        self.doctor_password = ["Nagarjun123", "Ankush123", "Prashant123", 
                                "Ashish123", "Sandip123", "Himanshu123", "Amit123"]
        self.doctor_age = [25, 24, 29, 29, 28, 23, 30]
        self.doctor_mobile_number = [9422887565, 123, 123, 123, 123, 123, 123]
        self.doctor_city = ["Gondiya", "Ranchi", "Nagpur", "Nagpur", "Mumbai", "Delhi", "Chennai"]

    def clear_screen(self):
        """Clear the console screen."""
        os.system('cls' if os.name == 'nt' else 'clear')

    def admin(self):
        while True:
            self.clear_screen()
            print("\t\t  _________________________")
            print("\t\t |                         |")
            print("\t\t |       Welcome Admin     |")
            print("\t\t |_________________________|")
            print("\n\n1. Doctor list \t2. Registered Patients \t3. Patients with Appointment")
            choice = int(input("Enter Your Choice: "))

            if choice == 1:
                for i, name in enumerate(self.doctor_name):
                    print(f"Name: {name}")
                input("\nPress Enter to return to the previous menu...")

            elif choice == 2:
                if not self.patient_name:
                    print("No Registered Patients yet.")
                    time.sleep(3)
                else:
                    for i, name in enumerate(self.patient_name):
                        print(f"{i}. {name}")
                    input("\nPress Enter to return to the previous menu...")

            elif choice == 3:
                if not self.patient_name_booking:
                    print("\nNo Appointments yet.")
                    time.sleep(3)
                else:
                    for i, name in enumerate(self.patient_name_booking):
                        print(f"{i}. {name}")
                    time.sleep(5)

            else:
                print("Wrong choice.")
                time.sleep(1)

    def patient(self):
        while True:
            self.clear_screen()
            print("\t\t  _________________________")
            print("\t\t |                         |")
            print("\t\t | Welcome to Patient Page!|")
            print("\t\t |_________________________|")
            print(" ")
            print("1. Login \t 2. Registration")
            choice = int(input("Enter your choice: "))

            if choice == 1:
                if not self.patient_mobile_number:
                    print("First register yourself then login..!")
                    time.sleep(1)
                else:
                    self.patient_login()
                break

            elif choice == 2:
                self.patient_registration()
                break

            else:
                print("\nYou entered wrong choice. Try again....!!!")
                time.sleep(1)

    def doctor(self):
        while True:
            self.clear_screen()
            print("\t\t  _________________________")
            print("\t\t |                         |")
            print("\t\t | Welcome to Doctor Page! |")
            print("\t\t |_________________________|")
            print(" ")

            print("1. Login \t 2. Registration")
            choice = int(input("Enter your choice: "))

            if choice == 1:
                if not self.doctor_mobile_number:
                    print("Register first...!")
                    time.sleep(1)
                else:
                    self.doctor_login()
                break

            elif choice == 2:
                self.doctor_registration()
                break

            else:
                print("Entered Wrong choice..")
                time.sleep(1)

    def patient_login(self):
        self.clear_screen()
        print("\t\t  _________________________")
        print("\t\t |                         |")
        print("\t\t |         Login            |")
        print("\t\t |_________________________|")

        mobile_number = int(input("Enter your Username (mobilenumber): "))
        password = input("Enter your Password: ")

        for i, number in enumerate(self.patient_mobile_number):
            if number == mobile_number and self.patient_password[i] == password:
                print(f"\nWelcome {self.patient_name[i]}, choose your doctor to book an appointment.")
                for j, doc in enumerate(self.doctor_name):
                    print(f"{j+1}. {doc}")
                doctor_choice = int(input("Enter doctor number: ")) - 1

                if 0 <= doctor_choice < len(self.doctor_name):
                    print(f"Doctor: {self.doctor_name[doctor_choice]}")
                    self.patient_name_booking.append(self.patient_name[i])
                    self.patient_age_booking.append(self.patient_age[i])
                    self.patient_gender_booking.append(self.patient_gender[i])
                    self.doctor_id.append(doctor_choice + 1)

                    print("\nBooking Successful!")
                    time.sleep(2)
                else:
                    print("Invalid doctor choice.")
                    time.sleep(1)
                return
        print("Login unsuccessful.")
        time.sleep(1)

    def patient_registration(self):
        self.clear_screen()
        print("\n\t\t | Welcome to Patient Registration Page!|\n")

        name = input("Please enter your name: ")
        age = int(input("Enter your age: "))
        mobile_number = int(input("Please enter your mobile number: "))

        if mobile_number in self.patient_mobile_number:
            print("Same mobile number is not allowed.")
            time.sleep(1)
        else:
            password = input("Enter password: ")
            self.patient_name.append(name)
            self.patient_age.append(age)
            self.patient_mobile_number.append(mobile_number)
            self.patient_password.append(password)
            print("Registration is successful.")
            time.sleep(1)

    def doctor_registration(self):
        self.clear_screen()
        print("\t\t ----------------------------------")
        print("\t\t| This is Doctor Registration Page |")
        print("\t\t ----------------------------------\n")

        name = input("Please enter your name: ")
        mobile_number = int(input("Please enter your mobile number: "))

        if mobile_number in self.doctor_mobile_number:
            print("Same mobile number is not allowed.")
            time.sleep(1)
        else:
            age = int(input("Enter age: "))
            city = input("Enter City: ")
            password = input("Enter password: ")

            self.doctor_name.append(name)
            self.doctor_age.append(age)
            self.doctor_mobile_number.append(mobile_number)
            self.doctor_city.append(city)
            self.doctor_password.append(password)

            print("Registration is successful.")
            time.sleep(1)

    def doctor_login(self):
        self.clear_screen()
        print("\t\t---------------------------------")
        print("\t\t| This is Doctor Login Page     |")
        print("\t\t---------------------------------")

        mobile_number = int(input("Enter your Username (mobilenumber): "))
        password = input("Enter your Password: ")

        for i, number in enumerate(self.doctor_mobile_number):
            if number == mobile_number and self.doctor_password[i] == password:
                self.clear_screen()
                print(f"\n\nWelcome Doctor {self.doctor_name[i]}")
                print("\n\nPress 1 to see your Appointments.")
                choice = int(input())

                if choice == 1:
                    appointments = [(pn, pd) for pn, pd in zip(self.patient_name_booking, self.doctor_id) if pd == (i + 1)]
                    if appointments:
                        for patient_name, _ in appointments:
                            print(f"Patient name: {patient_name}")
                    else:
                        print("No Appointments.")
                    time.sleep(3)
                return
        print("Login unsuccessful.")
        time.sleep(1)


if __name__ == "__main__":
    ap = AppointmentBooking()
    ap.data_add()

    while True:
        ap.clear_screen()
        print("---------------------------------------------------------------------")
        print("\t\t | Welcome to Doctor Appointment Booking |")
        print("----------------------------------------------------------------------\n")
        print("\n1. Doctor \t 2. Patient \t 3. Admin \t 4. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            ap.doctor()

        elif choice == 2:
            ap.patient()

        elif choice == 3:
            ap.admin()

        elif choice == 4:
            exit()

        else:
            print("Invalid choice. Try again.")
            time.sleep(1)
