class LetterBox(object):
    def __init__(self, top: str, right: str, bottom: str, left: str):
        self.top = list(top.strip().upper())
        self.right = list(right.strip().upper())
        self.bottom = list(bottom.strip().upper())
        self.left = list(left.strip().upper())

    def filter_words(self, words):
        filtered_words = []

        for word in words:
            letters = self.top + self.right + self.bottom + self.left

            if all(letter in letters for letter in word) and not has_consecutive_side_letters(word):
                filtered_words.append(word)

        return filtered_words
    
    def has_consecutive_side_letters(self, word):
        # In progress
        last_side = "none"
        this_side = "none"

        for letter in word:
            
            if letter in self.top:
                last_side = "top"
            elif letter in self.right:
                last_side = "right"
            elif letter in self.bottom:
                last_side = "bottom"
            elif letter in self.left:
                last_side = "left"
        
        return True



    def __str__(self):
        res = "  " + " ".join(self.top) + " \n\n"

        for i in range(len(self.right)):
            middle = " " * (len(self.top) * 2 + 2)
            res += self.left[i] + middle + self.right[i] + "\n\n"

        res += "  " + " ".join(self.bottom) + " \n\n"

        return res


def load_word_list(filename):
    with open(filename, 'r') as f:
        return [word.strip().upper() for word in f]


# def filter_words(words, box_letters):
#     filtered_words = []
#     for word in words:
#         if all(letter in box_letters for letter in word) and not has_consecutive_letters_from_same_side(word, box_letters):
#             filtered_words.append(word)
#     return filtered_words


# def has_consecutive_letters_from_same_side(word, box_letters):
#     # Implement logic to check for consecutive letters from the same side
#     # Consider using a dictionary to map letters to their sides


# def generate_word_chains(words, starting_letter, current_chain, min_length):
#     if len(current_chain) >= min_length and all(letter in words for letter in current_chain):
#         return [current_chain]
#     chains = []
#     for word in words:
#         if word[0] == starting_letter and word not in current_chain:
#             new_chain = current_chain + [word]
#             chains.extend(generate_word_chains(
#                 words, word[-1], new_chain, min_length))
#     return chains


# def find_shortest_chains(words, box_letters):
#     filtered_words = filter_words(words, box_letters)
#     chains = []
#     for word in filtered_words:
#         chains.extend(generate_word_chains(
#             filtered_words, word[-1], [word], 3))
#     return sorted(chains, key=len)


if __name__ == "__main__":
    box_letters = input(
        "Enter letters for top, right, and bottom sides separated by commas\nFor example: ABC, DEF, GHI, JKL\n> ").split(",")
    words = load_word_list("res/unix-words.txt")
    print("All words: " + str(len(words)))

    box = LetterBox(*box_letters)
    print("::LETTERBOX'D::\n" + str(box))
    print("Filtered words: " + str(len(box.filter_words(words))))

    # shortest_chains = find_shortest_chains(words, box_letters)
    # print("Shortest word chains:")
    # for chain in shortest_chains[:3]:
    # print(" - ".join(chain))
