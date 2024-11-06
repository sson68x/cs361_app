from add import workouts

def deleteWorkout():
    if not workouts:
        print("No workouts to delete.")
        return

    for index, workout in enumerate(workouts):
        print(f"{index + 1}. {workout}")

    try:
        workoutToDelete = int(input("Enter the # to delete: ")) - 1  # Zero-based index
        if 0 <= workoutToDelete < len(workouts):
            removedWorkout = workouts.pop(workoutToDelete)
            print(f"Workout '{removedWorkout}' has been removed.")

        else:
            print("Invalid selection.")

    except ValueError:
        print("Invalid input.")