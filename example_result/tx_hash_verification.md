# ✅ Transaction Verification: Patched `.send()` Function (bit library)

This file demonstrates a real testnet transaction created using the patched `services.py` file from this repository.

---

## 📦 Transaction Summary

- **Sender WIF**: `cW8JmqmQEwjYHjrL3E235CdbtQ2tM3GLY7ekB8L4izAUCSGcxFt9`
- **Receiver Address**: `n2KykcTd9cU2NdZPRSWVcGDWogFE3q6LsK`
- **Amount Sent**: `0.0002 BTC`
- **Broadcast Method**: `key.send()` using patched Bit library

---

## 🧾 Transaction Hash

```
3c1570c0cfe61da831414a36cf257baeb42eacaa1fe0c8b64a16e879e5b47ede
```

---

## 🔎 Verify on Blockstream

➡️ [View Transaction on Blockstream (Testnet)](https://blockstream.info/testnet/tx/3c1570c0cfe61da831414a36cf257baeb42eacaa1fe0c8b64a16e879e5b47ede)

---


## 💻 Commands Used to Produce This Transaction


```bash
# Check sender balance before sending
python3 bit_wallet.py --testnet balance cW8JmqmQEwjYHjrL3E235CdbtQ2tM3GLY7ekB8L4izAUCSGcxFt9
# Output:
# Balance: 0.00105473 BTC


# Check receiver balance before sending
python3 bit_wallet.py --testnet balance cNYhtSUvmrbmi4CWRBK525uu4oEGqZ3bjEUYZJGjshNWMUs4LoD9
# Output:
# Balance: 0.00016548 BTC


# Send BTC from sender to receiver
python3 bit_wallet.py --testnet send cW8JmqmQEwjYHjrL3E235CdbtQ2tM3GLY7ekB8L4izAUCSGcxFt9 n2KykcTd9cU2NdZPRSWVcGDWogFE3q6LsK 0.0002
# Output:
# Transaction sent! Hash: 3c1570c0cfe61da831414a36cf257baeb42eacaa1fe0c8b64a16e879e5b47ede


# Confirm new receiver balance
python3 bit_wallet.py --testnet balance cNYhtSUvmrbmi4CWRBK525uu4oEGqZ3bjEUYZJGjshNWMUs4LoD9
# Output:
# Balance: 0.00036548 BTC
```


---

## 🧪 Balance Change Proof

| Time       | Receiver Balance (BTC) |
|------------|-------------------------|
| Before     | `0.00016548`            |
| After Send | `0.00036548`            |

---

This confirms that the patched version of `bit.network.services` successfully broadcasts transactions using `.send()`.

🛠 Verified by: **Salim Ben Khadija**
