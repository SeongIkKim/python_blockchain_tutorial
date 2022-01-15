THIS REPOSIOTRY IS HANS_ON FOR [How to build a blockchain in python - Dante Sblendorio, Activestate](https://www.activestate.com/blog/how-to-build-a-blockchain-in-python/).

## What is a blockchain?

First cryptocurrency: Bitcoin recorded financial information in network.  
However, type of data stored is not restricted to storing financial information. Rather, It is inconsequential to and independent of the blockchain network.

Data characteristics which stored in a block chain
- **Immutable**
- **Unhackable**
- **Persistent(no loss of data)**
- **Distributed**

These qualities are necessary to maintain integrity of blockchain and the security of the network.

## Immutablity

Immutability can be implemented using a cryptographic hash function.
You can check whether the value is right by hashing value without disclosing value itself.

In order to ensure the immutability of the entire blockchain, approach of including a hash of the previous block within current block will be used.
It helps to protecting chain's integrity(partially, at least).  

However, it guarantees only partial chain as we said, so there is some danger someone modify a previous block and then recompute each of the following blocks.
Satoshi Nakamoto established a **proof-of-work** system to implement a single chronological history of the chain in the correct order in which transactions were made.

## Proof-Of-Work System

When new block is created, proof-of-work system requires scanning for a value that starts with a certain number of zero bits when hashed.
This value called `nonce`, and number of leading zero bits is `difficulty`.  

Average work required to creat a block increases exponentially with the number of leading zero bits, so the more blocks in chain, the harder to be modified.  

If new block is created, then it will initially stored in unconfirmed transactions. After confirming the new block is a valid proof(satisfying difficulty criteria), then the block is added in chain officially.
This process commonly known as `mining`.

## Usage Guide

Run flask server in local first.
```bash
$ python3 api.py
```

Get all existing block data in chain. 
```bash
$ curl http://127.0.0.1:5000/chain
```

Create new block with custom transaction to chain.
```bash
$ curl -X POST http://127.0.0.1:5000/block \
  -H 'Content-Type: application/x-www-form_urlencoded' \
  -d '{"transaction":"PUT SOME TRANSACTION"}' 
```





