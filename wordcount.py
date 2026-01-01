from collections import Counter
import string

print("Word Count Tool")

try:
    filename = input("Enter the filename: ")

    with open(filename, "r") as file:
        content = file.read()

    if not content.strip():
        print("The file is empty.")
    else:
        #  for counting Total lines
        file = open(filename, "r")
        lines = file.readlines()
        total_lines = len(lines)
        file.close()

        #  for counting Total words and characters
        words = content.split()
        total_words = len(words)
        total_chars = len(content)

        # Word frequency (ignore punctuation and case)
        translator = str.maketrans('', '', string.punctuation)
        cleaned_words = [w.translate(translator).lower() for w in words]
        word_freq = Counter(cleaned_words)

        print("\n--- Analysis Results ---")
        print(f"Total lines      : {total_lines}")
        print(f"Total words      : {total_words}")
        print(f"Total characters : {total_chars}")
        print("\nTop 10 Most Common Words:")
        for word, freq in word_freq.most_common(10):
            print(f"{word} : {freq}")

except FileNotFoundError:
    print("File not found. Please check the file name.")

except Exception as e:
    print("An unexpected error occurred:", e)

