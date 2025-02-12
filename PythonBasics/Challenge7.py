from secret import clue

def lucky():
    first_three_bits = clue(right_shift=5)

    next_eight_bits = clue(left_shift=6)

    middle_bits = clue(bw_and=8)

    other_bits = clue(bw_or=223)

    address = (first_three_bits << 11) | (next_eight_bits << 3) | middle_bits | other_bits

    return address