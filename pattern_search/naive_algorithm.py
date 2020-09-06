class NaiveAlgorithm():
    def __init__(self, pattern, text):
        self.pattern = pattern
        self.text = text
        self.lenPattern = len(pattern)
        self.lenText = len(text)
        self.search()

    def search(self):
        results = []
        if self.text == "":
            return results
        if self.pattern == "":
            return [0]
        for i in range(self.lenText - self.lenPattern + 1):
            j = 0
            while(j < self.lenPattern):
                if (self.text[i + j] != self.pattern[j]):
                    break
                j += 1
            if (j == self.lenPattern):
                results.append(i)
        return results


def naiveSearch(pattern, text):
    searchClass = NaiveAlgorithm(pattern, text)
    results = searchClass.search()
    return results


if __name__ == '__main__':
    text = "ABCABCAABBCCABCA"
    pattern = "CAB"
    results = naiveSearch(pattern, text)
    print(results)
    text = "ABCABCAABBCCABCA"
    pattern = "ABCABCAABBCCABCA"
    results = naiveSearch(pattern, text)
    print(results)
    text = "ABCABCAABBCCABCA"
    pattern = ""
    results = naiveSearch(pattern, text)
    print(results)
    text = ""
    pattern = "CAB"
    results = naiveSearch(pattern, text)
    print(results)
    text = ""
    pattern = ""
    results = naiveSearch(pattern, text)
    print(results)
