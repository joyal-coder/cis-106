# Problem 5: Weighted Exam Score Calculator (Repeat)

# Input exam scores
exam1 = float(input("Enter the first exam score: "))
exam2 = float(input("Enter the second exam score: "))

# Calculate total score (60% / 40%)
total_score = (exam1 * 0.60) + (exam2 * 0.40)

# Display the total score
print(f"Total Weighted Score: {total_score:.2f}")
