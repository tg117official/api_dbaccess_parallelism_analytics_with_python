# ---------------------------------------------
# Mapping Types in Python - Beyond `dict`
# ---------------------------------------------

# 1. defaultdict - from collections module
# Purpose: Automatically provides a default value for nonexistent keys

from collections import defaultdict

# Creating a defaultdict with default type int (default value will be 0)
word_count = defaultdict(int)

# Counting word frequency in a sentence
sentence = "hello world hello python"
for word in sentence.split():
    word_count[word] += 1  # If key doesn't exist, default is 0

print("DefaultDict Example - Word Count:")
print(dict(word_count))  # Convert to normal dict for display
print("\n")


# 2. OrderedDict (Python <3.7) - remembers the insertion order
# In Python 3.7+, regular dicts also maintain insertion order,
# but OrderedDict still has methods like move_to_end(), popitem(last=True)

from collections import OrderedDict

ordered_example = OrderedDict()
ordered_example['banana'] = 3
ordered_example['apple'] = 4
ordered_example['mango'] = 2

print("OrderedDict Example - Insertion Order Preserved:")
for key, value in ordered_example.items():
    print(f"{key}: {value}")
print("\n")

# Move 'banana' to end
ordered_example.move_to_end('banana')
print("After moving 'banana' to end:")
print(list(ordered_example.keys()))
print("\n")


# 3. ChainMap - Combines multiple dictionaries
# Purpose: Lookup across multiple dictionaries as if they were one

from collections import ChainMap

defaults = {'theme': 'light', 'language': 'English'}
user_settings = {'theme': 'dark'}

# ChainMap will check user_settings first, then defaults
settings = ChainMap(user_settings, defaults)

print("ChainMap Example - Combined Dictionaries:")
print("Theme:", settings['theme'])      # 'dark' from user_settings
print("Language:", settings['language'])  # 'English' from defaults
print("\n")


# 4. MappingProxyType - Read-only view of a dictionary
# Purpose: Provide a secure, read-only mapping view

from types import MappingProxyType

original_data = {'a': 1, 'b': 2}
readonly_view = MappingProxyType(original_data)

print("MappingProxyType Example - Read-Only Dictionary:")
print("Original Data:", readonly_view)

# Trying to modify the proxy will raise TypeError
try:
    readonly_view['c'] = 3
except TypeError as e:
    print("Error: Cannot modify read-only view:", e)

# But updating the original dict reflects in the proxy
original_data['c'] = 3
print("Updated Original Dict:", original_data)
print("Updated Read-Only View:", readonly_view)
print("\n")

# ---------------------------------------------------------
# These mapping types provide enhanced control and behavior
# beyond the regular dictionary depending on the use-case.
# ---------------------------------------------------------
