from web3 import Web3

ganache_url = "http://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))

account_1='0x574B27f79d36B2833fFD76947829ec2ef27E4E44'
account_2='0xaC7B357f57B1c0F4b8629d422A60c911E23CB427'
private_key='c338822839b278dffcb6ade81ab1da896587517e22eb6beaf7ab9c3d053eeeca'

nonce = web3.eth.getTransactionCount(account_1)
tx={
    'nonce':nonce,
        'to':account_2,
        'value':web3.toWei(1,'ether'),
        'gas':2000000,
        'gasPrice':web3.toWei('50','gWei')

}

signed_tx = web3.eth.account.signTransaction(tx, private_key)

tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
print('Transaction Has Id =',web3.toHex(tx_hash))