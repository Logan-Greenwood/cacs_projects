email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()

# remove single censored word from text
def censor_a_word(text, word):
    return text.replace(word, "redacted")

# print(censor_a_word(email_one, "learning algorithms"))

# remove word from text if word on a list
proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithm", "her", "herself"]


def remove_proprietary(text, terms_to_remove):
    for term in proprietary_terms:
        if term in text:
            text = text.replace(term, "redacted")
    return text

# print(remove_proprietary(email_two, proprietary_terms))


# remove phrase from text if phrase occurs too often
negative_words = ["concerned", "behind", "danger",
                  "dangerous", "alarming", "alarmed", "out of control",
                  "help", "unhappy", "bad", "upset", "awful",
                  "broken", "damage", "damaging", "dismal", "distressed",
                  "distressed", "concerning", "horrible", "horribly", "questionable"]


def remove_if_negative(text, words_to_remove):
    i = 0
    for word in words_to_remove:
        for word in text:
            if word == word:
                i += 1
                print(i)
remove_if_negative(email_three, negative_words)