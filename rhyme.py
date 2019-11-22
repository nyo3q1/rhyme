import csv
import MeCab  # type: ignore
from pykakasi import kakasi  # type: ignore


class Rhyme:
    def __init__(self, word: str, match_vowel: int = 2):
        self.__init_mecab()
        self.__init_kakasi()

        self.word = word
        self.match_vowel = match_vowel

    def __init_mecab(self):
        self.m = MeCab.Tagger("-Oyomi")

    def __init_kakasi(self):
        _kakasi = kakasi()
        _kakasi.setMode('H', 'a')  # hiragana to roman
        _kakasi.setMode('K', 'a')  # katakana to roman
        self.conv = _kakasi.getConverter()

    def yomi(self) -> str:
        return self.m.parse(self.word).rstrip('\n')

    def roman(self) -> str:
        return self.conv.do(self.yomi())

    def vowel(self) -> str:
        return "".join([x for x in self.roman() if x in "aiueon"])

    def rhyme(self) -> str:
        with open("test.csv") as f:
            reader = csv.reader(f)
            for row in reader:
                word, vowel = row
                if self.vowel()[-self.match_vowel:] == vowel[-self.match_vowel:]:
                    return word
        return ""


if __name__ == "__main__":
    import sys

    if len(sys.argv) > 2:
        rhyme = Rhyme(sys.argv[1], int(sys.argv[2]))
    else:
        rhyme = Rhyme(sys.argv[1])
    result = rhyme.rhyme()
    result = result if result else "何もない"
    print(result)
