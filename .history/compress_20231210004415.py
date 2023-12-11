import gzip
import base64
from urllib.parse import quote

def compress_and_encode(input_text):
    # Convert string to bytes
    input_bytes = input_text.encode('utf-8')

    # Compress the bytes using gzip
    compressed_data = gzip.compress(input_bytes)

    # Encode the compressed data using base64
    encoded_data = base64.urlsafe_b64encode(compressed_data).decode('utf-8')

    # Calculate compression percentage
    original_size = len(input_bytes)
    compressed_size = len(compressed_data)
    compression_percentage = ((original_size - compressed_size) / original_size) * 100

    # Print compression percentage
    print(f"Compression Percentage: {compression_percentage:.2f}%")

    return encoded_data

def decode_and_decompress(encoded_data):
    # Decode the base64-encoded data
    compressed_data = base64.urlsafe_b64decode(encoded_data)

    # Decompress the data using gzip
    decompressed_data = gzip.decompress(compressed_data)

    # Convert bytes back to string
    output_text = decompressed_data.decode('utf-8')

    return output_text

# Example usage
original_text = """
This is a sample text with paragraphs.
It can contain multiple lines of text.
The compression algorithm will compress this text into a URL-safe format.
"""

# Compress and encode the text
encoded_text = compress_and_encode(original_text)

# Print the encoded text
print("Encoded Text:")
print(encoded_text)

# Decode and decompress the text
decoded_text = decode_and_decompress(encoded_text)

# Print the decoded text
print("\nDecoded Text:")
print(decoded_text)
