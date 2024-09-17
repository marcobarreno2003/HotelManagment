# models.py
import heapq
from db_connection import connect_db

class User:
    """
    Represents a User in the system. Manages user registration and login with caching.
    """
    user_cache = {}  # In-memory cache for users

    def __init__(self, user_id, name, email, password, is_admin=False):
        self.id = user_id
        self.name = name
        self.email = email
        self.password = password
        self.is_admin = is_admin

    @staticmethod
    def register_user(name, email, password, is_admin=False):
        """
        Registers a new user and stores them in the database and cache.
        """
        connection = connect_db()
        if connection:
            try:
                cursor = connection.cursor()
                cursor.execute("""
                    INSERT INTO users (name, email, password, is_admin)
                    VALUES (%s, %s, %s, %s)
                """, (name, email, password, is_admin))
                connection.commit()
                cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
                user = cursor.fetchone()
                User.user_cache[user[0]] = user  # Cache user
                print(f"User {name} registered and cached.")
            except mysql.connector.Error as err:
                print(f"Error registering user: {err}")
            finally:
                connection.close()

    @staticmethod
    def login(email, password):
        """
        Handles user login by first checking the cache and then querying the database.
        """
        # Check the cache first
        for user in User.user_cache.values():
            if user[2] == email and user[3] == password:
                print(f"Welcome, {user[1]}! (from cache)")
                return user

        # Check the database if not in cache
        connection = connect_db()
        if connection:
            try:
                cursor = connection.cursor()
                cursor.execute("SELECT * FROM users WHERE email = %s AND password = %s", (email, password))
                user = cursor.fetchone()
                if user:
                    print(f"Welcome, {user[1]}!")
                    User.user_cache[user[0]] = user  # Cache user for future use
                    return user
                else:
                    print("Incorrect email or password.")
            except mysql.connector.Error as err:
                print(f"Error during login: {err}")
            finally:
                connection.close()
        return None


class Room:
    """
    Represents a Room in the hotel.
    """
    def __init__(self, number, room_type, price, available=True):
        self.number = number
        self.room_type = room_type
        self.price = price
        self.available = available

    def __lt__(self, other):
        """
        Comparison method for sorting rooms by price.
        """
        return self.price < other.price


class RoomManager:
    """
    Manages rooms with a heap (min-heap) for efficient price-based retrieval.
    """
    def __init__(self):
        self.rooms = []  # List of all rooms
        self.room_heap = []  # Min-heap for room prices

    def load_rooms(self):
        """
        Loads rooms from the database into the list and heap.
        """
        connection = connect_db()
        if connection:
            try:
                cursor = connection.cursor()
                cursor.execute("SELECT * FROM rooms WHERE available = TRUE ORDER BY number")
                room_data = cursor.fetchall()
                for room in room_data:
                    room_obj = Room(room[1], room[2], room[3], room[4])
                    self.rooms.append(room_obj)
                    heapq.heappush(self.room_heap, room_obj)  # Push to heap based on price
            except mysql.connector.Error as err:
                print(f"Error fetching rooms: {err}")
            finally:
                connection.close()

    def find_cheapest_room(self):
        """
        Returns the cheapest room using the heap.
        """
        if self.room_heap:
            return heapq.heappop(self.room_heap)  # Return and remove the cheapest room
        return None

    def find_room_by_number(self, number):
        """
        Finds a room by its number using a simple search.
        """
        for room in self.rooms:
            if room.number == number:
                return room
        return None


class HotelGraph:
    """
    A graph where nodes represent hotel locations and edges represent routes between them.
    Uses Dijkstra's Algorithm to find the shortest path between locations.
    """
    def __init__(self):
        self.graph = {}  # Dictionary of hotel locations and routes

    def add_location(self, hotel_name):
        """
        Adds a hotel location to the graph.
        """
        if hotel_name not in self.graph:
            self.graph[hotel_name] = []

    def add_route(self, hotel_from, hotel_to, cost):
        """
        Adds a route between two hotels with a cost (distance or time).
        """
        self.graph[hotel_from].append((hotel_to, cost))
        self.graph[hotel_to].append((hotel_from, cost))  # Undirected route

    def shortest_path(self, start, destination):
        """
        Uses Dijkstra's Algorithm to find the shortest path between two hotel locations.
        """
        queue = [(0, start)]  # Priority queue initialized with the start point
        distances = {location: float('inf') for location in self.graph}  # Infinite distance initially
        distances[start] = 0
        visited = set()

        while queue:
            current_cost, current_location = heapq.heappop(queue)

            if current_location in visited:
                continue
            visited.add(current_location)

            if current_location == destination:
                print(f"Shortest path from {start} to {destination} is {current_cost}")
                return current_cost

            for neighbor, route_cost in self.graph[current_location]:
                new_cost = current_cost + route_cost
                if new_cost < distances[neighbor]:
                    distances[neighbor] = new_cost
                    heapq.heappush(queue, (new_cost, neighbor))

        print(f"No path found from {start} to {destination}")
        return float('inf')
