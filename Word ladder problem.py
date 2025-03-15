from collections import deque

def word_ladder(begin_word, end_word, word_list):
    word_set = set(word_list)
    queue = deque([(begin_word, 1)])

    while queue:
        word, steps = queue.popleft()
        if word == end_word:
            return steps

        for i in range(len(word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                new_word = word[:i] + c + word[i+1:]
                if new_word in word_set:
                    queue.append((new_word, steps + 1))
                    word_set.remove(new_word)

    return 0

# Example usage
begin_word = "hit"
end_word = "cog"
word_list = ["hot", "dot", "dog", "lot", "log", "cog"]
print(word_ladder(begin_word, end_word, word_list))
