from enum import IntEnum, auto

# Common tags

case_nvapm = {'n': 'V.', 'g': 'K.', 'd': 'N.', 'a': 'G.', 'i': 'Įn.', 'l': 'Vt.', 'v': 'Š.', 'x': 'Il.', '-': None}
number_npam = {'p': 'dgs.', 's': 'vns.', 'd': 'dvisk.', '-': None}
reflexiveness_nv = {'y': 'sngr.', 'n': None}
gender_vapm = {'f': 'mot.', 'm': 'vyr.', 'n': 'bev.', '-': None} 
defineteness_vapm = {'y': 'įvardž.', 'n': None, '-': None}
type_varsqio = {'g': None, 'n': None, 'x': None}
type_pc = {'g': None}
degree_ar = {'p': 'nelygin.', 'c': 'aukšt.', 's': 'aukšč.', 'd': None, '-': None}

class Placeholder(IntEnum):
    CATEGORY = auto()
    TYPE = auto()
    VERB_FORM = auto()
    TENSE = auto()
    PERSON = auto()
    GENDER = auto()
    NUMBER = auto()
    VOICE = auto()
    POLARITY = auto()
    DEFINETENESS = auto()
    CASE = auto()
    REFLEXIVENESS = auto()
    MOOD = auto()
    NUMBER_FORM = auto()
    DEGREE = auto()
    NAME = auto()


# Categories

noun = [
    (Placeholder.CATEGORY, {'N': 'dkt.'}), # Category
    (Placeholder.TYPE, {'c': None, 'p': 'tikr.', 'n': None, 'x': None}), # Type
    (Placeholder.GENDER, {'c': 'bendr.', 'f': 'mot.', 'm': 'vyr.', '-': None}), #Gender
    (Placeholder.NUMBER, number_npam), # Number
    (Placeholder.CASE, case_nvapm), # Case
    (Placeholder.REFLEXIVENESS, reflexiveness_nv), # Reflexiveness
    (Placeholder.NAME, {'f': None, 's': None, 'g': None, '-': None}) # Name
]

verb = [
    (Placeholder.CATEGORY, {'V': 'vksm.'}), # Category
    (Placeholder.TYPE, type_varsqio,), # Type
    (Placeholder.VERB_FORM, {'i': 'bndr.', 'm': 'asm.', 'p': 'dlv.', 'a': 'pad.', 'h': 'pusd.', 'b': 'būdn.'}), # VForm
    (Placeholder.TENSE, {'p': 'es.', 's': 'būt.', 'a': 'būt-k.', 'q': 'būt-d.', 'f': 'būs.', '-': None}), # Tense
    (Placeholder.PERSON, {'1': '1.', '2': '2.', '3': '3.', '-': None}), # Person
    (Placeholder.NUMBER, {'p': 'dgs.', 's': 'vns.', 'd': 'dvisk.', '-': None}), # Number !DOC ISSUE: add -
    (Placeholder.GENDER, gender_vapm,), # Gender
    (Placeholder.VOICE, {'a': 'veik.', 'p': 'neveik.', 'n': 'reik.', '-': None}), # Voice
    (Placeholder.POLARITY, {'y': 'neig.', 'n': None}), # Negative / Polarity
    (Placeholder.DEFINETENESS, defineteness_vapm,), # Defineteness !DOC ISSUE : add -
    (Placeholder.CASE, case_nvapm,), # Case
    (Placeholder.REFLEXIVENESS, reflexiveness_nv,), # Reflexiveness
    (Placeholder.MOOD, {'i': 'tiesiog.', 's': 'tar.', 'm': 'liep.', '-': None}), # Mood
    (Placeholder.DEGREE, {'p': 'nelygin.', 'c': 'aukšt.', 's': 'aukšč.', '-': None}) # Degree
]

