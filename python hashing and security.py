#!/usr/bin/env python
# coding: utf-8

# In[1]:


import hashlib


# In[2]:


dir(hashlib)


# In[3]:


text = "Hello, How are you ?"


# # Hashing String Using MD5 

# In[4]:


md5_hash_obj = hashlib.md5(text.encode())


# In[5]:


print( f"The byte equivalent of MD5 hash is: \n{md5_hash_obj.digest()}")


# # Hashing String Using SHA1

# In[6]:


sha1_hash_obj = hashlib.sha1(text.encode())


# In[7]:


print( f"The byte equivalent of SHA1 hash is: \n{sha1_hash_obj.digest()}")


# # Hashing String Using SHA224

# In[8]:


sha224_hash_obj = hashlib.sha224(text.encode())


# In[9]:


print( f"The byte equivalent of SHA224 hash is: \n{sha224_hash_obj.digest()}")


# # Hashing String Using SHA256

# In[10]:


sha256_hash_obj = hashlib.sha256(text.encode())


# In[11]:


print( f"The byte equivalent of SHA256 hash is: \n{sha256_hash_obj.digest()}")


# # SALTING AND ITERARTION

# In[12]:


import uuid


# In[13]:


salt = uuid.uuid4().hex


# In[14]:


hash_pwd_1_obj = hashlib.sha512((salt + text).encode())


# In[15]:


hash1 = hash_pwd_1_obj.digest()


# In[16]:


print( f"The byte equivalent of SHA512 hash is: \n{hash1}")


# In[17]:


hash_pwd = hash_pwd_1_obj

for i in range(5):
    hash_pwd1  = hashlib.sha512(hash_pwd.digest())
    hash_pwd = hash_pwd1
    print(f"Hash {i} --> {hash_pwd.digest()} \n")


# In[18]:


print("Done")


# In[ ]:




