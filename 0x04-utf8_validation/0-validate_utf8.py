#!/usr/bin/python3
def validUTF8(data):
    # Variable to track the number of bytes in the current UTF-8 character
    num_bytes = 0

    for byte in data:
        # Check if the current byte is the start of a new UTF-8 character
        if num_bytes == 0:
            if (byte >> 7) == 0b0:
                # Single-byte character
                num_bytes = 0
            elif (byte >> 5) == 0b110:
                # Two-byte character
                num_bytes = 1
            elif (byte >> 4) == 0b1110:
                # Three-byte character
                num_bytes = 2
            elif (byte >> 3) == 0b11110:
                # Four-byte character
                num_bytes = 3
            else:
                # Invalid start of a character
                return False
        else:
            # Check if the current byte is a continuation byte
            if (byte >> 6) == 0b10:
                num_bytes -= 1
            else:
                # Invalid continuation byte
                return False

    # Check if all characters are complete (num_bytes is back to 0)
    return num_bytes == 0
