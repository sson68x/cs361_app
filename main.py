from add import addWorkout
from delete import deleteWorkout
from list import listWorkout


if __name__ == "__main__":
    print("Welcome to the Workout List app!")
    print("This app helps you track and manage your workout routines.")
    print("Let's get started on your fitness journey!")
    
    while True:
        print("\n")
        print("Please select one of the following options.")
        print("-------------------------------------------")
        print("1. Add a workout")
        print("2. Delete a workout")
        print("3. Workout List")
        print("4. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            addWorkout()
            
        elif choice == "2":
            deleteWorkout()

        elif choice == "3":
            listWorkout()
        
        elif choice == "4":
            break
        
        else:
            print("Invalid input. Please try again.")
    
    print("Thank you for using the Workout List app. Goodbye.")