from add import workouts

def listWorkout():
    if not workouts:
        print("There are no workouts currently.")

    else:
        print("Current Workouts: ")
        for index, workout in enumerate(workouts):
            listNumber = index + 1
            print(f"Workout #{listNumber}. {workout}")