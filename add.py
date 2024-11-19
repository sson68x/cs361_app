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

