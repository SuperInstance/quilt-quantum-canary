"""quilt-quantum-canary — polyformalism canary verified by quantum amplitude.

The polyformalism fleet canary is verified by encoding 'café Δ 日本語' as
a quantum amplitude (audio sample) and checking that the resulting
quantum state has the same byte hash across all substrate implementations.

This is polyformalism via quantum measurement: the canary is *canon* when
the measurement result is the same in every substrate.
"""
from .canary import quantum_canary, verify_all

__version__ = "0.1.0"
__all__ = ["quantum_canary", "verify_all"]
