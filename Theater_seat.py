ROWS = 10
LEFT_SEATS = 8
CENTER_SEATS = 12
RIGHT_SEATS = 8

TOTAL_COLS = LEFT_SEATS + CENTER_SEATS + RIGHT_SEATS + 2

seats = [["*" for _ in range(TOTAL_COLS)] for _ in range(ROWS)]

def get_seat_index(section, seat_num):
    if section == "L":
        return seat_num - 1
    elif section == "C":
        return LEFT_SEATS + 1 + seat_num - 1 
    elif section == "R":
        return LEFT_SEATS + CENTER_SEATS + 2 + seat_num - 1  
    return -1

def display_seats():
    print("\n--- THEATER SEATING ---")
    for row_index, row in enumerate(seats):
        row_str = ""
        for col_index, seat in enumerate(row):
            if col_index == LEFT_SEATS or col_index == LEFT_SEATS + CENTER_SEATS + 1:
                row_str += "  "  
            else:
                row_str += seat + " "
        print(f"Row {row_index+1:2}: {row_str}")
    print("\n* = Available | X = Booked")

def update_seat(action):
    section = input("Enter section (L = Left, C = Center, R = Right): ").strip().upper()
    if section not in ("L", "C", "R"):
        print("Invalid section.")
        return

    try:
        row = int(input(f"Enter row (1 to {ROWS}): "))
        if row < 1 or row > ROWS:
            print("Invalid row number.")
            return

        if section == "C":
            seat_num = int(input(f"Enter seat number in Center (1 to {CENTER_SEATS}): "))
            if seat_num < 1 or seat_num > CENTER_SEATS:
                print("Invalid seat number.")
                return
        else:
            seat_num = int(input(f"Enter seat number in {section} (1 to {LEFT_SEATS}): "))
            if seat_num < 1 or seat_num > LEFT_SEATS:
                print("Invalid seat number.")
                return

    except:
        print("Invalid input.")
        return

    col = get_seat_index(section, seat_num)
    if col == -1:
        print("Could not find seat.")
        return

    if action == "book":
        if seats[row-1][col] == "X":
            print("Seat already booked.")
        else:
            seats[row-1][col] = "X"
            print("Seat booked successfully.")
    elif action == "cancel":
        if seats[row-1][col] == "*":
            print("Seat is not booked.")
        else:
            seats[row-1][col] = "*"
            print("Booking cancelled.")

def main():
    
        display_seats()
        print("\n1. Book a seat")
        print("2. Cancel a seat")
        print("3. Exit")
        choice = input("Choose an option (1/2/3): ").strip()

        if choice == "1":
            update_seat("book")
            main()
        elif choice == "2":
            update_seat("cancel")
            main()
        elif choice == "3":
            print("Exiting the system!")
            
        else:
            print("Invalid choice.")

main()
