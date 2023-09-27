#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install openai


# In[2]:


import openai


# In[3]:


openai.api_key='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'


# In[6]:


def get_gpt_response(prompt, max_tokens = 200): 
    prompt = f" Answer the following question: {prompt}\nAnswer:"
    response = openai.Completion.create( 
        engine = "text-davinci-003", 
        prompt = prompt,
        max_tokens=500, 
        n=1, 
        temperature = 0.7)
    return response. choices[0].text.strip()


# In[8]:


prompt = "What are the key benefits of using renewable energy?" 
response = get_gpt_response(prompt)
print(response)


# In[ ]:




