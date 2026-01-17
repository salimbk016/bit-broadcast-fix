# 🧪 How to Test the Patched `.send()` Function in the `bit` Library

Follow these instructions to quickly verify that the patched `.send()` method works correctly using testnet BTC.

---

## 🛠 STEP 1: Replace the Faulty File

1. Run this command to locate your installed `services.py` file:

```bash
python3 -c "import bit.network; print(bit.network.__file__.replace('__init__.py', 'services.py'))"
```

2. Delete the broken file:

```bash
rm <output_path_from_above>
```

3. Download the fixed `services_patched.py` from this repository and place it there:

```bash
mv services_patched.py <output_path_from_above>
```

---

## 🔐 STEP 2: Generate Wallets (Testnet)

Run:
```bash
python3 send_test.py --testnet generate
```

This prints:
- A Bitcoin **address**
- A **WIF** (private key)

Run this twice to get a sender and receiver wallet.

---

## 💸 STEP 3: Get Testnet BTC

Paste the sender address into this faucet:
👉 [https://coinfaucet.eu/en/btc-testnet/](https://coinfaucet.eu/en/btc-testnet/)

Wait 1–3 minutes for confirmation.

---

## 💰 STEP 4: Check Wallet Balance

```bash
python3 send_test.py --testnet balance <sender_wif>
```

---

## 🚀 STEP 5: Send BTC

Send funds from sender to receiver:

```bash
python3 send_test.py --testnet send  <sender_wif> <receiver_address> <amount_in_btc>
```

Example:
```bash
python3 send_test.py --testnet send cR7... tb1q... 0.0001
```

Check your transaction:
👉 [https://blockstream.info/testnet/tx/<your_tx_hash>](https://blockstream.info/testnet/tx/)

---

## 📉 STEP 6: Check New Balance (Receiver)

```bash
python3 send_test.py --testnet balance <receiver_wif>
```

---

✅ You're Done!

You have now:
- Used the patched `.send()` function
- Sent BTC on testnet
- Verified the working TX on Blockstream

If something fails, double-check:
- You replaced the correct file
- The faucet confirmed the transfer
- You used the correct WIF and address
