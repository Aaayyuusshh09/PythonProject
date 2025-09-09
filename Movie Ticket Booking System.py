"""
Movie Ticket Booking System
Covers: input, variables, data types, lists, dicts, functions, loops,
if-else, nesting, global vars/constants, docstrings
"""

# ---- Global Constant ----
TICKET_PRICE = 200

# ---- Movies Database ----
movies = {
    "1": {"name": "Avengers: Endgame", "seats": 50},
    "2": {"name": "Spider-Man: No Way Home", "seats": 40},
    "3": {"name": "Inception", "seats": 30},
}

# ---- Bookings List ----
bookings = []  # store each booking as dict


# ---- Functions ----

def display_movies():
    """Show available movies and seats"""
    print("\n🎬 Available Movies:")
    for mid, details in movies.items():
        print(f"{mid}. {details['name']} (Seats left: {details['seats']})")


def book_ticket():
    """Book tickets for a movie"""
    display_movies()
    choice = input("Enter movie number: ")

    if choice not in movies:
        print("❌ Invalid movie selection.")
        return

    name = input("Enter your name: ")
    try:
        num_tickets = int(input("Enter number of tickets: "))
    except ValueError:
        print("⚠️ Invalid input. Tickets must be a number.")
        return

    if num_tickets <= 0:
        print("⚠️ Number of tickets must be at least 1.")
        return

    if num_tickets > movies[choice]["seats"]:
        print("❌ Not enough seats available.")
        return

    # Update seats
    movies[choice]["seats"] -= num_tickets

    # Calculate total price
    total = num_tickets * TICKET_PRICE

    # Save booking
    booking = {
        "customer": name,
        "movie": movies[choice]["name"],
        "tickets": num_tickets,
        "total_price": total
    }
    bookings.append(booking)

    print(f"✅ Booking Confirmed! {num_tickets} tickets for {movies[choice]['name']}")
    print(f"💰 Total Price: ₹{total}")


def show_bookings():
    """Display all bookings made"""
    if not bookings:
        print("⚠️ No bookings yet.")
        return

    print("\n--- Booking History ---")
    for b in bookings:
        print(f"👤 {b['customer']} | 🎬 {b['movie']} | 🎟️ {b['tickets']} | 💰 ₹{b['total_price']}")


def ticket_system_menu():
    """Main menu for ticket booking"""
    while True:
        print("\n--- Movie Ticket Booking System ---")
        print("1. Show Movies")
        print("2. Book Ticket")
        print("3. Show All Bookings")
        print("4. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            display_movies()
        elif choice == "2":
            book_ticket()
        elif choice == "3":
            show_bookings()
        elif choice == "4":
            print("👋 Thank you for using our system!")
            break
        else:
            print("❌ Invalid choice, try again.")


# ---- Run Program ----
ticket_system_menu()
