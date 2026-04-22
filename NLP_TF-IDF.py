# TF-IDF

# TF (Term Frequency)
# Out of all words in this sentence, how much share does this word take

# Doc1 : "I Love Python"
# Doc2 : "I Love Coding"
# Doc3 : "I Love AI"

# Doc1 : TF

# Step 1 :  
# TF(Word, Document) = count of word in document / total words in document

# Word         Count            TF

# I             1               1/3 = 0.33
# Love          1               1/3 = 0.33
# Python        1               1/3 = 0.33

# Step 2 : 
# IDF (Inverse Document Frequency)
# How many documents contain this word? : If everyone has it : Its not special

# IDF (Word) = log ( total documents / documents containing the word)

# Calculate for all 3 documents

# Word           Appears in how many documents          IDF = log(3 / count)

# I                       3                              log(3/3) = log(1) = 0
# Love                    3                              log(3/3) = log(1) = 0
# Python                  1                              log(3 / 1) = log(3) = 1.09
# Coding                  1                              log(3 / 1) = log(3) = 1.09
# AI                      1                              log(3 / 1) = log(3) = 1.09

# Step 3 : TF - IDF = TFxIDF

# For Doc1

# word          TF           IDF          TF-IDF
# I             0.33          0             0
# Love          0.33          0             0
# Python        0.33         1.09          0.36

# Real - World Connection

# 1. Google Search : Finds pages where your query words are rare and important
# 2. Resume Screening : Highlights specific skills
# 3. Email Spam Filter : "FREE", "WIN", "CLICK" --> high TF-IDF in spam docs
# 4. RAG / ChatGPT retrieval : Before embeddings, TF-IDF was used to find relevant chunks

# Limitation

# TF-IDF knows words are different, but it doesn't know they are related

# Feature                      BOW             TF-IDF

# Word Frequence                Y                Y
# Filters common words          N                Y 
# Word Order                    N                N 
# Semantic meaning              N                N 
# Sparse Vector                 Y                Y
