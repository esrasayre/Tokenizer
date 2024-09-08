def tokenize(input):
    tokenized = []
    punctuation = [".", "?", "!", ",", "'"]
    swap = ["\n", "\t"]
    ignore = ["#"]

    # Add spaces around punctuation
    for marker in punctuation:
        input = input.replace(marker, " " + marker + " ")

    # Replace newline and tab characters with spaces
    for character in swap:
        input = input.replace(character, " ")

    # Convert to lowercase
    input = input.lower()

    # Split the input into tokens
    input = input.split()

    # Ignore certain characters and remove empty tokens
    for token in input:
        if token and token not in ignore:
            tokenized.append(token)
    
    return tokenized

# Fun test case
sentence = "sOmeWHeRe oveR The RaiNBow"
print(tokenize(sentence))
