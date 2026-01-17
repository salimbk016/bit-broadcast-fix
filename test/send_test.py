import argparse
from bit import Key, PrivateKeyTestnet
from bit.network import NetworkAPI
from bit.network import fees

def get_key_class(is_testnet):
    """Returns the appropriate Key class based on network selection."""
    return PrivateKeyTestnet if is_testnet else Key

def generate(args):
    """Generates a new key and prints address and WIF."""
    KeyClass = get_key_class(args.testnet)
    k = KeyClass()
    print(f"Address: {k.address}")
    print(f"WIF: {k.to_wif()}")

def balance(args):
    """Checks balance for a WIF key."""
    try:
        KeyClass = get_key_class(args.testnet)
        k = KeyClass(args.wif)
        print(f"Balance: {k.get_balance('btc')} BTC")
    except Exception as e:
        print(f"Error checking balance: {e}")

def send(args):
    """Sends transactions."""
    try:
        KeyClass = get_key_class(args.testnet)
        k = KeyClass(args.wif)
        # bit library handles fee estimation and utxo selection automatically
        tx_hash = k.send([(args.dest, args.amount, 'btc')])
        print(f"Transaction sent! Hash: {tx_hash}")
    except Exception as e:
        print(f"Error sending transaction: {e}")


def main():
    parser = argparse.ArgumentParser(description="Python CLI Bitcoin Wallet using bit library")
    
    # Global arguments
    parser.add_argument('--testnet', action='store_true', help="Use Testnet (default is Mainnet)")

    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    subparsers.required = True

    # generate
    parser_gen = subparsers.add_parser('generate', help='Generate a new WIF')
    parser_gen.set_defaults(func=generate)


    # balance
    parser_bal = subparsers.add_parser('balance', help='Check balance')
    parser_bal.add_argument('wif', help='Wallet Import Format (WIF) key')
    parser_bal.set_defaults(func=balance)

    # send
    parser_send = subparsers.add_parser('send', help='Send BTC')
    parser_send.add_argument('wif', help='Sender Wallet Import Format (WIF) key')
    parser_send.add_argument('dest', help='Destination address')
    parser_send.add_argument('amount', type=float, help='Amount in BTC')
    parser_send.set_defaults(func=send)


    # Parse known args to separate global flags from subcommand args if mixed
    # But with simple argparse, global args must come BEFORE subcommand.
    args = parser.parse_args()
    
    if hasattr(args, 'func'):
        args.func(args)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
