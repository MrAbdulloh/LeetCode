# def sortSentence(s: str) -> str:
#     s_list = sorted(s.split(), key=lambda x: x[-1])
#     ans = []
#     for i in s_list:
#         ans.append(i.replace(i[-1], ''))
#
#     return ' '.join(ans)

def sortSentence(s: str) -> str:
    # words = s.split()
    # mapping = {}
    #
    # for word in words:
    #     index = int(word[-1])
    #     mapping[index] = word[:-1]
    # return ' '.join([mapping[i] for i in sorted(mapping)])
    word = s.split()
    mapping = {}
    for word in word:
        index = word[-1]
        mapping[index] = word[:-1]
    return ' '.join([mapping[i] for i in sorted(mapping)])


s = "is2 sentence4 This1 a3"
print(sortSentence(s))
