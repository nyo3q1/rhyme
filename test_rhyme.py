import unittest
from rhyme import Rhyme

class TestRhyme(unittest.TestCase):
    def test_word2roman(self):
        rhyme = Rhyme("しずおか")
        self.assertEqual(rhyme.roman(), "shizuoka")

        rhyme = Rhyme("シズオカ")
        self.assertEqual(rhyme.roman(), "shizuoka")

        rhyme = Rhyme("静岡")
        self.assertEqual(rhyme.roman(), "shizuoka")

    def test_vowel(self):
        rhyme = Rhyme("静岡")
        self.assertEqual(rhyme.vowel(), "iuoa")

        rhyme = Rhyme("ありがとう")
        self.assertEqual(rhyme.vowel(), "aiaou")

        rhyme = Rhyme("パイソン")
        self.assertEqual(rhyme.vowel(), "aion")
    
    def test_rhyme(self):
        rhyme = Rhyme("ありがとう")
        self.assertEqual(rhyme.rhyme(), "オリゴ糖")

        rhyme = Rhyme("ありがとう", len("ありがとう"))
        self.assertEqual(rhyme.rhyme(), "大麻草")

        rhyme = Rhyme("パイソン")
        self.assertEqual(rhyme.rhyme(), "厚切りジェイソン")

        rhyme = Rhyme("パイソン", len("パイソン"))
        self.assertEqual(rhyme.rhyme(), "")

if __name__ == "__main__":
    unittest.main()