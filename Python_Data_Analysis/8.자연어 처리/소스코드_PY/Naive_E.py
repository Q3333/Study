from nltk.tokenize import word_tokenize
import nltk

train = [('i like you', 'pos'),
('i hate you', 'neg'),
('you like me', 'neg'),
('i like her', 'pos')]

all_words = set(word.lower() for sentence in train
                                for word in word_tokenize(sentence[0]))
all_words                                

t = [({word: (word in word_tokenize(x[0])) for word in all_words}, x[1])
                                                            for x in train]
t                                                        



classifier = nltk.NaiveBayesClassifier.train(t)
classifier.show_most_informative_features()



test_sentence = 'i like MeRui'
test_sent_features = {word.lower():
                                    (word in word_tokenize(test_sentence.lower()))
                                     for word in all_words}
test_sent_features                                    


classifier.classify(test_sent_features)