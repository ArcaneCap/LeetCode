'''
A sentence is a list of words that are separated by a single space with no leading or trailing spaces.

You are given an array of strings sentences, where each sentences[i] represents a single sentence.

Return the maximum number of words that appear in a single sentence.
'''

# sentences[i] does not have leading or trailing spaces.
# All the words in sentences[i] are separated by a single space.

def mostWordsFound(sentences: list[str]) -> int:
    # Count number of spaces since each word = 1 space
    # The last word doesn't include a space so we add 1 to final max_value
    return max(sentence.count(" ") for sentence in sentences) + 1


# Exp. out = 6
sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]
print(mostWordsFound(sentences))

# Exp. out = 3
sentences = ["please wait", "continue to fight", "continue to win"]
print(mostWordsFound(sentences))