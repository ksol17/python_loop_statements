# Task 1: Your mood today
import random

# List of moods
moods = ["Happy", "Sad", "Energetic", "Calm","Excited", "Confused"]

# Days of the week
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# Loop through each day of the week
for i in range(len(days)):
    # Randomly select mood
    mood = random.choice(moods)
    # Print the mood for the day
    print(f"On {days[i]}, you were feeling {mood}.")