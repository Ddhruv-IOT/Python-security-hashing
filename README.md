# Python-security-hashing

# Overview:
It is the project for ShapeAi Bootcamp in python and network security.
<br> I have created this project to demonstrate the use of various algorithms from Hashlib.
<br> Also, I have demonstrated the use of salting and iteration on hashes to increase security and protection.

# What is Hashing: 
Hashing is a one-way function where a unique message digest is generated from an input file or a string of text.
<br> It's used to prevent unauthorized users from reading data from a file by rendering it into an unreadable form.

# What is Salt and Iteration: 
- salt is random data that is used as an additional input to a one-way function that hashes data, a password, or passphrase
- Iteration on hashes, is the way to make password hash more secure. In this, we first generate a hash from the base string and again generate the hash of the previous hash and so on. 

# Python Libraries Required:
- Hashlib - for proving random algorithms.
- Uuid - for generating random string for salting purposes.

# Algothrims Used:
- MD5
- SHA-1 
- SHA-224
- SHA-256
- SHA-512
