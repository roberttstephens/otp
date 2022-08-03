#!/usr/bin/env python3
from one_time_pad import (
    decode,
    encode,
    encrypt,
    decrypt,
)

MESSAGE = "MISSION BEGINS AT DAWN.TRAVEL TO COORDINATES:30UXC55106318."
ONE_TIME_PAD = "84034 78941 61496 64831 91801 10205 95258 18506 45423 46031 79803 45919 98375 86416 83649".replace(
    " ", ""
)
ENCODED_MESSAGE = "07899 04599 72186 49111 79965 99061 92333 00084 87715 55555 11100 06663 33111 88891".replace(
    " ", ""
)
ENCRYPTED_MESSAGE = (
    "39958 43103 18355 58310 69760 04813 84837 65661 41784 86752 76291 18398 57705 05252"
).replace(" ", "")

relevant_otp = ONE_TIME_PAD[5:]
key_indicator = ONE_TIME_PAD[:5]  # The starting point to encode.


def test_end_to_end():
    message = "THIS IS A TEST MESSAGE. ABC EASY AS 123."
    encoded = encode(message)
    decoded = decode(encoded)
    assert message == decoded
    encrypted = encrypt(encoded, relevant_otp)
    decrypted = decrypt(encrypted, relevant_otp)
    assert decrypted == encoded
    decoded_after_decrypted = decode(decrypted)
    assert decoded_after_decrypted == message


def test_encode():
    encoded_message = encode(MESSAGE)
    assert encoded_message == ENCODED_MESSAGE


def test_decrypt():
    assert decrypt(ENCRYPTED_MESSAGE, relevant_otp) == ENCODED_MESSAGE


def test_decode():
    assert decode(ENCODED_MESSAGE) == MESSAGE


def test_encrypt():
    assert (
        encrypt(ENCODED_MESSAGE, relevant_otp)
        == "3995843103183555831069760048138483765661417848675276291183985770505252"
    )
