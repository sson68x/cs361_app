workouts = []
predefined_workouts = ["Push-ups", "Squats", "Lunges", "Plank", "Jumping Jacks"]

def addWorkout():
    print("How would you like to add a workout?")
    print("1. Add workout manually")
    print("2. Choose from a predefined list")

    choice = input("Enter your choice: ")

    if choice == "1":
        workout = input("Please enter a workout: ")
        workouts.append(workout)
        print(f"Workout '{workout}' added to the list.")

    elif choice == "2":
        print("Select a workout from the list:")

        for index, workout in enumerate(predefined_workouts):
            print(f"{index + 1}. {workout}")

        try:
            workout_choice = int(input("Enter the number of the workout to add: ")) - 1

            if 0 <= workout_choice < len(predefined_workouts):
                selected_workout = predefined_workouts[workout_choice]
                workouts.append(selected_workout)
                print(f"Workout '{selected_workout}' added to the list.")

            else:
                print("Invalid selection.")

        except ValueError:
            print("Invalid input. Please enter a number.")

    else:
        print("Invalid choice. Please select 1 or 2.")

def deleteWorkout():
    if not workouts:
        print("No workouts to delete.")
        return

    for index, workout in enumerate(workouts):
        print(f"Workout #{index + 1}. {workout}")

    try:
        workoutToDelete = int(input("Enter the # to delete: ")) - 1  # Zero-based index
        if 0 <= workoutToDelete < len(workouts):
            print("Deleting the workout will remove it permanently.")
            askAgain = int(input("Enter 1 to Continue or 2 to Cancel: "))

            if askAgain == 1:
                confirmDelete = input("Are you sure you want to delete this workout? (Y/N): ").lower()

                if confirmDelete == "y":
                    removedWorkout = workouts.pop(workoutToDelete)
                    print(f"Workout '{removedWorkout}' has been removed.")

                elif confirmDelete == "n":
                    return    
                    
                else:
                    print("Invalid selection.")

            elif askAgain == 2:
                return                

        else:
            print("Invalid selection.")

    except ValueError:
        print("Invalid input.")

def listWorkout():
    if not workouts:
        print("There are no workouts currently.")

    else:
        print("Current Workouts: ")
        for index, workout in enumerate(workouts):
            listNumber = index + 1
            print(f"Workout #{listNumber}. {workout}")


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