"""One Line, One Minute: The Vending Machine Pickup Line Contest.

The joke: a vending machine flirts like a smooth-talking admirer who
knows it messed up. It watched you press B4, then dropped B5 instead —
a heartbreak in snack form. Now it is making amends the only way a
vending machine can: by offering the next one free, "on the coil,"
playing on the bar phrase "on the house" with the spiral coil that
actually holds and drops the snacks.
"""

import os

ENTRY = "Hey. I watched you press B4 and walk away hurt when I dropped B5. Let me make it up to you — this one is on the coil."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
