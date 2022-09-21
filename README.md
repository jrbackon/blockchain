# Blockchain Research

## poc_blockchain.py

**_BabsonCoin (BabC)_** 

**Transactions**:

t1 = "Kali sends 2 BabC to Jacob"

t2 = "Evie sends 4.1 BabC to Jacob"

t3 = "Kristen sends 3.2 BabC to Jacob"

t4 = "Jacob sends 0.3 BabC to Kali"

t5 = "Jacob sends 1 BabC to Evie"

t6 = "Kali sends 5.4 BabC to Kristen"


**->** = a hash function typically SHA256

**Bn** = Block n, where n is the nth block in the chain

**"AAA"** = the initial string, typically a random or semi-random number


B1 ("AAA", t1, t2) -> 76fd89, B2 ("76fd89", t3, t4) -> 8923ff, B3 ("8923ff", t5, t6)

### POC
This ultra-simple blockchain explains the basic idea and shows how it is impossible to change (or hack) transactions without recalculating all hashes for the entire chain. 

Special thanks to YouTuber NeuralNine for his tutorial.
https://youtu.be/pYasYyjByKI

