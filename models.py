from db_connection import connect_db

class User:
    user_cache = {}  # In-memory cache for users

    def __init__(self, user_id, name, email, password, role='staff'):
        self.id = user_id
        self.name = name
        self.email = email
        self.password = password
        self.role = role

    @staticmethod
    def register_user(name, email, password, role='staff'):
        connection = connect_db()
        if connection:
            try:
                cursor = connection.cursor()
                cursor.execute("""
                    INSERT INTO users (name, email, password, role)
                    VALUES (%s, %s, %s, %s)
                """, (name, email, password, role))
                connection.commit()
                print(f"User {name} registered successfully with role {role}.")
            except mysql.connector.Error as err:
                print(f"Error registering user: {err}")
            finally:
                connection.close()

    @staticmethod
    def login(email, password):
        connection = connect_db()
        if connection:
            try:
                cursor = connection.cursor()
                cursor.execute("SELECT * FROM users WHERE email = %s AND password = %s", (email, password))
                user = cursor.fetchone()
                if user:
                    print(f"Welcome, {user[1]}!")  # Greet the user
                    return User(user[0], user[1], user[2], user[3], user[4])  # Return the user object with details
                else:
                    print("Invalid email or password.")
            except mysql.connector.Error as err:
                print(f"Error during login: {err}")
            finally:
                connection.close()
        return None
class Room:
    def __init__(self, number, room_type, price, available=True):
        self.number = number
        self.room_type = room_type
        self.price = price
        self.available = available

class RoomManager:
    def __init__(self):
        self.rooms = []

    def load_rooms(self):
        connection = connect_db()
        if connection:
            try:
                cursor = connection.cursor()
                cursor.execute("SELECT * FROM rooms")
                room_data = cursor.fetchall()
                self.rooms = [Room(r[1], r[2], r[3], r[4]) for r in room_data]
            except mysql.connector.Error as err:
                print(f"Error loading rooms: {err}")
            finally:
                connection.close()

    def add_room(self, room):
        connection = connect_db()
        if connection:
            try:
                cursor = connection.cursor()
                cursor.execute("""
                    INSERT INTO rooms (number, room_type, price, available)
                    VALUES (%s, %s, %s, %s)
                """, (room.number, room.room_type, room.price, room.available))
                connection.commit()
                print(f"Room {room.number} added.")
            except mysql.connector.Error as err:
                print(f"Error adding room: {err}")
            finally:
                connection.close()

    def delete_room(self, room_number):
        connection = connect_db()
        if connection:
            try:
                cursor = connection.cursor()
                cursor.execute("DELETE FROM rooms WHERE number = %s", (room_number,))
                connection.commit()
                print(f"Room {room_number} deleted.")
            except mysql.connector.Error as err:
                print(f"Error deleting room: {err}")
            finally:
                connection.close()

    def view_rooms(self):
        for room in self.rooms:
            print(f"Room {room.number}, Type: {room.room_type}, Price: {room.price}")
import heapq

class Task:
    def __init__(self, task_name, priority, assigned_staff=None):
        self.task_name = task_name
        self.priority = priority
        self.assigned_staff = assigned_staff

    def __lt__(self, other):
        return self.priority < other.priority  # Compare tasks based on priority

class TaskScheduler:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        heapq.heappush(self.tasks, task)
        print(f"Task '{task.task_name}' added to the schedule with priority {task.priority}.")

    def assign_task(self, staff_member):
        if self.tasks:
            task = heapq.heappop(self.tasks)
            task.assigned_staff = staff_member
            print(f"Task '{task.task_name}' assigned to {staff_member}.")
        else:
            print("No tasks available.")

    def view_tasks(self):
        for task in self.tasks:
            print(f"Task: {task.task_name}, Priority: {task.priority}, Assigned to: {task.assigned_staff}")
