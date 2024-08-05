# Open the file "story.txt" in read mode
with open("story.txt", "r") as f:
    # Read the entire content of the file
    story = f.read()

    # Initialize a set to store unique words
    words = set()
    start_of_word = -1

    # Define the start and end delimiters for the target words
    target_start = "<"
    target_end = ">"

# Iterate through each character in the story
for i, char in enumerate(story):
    # Check if the character is the start delimiter
    if char == target_start:
        start_of_word = i

    # Check if the character is the end delimiter and a start has been found
    if char == target_end and start_of_word != -1:
        # Extract the word between the delimiters
        word = story[start_of_word: i + 1]
        # Add the word to the set
        words.add(word)
        # Reset the start_of_word
        start_of_word = -1

# Initialize a dictionary to store user inputs for each word
answers = {}

# Prompt the user to enter a replacement for each word
for word in words:
    answer = input("Enter the word for " + word + ":")
    answers[word] = answer

# Replace each word in the story with the user's input
for word in words:
    story = story.replace(word, answers[word])

# Print the modified story
print(story)