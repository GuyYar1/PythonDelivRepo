import base64


# Function to encode a string to Base64
def encode_to_base64(input_string):
    # Convert string to bytes
    input_bytes = input_string.encode('utf-8')

    # Encode bytes to Base64
    encoded_bytes = base64.b64encode(input_bytes)

    # Convert bytes back to a UTF-8 string
    encoded_string = encoded_bytes.decode('utf-8')

    return encoded_string
