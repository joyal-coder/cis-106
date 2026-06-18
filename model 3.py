# Problem 1: Weighted Exam Score Calculator

# Input exam scores from the keyboard
exam1 = float(input("Enter the first exam score: "))
exam2 = float(input("Enter the second exam score: "))

# Calculate total score using 60% and 40% weightings
total_score = (exam1 * 0.60) + (exam2 * 0.40)

# Display the total formatted to two decimal places
print(f"Total Weighted Score: {total_score:.2f}")
