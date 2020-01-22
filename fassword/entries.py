from fassword.utils import load_data
from getpass import getpass
from cryptography.fernet import Fernet
from fassword.utils import save_data
from sys import exit
import cryptography

def init_data():
    print("\nStarting first time setup\n")
    password_match = False

    while not password_match:
        password = getpass("Enter a new master password: ")
        confirmation = getpass('Confirm your password: ')
    
        if password == confirmation:
            password_match = True
        else:
            print('\nPasswords do not match. Try again\n')
            
    key = Fernet.generate_key()
    fern = Fernet(key)
    master = fern.encrypt(bytes(password, 'utf-8'))

    data = {
        'key': key.decode('utf-8'),
        'master': master.decode('utf-8'),
        'entry': {} 
    }

    save_data(data)

def unlock_master():
    data = load_data()
    attempt = bytes(getpass("Enter your master password: "), 'utf-8')
    f = Fernet(bytes(data['key'], 'utf-8'))
 
    master = f.decrypt(bytes(data['master'], 'utf-8'))
    if master == attempt:

        return master == attempt
    else:
        exit("You entered the wrong password")    

def add_entry(entry):
   
    """
    Stuff to check if password exists, and if it does not,
    encrypt, store and save data.
    throw error if password is there.
    """
    
    loaded_data = load_data()
    if entry in loaded_data["entry"]:
    
        print(f"{entry} is already in the database retry")
    else:
        key = bytes(loaded_data['key'], 'utf-8')
        g = Fernet(key)
        gottenpass = getpass(f"please enter the password for {entry}: ")
        encrypted_pass = g.encrypt(bytes(gottenpass, 'utf-8'))
        loaded_data['entry'][entry] = encrypted_pass.decode('utf-8')
        save_data(loaded_data)

def decrypt_entry(entry):
    
    loaded_data2 = load_data()
    if entry in loaded_data2["entry"]:
        print("Before we get on with this you just need to confirm you are you lmao")
        unlock_master()
        # Do the decrypty stuff
        key2 = bytes(loaded_data2['key'], 'utf-8')
        h = Fernet(key2)
        data4decrypt = loaded_data2["entry"]
        password = data4decrypt[entry]
        decrypted_pass = h.decrypt(bytes(password, 'utf-8'))
        decrypted_pass = decrypted_pass.decode('utf-8')
        print(decrypted_pass)
            
    else:
        print("Whatever you entered in not in our databases get troled ( ͡° ͜ʖ ͡°)")

    pass