adjective = [
    (Placeholder.CATEGORY, {'A': 'bdv.'}), # Category
    (Placeholder.TYPE, type_varsqio,), # Type
    (Placeholder.DEGREE, degree_ar,), # Degree
    (Placeholder.GENDER, gender_vapm,), # Gender
    (Placeholder.NUMBER, number_npam,), # Number
    (Placeholder.CASE, case_nvapm,), # Case
    (Placeholder.DEFINETENESS, defineteness_vapm), # Defineteness
]

pronoun = [
    (Placeholder.CATEGORY, {'P': 'įv.'}), # Category
    (Placeholder.TYPE, type_pc,), # Type
    (Placeholder.GENDER, gender_vapm,), # Gender
    (Placeholder.NUMBER, number_npam,), # Number
    (Placeholder.CASE, case_nvapm,), # Case
    (Placeholder.DEFINETENESS, defineteness_vapm), # Defineteness
]

numeral = [
    (Placeholder.CATEGORY, {'M': 'sktv.'}), # Category
    (Placeholder.TYPE, {'c': 'kiek.', 'o': 'kelint.', 'l': 'kuopin.', 'm': 'daugin.', 'n': None, 'x': None, '-': None}), # Type
    (Placeholder.GENDER, gender_vapm,), # Gender
    (Placeholder.NUMBER, number_npam,), # Number
    (Placeholder.CASE, case_nvapm,), # Case
    (Placeholder.NUMBER_FORM, {'d': 'arab.', 'r': 'rom.', 'l': 'raid.', 'm': 'mišr.', '-': None}), # Form !DOC ISSUE: add -
    (Placeholder.DEFINETENESS, defineteness_vapm,), # Defineteness
]

adverb = [
    (Placeholder.CATEGORY, {'R': 'prv.'}), # Category
    (Placeholder.TYPE, type_varsqio,), # Type
    (Placeholder.DEGREE, degree_ar), # Degree
]

preposition = [
    (Placeholder.CATEGORY, {'S': 'prl.'}), # Category
    (Placeholder.TYPE, type_varsqio,), # Type
    (Placeholder.CASE, {'g': 'K.', 'd': 'N.', 'a': 'G.', 'i': 'Įn.', '-': None}) # Case !DOC ISSUE: add -
]

conjunction = [
    (Placeholder.CATEGORY, {'C': 'jng.'}), # Category
    (Placeholder.TYPE, type_pc), # Type
]

particle = [
    (Placeholder.CATEGORY, {'Q': 'dll.'}), # Category
    (Placeholder.TYPE, {'g': None, 'n': None, 'x': None, '-': None}) # Type !DOC ISSUE: add -
]

interjection = [
    (Placeholder.CATEGORY, {'I': 'jst.'}), # Category
    (Placeholder.TYPE, type_varsqio), # Type
]

onomatopoeia = [
    (Placeholder.CATEGORY, {'O': 'išt.'}), # Category
    (Placeholder.TYPE, type_varsqio), # Type
]

abbreviation = [
    (Placeholder.CATEGORY, {'O': None}), # Category
    (Placeholder.TYPE, {'s': 'sutr.', 'a': 'akr.', 'n': None, 'x': None}), # Type
]

others = [
    (Placeholder.CATEGORY, {'X': 'kita'}), # Category
    (Placeholder.TYPE, {'f': 'užs.', 't': None, 'p': None, 'h': None, 'l': None, 'e': None, 'i': None, 'g': None, '-': None, 'r': None}) # Type !DOC ISSUE: add r, duplicate t
]

punctuation = [
    (Placeholder.CATEGORY, {'T': 'skyr.'}), # Category
    (Placeholder.TYPE, {'p': None, 'c': None, 's': None, 'n': None, 'q': None, 'e': None, 'i': None, 'h': None, 'l': None, 'r': None, 'u': None, 't': None, 'x': None}), # Type
]

