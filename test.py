
#using this for local masking test. 

import unittest
from helpers import mask_data


class TestHelpers(unittest.TestCase):

    def test_mask_data(self):
        original_data = "192.168.1.1"
        masked_data = mask_data(original_data)
        self.assertNotEqual(original_data, masked_data, "Masking failed.")

if __name__ == "__main__":
    unittest.main()
