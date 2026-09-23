# quilt-quantum-canary

> **Canon through quantum.**
> The polyformalism fleet canary verified by quantum amplitude measurement.

## TL;DR

```python
from quilt_quantum_canary import verify_all

result = verify_all()
print(result["fleet_canary"])  # 0x024a555471370b18d
for scheme, qc in result["quantum_canaries"].items():
    print(f"{scheme}: 0x{qc:016x} (matches={result[f'{scheme}_matches']})")
```

## What this is

The Quilt polyformalism fleet has a canary: `fnv1a-64("café Δ 日本語")`
= `0x024a555471370b18d`. All 7 ports (Python, Rust, JS, etc.) produce
this same hash. This is the substrate walker canon's load-bearing
test.

This repo extends the test to **quantum substrates**. The canary is
encoded as audio → quantum state → measurement → FNV-1a. The result
should match the fleet canary.

5 quantum schemes:
- **QPAM** — Quantum Probability Amplitude Modulation
- **SQPAM** — Single-Qubit PAM
- **MSQPAM** — Multi-channel Single-Qubit
- **QSM** — Quantum State Modulation
- **MQSM** — Multi-channel QSM

## Architecture

```
canary string → audio samples (16kHz)
    ↓
quantum state (5 schemes)
    ↓
measurement (8 bits)
    ↓
FNV-1a of bit string
    ↓
quantum canary (hex int)
```

## License

MIT — Casey / SuperInstance, Sept 23, 2026
