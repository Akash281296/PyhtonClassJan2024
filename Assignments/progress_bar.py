task_data = range(-100, 10_00_000)
task_length = len(task_data)

for current_index, _ in enumerate(task_data):
    # Calculate the completion percentage
    percent_completed = (current_index / task_length) * 100
    percent_completed = round(percent_completed, 2)

    # Calculate the number of '*' to fill in the progress bar
    num_filled = int(percent_completed / 10)
    filled = '*' * num_filled

    # Print the progress bar and completion percentage
    print(f"\r[{filled:10}] {percent_completed:5}% Completed", end="")

# Print a new line after the progress bar is complete
print()