#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Spacy is a popular natural language processing library that provides part-of-speech tagging (POS) as one of its core functionalities. 
# POS tagging is the process of labeling each word in a text with its corresponding part of speech, such as noun, verb, adjective, etc.
# In Spacy, POS tagging can be performed using the pos_ attribute of a token object, which represents a single word in a text. 
# The pos_ attribute returns a string that represents the part of speech of the token, based on the specific language model used by Spacy.


# In[5]:


import pandas as pd
data = pd.read_csv("samples_main.csv")


# In[6]:


data.head(5)


# In[7]:


sentences = data['sentence']


# In[8]:


sent1 = data.sentence.tolist()


# In[9]:


sent1


# In[ ]:


#Converting Tokens into String


# In[10]:



sent_string = ''.join(map(str, sent1))


# In[11]:


sent_string


# In[12]:


import re

#text = "The temperature is 25.5 degrees Celsius."
pattern = r"([-+]?\d*\.\d+|\d+)\s*(°|degrees)\s*(Celsius|C|Fahrenheit|F)?"

match = re.search(pattern, sent_string)

if match:
    temperature = float(match.group(1))
    unit = match.group(3) or "Celsius"  # default to Celsius if no unit specified
    print(f"Temperature is {temperature} {unit}.")
else:
    print("No temperature found in the text.")


# In[13]:


import re

#text = "The temperature is 25.5 degrees Celsius."

pattern = r"\b\d+(?:\.\d+)?\s*(?:degrees?\s*(?:Celsius|C|Fahrenheit|F))\b"

matches = re.findall(pattern, sent_string)

print(matches)


# In[14]:


import re

#text = "The Temperature outside is 25 degrees Celsius. The boiling point of water is 100 degrees Celsius."

# Match sentences containing the word "Temperature"
sentences = re.findall(r'[A-Z][^.?!]*Temperature[^.?!]*[.?!]', sent_string)

# Print the matching sentences
for sentence in sentences:
    print(sentence)


# In[15]:


import spacy

nlp = spacy.load("en_core_web_sm")

def clean_text(text):
    doc = nlp(text)
    tokens = [token.text for token in doc if not token.is_stop and not token.is_punct]
    return " ".join(tokens)

#text = "Hello, this is a sample text. Let's clean it!"
cleaned_text = clean_text(sent_string)
print(cleaned_text)


# In[16]:


import re

#text = "The Temperature outside is 25 degrees Celsius. The boiling point of water is 100 degrees Celsius."

# Match sentences containing the word "Temperature"
sentences = re.findall(r'[A-Z][^.?!]*Temperature[^.?!]*[.?!]', cleaned_text)

# Print the matching sentences
for sentence in sentences:
    print(sentence)


# In[20]:


import re

#text = "The Temperature outside is 25 degrees Celsius. The boiling point of water is 100 degrees Celsius."

# Match sentences containing the word "Temperature"
sentences = re.findall(r'[A-Z][^.?!]*Patient[^.?!]*[.?!]', cleaned_text)

# Print the matching sentences
for sentence in sentences:
    print(sentence)


# In[21]:


import re

#text = "The Temperature outside is 25 degrees Celsius. The boiling point of water is 100 degrees Celsius."

# Match sentences containing the word "Temperature"
sentences = re.findall(r'[A-Z][^.?!]*Heart rate[^.?!]*[.?!]', cleaned_text)

# Print the matching sentences
for sentence in sentences:
    print(sentence)


# In[22]:


import re

#text = "The Temperature outside is 25 degrees Celsius. The boiling point of water is 100 degrees Celsius."

# Match sentences containing the word "Temperature"
sentences = re.findall(r'[A-Z][^.?!]*medical[^.?!]*[.?!]', cleaned_text)

# Print the matching sentences
for sentence in sentences:
    print(sentence)


# In[29]:



# Match sentences containing the word "Temperature"
sentences = re.findall(r'[A-Z][^.?!]*conditions[^.?!]*[.?!]', cleaned_text)

# Print the matching sentences
for sentence in sentences:
    print(sentence)


# In[ ]:


# Match sentences containing the word "Temperature"
# sentences = re.findall(r'[A-Z][^.?!]*medical[^.?!]*[.?!]', cleaned_text)

# # Print the matching sentences
# for sentence in sentences:
#     print(sentence)

