import json

from flask import Flask, request

from blockchain import Blockchain

app = Flask(__name__)

blockchain = Blockchain()


@app.route('/chain', methods=['GET'])
def get_chain():
    """return all existing chain data"""
    chain_data = []
    for block in blockchain.chain:
        chain_data.append(block.__dict__)
    return json.dumps({"length": len(chain_data),
                       "chain": chain_data})

@app.route('/block', methods=['POST'])
def create_new_block():
    """create new block"""
    data = request.get_json(force=True)
    transaction = data['transaction']
    blockchain.add_new_transaction(transaction)
    new_block_index = blockchain.mine()
    new_block = blockchain.chain[new_block_index].__dict__
    return json.dumps({"new_block": new_block})

app.run(debug=True, port=5000)
