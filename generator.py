#!/usr/bin/env python3
import subprocess

from helpers import format_into_five

result = subprocess.run(
    ["shuf", "--random-source=/dev/random", "-r", "-i 0-99999", "-n 500"],
    stdout=subprocess.PIPE,
    check=True,
    encoding="utf-8",
)

codes = []
for line in result.stdout.rstrip("\n").split("\n"):
    number = int(line)
    codes.append("{:05d}".format(number))

print(format_into_five("".join(codes)))
