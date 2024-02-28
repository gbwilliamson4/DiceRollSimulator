import unittest
from main import *


class MyTestCase(unittest.TestCase):

    def create_dice_instances(self):
        list_dice = create_dice_instances(5, 6)
        self.assertEqual(list_dice, 5)


if __name__ == '__main__':
    unittest.main()
