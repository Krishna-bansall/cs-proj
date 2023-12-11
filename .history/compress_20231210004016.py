def compress_text(input_text):
    compressed_text = ""
    count = 1

    # Iterate through the input text
    for i in range(1, len(input_text)):
        if input_text[i] == input_text[i - 1]:
            # Increment the count if the current character is the same as the previous one
            count += 1
        else:
            # Append the character and its count to the compressed text
            compressed_text += input_text[i - 1] + str(count)
            count = 1

    # Append the last character and its count
    compressed_text += input_text[-1] + str(count)

    return compressed_text

def decompress_text(compressed_text):
    decompressed_text = ""

    # Iterate through the compressed text
    i = 0
    while i < len(compressed_text):
        # Extract the character
        char = compressed_text[i]

        # Move to the next index to get the count
        i += 1

        # Extract the count as a string until a non-digit character is encountered
        count_str = ""
        while i < len(compressed_text) and compressed_text[i].isdigit():
            count_str += compressed_text[i]
            i += 1

        # Convert the count string to an integer
        count = int(count_str)

        # Append the character repeated count times to the decompressed text
        decompressed_text += char * count

    return decompressed_text

# Example
original_text = "aaabbbbcccddee"
compressed_text = compress_text(original_text)
decompressed_text = decompress_text(compressed_text)

print("Original text:", original_text)
print("Compressed text:", compressed_text)
print("Decompressed text:", decompressed_text)
