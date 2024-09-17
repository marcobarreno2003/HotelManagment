# main.py
from models import RoomManager, HotelGraph

def menu():
    room_manager = RoomManager()
    hotel_graph = HotelGraph()
    
    room_manager.load_rooms()  # Load rooms from the database
    
    # Example: Adding hotel locations and routes
    hotel_graph.add_location("Hotel A")
    hotel_graph.add_location("Hotel B")
    hotel_graph.add_location("Hotel C")
    hotel_graph.add_route("Hotel A", "Hotel B", 10)
    hotel_graph.add_route("Hotel B", "Hotel C", 5)
    
    while True:
        print("\n1. Find the cheapest room")
        print("2. Find the shortest route between hotels")
        print("3. Exit")
        option = input("Choose an option: ")

        if option == "1":
            cheapest_room = room_manager.find_cheapest_room()
            if cheapest_room:
                print(f"Cheapest room: {cheapest_room.number}, Price: {cheapest_room.price}")
            else:
                print("No available rooms.")

        elif option == "2":
            start = input("Enter the starting hotel: ")
            end = input("Enter the destination hotel: ")
            hotel_graph.shortest_path(start, end)

        elif option == "3":
            print("Exiting the system.")
            break

if __name__ == "__main__":
    menu()
