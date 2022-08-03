#!/usr/bin/env python3


def format_into_five(string):
    formatted_chars = []
    for index, char in enumerate(string, start=1):
        formatted_chars.append(char)
        if not index % 5:
            formatted_chars.append(" ")
    return "".join(formatted_chars).strip()
