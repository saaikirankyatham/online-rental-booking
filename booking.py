import inquirer
import sys


class Inventory:
    # in stock
    def __init__(self, bikes, cycles, cars, boats):
        self.bikes = bikes
        self.cycles = cycles
        self.cars = cars
        self.boats = boats

    def display_stock(self):
        print(f'We have currently {self.bikes} bikes available to rent.')
        print(f'We have currently {self.cycles} cycles available to rent.')
        print(f'We have currently {self.cars} cars available to rent.')
        print(f'We have currently {self.boats} boats available to rent.')



class Customer:
    def __init__(self):
        self.customers = []
        self.customer_name = None
        self.mobile_number = None
        self.email_id = None


    def view_customer_list(self):
        if self.customers:
            for customer in self.customers:
                customer_name = customer.get('customer_name')
                mobile_number = customer.get('mobile_number')
                email_id = customer.get('email_id')
                print(f'{customer_name}, {mobile_number}, {email_id}')

    def get_customer_names(self):
        return [customer.get('customer_name') for customer in self.customers]

    def add_customer(self):
        self.customers.append({
            'customer_name': input("Please enter your name: "),
            'mobile_number': input("Please enter your mobile number: "),
            'email_id': input("Please enter your email id: ")
        })
        print('Customer added successfully.')


class Booking(Customer, Inventory):
    def __init__(self, rentals):
        self.rentals = rentals

    def rental_booking(self, customer_obj,inventory_obj):
        all_customers = customer_obj.get_customer_names()
        if all_customers:
            print('Select the Customer:', *customer_obj.get_customer_names(), sep='\n')
            customer_name = input("Enter Customer Name: ")
            if customer_name in all_customers:
                rental_date = input('Enter Rental Date: ')
                return_date = input('Enter Return Date: ')
                print('Select the Vehicle Type:', *['bikes', 'cycles', 'cars', 'boats'], sep='\n')
                vehicle_type = input("Enter Vehicle Type: ")
                if vehicle_type == 'bikes':
                    if inventory_obj.bikes <= 0:
                        print("Sorry! We have currently {} bikes available to rent.".format(self.bikes))
                        return None
                    inventory_obj.bikes -= 1
                elif vehicle_type == 'cycles':
                    if inventory_obj.cycles <= 0:
                        print("Sorry! We have currently {} cycles available to rent.".format(inventory_obj.cycles))
                        return None
                    inventory_obj.cycles -= 1
                elif vehicle_type == 'cars':
                    if inventory_obj.cars <= 0:
                        print("Sorry! We have currently {} cars available to rent.".format(inventory_obj.cars))
                        return None
                    inventory_obj.cars -= 1
                elif vehicle_type == 'boats':
                    if inventory_obj.boats <= 0:
                        print("Sorry! We have currently {} boats available to rent.".format(inventory_obj.boats))
                        return None
                    inventory_obj.boats -= 1
                else:
                    print('Invalid Vehicle Type')
                    return None

                self.rentals.append({
                    'customer_name': customer_name,
                    'rental_date': rental_date,
                    'return_date': return_date,
                    'vehicle_type': vehicle_type
                })
                print('Rental booking successfull')
            else:
                print('Invalid Customer Name. Try again.')
                return None
        else:
            print('Zero Customers. Try again.')
            return None


    def show_rentals(self):
        print(self.rentals)


def main():
    inventory_instance = Inventory(2, 3, 1, 2)
    customer_instance = Customer()
    booking_instance = Booking([])
    is_done = False
    while not is_done:
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
            customer_instance.add_customer()
        elif choice == 2:
            booking_instance.rental_booking(customer_instance,inventory_instance)
        elif choice == 3:
            customer_instance.view_customer_list()
        elif choice == 4:
            inventory_instance.show_rentals()
        elif choice == 5:
            inventory_instance.display_stock()
        elif choice == 6:
            sys.exit()
main()
