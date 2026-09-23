"""Quantum-polyformalism canary verification."""


CANARY_INPUT = "café Δ 日本語"


def _fnv1a_64(s: str) -> int:
    """FNV-1a 64-bit hash, byte-for-byte reproducible across languages."""
    h = 0xcbf29ce484222325
    for b in s.encode("utf-8"):
        h = h ^ b
        h = (h * 0x100000001b3) & 0xffffffffffffffff
    return h


def classical_canary() -> int:
    """The fleet canary: fnv1a-64 of 'café Δ 日本語'."""
    return _fnv1a_64(CANARY_INPUT)


def quantum_canary(scheme: str = "QPAM") -> int:
    """Compute a quantum-derived canary: FNV-1a of measurement bits."""
    # Lazy import to avoid circular issues
    import sys
    import os
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "quilt-quantum-audio"))
    from quilt_quantum_audio import lore_to_quantum_canon
    
    result = lore_to_quantum_canon(CANARY_INPUT, scheme=scheme)
    bits = result["measurement_bits"]
    bit_str = "".join(str(b % 2) for b in bits)
    return _fnv1a_64(bit_str)


def verify_all():
    """Verify quantum canary for all 5 schemes, compare to fleet canary."""
    fleet = classical_canary()
    out = {"fleet_canary": fleet, "quantum_canaries": {}}
    for scheme in ["QPAM", "SQPAM", "MSQPAM", "QSM", "MQSM"]:
        qc = quantum_canary(scheme)
        out["quantum_canaries"][scheme] = qc
        out[f"{scheme}_matches"] = (qc == fleet)
    return out


if __name__ == "__main__":
    print("=== Quantum-polyformalism canary verification ===")
    result = verify_all()
    print(f"Fleet canary (classical fnv1a): 0x{result['fleet_canary']:016x}")
    print()
    for scheme, qc in result["quantum_canaries"].items():
        match = "✓ MATCH" if result[f"{scheme}_matches"] else "✗ DIVERGE"
        print(f"  {scheme:8}: 0x{qc:016x}  ({match})")
    
    n_match = sum(1 for s in ["QPAM", "SQPAM", "MSQPAM", "QSM", "MQSM"] if result[f"{s}_matches"])
    print(f"\n{n_match}/5 quantum schemes match fleet canary")
