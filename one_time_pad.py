#!/usr/bin/env python3
from helpers import format_into_five

ALPHABET = {
    "A": "1",
    "B": "70",
    "C": "71",
    "D": "72",
    "E": "2",
    "F": "73",
    "G": "74",
    "H": "75",
    "I": "3",
    "J": "76",
    "K": "77",
    "L": "78",
    "M": "79",
    "N": "4",
    "O": "5",
    "P": "80",
    "Q": "81",
    "R": "82",
    "S": "83",
    "T": "6",
    "U": "84",
    "V": "85",
    "W": "86",
    "X": "87",
    "Y": "88",
    "Z": "89",
}
SPECIAL_CHARS = {
    "FIG": "90",
    ".": "91",
    ":": "92",
    "'": "93",
    "/": "94",
    "+": "95",
    "-": "96",
    "=": "97",
    "REQ": "98",
    " ": "99",
}
INTEGERS = {
    "0": "000",
    "1": "111",
    "2": "222",
    "3": "333",
    "4": "444",
    "5": "555",
    "6": "666",
    "7": "777",
    "8": "888",
    "9": "999",
}

CODEBOOK = {
    "ABORT": "001",
    "AGENT": "018",
    "AIRPORT": "023",
    "ANSWER": "035",
    "AUTHORITY": "042",
    "BEGINS AT": "045",
    "CAR": "123",
    "CHALLENGE CODE": "056",
    "CODEBOOK": "052",
    "COORDINATES": "061",
    "MISSION": "078",
    "SATELLITE": "135",
    "SHIP": "132",
    "SUBWAY": "147",
    "SUCCESS": "128",
    "TELEPHONE": "156",
    "TRAIN": "112",
    "TRANSFER": "158",
    "TRANSIT": "095",
    "TRAVEL": "117",
    "UNABLE TO": "165",
    "URGENT": "163",
    "VERIFY": "167",
    "YESTERDAY": "173",
}
EVERYTHING_BUT_CODEBOOK = {**ALPHABET, **INTEGERS, **SPECIAL_CHARS}
CONVERSION_TABLE = {**EVERYTHING_BUT_CODEBOOK, **CODEBOOK}
DECODE_CONVERSION_TABLE = dict(map(reversed, CONVERSION_TABLE.items()))


def encode_without_codebook(message):
    encoded = []
    for char in message:
        encoded_char = EVERYTHING_BUT_CODEBOOK[char]
        encoded.append(encoded_char)
    return "".join(encoded)


def encode_with_codebook(encoded_message):
    encoded_codebook = {}
    for word, code in CODEBOOK.items():
        encoded_codebook[encode_without_codebook(word)] = code

    for encoded_word, code in encoded_codebook.items():
        encoded_message = encoded_message.replace(encoded_word, code)
    return "".join(encoded_message)


def encode(message):
    return encode_with_codebook(encode_without_codebook(message))


def decode(encoded_message):
    has_been_decoded_count = 0
    decoded_message = ""
    decoded_list = sorted(
        CONVERSION_TABLE,
        key=lambda k: len(CONVERSION_TABLE[k]),
        reverse=True,
    )
    # Move the space to just after the numbers.
    decoded_list.remove(" ")
    decoded_list.insert(10, " ")
    while decoded_values := _chunk_decode(encoded_message, has_been_decoded_count):
        (decoded, has_been_decoded_count) = decoded_values
        if decoded is None:
            break
        decoded_message += decoded
    return decoded_message


def _chunk_decode(encoded_message, has_been_decoded_count):
    first_non_decoded_chars = get_first_non_decoded_chars(
        encoded_message, has_been_decoded_count, 3
    )
    if first_non_decoded_chars is None:
        return
    for i in range(3, 0, -1):
        if decoded := DECODE_CONVERSION_TABLE.get(first_non_decoded_chars[:i]):
            has_been_decoded_count += i
            return decoded, has_been_decoded_count
    return decoded, has_been_decoded_count


def get_first_non_decoded_chars(
    encoded_message, has_been_decoded_count, number_of_chars
):
    start = has_been_decoded_count
    end = start + number_of_chars
    return encoded_message[start:end]


def decrypt(encrypted_message, relevant_otp):
    decrypted_char_list = []
    for index, encrypted_char in enumerate(encrypted_message):
        corresponding_otp_char = int(relevant_otp[index])
        encrypted_int = int(encrypted_char)
        decrypted_int = encrypted_int + corresponding_otp_char
        decrypted_char_list.append(str(decrypted_int)[-1])
    return "".join(decrypted_char_list)


def encrypt(encoded_message, relevant_otp):
    encrypted_char_list = []
    for index, encoded_char in enumerate(encoded_message):
        corresponding_otp_char = int(relevant_otp[index])
        encoded_int = int(encoded_char)
        if corresponding_otp_char > encoded_int:
            encoded_int += 10
        encrypted_char_list.append(str(encoded_int - corresponding_otp_char))

    return "".join(encrypted_char_list)
