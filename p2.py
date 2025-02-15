def get_user_input():
    #Prompts the user to enter valid input.
    #Handles the empty input.
    while True:
        user_input = input("Please enter a sentence or paragraph: ").strip()
        if not user_input:
            print("Input cannot be empty. Please enter a valid sentence/paragraph.")
        else:
            return user_input

def word_count(str):
    #Count the no.of words in the input.
    words = str.split()
    return len(words)
    

def main():
    #Main function to execute the program.
    print("Welcome to WORD COUNTER!")

    #To get input from the user.
    user_input = get_user_input()

    #Count the no.of words.
    wordcount = word_count(user_input)

    # Display the word count
    print(f"The number of words in the input is: {wordcount}")

if __name__ == "__main__":
    main()