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
Certainly! Here's a 35-paragraph poem for you:

In a garden of twilight, where shadows dance,
Whispers of the wind weave a mystic trance.
Moonlight caresses the petals so fair,
As stars in the night sky tenderly share.

Beneath the ancient oak, a storyteller's throne,
Leaves rustle tales in a language unknown.
Mysteries unfold in the silver moon's gleam,
A symphony of nature, a celestial dream.

On the canvas of night, constellations ignite,
A cosmic ballet, a celestial light.
Galaxies twirl in a cosmic ballet,
Painting the heavens in hues of astral ballet.

A river of stardust, a celestial stream,
Flows through the cosmos, an ethereal dream.
Planets pirouette in a cosmic waltz,
As comets compose their ephemeral scherzo.

Oceans of silence, a celestial sea,
Reflect the wonders of infinity.
In the silence between heartbeats and breaths,
The universe whispers its secrets in depth.

Mountains stand tall, ancient guardians of time,
Their peaks touch the heavens in prose and rhyme.
Valleys below cradle stories untold,
As time's river weaves tales, both young and old.

A phoenix rises from ashes of night,
In the alchemy of dawn, pure and bright.
Sunrise paints the sky in hues of fire,
A canvas ablaze, a celestial pyre.

Through meadows adorned in dew-kissed attire,
The dance of the zephyrs stirs nature's lyre.
Petals unfold in the dawn's tender light,
A symphony of colors, morning's delight.

Butterflies waltz on a canvas of air,
Their delicate wings, a ballet so rare.
Whispers of breeze carry secrets untold,
As nature's tableau gracefully unfolds.

The murmur of leaves in an ancient wood,
A serenade to life, both bad and good.
Beneath the arch of the emerald canopy,
Earth's heartbeat echoes in soft symphony.

In the tapestry woven by time's swift hand,
Echoes of laughter and footsteps in sand.
A journey unfolds, a story untold,
In the book of existence, both timid and bold.

Footprints in snow, a transient art,
Marking the passage of a beating heart.
Winter's embrace, a blanket so white,
A silent sonnet to the hush of night.

Through seasons that change with the turning tide,
In the ebb and flow, life's rhythm and guide.
Each paragraph written in nature's own hand,
A poem of existence, both grand and unplanned.

So, in this verse, let the echoes resound,
In the vast cosmic silence, let words be found.
A poem of life, both fleeting and vast,
A journey of moments, a tapestry cast.
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
