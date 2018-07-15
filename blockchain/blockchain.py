import functools

MINING_REWARD = 10

genesis_block = {'previous_hash': '',
                 'index': 0,
                 'transactions': []}
# Inicialize our (empty) blockchain list
blockchain = [genesis_block]
# outstanding transactions
open_transactions = []
owner = 'Andronikus'
participants = set()


def get_last_blockchain_value():
    """ Return the last value of the current blockchain """
    if len(blockchain) < 1:
        return None
    return blockchain[-1]

def hash_block(block):
    return '-'.join([str(block[key]) for key in block])

def get_balance(participant):

    tx_sender = [[tx['amount'] for tx in block['transactions'] if tx['sender'] == participant] for block in blockchain]
    open_tx_sender = [tx['amount'] for tx in open_transactions if tx['sender'] == participant]
    tx_sender.append(open_tx_sender)

    amount_sent = functools.reduce(lambda tx_sum, tx_amount: tx_sum + sum(tx_amount) if len(tx_amount) > 0 else tx_sum,tx_sender,0)
    
    tx_received = [[tx['amount'] for tx in block['transactions'] if tx['recipient'] == participant] for block in blockchain]
    amount_received = functools.reduce(lambda tx_sum, tx_amount: tx_sum + sum(tx_amount) if len(tx_amount) > 0 else tx_sum,tx_received,0)

    return amount_received - amount_sent

def verify_transaction(transaction):
    sender_balance = get_balance(transaction['sender'])

    return sender_balance >= transaction['amount']

def add_transaction(recipient, sender=owner, amount=1.0):
    """ Append a new value as well as the last blockchain value to the blockchain

    Arguments:
        :sender: the sender of the transaction
        :recipient: the recipient of the transaction
        :amount: the amount of coins transfered (default = 1.0)
    """

    transaction = {'sender': sender, 'recipient': recipient, 'amount': amount}
    
    if verify_transaction(transaction):
        open_transactions.append(transaction)
        participants.add(sender)
        participants.add(recipient)
        return True
    else:
     return False


def mine_block():
    last_block = blockchain[-1]
    hashed_block = hash_block(last_block)

    reward_block = {'sender': 'MINING',
                    'recipient' : owner,
                    'amount': MINING_REWARD}
    
    copied_transactions = open_transactions[:]
    copied_transactions.append(reward_block)

    block = {'previous_hash': hashed_block,
             'index': len(blockchain),
             'transactions': copied_transactions}

    blockchain.append(block)
    return True


def get_transaction_value():
    """ Returns the input of the user (a new transaction amount) as a float. """
    # Get the user input, transform it from a string to a float and store it in user_input
    tx_recipient = input('Enter the recipient: ')
    tx_amount = float(input('Enter the amount to transfer: '))
    return (tx_recipient, tx_amount)


def get_user_choice():
    user_input = input('Your choice: ')
    return user_input


def print_blockchain_elements():
    # Output the blockchain list to the console
    for block in blockchain:
        print('Outputting block')
        print(block)


def verify_chain():

    for (index,block) in enumerate(blockchain):
        if index == 0:
            continue
        else:
            if block['previous_hash'] != hash_block(blockchain[index-1]):
                return False
    return True


wait_for_input = True
while wait_for_input:
    print('1 - Add a new transaction value')
    print('2 - Mine a new block')
    print('3 - Print the blockchain blocks')
    print('4 - Print participants')
    print('5 - Check transaction validity')
    print('h - Hack blockchain')
    print('q - Quit')
    print('Please choose a choice: ')
    user_choice = get_user_choice()

    if user_choice == '1':
        recipient, amount = get_transaction_value()
        if add_transaction(recipient, amount=amount):
            print('transaction added!')
            print('Balance of {}: {:6.2f}'.format(owner, get_balance(owner)))
        else:
            print('transaction not completed!')
            
        print(open_transactions)
    elif user_choice == '2':
        if mine_block():
            open_transactions = []
            print('Balance of {}: {:6.2f}'.format(owner, get_balance(owner)))
    elif user_choice == '3':
        print_blockchain_elements()
    elif user_choice == '4':
        print(participants)
    elif user_choice == 'h':
        if len(blockchain) >= 1:
            blockchain[0] = {'previous_hash': '',
                             'index': 0,
                             'transactions': [{'sender': 'Max', 'recipient': 'Andronikus', 'amount': 3.5}]}
    elif user_choice == 'q':
        wait_for_input = False
    else:
        print('Input was invalid, please pick up a valid one from the list')

    
    if not verify_chain():
        print('Invalid blockchain')
        break
    
# executed after the loop
else:
    print('user left the console')


print('Done!')
