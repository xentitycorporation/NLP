#!/usr/bin/env python
# coding: utf-8

# In[1]:


text = "David is the technician. The patient is shy. She is a Australian shepherd collie. Mix 69 lbs today, 11 years old. Temperature was one Oh, 17 F. Heart rate was 108. respiratory rate was 48 she was also panting. Patient is presented today for a year. Year hematoma Owner noticed it last week on Wednesday. Um, otherwise doing well. Eating, drinking, urinating and defecating. Okay, no current medications, No heart murmur, plan tic. Um and his current diet is cables. And that's vaccines are not up to date. And there's no previous records. Hi, it's dark debates with medical notes for Shy Heller. H E l L E r Patient number 1 to 1913 on physical examination. Oral, uh, mild tartar. PM four left upper. Um, oral exam, right. Hematoma of penna scan debris A you your cytology? Um scant cocci and yeast A You, um, under integumentary right. Subq mass at, uh, rite stifle. One centimeter in diameter. Roughly spherical. Uh, additionally, right. Lateral thorax, A one centimeter subq mass Each are freely movable. Uh, ocular lenticular sclerosis. Ou You can enter default normals for the rest with the exception of reproductive hooded vulva assessment. Oral hematoma roll out secondary to yeast and or cocci Bacterial infection. Um, otherwise apparently healthy on examination plan. Rabies vaccine. Uh, one year subcutaneously right behind, uh, air cleaning a u o Sarnia installed a you, uh, half of 100 mg Rivera P o b i d. Times seven days gave owner estimate for drainage and bandaging of hematoma versus doing, um, full surgical, uh, repair"


# In[2]:


get_ipython().system('pip install medspacy')


# In[3]:


import medspacy
from medspacy.ner import TargetRule


# In[8]:


from medspacy.ner import TargetRule
from medspacy.visualization import visualize_ent


# In[4]:


nlp = medspacy.load()
print(nlp.pipe_names)


# In[9]:


nlp.get_pipe('medspacy_target_matcher').add([TargetRule('Roughly spherical', 'CONDITION'), TargetRule('lenticular sclerosis', 'CONDITION'), TargetRule('Bacterial infection', 'CONDITION')])
doc = nlp("David is the technician. The patient is shy. She is a Australian shepherd collie. Mix 69 lbs today, 11 years old. Temperature was one Oh, 17 F. Heart rate was 108. respiratory rate was 48 she was also panting. Patient is presented today for a year. Year hematoma Owner noticed it last week on Wednesday. Um, otherwise doing well. Eating, drinking, urinating and defecating. Okay, no current medications, No heart murmur, plan tic. Um and his current diet is cables. And thats vaccines are not up to date. And there's no previous records. Hi, it's dark debates with medical notes for Shy Heller. H E l L E r Patient number 1 to 1913 on physical examination. Oral, uh, mild tartar. PM four left upper. Um, oral exam, right. Hematoma of penna scan debris A you your cytology? Um scant cocci and yeast A You, um, under integumentary right. Subq mass at, uh, rite stifle. One centimeter in diameter. Roughly spherical. Uh, additionally, right. Lateral thorax, A one centimeter subq mass Each are freely movable. Uh, ocular lenticular sclerosis. Ou You can enter default normals for the rest with the exception of reproductive hooded vulva assessment. Oral hematoma roll out secondary to yeast and or cocci Bacterial infection. Um, otherwise apparently healthy on examination plan. Rabies vaccine. Uh, one year subcutaneously right behind, uh, air cleaning a u o Sarnia installed a you, uh, half of 100 mg Rivera P o b i d. Times seven days gave owner estimate for drainage and bandaging of hematoma versus doing, um, full surgical, uh, repair")


# In[10]:


for ent in doc.ents:
    print(ent, ent._.is_negated, ent._.is_family, ent._.is_historical)
medspacy.visualization.visualize_ent(doc)


# In[ ]:





# In[ ]:




