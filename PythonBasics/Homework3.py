VALID_TONES_SET = {'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B'}
VALID_TONES_LIST = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
INTERVALS = {
    0: 'unison',
    1: 'minor 2nd',
    2: 'major 2nd',
    3: 'minor 3rd',
    4: 'major 3rd',
    5: 'perfect 4th',
    6: 'diminished 5th',
    7: 'perfect 5th',
    8: 'minor 6th',
    9: 'major 6th',
    10: 'minor 7th',
    11: 'major 7th'}


class Tone:
    """Represents a musical tone."""

    def __init__(self, note):
        self.note = note

    @property
    def note(self):
        return self._note

    @note.setter
    def note(self, value):
        if value not in VALID_TONES_SET:
            raise ValueError(f'{value} is not a valid musical tone')
        self._note = value

    def __str__(self):
        return self._note

    def __eq__(self, other):
        if isinstance(other, Tone):
            return self._note == other._note
        return False

    def __hash__(self):
        return hash(self._note)

    def __add__(self, other):
        if type(other) == Tone:
            return Chord(self, other)
        elif type(other) == Interval:
            tone_index = VALID_TONES_LIST.index(self._note)
            new_index = (tone_index + other.steps) % len(VALID_TONES_LIST)
            return Tone(VALID_TONES_LIST[new_index])
        else:
            raise TypeError('Invalid operation')

    def __sub__(self, other):
        if type(other) == Tone:
            first_tone_index = VALID_TONES_LIST.index(self._note)
            second_tone_index = VALID_TONES_LIST.index(str(other))
            steps = (first_tone_index - second_tone_index) % len(VALID_TONES_LIST)
            return Interval(steps)
        elif type(other) == Interval:
            tone_index = VALID_TONES_LIST.index(self._note)
            new_index = (tone_index - other.steps) % len(VALID_TONES_LIST)
            return Tone(VALID_TONES_LIST[new_index])
        else:
            raise TypeError('Invalid operation')


class Interval:
    """Represents a musical interval."""

    def __init__(self, steps):
        self._steps = steps

    @property
    def steps(self):
        return self._steps

    @steps.setter
    def steps(self, value):
        if value < 0:
            raise ValueError(f'{value} is not a positive number')

        self._steps = value % 12

    def __str__(self):
        return INTERVALS[self._steps]

    def __add__(self, other):
        if type(other) == Interval:
            new_steps = (self.steps + other.steps) % 12
            return Interval(new_steps)

        raise TypeError(f'Cannot add {type(other)} to Interval')

    def __neg__(self):
        return Interval(-self._steps)


class Chord:
    """Represents a musical chord."""

    def __init__(self, main_tone, *tones):
        self._tones = {main_tone, *tones}
        self._main_tone = main_tone  # Keep root so we don't cast to list
        if len(self._tones) < 2:
            raise TypeError('Cannot have a chord made of only 1 unique tone')

    def __str__(self):
        root_index = VALID_TONES_LIST.index(str(self._main_tone))
        sorted_tones = sorted(self._tones, key=lambda tone: (VALID_TONES_LIST.index(str(tone)) - root_index) % len(VALID_TONES_LIST))

        return "-".join(str(tone) for tone in sorted_tones)

    def __add__(self, other):
        if type(other) == Tone:
            new_tones = self._tones | {other}  # Union of sets
            return Chord(self._main_tone, *new_tones)
        elif type(other) == Chord:
            new_tones = self._tones | other._tones  # Union of sets
            new_main_tone = self._main_tone
            return Chord(new_main_tone, *new_tones)
        else:
            raise TypeError('Invalid operation')

    def __sub__(self, other):
        if type(other) == Tone:
            if other not in self._tones:
                raise TypeError(f"Cannot remove tone {other} from chord {self}")

            new_tones = self._tones - {other}
            if len(new_tones) < 2:
                raise TypeError("Cannot have a chord made of only 1 unique tone")

            new_main_tone = next(iter(new_tones))
            return Chord(new_main_tone, *(new_tones - {new_main_tone}))

        raise TypeError(f"Cannot subtract {type(other)} from Chord")

    def is_minor(self):
        main_tone_index = VALID_TONES_LIST.index(str(self._main_tone))
        for tone in self._tones:
            if VALID_TONES_LIST.index(str(tone)) - main_tone_index == 3:
                return True

        return False

    def is_major(self):
        steps = 0
        main_tone_index = VALID_TONES_LIST.index(str(self._main_tone))
        for tone in self._tones:
            if VALID_TONES_LIST.index(str(tone)) - main_tone_index == 4:
                return True

        return False

    def is_power_chord(self):
        if not self.is_minor() and not self.is_major():
            return True

        return False

    def transposed(self, interval):
        if type(interval) != Interval:
            raise TypeError("Transposition requires an Interval object")

        transposed_tones = set()
        for tone in self._tones:
            original_index = VALID_TONES_LIST.index(str(tone))
            transposed_index = (original_index + interval.steps) % 12
            transposed_tone = Tone(VALID_TONES_LIST[transposed_index])
            transposed_tones.add(transposed_tone)

        main_tone_index = VALID_TONES_LIST.index(str(self._main_tone))
        transposed_main_tone_index = (main_tone_index + interval.steps) % 12
        transposed_main_tone = Tone(VALID_TONES_LIST[transposed_main_tone_index])

        return Chord(transposed_main_tone, *transposed_tones)