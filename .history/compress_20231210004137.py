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
original_text = '''Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum nec justo auctor, convallis nulla in, facilisis neque. In hac habitasse platea dictumst. Proin eget efficitur lacus. Suspendisse potenti. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Sed venenatis augue nec erat aliquam, at facilisis massa cursus. Sed ultrices fermentum arcu, sit amet vehicula ligula tempor ut.

Nulla facilisi. Sed ultricies, velit nec hendrerit ultrices, ligula mauris congue velit, id vulputate orci elit vel tortor. Quisque eget nisl non nisi luctus sodales. Integer ut urna bibendum, varius ligula nec, tristique neque. Aliquam erat volutpat. Sed posuere malesuada arcu, non facilisis orci efficitur eu. Vivamus et varius ligula. Vestibulum tristique, nunc nec gravida tristique, justo leo vehicula nunc, ac suscipit ex odio vel urna.

Praesent tincidunt quam at elit mattis lacinia. Curabitur vitae ex eu libero condimentum fermentum a a magna. Sed tincidunt augue eget congue imperdiet. Vivamus tristique odio id neque consectetur, vel laoreet libero venenatis. Ut interdum velit auctor, ultrices libero ac, fermentum elit. Integer tincidunt mauris eu efficitur blandit. Aliquam id elit vel purus pellentesque bibendum nec nec libero.

Fusce suscipit massa a lectus ultricies, ac bibendum velit vestibulum. Aenean scelerisque lacus quis enim malesuada, eu consequat purus tristique. Maecenas accumsan, nisi et condimentum feugiat, justo quam fermentum tortor, at luctus leo tortor ac nisi. Vestibulum commodo ullamcorper fermentum. Aenean dignissim metus vel tellus gravida, sit amet vestibulum justo consequat. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas.

Quisque in ultricies neque, vel lacinia nulla. Integer bibendum massa eu enim interdum, eu finibus quam bibendum. Vestibulum auctor facilisis nunc, nec bibendum orci suscipit vel. Donec nec orci vel justo aliquam tristique vel a arcu. Nam vitae ligula euismod, eleifend urna sit amet, imperdiet velit. Aenean congue, nunc vel feugiat vulputate, tortor nisi ultricies tellus, in rhoncus libero risus ut libero. Suspendisse potenti. Integer nec lectus at erat fermentum varius a at lacus.





'''
compressed_text = compress_text(original_text)
decompressed_text = decompress_text(compressed_text)

print("Original text:", original_text)
print("Compressed text:", compressed_text)
print("Decompressed text:", decompressed_text)
