import base64
import re
from common_imports import *

# Function to encode a string to Base64
def encode_to_base64(input_string):
    # Convert string to bytes
    input_bytes = input_string.encode('utf-8')

    # Encode bytes to Base64
    encoded_bytes = base64.b64encode(input_bytes)

    # Convert bytes back to a UTF-8 string
    encoded_string = encoded_bytes.decode('utf-8')

    return encoded_string


def decode_from_base64(encoded_string):
    # Convert UTF-8 string to bytes
    encoded_bytes = encoded_string.encode('utf-8')

    # Decode Base64 bytes
    decoded_bytes = base64.b64decode(encoded_bytes)

    # Convert bytes back to UTF-8 string
    decoded_string = decoded_bytes.decode('utf-8')

    return decoded_string


def readprofile(filepath):

    with open(filepath, 'r+') as file:
        file_content = file.read()
        return decode_from_base64(file_content)


def extract_api_key(input_string):
    # Define the regex pattern to match "appid = " followed by the API key
    pattern = r"appid\s*=\s*([^\s\n]+)"

    # Search for the pattern in the input string
    match = re.search(pattern, input_string)

    # If a match is found, return the first captured group (the API key)
    if match:
        return match.group(1)
    else:
        return None
