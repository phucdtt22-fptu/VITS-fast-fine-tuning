'''
Defines the set of symbols used in text input to the model.
'''

'''# japanese_cleaners2
_pad        = '_'
_punctuation = ',.!?-~…'
_letters = 'AEINOQUabdefghijkmnoprstuvwyzʃʧʦ↓↑ '
'''

#  vietnamese_cleaners
_pad        = '_'
_punctuation = ',.!?-~…'
_letters = 'aAăĂâÂbBcCdDđĐeEêÊfFgGhHiIjJkKlLmMnNoOôÔơƠpPqQrRsStTuUưƯvVxXyYzZ!\'(),-.:;? '


# Export all symbols:
symbols = [_pad] + list(_punctuation) + list(_letters)

# Special symbol ids
SPACE_ID = symbols.index(" ")
