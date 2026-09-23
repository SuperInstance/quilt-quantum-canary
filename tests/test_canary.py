import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', 'quilt-canary'))

import unittest

from quilt_quantum_canary import quantum_canary, verify_all


class TestQuantumCanary(unittest.TestCase):

    def test_single_scheme(self):
        qc = quantum_canary("QPAM")
        # Should be an integer
        self.assertIsInstance(qc, int)
        self.assertGreater(qc, 0)

    def test_all_schemes(self):
        result = verify_all()
        self.assertIn("QPAM", result["quantum_canaries"])
        self.assertIn("MQSM", result["quantum_canaries"])

    def test_determinism(self):
        qc1 = quantum_canary("QPAM")
        qc2 = quantum_canary("QPAM")
        self.assertEqual(qc1, qc2)


if __name__ == "__main__":
    unittest.main()
