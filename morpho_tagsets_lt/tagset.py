from enum import Enum, auto

class Category(Enum):
    NOUN = auto()
    VERB = auto()
    ADJECTIVE = auto()
    PRONOUN = auto()
    ADVERB = auto()
    PREPOSITION = auto()
    CONJUNCTION = auto()
    NUMERAL = auto()
    PARTICLE = auto()
    INTERJECTION = auto()
    ONOMATOPOEIA = auto()
    ABBREVIATION = auto()
    RESIDUAL = auto()
    PUNCTUATION_AND_SYMBOLS = auto()

# Noun

class NounType(Enum):
    COMMON = auto()
    PROPER = auto()
    SUBSTANDARD = auto()
    OBSCENE = auto()

class NounGender(Enum):
    COMMON = auto()
    FEMININE = auto()
    MASCULINE = auto()
    IRRELEVANT = auto()

class NounNumber(Enum):
    PLURAL = auto() 
    SINGULAR = auto()
    DUAL = auto()
    IRRELEVANT = auto()

class NounCase(Enum):
    NOMINATIVE = auto()
    GENITIVE = auto()
    DATIVE = auto()
    ACCUSATIVE = auto()
    INSTRUMENTAL = auto()
    LOCATIVE = auto()
    VOCATIVE = auto()
    ILLIATIVE = auto()
    IRRELEVANT = auto()

class NounReflexiveness(Enum):
    YES = auto()
    NO = auto()

class NounName(Enum):
    FIRST = auto()
    SURNAME = auto()
    GEOGRAPHIC = auto()
    IRRELEVANT = auto()

# Verb

class VerbType(Enum):
    GENERAL = auto()
    SUBSTANDARD = auto()
    OBSCENE = auto()

class VerbForm(Enum):
    INFINITIVE = auto()
    MAIN = auto()
    PARTICIPLE = auto()
    ADVERBIAL_PARTICIPLE = auto()
    HALF_PARTICIPLE = auto()
    ADVERBIAL_PARTICIPLE2 = auto()

class VerbTense(Enum):
    PRESENT = auto()
    SIMPLE_PAST = auto()
    PAST_TENSE = auto()
    PAST_FREQUENTATIVE = auto()
    FUTURE = auto()

class VerbPerson(Enum):
    FIRST = auto()
    SECOND = auto()
    THIRD = auto()
    IRRELEVANT = auto()

class VerbNumber(Enum):
    PLURAL = auto()
    SINGULAR = auto()
    DUAL = auto()

class VerbGender(Enum):
    MASCULINE = auto()
    FEMININE = auto()
    NEUTER = auto()
    IRRELEVANT = auto()

class VerbVoice(Enum):
    ACTIVE = auto()
    PASSIVE = auto()
    NECESSITY = auto()
    IRRELEVANT = auto()

class VerbNegative(Enum):
    YES = auto()
    NO = auto()

class VerbDefineteness(Enum):
    YES = auto()
    NO = auto()

class VerbCase(Enum):
    NOMINATIVE = auto()
    GENITIVE = auto()
    DATIVE = auto()
    ACCUSATIVE = auto()
    INSTRUMENTAL = auto()
    LOCATIVE = auto()
    VOCATIVE = auto()
    ILLIATIVE = auto()
    IRRELEVANT = auto()

class VerbReflexiveness(Enum):
    YES = auto()
    NO = auto()

class VerbMood(Enum):
    INDICATIVE = auto()
    SUBJUNCTIVE = auto()
    IMPERATIVE = auto()
    IRRELEVANT = auto()

class VerbDegree(Enum):
    POSITIVE = auto()
    COMPARATIVE = auto()
    SUPERLATIVE = auto()
    IRRELEVANT = auto()

# Adjective

class AdjectiveType(Enum):
    GENERAL = auto()
    SUBSTANDARD = auto()
    OBSCENE = auto()

class AdjectiveDegree(Enum):
    POSITIVE = auto()
    COMPARATIVE = auto()
    SUPERLATIVE = auto()
    DIMINUTIVE = auto()
    IRRELEVANT = auto()

class AdjectiveGender(Enum):
    FEMININE = auto()
    MASCULINE = auto()
    NEUTER = auto()
    IRRELEVANT = auto()

class AdjectiveNumber(Enum):
    PLURAL = auto()
    SINGULAR = auto()
    DUAL = auto()
    IRRELEVANT = auto()

