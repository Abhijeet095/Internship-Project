import random
import string

# Pre-defined lists of adjectives and nouns
adjectives = ['Cool', 'Happy', 'Bright', 'Silly', 'Mighty']
nouns = ['Tiger', 'Dragon', 'Panda', 'Phoenix', 'Unicorn']

def generate_username(include_numbers=True, include_special_chars=True):
    # Select random adjective and noun
    adjective = random.choice(adjectives)
    noun = random.choice(nouns)
    username = adjective + noun
    
    # Add numbers if specified
    if include_numbers:
        username += str(random.randint(0, 999))

    # Add special characters if specified
    if include_special_chars:
        special_chars = random.choice(string.punctuation)
        username += special_chars

    return username

def save_username_to_file(username, filename='usernames.txt'):
    with open(filename, 'a') as file:
        file.write(username + '\n')

def get_user_input(prompt, valid_options):
    while True:
        user_input = input(prompt).lower()
        if user_input in valid_options:
            return user_input
        else:
            print("Invalid option. Please try again.")

def main():
    print("Welcome to the Username Generator!")
    
    include_numbers = get_user_input("Include numbers in username? (y/n): ", ['y', 'n']) == 'y'
    include_special_chars = get_user_input("Include special characters in username? (y/n): ", ['y', 'n']) == 'y'
    
    username = generate_username(include_numbers, include_special_chars)
    print(f"Generated Username: {username}")
    
    save_option = get_user_input("Would you like to save the username to a file? (y/n): ", ['y', 'n']) == 'y'
    if save_option:
        save_username_to_file(username)
        print("Username saved to 'usernames.txt'")

if __name__ == "__main__":
    main()
