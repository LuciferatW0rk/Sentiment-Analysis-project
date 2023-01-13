import random
def getreply(message):
    x = open('positive.txt', 'r')
    pos = x.readlines()
    y = open('negative.txt', 'r')
    neg = y.readlines()
    lp = len(pos)
    ln = len(neg)
    X_train = []
    for i in range(lp):
        X_train.append(pos[i])
    for i in range(ln):
        X_train.append(neg[i])
    y_train = []
    for i in range(lp):
        y_train.append(1)
        # 1 is for positive
    for i in range(ln):
        y_train.append(0)
        # 0 is for negative

    ##data cleaning
    import nltk
    from nltk.corpus import stopwords
    from nltk.tokenize import RegexpTokenizer
    from nltk.stem.snowball import SnowballStemmer
    tokenizer = RegexpTokenizer(r'\w+')
    en_stopwords = set(stopwords.words('english'))
    sno = SnowballStemmer('english')

    def getcleanedtext(text):
        text = text.lower()

        # tokenization and stopword removal
        tokens = tokenizer.tokenize(text)
        new_tokens = [token for token in tokens if token not in en_stopwords]
        stemmed_tokens = [sno.stem(token) for token in new_tokens]

        clean_text = " ".join(stemmed_tokens)

        return clean_text

    # test split
    X_test = [message]

    x_clean = [getcleanedtext(i) for i in X_train]
    xt_clean = [getcleanedtext(i) for i in X_test]

    # vectorization
    from sklearn.feature_extraction.text import CountVectorizer
    cv = CountVectorizer(ngram_range=(1, 2))
    x_vec = cv.fit_transform(x_clean).toarray()
    xt_vec = cv.transform(xt_clean).toarray()

    # Multinomial Naive Bayes
    from sklearn.naive_bayes import MultinomialNB
    mn = MultinomialNB()
    mn.fit(x_vec, y_train)
    y_pred = mn.predict(xt_vec)
    return y_pred
plist = ["We are glad it was to your liking ","Thanks, Please chose our service again","Thanks for the positive review"]
nlist = ["Sorry to dissapoint you","Sorry, we will try to improve that","We are sorry for our bad service"]
def bot(message):
    p = getreply(message)
    if p == 0:
        reply = random.choice(nlist)
    elif p == 1:
        reply = random.choice(plist)
    return reply
    message = ("Alice : Anything else? \n" "Human : ")

message = input("Type bye to end the chat or a simple greeting to contact with us \nHuman : ")
if "bye" not in message.lower():
    message = input("Alice : Hi I am Alice, What can I help you with? \nFeed back or Query \nHuman : ")

while True:
    if "bye" in message.lower():
        print("Alice : Bye, Thanks for contacting us")
        break
    elif "feed back" in message.lower():
        print("Alice : What is your opinion regarding our Service?")
        #can be later replaced by any specific type of service
        message = input("Human : ")
        print("Alice : ",bot(message))
        print("Alice : Anything else you would want to add ?")
        message = input("Human : ")
        while "no" not in message:
            message = input("Alice : What do yo want to add? \nHuman : ")
            print("Alice : ", bot(message))
            print("Alice : Anything else you would want to add ?")
            message = input("Human : ")
        if "no" in message :
            print("Alice : ok then bye?")
    elif "query" in message.lower():
        print("Work in progress")
        break

    message = input("Human : ")

