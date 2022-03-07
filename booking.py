import sys


class Inventory:
    bikes = 2
    cycles = 3
    cars = 1
    boats = 2
    # # in stock
    def __init__(self):
        pass

    def display_stock(self):
        print(f'We have currently {self.bikes} bikes available to rent.')
        print(f'We have currently {self.cycles} cycles available to rent.')
        print(f'We have currently {self.cars} cars available to rent.')
        print(f'We have currently {self.boats} boats available to rent.')



class Customer:
    customers = []

    def __init__(self):
        pass

    def view_customer_list(self):
        if self.customers:
            print ("{:<8} {:<15} {:<10}".format('Name', 'Number', 'Email-id'))
            for customer in self.customers:
                customer_name = customer.get('customer_name')
                mobile_number = customer.get('mobile_number')
                email_id = customer.get('email_id')
                print ("{:<10} {:<15} {:<10}".format(customer_name, mobile_number, email_id))
        else:
            print('--------- NO CUSTOMERS ---------')



    def get_customer_names(self):
        return [customer.get('customer_name') for customer in self.customers]

    def add_customer(self):
        self.customers.append({
            'customer_name': input("Please enter your name: "),
            'mobile_number': input("Please enter your mobile number: "),
            'email_id': input("Please enter your email id: ")
        })
        print('--------- CUSTOMER ADDED SUCCESSFULLY ---------')


class Booking(Customer, Inventory):
    rentals = []
    def __init__(self):
        super().__init__()

    def rental_booking(self):
        all_customers = self.get_customer_names()
        if all_customers:
            print('Select the Customer:', *all_customers, sep='\n')
            customer_name = input("Enter Customer Name: ")
            if customer_name in all_customers:
                rental_date = input('Enter Rental Date: ')
                return_date = input('Enter Return Date: ')
                print('Select the Vehicle Type:', *['bikes', 'cycles', 'cars', 'boats'], sep='\n')
                vehicle_type = input("Enter Vehicle Type: ")
                if vehicle_type == 'bikes':
                    if self.bikes <= 0:
                        print("Sorry! We have currently {} bikes available to rent.".format(self.bikes))
                        return None
                    self.bikes -= 1
                elif vehicle_type == 'cycles':
                    if self.cycles <= 0:
                        print("Sorry! We have currently {} cycles available to rent.".format(self.cycles))
                        return None
                    self.cycles -= 1
                elif vehicle_type == 'cars':
                    if self.cars <= 0:
                        print("Sorry! We have currently {} cars available to rent.".format(self.cars))
                        return None
                    self.cars -= 1
                elif vehicle_type == 'boats':
                    if self.boats <= 0:
                        print("Sorry! We have currently {} boats available to rent.".format(self.boats))
                        return None
                    self.boats -= 1
                else:
                    print('--------- INVALID INVENTORY TYPE ---------')
                    return None

                self.rentals.append({
                    'customer_name': customer_name,
                    'rental_date': rental_date,
                    'return_date': return_date,
                    'vehicle_type': vehicle_type
                })
                print('--------- RENTAL BOOKING SUCCESSFULL ---------')
            else:
                print('--------- INVALID CUSTOMER NAME. TRY AGAIN ---------')
        else:
            print('--------- NO CUSTOMERS ---------')


    def show_rentals(self):
        if self.rentals:
            print ("{:<8} {:<15} {:<10} {:<10}".format('Name', 'Rental-Date', 'Return-Date', 'Vehicle-Type'))
            for rental in self.rentals:
                customer_name = rental.get('customer_name')
                rental_date = rental.get('rental_date', None)
                return_date = rental.get('return_date', None)
                vehicle_type = rental.get('vehicle_type', None)
                print ("{:<8} {:<15} {:<10} {:<10}".format(customer_name, rental_date, return_date, vehicle_type))
        else:
            print('--------- NO RENTAL BOOKINGS ARE OCCURRED ---------')

def main():
    booking_instance = Booking()
    is_done = False
    while not is_done:
        try:
            print(
                ''' ====== MENU =======
                1. Add Customer
                2. Add rental booking
                3. See Customer List
                4. See rental booking list
                5. See Inventory of vehicles available
                6. Exit
                '''
            )
            choice = int(input("Enter Choice:"))
            if choice == 1:
                booking_instance.add_customer()
            elif choice == 2:
                booking_instance.rental_booking()
            elif choice == 3:
                booking_instance.view_customer_list()
            elif choice == 4:
                booking_instance.show_rentals()
            elif choice == 5:
                booking_instance.display_stock()
            elif choice == 6:
                sys.exit()
        except Exception as ex:
            print("Exception Triggered -> ", str(ex))
            continue

main()
