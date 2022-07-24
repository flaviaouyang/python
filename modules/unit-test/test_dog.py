import unittest, dog

class TestDog(unittest.TestCase):
  
  def test_name(self):
    self.assertEqual("The dog's name: Fido", dog.print_name("Fido"))
    
  def test_age(self):
    self.assertEqual("The dog's age: 3", dog.print_age(3))
# how to run the tests:
# python3 -m unittest test_dog.py

# output:
# .
# ----------------------------------------------------------------------
# Ran 1 test in 0.000s

# OK

if __name__ == "__main__":
  unittest.main()
  # with this, we can run the tests by simply running the file.