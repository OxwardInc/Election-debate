import random

# Function to adjust popularity and decency scores
def adjust_scores(popularity, decency, pop_change, dec_change):
    return popularity + pop_change, decency + dec_change

# Function to display the weekly report
def weekly_report(week, popularity, decency):
    print("\nWeek:", week)
    print("Popularity:", popularity)
    print("Decency:", decency)

# Function to get the user's choice from a list of options
def get_user_choice(prompt, options):
    while True:
        print(prompt)
        for i, option in enumerate(options, 1):
            print(f"{i}. {option}")
        choice = int(input("Choose an option: "))
        if 1 <= choice <= len(options):
            return choice
        print("Invalid choice. Try again.")

# Main game loop
def run_game():
    # Initial scores
    popularity = 50
    decency = 50
    week = 1
    num_weeks = 10

    # Introduction
    print("Welcome, candidate!")
    party = input("Which party do you want to represent (e.g., Democrat, Republican, Independent)? ")

    # Game loop
    while week <= num_weeks:
        # Weekly report
        weekly_report(week, popularity, decency)

        # Debate question and answers
        questions = [
            ("What's your stance on healthcare?", ["Universal healthcare", "Private healthcare", "Mixed system"]),
            ("How do you approach climate change?", ["Strong regulations", "Market solutions", "Ignore"]),
            ("What is your policy on education?", ["Public funding", "Vouchers", "Charter schools"])
        ]

        # Randomly select a question
        question, answers = random.choice(questions)
        choice = get_user_choice(question, answers)

        # Impact on scores based on chosen answer
        if choice == 1:
            popularity, decency = adjust_scores(popularity, decency, 5, 10)
        elif choice == 2:
            popularity, decency = adjust_scores(popularity, decency, 10, 5)
        elif choice == 3:
            popularity, decency = adjust_scores(popularity, decency, 20, -10)

        # Offer a dirty scheme with a 30% chance
        if random.random() < 0.3:
            choice = get_user_choice("A lobbyist offers you a dirty scheme. Do you accept?", ["Yes", "No"])
            if choice == 1:
                popularity, decency = adjust_scores(popularity, decency, 15, -20)
            elif choice == 2:
                popularity, decency = adjust_scores(popularity, decency, -5, 10)

        # Move to the next week
        week += 1

    # Final report
    print("\nFinal Report")
    print("Party:", party)
    print("Final Popularity:", popularity)
    print("Final Decency:", decency)
    
    if popularity >= 70 and decency >= 70:
        print("Congratulations! You've won the presidency with integrity!")
    elif popularity >= 70 and decency < 70:
        print("You've won the presidency, but at what cost?")
    else:
        print("You didn't win the presidency. Better luck next time.")

# Run the game
run_game()
