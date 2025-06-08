#from https://github.com/keithito/tacotron  


#from text import dict
from text import endict, rudict, uydict


_pad = "_"
_punctuation = "!'(),.:;? "
_special = "-"
_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzABCÇDEFGĞHIİJKLMАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюяæøœɪqʁw"
_silences = ["@sp", "@spn", "@sil"]

# Prepend "@" to French phonemes from the dictionary
_phonemes_en = ["@" + s for s in endict.valid_symbols]
_phonemes_ru = ["@" + s for s in rudict.valid_symbols]
_phonemes_uy = ["@" + s for s in uydict.valid_symbols]

# Export all symbols:
symbols = (
    [_pad]
    + list(_special)
    + list(_punctuation)
    + list(_letters)
    + _phonemes_en
    + _phonemes_ru
    + _phonemes_uy
    + _silences
)
