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

## Blockchain and FastAPI
Special thanks to YouTuber rithmic for his tutorial
https://youtu.be/G5M4bsxR-7E

_command to launch API_: uvicorn main:app --reload

This version of the block chain implements a very simple proof of work process to generate a new block. It also includes functions to verify the integrity of the chain and looks for changes. A simple API allows interaction with the blockchain via a browser.

## Current Issues
- This implementation of blockchain doesn't use public key infrastructure to verify the people posting the data to the chain. In the Bitcoin implementation the public keys of giver and receiver of the coin (or their wallets) are part of the data used to calculate the hash. This ensures the coin in a given block can only be accessed with the associated and correct private key.
- This implementation of the blockchain doesn't address consensus. 
- My original idea was to leverage the resources of the client machine connecting to a server to participate in block validation and then send the associated coin to the server. The problem is, in order to ensure there is an available block for each TCP session there can't be competition for validation or clients risk not being able to "afford" their connecton to the server. If each session creates a new block, what puts a limit on the availability of the coin? In other words, what gives this coin value? 
- I need to better understand the economics of what gives digital currency real world value in order to iterate this idea.