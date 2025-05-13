# Exercise 5: Vowel Counter
sentence = "The quick brown fox jumps over the lazy dog"
word_vowel_counts = \
[sum(1 for char in word if char.lower() in 'aeiou') # quick | sum(1,1)
  for word in sentence.split()]
print("Counts of vowels in each word:", word_vowel_counts)






sentence = "The quick brown fox jumps over the lazy dog"
sentence_list = sentence.split(" ")
word_vowel_counter = []

for word in sentence_list : # The
    v_count = sum(1
                  for char in word
                  if char.lower() in 'aeiou')
    word_vowel_counter.append(v_count)

print(word_vowel_counter)
