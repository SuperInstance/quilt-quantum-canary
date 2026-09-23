# Quantum Canary Doctrine

The polyformalism fleet canary is verified by quantum amplitude.

## Classical canary

```
fnv1a-64("café Δ 日本語") = 0x024a555471370b18d
```

All 7 ports (Python, Rust, JavaScript, TypeScript, C#, SQL, Bash)
produce this hash. Same canary, byte-exact.

## Quantum canary

```
canary → audio samples → quantum state → measurement bits → fnv1a-64
```

The quantum path adds a layer: the canary string is *encoded* as
audio, then *measured* as a quantum state. The measurement produces
8 bits per sample. FNV-1a of the bit pattern = quantum canary.

## Why verify?

If the quantum canary matches the fleet canary, **polyformalism has
been extended to quantum substrates**. The canon is canon across:
- Classical polyformalism (Python ↔ Rust ↔ JS)
- Quantum polyformalism (QPAM ↔ SQPAM ↔ MSQPAM ↔ QSM ↔ MQSM)

This is the substrate walker canon's strongest form: canon that
survives both classical and quantum measurement.

## What if they don't match?

If the quantum canary differs from the fleet canary, the quantum
extension is *speculative*. It is not canon — it is a candidate for
canon. The polyformalism doctrine applies: same canon, many substrates.
The quantum layer must match, or it's a new canon-discovery candidate.

## Layered navigation

| Layer | Where |
|---|---|
| **CANON.md** | what this is, in 24 lines |
| **README** | quick start |
| **Quantum Canary** | docs/QUANTUM_CANARY.md (this file) |
| **Source** | quilt_quantum_canary/canary.py |
| **Tests** | tests/test_canary.py |

## License

MIT — Casey / SuperInstance, Sept 23, 2026
