# Task 1: Your mood tracker

import random

 # List of moods
moods = ["Happy", "Sad", "Energetic", "Calm", "Excited", "Tired", "Confused"]

# Days of the week
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# Times of the day
times_of_the_day = ["morning", "afternoon", "evening"]

# Nested loop to iterate over days and times of the day
for day in days:
    for time in times_of_the_day:
        # Randomly select a mood
        mood = random.choice(moods)
        # Print the mood for the current day and time
        print(f"On {day} {time} you were {mood}.")