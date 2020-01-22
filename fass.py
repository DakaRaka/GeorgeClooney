from fassword.utils import load_data
import argparse
from fassword.entries import init_data
from fassword.entries import add_entry
from fassword.entries import unlock_master
from fassword.entries import decrypt_entry
from fassword.entries import list_entrys
parser = argparse.ArgumentParser()

parser.add_argument(
    'entry',
    type=str,
    help="The desired password to decrypt"
)

parser.add_argument(
    '-a', '--add',
    action="store_true",
    default=False,
    help="Add entry to password store"
)

parser.add_argument(
    '-d', '--delete',
    action="store_true",
    default=False,
    help="Delete an entry"
)


args = parser.parse_args()



def main():
    data = load_data()

    if not data:
        init_data() 
    if args.add:
        unlock_master()
        add_entry(args.entry)
    else:
        decrypt_entry(args.entry)
    #Carry on with


main()
