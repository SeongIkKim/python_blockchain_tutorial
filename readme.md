# Introduction

## What is a blockchain?

First cryptocurrency: Bitcoin recorded financial information in network.  
However, type of data stored is not restricted to storing financial information. Rather, It is inconsequential to and independent of the blockchain network.

Data characteristics which stored in a block chain
- Immutable
- Unhackable
- Persistent(no loss of data)
- Distributed

These qualities are necessary to maintain integrity of blockchain and the security of the network.

## Immutablity

Immutability can be implemented using a cryptographic hash function.
You can check whether the value is right by hashing value without disclosing value itself.

In order to ensure the immutability of the entire blockchain, approach of including a hash of the previous block within current block will be used.
It helps to protecting chain's integrity(partially, at least).


