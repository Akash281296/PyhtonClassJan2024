# Initialize an empty queue
queue = []

# Function to push an element into the queue
def push(element):
    queue.append(element)
    print(f"Added {element} to the queue")

# Function to pop an element from the queue
def pop():
    if not is_empty():
        popped_element = queue.pop(0)
        print(f"Removed {popped_element} from the queue")
        return popped_element
    else:
        print("Queue is empty. Cannot pop.")

# Function to check the size of the queue
def status():
    print(f"Current queue size: {len(queue)}")

# Function to check if the queue is empty
def is_empty():
    return len(queue) == 0

# Main loop to interact with the queue
while True:
    print("\nQueue Operations:")
    print("1. Push")
    print("2. Pop")
    print("3. Status")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        value = input("Enter the value to push: ")
        push(value)
    elif choice == "2":
        pop()
    elif choice == "3":
        status()
    elif choice == "4":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please enter a valid option.")