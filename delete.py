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
            print("Deleting the workout will remove it permanently.")
            askAgain = int(input("Enter 1 to Continue or 2 to Cancel: "))

            if askAgain == 1:
                confirmDelete = input("Are you sure you want to delete this workout? (Y/N): ")

                if confirmDelete == "Y" or confirmDelete == "y":
                    removedWorkout = workouts.pop(workoutToDelete)
                    print(f"Workout '{removedWorkout}' has been removed.")

                elif confirmDelete == "N" or confirmDelete =="n":
                    return    
                    
                else:
                    print("Invalid selection.")

            elif askAgain == 2:
                return                

        else:
            print("Invalid selection.")

    except ValueError:
        print("Invalid input.")