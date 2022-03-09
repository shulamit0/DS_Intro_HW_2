def reverse(sentence=None, word=None):
    if not isinstance(sentence, str) or not isinstance(word, str) :
        return "invalid input"

    else:
        if sentence.count(word) == 0:
            return "The word was not found"

        else:
            new_sentence = sentence.replace(word, word[::-1], 1)
            return new_sentence
#
# #examples:
#
# print(reverse("Dani likes bananas, Dani also likes apples likes", "likes"))
# print(reverse("Dani likes bananas, Dani also likes apples", 2))
# print(reverse("Dani likes bananas, Dani also likes apples", "ke"))
# print(reverse("Dani likes bananas, Dani also likes apples", "potato"))
# print(reverse("Dani likes bananas, Dani also likes apples", "apples"))
