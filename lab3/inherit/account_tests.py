import unittest
import account

class TestCases(unittest.TestCase):
   def test_1(self):
      savings = account.Account(1000)
      self.assertEqual(savings.getBalance(), 1000)


   def test_2(self):
      savings = account.Account(1000)
      self.assertEqual(savings.getBalance(), 1000)
      savings.purchaseItem(20)
      self.assertEqual(savings.getBalance(), 980)


   def test_3(self):
      savings = account.Account(1000)
      self.assertEqual(savings.getBalance(), 1000)
      savings.returnItem(20)
      self.assertEqual(savings.getBalance(), 1020)
   
   def test_4(self):
      savings = account.PremiumAccount(1000)
      self.assertEqual(savings.getBalance(), 1000)
      savings.returnItem(20)
      self.assertEqual(savings.getBalance(), 1018)
   
   def test_5(self):
      savings = account.PremiumAccount(1000)
      self.assertEqual(savings.getBalance(), 1000)
      savings.purchaseItem(30)
      self.assertEqual(savings.getBalance(), 973)
   
   def test_6(self):
      savings = account.PremiumAccount(567)
      self.assertEqual(savings.getBalance(), 567)
      savings.returnItem(95)
      savings.purchaseItem(95)
      self.assertEqual(savings.getBalance(), 567)
   

# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