categories = [
    (noun, (Placeholder.CATEGORY, Placeholder.TYPE, Placeholder.REFLEXIVENESS, Placeholder.GENDER, Placeholder.NUMBER, Placeholder.CASE)),
    (verb,{ 
        2: {
            'i': (Placeholder.CATEGORY, Placeholder.VERB_FORM, Placeholder.POLARITY, Placeholder.REFLEXIVENESS),
            'm': (Placeholder.CATEGORY, Placeholder.VERB_FORM, Placeholder.POLARITY, Placeholder.REFLEXIVENESS, Placeholder.MOOD, Placeholder.TENSE, Placeholder.NUMBER, Placeholder.PERSON),
            'p': (Placeholder.CATEGORY, Placeholder.VERB_FORM, Placeholder.POLARITY, Placeholder.REFLEXIVENESS, Placeholder.TYPE, Placeholder.TENSE, Placeholder.DEGREE, Placeholder.DEFINETENESS, Placeholder.GENDER, Placeholder.NUMBER, Placeholder.CASE),
            'a': (Placeholder.CATEGORY, Placeholder.VERB_FORM, Placeholder.POLARITY, Placeholder.REFLEXIVENESS, Placeholder.TENSE),
            'h': (Placeholder.CATEGORY, Placeholder.VERB_FORM, Placeholder.POLARITY, Placeholder.REFLEXIVENESS, Placeholder.GENDER, Placeholder.NUMBER),
            'b': (Placeholder.CATEGORY, Placeholder.VERB_FORM, Placeholder.POLARITY, Placeholder.REFLEXIVENESS),
        }
    }
    ),
    (adjective,  (Placeholder.CATEGORY, Placeholder.DEGREE, Placeholder.DEFINETENESS, Placeholder.GENDER, Placeholder.NUMBER, Placeholder.CASE)),
    (pronoun, (Placeholder.CATEGORY, Placeholder.DEFINETENESS, Placeholder.GENDER, Placeholder.NUMBER, Placeholder.CASE)),
    (numeral, (Placeholder.CATEGORY, Placeholder.NUMBER_FORM, Placeholder.TYPE, Placeholder.DEFINETENESS, Placeholder.GENDER, Placeholder.NUMBER, Placeholder.CASE)),
    (adverb,  (Placeholder.CATEGORY, Placeholder.DEGREE)),
    (preposition, (Placeholder.CATEGORY, Placeholder.CASE)),
    (conjunction, (Placeholder.CATEGORY, )),
    (particle, (Placeholder.CATEGORY, )),
    (interjection, (Placeholder.CATEGORY, )),
    (onomatopoeia, (Placeholder.CATEGORY, )),
    (abbreviation, (Placeholder.CATEGORY, )),
    (others, (Placeholder.CATEGORY, )),
    (punctuation, (Placeholder.CATEGORY, ))
]

category_map = {}

# Use to sort jablonskis tags
placeholder_sort_order_dict = {
    'sampl.': Placeholder.CATEGORY + 1, # MWE
    'tęs.': Placeholder.CATEGORY + 1
}

for cat in categories:
    category_map[list(cat[0][0][1].keys())[0]] = cat
    
    for placeholder, tags in cat[0]:
        for v in tags.values():
            if v:
                placeholder_sort_order_dict[v] = placeholder.value if placeholder.value == 1 else placeholder.value + 1

def get_jablonskis_tags(multext_east):
    category = category_map[multext_east[0]][0]
    category_tag_order = category_map[multext_east[0]][1]
    
    tags = []
    
    for i, code in enumerate(multext_east):
        tags.append( category[i][code] )
    
    # Handle verb multiple mappings
    if isinstance(category_tag_order, dict):
        for index, value in category_tag_order.items():
            category_tag_order = value[multext_east[index]]
            break
    
    order_map = {each[0]:i for i, each in enumerate(category)}

    # Probably too slow to map each time
    for i in category_tag_order:
        if tags[i]:
            yield order_map[tags[i]]

def sort_jablonskis_tags(jablonskis_tags):
    jablonskis_tags.sort(key=lambda k:placeholder_sort_order_dict[k])
