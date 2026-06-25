import json

FILE_NAME = "scores.json"


def load_data():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except:
        return {"scores": []}


def save_data(data):
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)


def start_quiz():
    
    data = load_data()

    score = 0

    print("\nQuestion 1:")
    answer = input("What is the capital of France? ")

    if answer.lower() == "paris":
        score += 1

    print("\nQuestion 2:")
    answer = input("What is 5 + 5? ")

    if answer == "10":
        score += 1

    print("\nQuestion 3:")
    answer = input("What programming language are you learning? ")

    if answer.lower() == "python":
        score += 1

    data["scores"].append(score)

    save_data(data)

    print(f"\nYour score: {score}/3")


def view_scores():
    data = load_data()

    if not data["scores"]:
        print("\nNo scores recorded yet.")
        return

    print("\nPrevious Scores:")
    
    for i, score in enumerate(data["scores"], start=1):
        print(f"Attempt {i}: {score}/3")

    total = len(data["scores"])
    average = sum(data["scores"]) / total

    print(f"\nTotal attempts: {total}")
    print(f"Average score: {average:.2f}/3")


def delete_scores():
    data = load_data()

    if not data["scores"]:
        print("\nNo scores to delete.")
        return

    confirm = input("\nAre you sure you want to delete all scores? (yes/no): ")

    if confirm.lower() == "yes":
        data["scores"] = []
        save_data(data)
        print("All scores deleted.")
    else:
        print("Deletion cancelled.")


def menu():

    while True:

        print("\n===== QUIZ APPLICATION =====")
        print("1. Start Quiz")
        print("2. View Score History")
        print("3. Delete Score History")
        print("4. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            start_quiz()

        elif choice == "2":
            view_scores()

        elif choice == "3":
            delete_scores()

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid option.")


menu()