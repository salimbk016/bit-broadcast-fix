# bit Python Library `.send()` Bug Fix – Broadcast Transactions Working Again

This repository provides a verified patch for a critical bug in the [`bit`](https://github.com/ofek/bit) Bitcoin Python library where `.send()` silently fails to broadcast transactions to the Bitcoin network.

## The Problem

When using `key.send(...)`, the method sometimes:
- Returns a TXID that does **not exist** on the blockchain
- Fails silently without raising any clear exception

Root cause:
- Deprecated or broken broadcast endpoints
- Malformed HTTP payload for Blockstream's API

## The Fix

This repo includes a patched version of `bit/network/services.py` that:
- Corrects the `BlockstreamAPI` payload format
- Removes deprecated broadcast services

## 📦 Contents

```
bit-broadcast-fix/
├── bit_patch/
│   └── services_patched.py              # ✅ Patched file
├── test/
│   ├── send_test.py            # 🧪 Script to generate, send, and check balances
│   └── STEP_BY_STEP.md         # 📘 Detailed usage guide with faucet link and commands
├── example_result/
│   └── tx_hash_verification.md # 📄 Real TX hash + balance proof
├── report/
│   └── Technical_Report.pdf    # 📑 Full root cause analysis
├── LICENSE                     # 📜 Simple patch license
└── README.md                   # 🧭 Project overview
```

## How to Apply the Fix

1. Locate the `services.py` file in your environment:

```bash
python3 -c "import bit.network; print(bit.network.__file__.replace('__init__.py', 'services.py'))"
```

2. Replace it with the patched version:

```bash
cp services_patched.py <path_from_step_1>
```

---

## How to Test the Fix

1. Open the step-by-step guide:
   - [`test/STEP_BY_STEP.md`](test/STEP_BY_STEP.md)

2. Generate test wallets:
   ```bash
   python send_test.py --testnet generate
   ```

3. Fund a wallet using:
   👉 [https://coinfaucet.eu/en/btc-testnet/](https://coinfaucet.eu/en/btc-testnet/)

4. Send BTC using the script:
   ```bash
   python send_test.py --testnet send --wif_sender <wif> --to <receiver> --amount <amount>
   ```

5. Confirm TX on Blockstream:
   - View result in [`example_result/tx_hash_verification.md`](example_result/tx_hash_verification.md)

---

## 📄 Resources

- 📘 [Technical Report PDF](report/Technical-Report.pdf)
- 💬 [Stack Overflow Answer](https://stackoverflow.com/questions/74153386/...)
- ✅ [Transaction Proof](example_result/tx_hash_verification.md)
- 🧭 [Usage Guide](test/STEP_BY_STEP.md)

## 🙋‍♂️ Author

Liosna  
Created January 2026  
Open for collaboration or integration into the official repository.
