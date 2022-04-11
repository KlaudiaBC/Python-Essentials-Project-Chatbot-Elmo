tutaj sie zaczyna:
# Text preprocessing
# Bag of words - words included in
# tags and patterns, which will be a base for
# search for the right answer
for intent in intents['Intents']:
    for pattern in intent['patterns']:
        # take each word and tokenize it
        w = nltk.word_tokenize(pattern)
        words.extend(w)
        # adding documents (patterns)
        documents.append((w, intent['tag']))
        # adding classes (tags) to the class list
        if intent['tag'] not in classes:
            classes.append(intent['tag'])
        if intent['responses'] not in responses:
            responses.append((intent['responses'], intent['tag']))

# Lemmatization -  create base word,
# in attempt to represent related words,
# tokenized words are converted into shorten
# root words to remove redundancy
words = [lemmatizer.lemmatize(w) for w in words if w not in ignore_words]
words = sorted(list(set(words)))

# Create a sorted list of tags
classes = sorted(list(set(classes)))

print(len(documents), "documents", documents)
print(len(classes), "classes", classes)
print(len(words), "unique lemmatized words", words)

# taking each response from each intent and connect it with a tag,
# building a list of responses
# for intent in intents['Intents']:
#     for response in intent['responses']:
#         # adding documents (patterns)
#         classes.append(intent['responses'])

# print(responses)


message = input()

def process_answer():
    for msg in message:
        # fix this words procesing!!
        # take each word and lemma
        msg = nlp(message)
        for token in msg:
            msg_lem = token.lemma_
        
        print(msg_lem)



    # check = any(item in msg_lem for item in words)
    # if check == True:

    if msg_lem in words:
        for word in words:
            if word == msg_lem:


                for document in documents:
                    if word in document:
                        print("word is", document[1])
                                
    else:
        print("none")


process_answer()

# res = [i[1] for i in documents]
# print(res)



# def display_question(question):
#     """
#     Iterate over key/value pairs in dict and print them
#     """
#     for key, value in question_dict.items():
#         if key == question:
#             print(value)