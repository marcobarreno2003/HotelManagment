from models import RoomManager, TaskScheduler, User
from utils import validate_email, validate_password

def admin_menu(user):
    room_manager = RoomManager()
    room_manager.load_rooms()

    while True:
        print(f"\nHello, {user.name} (Admin)!")
        print("\n1. Manage rooms")
        print("2. Manage staff tasks")
        print("3. Logout")
        option = input("Choose an option: ")

        if option == "1":
            manage_rooms()
        elif option == "2":
            manage_staff_tasks()
        elif option == "3":
            print(f"Goodbye, {user.name}!")
            break

def staff_menu(user):
    print(f"\nHello, {user.name} (Staff)!")
    while True:
        print("\n1. Manage reservations")
        print("2. View tasks")
        print("3. Logout")
        option = input("Choose an option: ")

        if option == "1":
            # Reservation management not implemented
            print("Reservation management coming soon.")
        elif option == "2":
            # View staff tasks
            print("Task viewing coming soon.")
        elif option == "3":
            print(f"Goodbye, {user.name}!")
            break

def cleaner_menu(user):
    print(f"\nHello, {user.name} (Cleaner)!")
    while True:
        print("\n1. View my tasks")
        print("2. Logout")
        option = input("Choose an option: ")

        if option == "1":
            print("Task viewing coming soon.")
        elif option == "2":
            print(f"Goodbye, {user.name}!")
            break

def manage_rooms():
    room_manager = RoomManager()
    room_manager.load_rooms()

    while True:
        print("\n1. Add a new room")
        print("2. View all rooms")
        print("3. Delete a room")
        print("4. Go back")
        option = input("Choose an option: ")

        if option == "1":
            number = int(input("Enter room number: "))
            room_type = input("Enter room type (Single/Double/Suite): ")
            price = float(input("Enter room price: "))
            room_manager.add_room(Room(number, room_type, price))
        elif option == "2":
            room_manager.view_rooms()
        elif option == "3":
            room_number = int(input("Enter the room number to delete: "))
            room_manager.delete_room(room_number)
        elif option == "4":
            break

def manage_staff_tasks():
    task_scheduler = TaskScheduler()

    while True:
        print("\n1. Add a new task")
        print("2. Assign task to staff")
        print("3. View all tasks")
        print("4. Go back")
        option = input("Choose an option: ")

        if option == "1":
            task_name = input("Enter task name: ")
            priority = int(input("Enter task priority (1-5): "))
            task_scheduler.add_task(Task(task_name, priority))
        elif option == "2":
            staff_member = input("Enter staff member's name: ")
            task_scheduler.assign_task(staff_member)
        elif option == "3":
            task_scheduler.view_tasks()
        elif option == "4":
            break

def login_or_register():
    while True:
        print("\n1. Register")
        print("\n2. Login")
        print("\n3. Exit")
        option = input("Choose an option: ")

        if option == "1":
            name = input("Enter your name: ")
            email = input("Enter your email: ")
            if validate_email(email):
                password = input("Enter your password: ")
                if validate_password(password):
                    role = input("Enter role (admin, staff, cleaner): ")
                    User.register_user(name, email, password, role)
        elif option == "2":
            email = input("Enter your email: ")
            password = input("Enter your password: ")
            user = User.login(email, password)
            if user:
                if user.role == "admin":
                    admin_menu(user)
                elif user.role == "staff":
                    staff_menu(user)
                elif user.role == "cleaner":
                    cleaner_menu(user)
        elif option == "3":
            print("Exiting the system.")
            break

if __name__ == "__main__":
    login_or_register()
