while True:
    # Get input from the user for 'n'
    user_input = input("Enter a number for 'n' (enter 'q' to quit): ")

    # Check if the user wants to quit
    if user_input.lower() == 'q':
        print("Exiting the program.")
        break

    try:
        n = int(user_input)

        # Print the pattern with "*" characters and excluding the center column
        for i in range(1, n + 1):
            spaces = " " * (n - i)
            stars = "*" * i
            pattern = spaces + stars + " " + stars
            print(pattern)
            
        for i in range(n - 1, 0, -1):
            spaces = " " * (n - i)
            stars = "*" * i
            pattern = spaces + stars + " " + stars
            print(pattern)

    except ValueError:
        print("Invalid input. Please enter a number or 'q' to quit.")