class AdjectiveCase(Enum):
    NOMINATIVE = auto()
    GENITIVE = auto()
    DATIVE = auto()
    ACCUSATIVE = auto()
    INSTRUMENTAL = auto()
    LOCATIVE = auto()
    VOCATIVE = auto()
    ILLIATIVE = auto()
    IRRELEVANT = auto()

class AdjectiveDefineteness(Enum):
    YES = auto()
    NO = auto()

# Pronoun

class PronounType(Enum):
    GENERAL = auto()

class PronounGender(Enum):
    FEMININE = auto()
    MASCULINE = auto()
    NEUTER = auto()
    IRRELEVANT = auto()

class PronounNumber(Enum):
    PLURAL = auto()
    SINGULAR = auto()
    DUAL = auto()
    IRRELEVANT = auto()

class PronounCase(Enum):
    NOMINATIVE = auto()
    GENITIVE = auto()
    DATIVE = auto()
    ACCUSATIVE = auto()
    INSTRUMENTAL = auto()
    LOCATIVE = auto()
    VOCATIVE = auto()
    ILLIATIVE = auto()
    IRRELEVANT = auto()

class PronounDefineteness(Enum):
    YES = auto()
    NO = auto()

# Numeral

class NumeralType(Enum):
    CARDINAL = auto()
    ORDINAL = auto()
    COLLECT = auto()
    MULTIPLE = auto()
    SUBSTANDARD = auto()
    OBSCENE = auto()
    IRRELEVANT = auto()

class NumeralGender(Enum):
    FEMININE = auto()
    MASCULINE = auto()
    NEUTER = auto()
    IRRELEVANT = auto()

class NumeralNumber(Enum):
    PLURAL = auto()
    SINGULAR = auto()
    IRRELEVANT = auto()

class NumeralCase(Enum):
    NOMINATIVE = auto()
    GENITIVE = auto()
    DATIVE = auto()
    ACCUSATIVE = auto()
    INSTRUMENTAL = auto()
    LOCATIVE = auto()
    VOCATIVE = auto()
    ILLIATIVE = auto()
    IRRELEVANT = auto()

class NumeralForm(Enum):
    ROMAN = auto()
    LETTER = auto()
    MIXED_FORM = auto()

class NumeralDefineteness(Enum):
    YES = auto()
    NO = auto()
    IRRELEVANT = auto()

# Adverb

class AdverbType(Enum):
    SUBSTANDARD = auto()
    OBSCENE = auto()

class AdverbDegree(Enum):
    COMPARATIVE = auto()
    SUPERLATIVE = auto()
    DIMINUTIVE = auto()

# Preposition

class PrepositionType(Enum):
    SUBSTANDARD = auto()
    OBSCENE = auto()

class PrepositionCase(Enum):
    DATIVE = auto()
    ACCUSATIVE = auto()
    INSTRUMENTAL = auto()

# Conjunction

class ConjunctionType(Enum):
    GENERAL = auto()

# Particle

class ParticleType(Enum):
    GENERAL = auto()
    SUBSTANDARD = auto()
    OBSCENE = auto()

# Interjection

class InterjectionType(Enum):
    GENERAL = auto()
    SUBSTANDARD = auto()
    OBSCENE = auto()

# Onomatopoeia

class OnomatopoeiaType(Enum):
    GENERAL = auto()
    SUBSTANDARD = auto()
    OBSCENE = auto()

# Abbreviation

class AbbreviationType(Enum):
    SHORTENING = auto()
    ACRONYM = auto()
    SUBSTANDARD = auto()
    OBSCENE = auto()
    
# Residual

class ResidualType(Enum):
    FOREIGN = auto()
    TYPO = auto()
    SEGMENTATION = auto()
    TAG = auto()
    LINK = auto()
    E_MAIL_ADDRESS = auto()
    NICKNAME = auto()
    FRAGMENT = auto()
    LETTER = auto()
    OTHER = auto()

# Punctuation

class PunctuationType(Enum):
    FULL_STOP_PERIOD = auto()
    COMMA = auto()
    SEMICOLON = auto()
    COLON = auto()
    QUESTION_MARK = auto()
    EXCLAMATION_MARK = auto()
    ELLIPSIS = auto() # ...
    DASH_MINUS = auto() # - – — 
    OPENING_BRACKET = auto() # ( [ {
    CLOSING_BRACKET = auto() # ) ] }
    QUOTATION_MARK = auto() # " ' „ “
    SLASH_STROKE = auto() # /
    OTHER_MARKS_SYMBOLS = auto() # |\*%^$
