N = 7
PITCHES = ["до", "ре", "ми", "фа", "соль", "ля", "си"]
LONG_PITCHES = ["до-о", "ре-э", "ми-и", "фа-а", "со-оль", "ля-а", "си-и"]
INTERVALS = ["прима", "секунда", "терция", "кварта", "квинта", "секста", "септима"]


class Note:
    def __init__(self, pitch, is_long=False):
        self.pitch = PITCHES.index(pitch)
        self.is_long = is_long

    def __str__(self):
        return LONG_PITCHES[self.pitch] if self.is_long else PITCHES[self.pitch]

    def __le__(self, other):
        return self.pitch <= other.pitch

    def __eq__(self, other):
        return self.pitch == other.pitch

    def __lt__(self, other):
        return self.pitch < other.pitch

    def __gt__(self, other):
        return self.pitch > other.pitch

    def __ge__(self, other):
        return self.pitch >= other.pitch

    def __rshift__(self, other):
        return Note(PITCHES[(self.pitch + other) % N], self.is_long)

    def __lshift__(self, other):
        return Note(PITCHES[(self.pitch - other) % N], self.is_long)

    def get_interval(self, other):
        return INTERVALS[abs(self.pitch - other.pitch)]


class Melody:
    def __init__(self, notes=None):
        self.notes = notes.copy() if notes else []

    def __str__(self):
        k = 0
        res = []
        for i in self.notes:
            if not k:
                res.append(str(i).capitalize())
                k = 1
            else:
                res.append(str(i))
        return ', '.join(res)

    def append(self, item):
        self.notes.append(item)

    def replace_last(self, item):
        self.notes[-1] = item

    def remove_last(self):
        return self.notes.pop()

    def clear(self):
        return self.notes.clear()

    def __len__(self):
        return len(self.notes)

    def __rshift__(self, other):
        return Melody([n >> other for n in self.notes]) \
            if self.notes and max([n.pitch for n in self.notes]) + other < N else Melody(self.notes)

    def __lshift__(self, other):
        return Melody([n << other for n in self.notes]) \
            if self.notes and min([n.pitch for n in self.notes]) - other >= 0 else Melody(self.notes)


melody = Melody([Note('фа'), Note('ми'), Note('ре'), Note('до'), Note('ля')])
print(melody)
melody.replace_last(Note('си', True))
print(melody)
melody.remove_last()
print(melody)
melody.append(Note('соль', True))
melody.append(Note('соль', True))
print(melody)
