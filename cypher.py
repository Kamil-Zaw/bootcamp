def encode_message(message):
    encoded_message = ""
    for char in message:
        if char.isalpha():  # Check if the character is an alphabet
            char = char.lower()  # Convert the character to lowercase
            encoded_char = chr((ord(char) - ord('a') + 15) % 26 + ord('a'))
            encoded_message += encoded_char
        else:
            encoded_message += char   
    return encoded_message

# Example usage
message = "Kamil"
encoded_message = encode_message(message)
print("Encoded Message:", encoded_message)