N = 7
PITCHES = ["до", "ре", "ми", "фа", "соль", "ля", "си"]
LONG_PITCHES = ["до-о", "ре-э", "ми-и", "фа-а", "со-оль", "ля-а", "си-и"]
INTERVALS = ["прима", "секунда", "терция", "кварта", "квинта", "секста", "септима"]


class Note:
    def __init__(self, note, is_long=False):
        self.note = note
        self.index = PITCHES.index(note)
        self.is_long = is_long
        self.notes = {'до': 'до-о', 'ре': 'ре-э', 'ми': 'ми-и', 'фа': 'фа-а',
                      'соль': 'со-оль', 'ля': 'ля-а', 'си': 'си-и'}

    def __str__(self):
        if self.is_long:
            return self.notes[self.note]
        else:
            return self.note

    def __eq__(self, other):
        if self.index == other.index:
            return True
        return False

    def __ne__(self, other):
        if self.index != other.index:
            return True
        return False

    def __lt__(self, other):
        if self.index < other.index:
            return True
        return False

    def __le__(self, other):
        if self.index <= other.index:
            return True
        return False

    def __gt__(self, other):
        if self.index > other.index:
            return True
        return False

    def __ge__(self, other):
        if self.index >= other.index:
            return True
        return False

    def __lshift__(self, other):
        return Note(PITCHES[(self.index - other) % N], self.is_long)

    def __rshift__(self, other):
        return Note(PITCHES[(self.index + other) % N], self.is_long)

    def get_interval(self, other):
        return INTERVALS[abs(self.index - other.index)]


fa1 = Note("фа", True)
fa2 = Note("фа")
la = Note("ля", True)
print(la.get_interval(fa1))
print(fa1.get_interval(fa2))
print(fa1.get_interval(Note('си')))
