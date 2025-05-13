# 271. Encode and Decode Strings
#
# Description:
# Design an algorithm to encode a list of strings to a single string. The encoded string is then sent over a network
# and is decoded back to the original list of strings.
# Implement the functions:
#   encode(strs: List[str]) -> str
#   decode(s: str) -> List[str]
#
# Constraints:
# 1 <= strs.length <= 10^4
# 0 <= strs[i].length <= 10^4
# strs[i] contains any possible characters (including empty string).

from typing import List
import unittest

def encode(strs: List[str]) -> str:
    """
    Encodes a list of strings to a single string.
    """
    # TODO: Implement encoding logic
    pass


def decode(s: str) -> List[str]:
    """
    Decodes a single encoded string back to a list of strings.
    """
    # TODO: Implement decoding logic
    pass

class TestEncodeDecodeStrings(unittest.TestCase):
    def setUp(self):
        self.test_cases = [
            {"strs": ["hello","world"], "id": "Simple words"},
            {"strs": ["",""],         "id": "Empty strings"},
            {"strs": [],                 "id": "Empty list"},
            {"strs": ["/user:data","foo|bar",""], "id": "Special chars and empty"},
            {"strs": ["a" * 1000],      "id": "Long string"},
        ]

    def test_encode_decode(self):
        for case in self.test_cases:
            with self.subTest(case=case["id"]):
                encoded = encode(case["strs"])
                decoded = decode(encoded)
                self.assertIsInstance(encoded, str,   "Encoded result should be a string")
                self.assertIsInstance(decoded, list,  "Decoded result should be a list")
                self.assertEqual(
                    decoded,
                    case["strs"],
                    f"Round-trip failed for case '{case['id']}'"
                )

if __name__ == "__main__":
    unittest.main()
