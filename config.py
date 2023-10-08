# After 613750th line, data isn't aligned properly. the entire dataset has 6198109 lines
LAST_LINE = 613750

# Lines will be concatenated if they're less than this threshold in length
MIN_CHAR_THRESHOLD = 40

GOOGLE_TRANSLATE_BATCH_SIZE = 150_000
# GOOGLE_TRANSLATE_BATCH_SIZE = 1_048

# Normalize persian lines using Hazm
NORMALIZE_PERSIAN = True

# remove the explanations in parentheses
REMOVE_PARENTHESES = True

REMOVE_EMOJIS = True

# All sorts of punctuation
REMOVE_PUNCTUATION = False
# Stuff like -, ...,
REMOVE_EXTRA_PUNCTUATION = True

