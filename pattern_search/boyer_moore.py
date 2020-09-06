
class BoyerMooreSearch():
    def __init__(self, pattern, text):
        self.text = text
        self.pattern = pattern    

    def badCharPreprocess(self):
        self.bcTable = {}
        for i in range(len(self.pattern)):
            self.bcTable[self.pattern[i]] = i

    def goodSuffixPreprocess1(self):
        patternLen = len(self.pattern)
        i = patternLen
        j = i + 1
        self.borders = [0]*j
        self.borders[i] = j
        self.gsTable = [0]*j
        while i > 0:
            while j <= patternLen and self.pattern[i-1] != self.pattern[j-1]:
                if self.gsTable[j] == 0:
                    self.gsTable[j] = j - i
                j = self.borders[j]
            i -= 1
            j -= 1
            self.borders[i] = j

    def goodSuffixPreprocess2(self):
        j = self.borders[0]
        for i in range(len(self.pattern)+1):
            if self.gsTable[i] == 0:
                self.gsTable[i] = j
            if i == j:
                j = self.borders[j]

    def bmPreprocess(self):
        self.badCharPreprocess()
        self.goodSuffixPreprocess1()
        self.goodSuffixPreprocess2()

    def search(self):
        self.bmPreprocess()
        i = 0
        results = []
        if self.text == '':
            return results
        if self.pattern == '':
            return [0]
        patternLen = len(self.pattern)
        textLen = len(self.text)
        while i <= textLen - patternLen:
            j = patternLen - 1
            while j >= 0 and self.pattern[j] == self.text[i+j]:
                j -= 1
            if j < 0:
                results.append(i)
                i += self.gsTable[0]
            else:
                goodSuffixShift = self.gsTable[j+1]
                badCharShift = j - self.bcTable.get(self.text[i+j], -1)
                i += max(goodSuffixShift, badCharShift)
        return results


def BMSearch(pattern, text):
    searchClass = BoyerMooreSearch(pattern, text)
    results = searchClass.search()
    return results
    # for i in results:
    #     print(f"Pattern '{pattern}' found at id {i}")


if __name__ == '__main__':
    text = "ABCABCAABBCCABCA"
    pattern = "CAB"
    result = BMSearch(pattern, text)
    print(result)
    text = "ABCABCAABBCCABCA"
    pattern = "ABCABCAABBCCABCA"
    result = BMSearch(pattern, text)
    print(result)
    text = "ABCABCAABBCCABCA"
    pattern = ""
    result = BMSearch(pattern, text)
    print(result)
    text = ""
    pattern = "CAB"
    result = BMSearch(pattern, text)
    print(result)
    text = ""
    pattern = ""
    result = BMSearch(pattern, text)
    print(result)
