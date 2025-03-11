"""You are given a list of sentences. Create a word tree from each sentence and find how many times the word is appeared in other word trees."""
sentences = ["My name is Ram", "He is a good person", "You should be careful while coding", "He can do better", 
             "The person is mysterious", "Jay Shree Ram", "It is my pen."]

word_trees=[sentence.split(" ") for sentence in sentences]
word_counts={}
for tree in word_trees:
    for word in tree:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

print("word_trees =", word_trees)
print("Number of times each word appears:")
print(word_counts)