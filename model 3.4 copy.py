# Problem 4: Job Earnings Splitter

# Input total money earned
total_amount = float(input("Enter the total amount received for the job: "))

# Split evenly among 3 people
individual_share = total_amount / 3

# Display individual earnings
print(f"Each person will receive: ${individual_share:.2f}")
