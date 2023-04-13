a = {'до': 'до-о', 'ре': 'ре-э', 'ми': 'ми-и', 'фа': 'фа-а', 'соль': 'со-оль', 'ля': 'ля-а', 'си': 'си-и'}
PITCHES = ["до", "ре", "ми", "фа", "соль", "ля", "си"]


class Note:
    def __init__(self, note, is_long=False):
        if is_long:
            self.note = a[note]
        else:
            self.note = note

    def __str__(self):
        return self.note


class LoudNote(Note):
    def __str__(self):
        return self.note.upper()


class DefaultNote(Note):
    def __init__(self, note='до', is_long=False):
        if is_long:
            self.note = a[note]
        else:
            self.note = note


class NoteWithOctave(Note):
    def __init__(self, note, octave, is_long=False):
        if is_long:
            self.note = a[note]
        else:
            self.note = note
        self.octave = octave

    def __str__(self):
        return f'{self.note} ({self.octave})'


print(Note("соль"))

print(LoudNote(PITCHES[4]))
print(LoudNote("си", is_long=True))

print(DefaultNote("ми"))
print(DefaultNote())
print(DefaultNote(is_long=True))

print(NoteWithOctave("ре", "первая октава"))
print(NoteWithOctave("ля", "малая октава", is_long=True))
