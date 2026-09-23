# quilt-quantum-canary

**What this repo is**: polyformalism canary verified by quantum amplitude.

Substrate transition in 24 lines:
- canary string "café Δ 日本語" → audio → quantum state → measurement bits
- FNV-1a of measurement bits = quantum-derived canary
- compare to fleet canary (0x024a555471370b18d)
- if all 5 quantum schemes match → canon is canon

The polyformalism fleet canary (same hash across Python/Rust/JS/etc.)
now extends to quantum: same hash across QPAM/SQPAM/MSQPAM/QSM/MQSM.
Canon that survives the quantum measurement is canon that survives
*all* substrates.

Layered navigation: README.md → docs/QUANTUM_CANARY.md → quilt_quantum_canary/canary.py → tests/test_canary.py
