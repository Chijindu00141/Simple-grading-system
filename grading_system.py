def get_grade(score):
    if 70 <= score <= 100:
        return 'A'
    elif 60 <= score < 70:
        return 'B'
    elif 50 <= score < 60:
        return 'C'
    elif 45 <= score < 50:
        return 'D'
    elif 40 <= score < 45:
        return 'E'
    elif 0 <= score < 40:
        return 'F'
    else:
        return 'Invalid score'

# User input
try:
    score = float(input("Enter your score (0-100): "))
    grade = get_grade(score)
    print(f"Your grade is: {grade}")
except ValueError:
    print("Please enter a valid number.")
