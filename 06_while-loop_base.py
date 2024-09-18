'''
Write Python program :
    get an input for a number to count to
    if input is "q" or "quit", the program exits
    else write numbers from 1 to the number in one line, separated by space and goes back to the input
'''

def count_to_number():
    while True:
        user_input = input("Enter a number to count to (or 'q'/'quit' to exit): ")
        
        if user_input.lower() in ["q", "quit"]:
            print("Exiting the program.")
            break
        
        try:
            count_to = int(user_input)
            numbers = " ".join(str(i) for i in range(1, count_to + 1))
            print(numbers)
        except ValueError:
            print("Please enter a valid number or 'q'/'quit' to exit.")

count_to_number()