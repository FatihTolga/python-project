age = input("Are you a cigarette addict older than 75 years old? Yes/No: ").strip().title()

chronic = input("Do you have a severe chronic disease? Yes/No: ").strip().title()

immune = input("Is your immune system too weak? Yes/No: ").strip().title()

if age and chronic and immune == "Yes":
    print("You are in risky group")
elif age and chronic and immune == "No":
    print("You are not in risky group")
