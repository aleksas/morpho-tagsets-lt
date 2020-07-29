# Common tags

case_nvapm = {'n': 'V.', 'g': 'K.', 'd': 'N.', 'a': 'G.', 'i': 'Įn.', 'l': 'Vt.', 'v': 'Š.', 'x': 'Il.', '-': None}
number_npam = {'p': 'dgs.', 's': 'vns.', 'd': 'dvisk.', '-': None}
reflexiveness_nv = {'y': 'sngr.', 'n': None}
gender_vapm = {'f': 'mot.', 'm': 'vyr.', 'n': 'bev.', '-': None} 
defineteness_vapm = {'y': 'įvardž.', 'n': None, '-': None}
type_varsqio = {'g': None, 'n': None, 'x': None}
type_pc = {'g': None}
degree_ar = {'p': 'nelygin.', 'c': 'aukšt.', 's': 'aukšč.', 'd': None, '-': None}

# Categories

noun = [
    {'N': 'dkt.'}, # Category
    {'c': None, 'p': 'tikr.', 'n': None, 'x': None}, # Type
    {'c': 'bendr.', 'f': 'mot.', 'm': 'vyr.', '-': None}, #Gender
    number_npam, # Number
    case_nvapm, # Case
    reflexiveness_nv, # Reflexiveness
    {'f': None, 's': None, 'g': None, '-': None} # Name
]

verb = [
    {'V': 'vksm.'}, # Category
    type_varsqio, # Type
    {'i': 'bndr.', 'm': 'asm.', 'p': 'dlv.', 'a': 'pad.', 'h': 'pusd.', 'b': 'būdn.'}, # VForm
    {'p': 'es.', 's': 'būt.', 'a': 'būt-k.', 'q': 'būt-d.', 'f': 'būs.', '-': None}, # Tense
    {'1': '1.', '2': '2.', '3': '3.', '-': None}, # Person
    {'p': 'dgs.', 's': 'vns.', 'd': 'dvisk.', '-': None}, # Number !DOC ISSUE: add -
    gender_vapm, # Gender
    {'a': 'veik.', 'p': 'neveik.', 'n': 'reik.', '-': None}, # Voice
    {'y': 'neig.', 'n': None}, # Negative
    defineteness_vapm, # Defineteness !DOC ISSUE : add -
    case_nvapm, # Case
    reflexiveness_nv, # Reflexiveness
    {'i': 'tiesiog.', 's': 'tar.', 'm': 'liep.', '-': None}, # Mood
    {'p': 'nelygin.', 'c': 'aukšt.', 's': 'aukšč.', '-': None} # Degree
]

adjective = [
    {'A': 'bdv.'}, # Category
    type_varsqio, # Type
    degree_ar, # Degree
    gender_vapm, # Gender
    number_npam, # Number
    case_nvapm, # Case
    defineteness_vapm # Defineteness
]

pronoun = [
    {'P': 'įv.'}, # Category
    type_pc, # Type
    gender_vapm, # Gender
    number_npam, # Number
    case_nvapm, # Case
    defineteness_vapm # Defineteness
]

numeral = [
    {'M': 'sktv.'}, # Category
    {'c': 'kiek.', 'o': 'kelint.', 'l': 'kuopin.', 'm': 'daugin.', 'n': None, 'x': None, '-': None}, # Type
    gender_vapm, # Gender
    number_npam, # Number
    case_nvapm, # Case
    {'d': 'arab.', 'r': 'rom.', 'l': 'raid.', 'm': 'mišr.', '-': None}, # Form !DOC ISSUE: add -
    defineteness_vapm, # Defineteness
]

adverb = [
    {'R': 'prv.'}, # Category
    type_varsqio, # Type
    degree_ar # Degree
]

preposition = [
    {'S': 'prl.'}, # Category
    type_varsqio, # Type
    {'g': 'K.', 'd': 'N.', 'a': 'G.', 'i': 'Įn.', '-': None} # Case !DOC ISSUE: add -
]

conjunction = [
    {'C': 'jng.'}, # Category
    type_pc # Type
]

particle = [
    {'Q': 'dll.'}, # Category
    {'g': None, 'n': None, 'x': None, '-': None} # Type !DOC ISSUE: add -
]

interjection = [
    {'I': 'jst.'}, # Category
    type_varsqio # Type
]

onomatopoeia = [
    {'O': 'išt.'}, # Category
    type_varsqio # Type
]

abbreviation = [
    {'Y': None}, # Category
    {'s': 'sutr.', 'a': 'akr.', 'n': None, 'x': None} # Type
]

others = [
    {'X': 'kita'}, # Category
    {'f': 'užs.', 't': None, 'p': None, 'h': None, 'l': None, 'e': None, 'i': None, 'g': None, 't': None, '-': None, 'r': None} # Type !DOC ISSUE: add r
]

punctuation = [
    {'T': 'skyr.'}, # Category
    {'p': None, 'c': None, 's': None, 'n': None, 'q': None, 'e': None, 'i': None, 'h': None, 'l': None, 'r': None, 'u': None, 't': None, 'x': None} # Type
]

# Helpers

categories = [
    (noun, (0, 1, 5, 2, 3, 4)),
    (verb, (0, 2, 8, 11, 12, 7, 3, 13, 9, 6, 5, 10, 4)),
    (adjective,  (0, 2, 6, 3, 4, 5)),
    (pronoun, (0, 5, 2, 3, 4)),
    (numeral, (0, 5, 1, 6, 2, 3, 4)),
    (adverb,  (0, 2)),
    (preposition, (0, 2)),
    (conjunction, (0, )),
    (particle, (0, )),
    (interjection, (0, )),
    (onomatopoeia, (0, )),
    (abbreviation, (0, 1)),
    (others, (0, )),
    (punctuation, (0, ))
]

category_map = { list(category[0][0].keys())[0]: category for category in categories }

def get_jablonskis_tags(multext_east):
    category = category_map[multext_east[0]][0]
    category_order = category_map[multext_east[0]][1]

    tags = []
    
    for i, code in enumerate(multext_east):
        tags.append( category[i][code] )
    
    for i in category_order:
        tag = tags[i]
        if tag:
            yield tag
