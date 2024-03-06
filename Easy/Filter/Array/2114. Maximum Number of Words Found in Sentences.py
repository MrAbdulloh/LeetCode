def mostWordsFound(sentences: list[str]) -> int:
    # result = []
    # for sentence in sentences:
    #     words = sentence.split()
    #     result.append(len(words))
    # return max(result)

    return max((len(sentence.split()) for sentence in sentences))


sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]
print(mostWordsFound(sentences))
