def tokenize(input):
    tokenized = []
    punctuation = [".", "?", "!", ",", "'"]
    swap = ["\n", "\t"]
    ignore = ["#"]

    for marker in punctuation:
        input = input.replace(marker, " " + marker)

    for character in swap:
        input = input.replace(character, " ")

    input = input.lower()

    input = input.split(" ")

    for token in input:
        if token not in ignore:
            tokenized.append(token)
    return(tokenized)

sentence = "This is a sample sentence."
print(tokenize(sentence))