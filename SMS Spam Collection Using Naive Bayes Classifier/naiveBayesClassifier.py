import pandas as pd
import numpy as np
import sys

class NaiveBayesFilter:
    def __init__(self):
        self.data = []
        self.vocabulary = [] #returns tuple of unique words
        self.proba = []
        self.prob = []
        self.p_spam = 0 #Probability of Spam
        self.p_ham = 0  #Probability of Ham
        # Initiate parameters
        self.parameters_spam = {unique_word: 0 for unique_word in self.vocabulary}
        self.parameters_ham = {unique_word: 0 for unique_word in self.vocabulary}

    def fit(self, X, y):
        for sms in X:
            for word in sms:
                self.vocabulary.append(word)

        self.vocabulary = list(set(self.vocabulary))

        word_counts_per_sms = {unique_word: [0] * len(X) for unique_word in self.vocabulary}
        for index, sms in enumerate(X):
            for word in sms:
                word_counts_per_sms[word][index] += 1

        word_counts = pd.DataFrame(word_counts_per_sms)
        self.data = pd.concat([y, X, word_counts], axis=1)

        print(self.data)

        spam_messages = self.data[self.data['Label'] == 'spam']
        ham_messages = self.data[self.data['Label'] == 'ham']

        # P(Spam) and P(Ham)
        self.p_spam = len(spam_messages) / len(self.data)
        self.p_ham = len(ham_messages) / len(self.data)

        # N_Spam
        n_words_per_spam_message = spam_messages['SMS'].apply(len)
        n_spam = n_words_per_spam_message.sum()

        # N_Ham
        n_words_per_ham_message = ham_messages['SMS'].apply(len)
        n_ham = n_words_per_ham_message.sum()

        # N_Vocabulary
        n_vocabulary = len(self.vocabulary)

        # Laplace smoothing
        alpha = 1

        print('Number of words in spam messages is: ' + str(n_spam) + '\n')
        print('Number of words in ham messages is: ' + str(n_ham) + '\n')
        print('Number of unique words are: ' + str(n_vocabulary))

        # Calculate parameters
        for word in self.vocabulary:
            n_word_given_spam = spam_messages[word].sum() # spam_messages already defined
            p_word_given_spam = (n_word_given_spam + alpha) / (n_spam + alpha*n_vocabulary)
            self.parameters_spam[word] = p_word_given_spam

            n_word_given_ham = ham_messages[word].sum() # ham_messages already defined
            p_word_given_ham = (n_word_given_ham + alpha) / (n_ham + alpha*n_vocabulary)
            self.parameters_ham[word] = p_word_given_ham

        return self.data


    def predict_proba(self, X):
        "*** YOUR CODE HERE ***"
        # Isolating spam and ham messages first
        self.proba_dict = {sentences: [1] * 2 for sentences in range(len(X))}
        for index, sms in enumerate(X):
            for word in sms:
                if word in self.vocabulary:
                    self.proba_dict[index][0] *= self.parameters_ham[word]
                    self.proba_dict[index][1] *= self.parameters_spam[word]
                else:
                    self.proba_dict[index][0] *= 1
                    self.proba_dict[index][1] *= 1

        # print(self.proba_dict)

        proba_table = pd.DataFrame(self.proba_dict,index=['ham','spam']).T
        
        predict_list = []
        for i in range(len(proba_table)):
            if proba_table.loc[i,'spam'] > proba_table.loc[i,'ham']:
                predict_list.append('spam')
            else:
                predict_list.append('ham')
        predict_table = pd.DataFrame(predict_list,columns=['predict'])
        # print(predict_list)

        self.proba = pd.concat([X, proba_table,predict_table], axis=1)

        return self.proba

    def score(self,y,predict_label):
        A = [[0,0], 
            [0, 0]]
        for i in range(len(y)):
            if (predict_label[i] ==  'ham') & (y[i] == 'ham'):
                A[0][0] += 1
            elif (predict_label[i] ==  'spam') & (y[i] == 'spam'):
                A[1][1] += 1
            elif (predict_label[i] ==  'spam') & (y[i] == 'ham'):
                A[1][0] += 1
            else :
                A[0][1] += 1

        for line in A:
            print ('  '.join(map(str, line)))

        precision = A[0][0] / (A[0][0] + A[1][0])
        recall = A[0][0] / (A[0][0] + A[0][1])
        F1 = (2*precision*recall)/(precision+recall)

        accuracy = (A[0][0] + A[1][1])/len(y)
        print('Naive Bayes accuracy: ', accuracy*100,'%')
        return precision,recall,F1


