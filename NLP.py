# NLP

# Teach computers / machines to understand and process human language (text)

# Eg : 
# 1. ChatGPT 
# 2. Spam detection
# 3. Search engines
# 4. Chatbots

# Session 1 : Text Preprocessing

# text = "Hello World"

# 1. Convert to lower case

# machine is good

# text = text.lower()
# print(text)

# 2. Remove Punctuation marks

# import string
# text = "Hello!! How are you?"
# text = text.lower()
# print(text)
# cleaned_text = text.translate(str.maketrans('', '', string.punctuation))

# print(cleaned_text)

# 3. Tokenization

# text = "I love Python"
# words = text.split()
# print(words)

# 4. Stopword Removal

# stopwords = ["is", "am", "the", "and"]
# text = "I am learning Python"
# words = text.split()
# # print(words)
# filtered_words = []

# for w in words:
#     if w not in stopwords:
#         filtered_words.append(w)

# print(filtered_words)

# Q create a pipeline using above all stages : 1 -> 2 -> 3 -> 4

text = "I want to learn Python"
text = "Machine Learning is AWESOME!!!!"