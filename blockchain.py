#Initializing our blockchain list
genesis_block = {
    'previous_hash': '',
    'index': 0,
    'transactions': []
}
blockchain = [genesis_block]
open_transactions = []
owner = 'Katie'
participants = {'Katie'}


def hash_block(block):
    return '-'.join([str(block[key]) for key in block])

def get_last_blockchain_value():
    """Returns the last value of the current blockchain."""
    if len(blockchain) < 1:
        return None
    return blockchain[-1]


def add_transaction(recipient, sender = owner, amount=1.0):
    """Append a new value as well as the last blockchain value to the blockchain.

    Argumments:
        :sender: The sender of the transaction.
        :recipient: The recipient of the transaction.
        :amount: The amount of coins sent with the transaction (default = 1.0 coin).
    """
    transaction = {
        'sender': sender,
        'recipient': recipient,
        'amount': amount
    }
    open_transactions.append(transaction)
    participants.add(sender)
    participants.add(recipient)
    


def mine_block():
    #Take all open transactions and add them to a new block.
    last_block = blockchain[-1]
    hashed_block = hash_block(last_block)
    block = {
        'previous_hash': hashed_block,
        #Index not necessary but can add more metadata.
        'index': len(blockchain),
        'transactions': open_transactions
    }
    blockchain.append(block)


def get_transaction_value():
    """Returns the input of the user (the recipient names and a new transaction amount as a float)."""
    tx_recipient = input('Enter the recipient of the transaction: ')
    tx_amount = float(input('Your transaction amount please: '))
    return tx_recipient, tx_amount


def get_user_choice():
    """Propmtts the user for its choice and returns it."""
    user_input = input('Your choice: ')
    return user_input


def print_blockchain_elements():
    """Output all blocks of the blockchain."""
     #Output the blockchain list to the console.
    for block in blockchain:
        print('Outputting block')
        print(block)
    else:
        print('-' * 20)


def verify_chain():
    """Compare a stored hashed in a given block with the recalucaled hash of the previous block."""
    #Enumerate will give you back a typle which contains the index of the element and the element itself.
    for (index, block) in enumerate(blockchain):
        if index == 0:
            continue
        #Recaulating the hash of the last block and comparing it with the prevously stored hash.
        if block['previous_hash'] != hash_block(blockchain[index - 1]):
            return False
    return True



#Alternative to using "break" using a condition in the while loop
waiting_for_input = True

#A while loop for the user input interface. Exits once waiting_for_input is False or when break is called
while waiting_for_input:
    print('Please choose')
    print('1: Add a new transaction value')
    print('2: Mine a new block')
    print('3: Output the blockchain blocks')
    print('4: Output participants')
    print('h: Manipulate the chain')
    print('q: Quit')
    user_choice = get_user_choice()
    if user_choice == '1':
        tx_data = get_transaction_value()
        #Get access to the tx_data tuple
        recipient, amount = tx_data
        #Add the transaction amount to the blockchain
        add_transaction(recipient, amount=amount)
        print(open_transactions)
    elif user_choice == '2':
        mine_block()
    elif user_choice == '3':
        print_blockchain_elements()
    elif user_choice == '4':
        print(participants)
    elif user_choice == 'h':
        if len(blockchain) >= 1:
            blockchain[0] = {
                'previous_hash': '',
                'index': 0,
                'transactions': [{'sender': 'Chris', 'recipient': 'Katie', 'amount': 100}]
            }
    elif user_choice == 'q':
        waiting_for_input = False
    else:
        print('Input was invalid, please pick a value from the list!')
    if not verify_chain():
        print_blockchain_elements()
        print('Invalid blockchain!')
        break
#Else statement only executes once the loop is done. It's outside the loop by lack of indetation.
else:
    print('User left!')


print('Done!')