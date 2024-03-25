def generate_ascii_art(text):
    # Define ASCII art characters for different levels of brightness
    ascii_chars = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

    # Initialize an empty string to store the ASCII art
    ascii_art = ""

    # Iterate over each character in the input text
    for char in text:
        # Get the ASCII value of the character
        ascii_value = ord(char)
        
        # Convert the ASCII value to an index in the range 0-9
        index = ascii_value % 10

        # Append the corresponding ASCII character to the ASCII art string
        ascii_art += ascii_chars[index]

    # Return the generated ASCII art
    return ascii_art

# Example usage:
input_text = "Hello, ASCII!"
ascii_art = generate_ascii_art(input_text)
print(ascii_art)
