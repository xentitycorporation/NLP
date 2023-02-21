#!/usr/bin/env python
# coding: utf-8

# In[4]:


#For installing Spacy
# pip install nltk

# pip install spacy==2.3.5

# pip install https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-2.3.1/en_core_web_sm-2.3.1.tar.gz


# In[31]:


import spacy
 

nlp = spacy.load("en_core_web_sm")


# In[2]:



# doc = load_model("Hi my name is mak")
# doc


# In[ ]:


# #For Generating POS use following code
# #Use sample file with sentence column to generate POS header column
# import csv

# with open('POS_sample.csv', 'r') as csv_file:
#     csv_reader = csv.reader(csv_file)
#     header = next(csv_reader)  # skip header row
#     text_col_index = header.index('sentence')  # assume 'text' is the column header
#     rows = list(csv_reader)
#     texts = [row[text_col_index] for row in rows]

# pos_texts = []
# for text in texts:
#     doc = nlp(text)
#     pos_text = ' '.join([f'{token.text}/{token.pos_}' for token in doc])
#     pos_texts.append(pos_text)
    
# with open('output_POS_Combined.csv', 'w', newline='') as csv_file:
#     csv_writer = csv.writer(csv_file)
#     csv_writer.writerow(header + ['pos'])  # add 'pos' as new column header
#     for i, row in enumerate(rows):
#         pos_row = row + [pos_texts[i]]
#         csv_writer.writerow(pos_row)


# In[3]:


import pandas as pd
data = pd.read_csv("output_POS_Combined.csv")


# In[4]:


data.head(10)


# In[5]:


#GENERATING 'NER_TAGS' For Every Sentence
import csv

with open('output_POS_Combined.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    header = next(csv_reader)  # skip header row
    text_col_index = header.index('sentence')  # assume 'sentence' is the column header
    rows = list(csv_reader)
    texts = [row[text_col_index] for row in rows]


# In[6]:


ner_texts = []
for text in texts:
    doc = nlp(text)
    ner_text = ' '.join([f'{token.text}/{token.ent_type_}' if token.ent_type_ else token.text for token in doc])
    ner_texts.append(ner_text)


# In[7]:


with open('output_NER.csv', 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(header + ['NER_TAGS'])  # add 'ner' as new column header
    for i, row in enumerate(rows):
        ner_row = row + [ner_texts[i]]
        csv_writer.writerow(ner_row)


# In[8]:


#For generating LEMMA
import csv

with open('output_NER.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    header = next(csv_reader)  # skip header row
    text_col_index = header.index('sentence')  # assume 'text' is the column header
    rows = list(csv_reader)
    texts = [row[text_col_index] for row in rows]


# In[9]:


lemma_texts = []
for text in texts:
    doc = nlp(text)
    lemma_text = ' '.join([token.lemma_ for token in doc])
    lemma_texts.append(lemma_text)


# In[10]:


with open('output_Lemma_Main.csv', 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(header + ['lemma'])  # add 'lemma' as new column header
    for i, row in enumerate(rows):
        lemma_row = row + [lemma_texts[i]]
        csv_writer.writerow(lemma_row)


# In[11]:


#For generating Dependancy Parser


# In[12]:


import csv

with open('output_Lemma_Main.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    header = next(csv_reader)  # skip header row
    text_col_index = header.index('sentence')  # assume 'text' is the column header
    rows = list(csv_reader)
    texts = [row[text_col_index] for row in rows]


# In[13]:


dep_texts = []
for text in texts:
    doc = nlp(text)
    dep_text = ' '.join([f'{token.text}/{token.dep_}/{token.head.text}' for token in doc])
    dep_texts.append(dep_text)


# In[14]:


with open('output_DEP.csv', 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(header + ['dep'])  # add 'dep' as new column header
    for i, row in enumerate(rows):
        dep_row = row + [dep_texts[i]]
        csv_writer.writerow(dep_row)


# In[15]:


##For generating SHAPE


# In[16]:


with open('output_DEP.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    header = next(csv_reader)  # skip header row
    text_col_index = header.index('sentence')  # assume 'text' is the column header
    rows = list(csv_reader)
    texts = [row[text_col_index] for row in rows]


# In[17]:


shape_texts = []
for text in texts:
    doc = nlp(text)
    shape_text = ' '.join([token.shape_ for token in doc])
    shape_texts.append(shape_text)


# In[18]:


with open('output_SHAPE.csv', 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(header + ['shape'])  # add 'shape' as new column header
    for i, row in enumerate(rows):
        shape_row = row + [shape_texts[i]]
        csv_writer.writerow(shape_row)


# In[19]:


#For generating Token to know if token is an alpha character?


# In[24]:


import csv

with open('output_SHAPE.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    header = next(csv_reader)  # skip header row
    text_col_index = header.index('sentence')  # assume 'text' is the column header
    rows = list(csv_reader)
    texts = [row[text_col_index] for row in rows]


# In[25]:


is_alpha_texts = []
for text in texts:
    doc = nlp(text)
    is_alpha_text = ' '.join([str(token.is_alpha) for token in doc])
    is_alpha_texts.append(is_alpha_text)


# In[26]:


with open('output_ISALPHA.csv', 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(header + ['is_alpha'])  # add 'is_alpha' as new column header
    for i, row in enumerate(rows):
        is_alpha_row = row + [is_alpha_texts[i]]
        csv_writer.writerow(is_alpha_row)


# In[27]:


#For generating Token to know if token has an any STOPWORD?


# In[28]:


with open('output_ISALPHA.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    header = next(csv_reader)  # skip header row
    text_col_index = header.index('sentence')  # assume 'text' is the column header
    rows = list(csv_reader)
    texts = [row[text_col_index] for row in rows]


# In[29]:


shape_texts = []
for text in texts:
    doc = nlp(text)
    shape_text = ' '.join([str(token.is_stop) for token in doc])
    shape_texts.append(shape_text)


# In[30]:


with open('output_Linguistic_Features.csv', 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(header + ['STOPWORDS'])  # add 'shape' as new column header
    for i, row in enumerate(rows):
        shape_row = row + [shape_texts[i]]
        csv_writer.writerow(shape_row)


# In[ ]:




