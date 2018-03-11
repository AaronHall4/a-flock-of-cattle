
import pickle
# import numpy as np

from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import SGDClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.svm import LinearSVC
from sklearn.svm import SVC

import nltk
from nltk.corpus import stopwords



race_lut = ['dwarf', 'elf', 'halfling', 'human', 'dragonborn', 'gnome', 'half-elf', 'half-orc', 'tiefling']
class_lut = ['barbarian', 'bard', 'cleric', 'druid', 'fighter', 'monk', 'paladin', 'ranger', 'rogue', 'sorcerer', 'warlock', 'wizard']
race_dict = {'dwarf':0, 'elf':1, 'halfling':2, 'human':3, 'dragonborn':4, 'gnome':5, 'half-elf':6, 'half-orc':7, 'tiefling':8, 'half elf':6}
class_dict = {'barbarian':0, 'bard':1, 'cleric':2, 'druid':3, 'fighter':4, 'monk':5, 'paladin':6, 'ranger':7, 'rogue':8, 'sorcerer':9, 'warlock':10, 'wizard':11, 'figher':4}



def stemmed_words(doc):
  stemmer = nltk.stem.snowball.SnowballStemmer('english')  #nltk.stem.PorterStemmer()
  analyzer = CountVectorizer().build_analyzer()

  f = open('custom_stopwords.txt', 'r')
  custom_stops = f.read().split()
  f.close()
  stops = set(stopwords.words('english')).union(custom_stops)
  return (stemmer.stem(w) for w in analyzer(doc) if w.lower() not in stops)


def get_pipeline(balanced=True):
    f = open('data_lst', 'rb')
    data = pickle.load(f)
    f.close()

    story_lst = [d[0] for d in data]    

    race_lst = [race_dict[d[1]] for d in data]
    class_lst = [class_dict[d[2]] for d in data]
    
    
    weight = 'balanced' if balanced else None
    race_clf = Pipeline([('vect', CountVectorizer(analyzer=stemmed_words)),
                         ('tfidf', TfidfTransformer()),
                         ('clf', LinearSVC(loss='hinge', class_weight=weight))])
    class_clf = Pipeline([('vect', CountVectorizer(analyzer=stemmed_words)),
                          ('tfidf', TfidfTransformer()),
                          ('clf', LinearSVC(loss='hinge', class_weight=weight))])

    race_pipeline = race_clf.fit(story_lst, race_lst)
    class_pipeline = class_clf.fit(story_lst, class_lst)

    return race_pipeline, class_pipeline

def leave_one_out_acc():
    f = open('data_lst', 'rb')
    data = pickle.load(f)
    f.close()

    story_lst = [d[0] for d in data]    

    race_lst = [race_dict[d[1]] for d in data]
    class_lst = [class_dict[d[2]] for d in data]
    
    race_correct = [0 for i in range(len(race_lut))]
    class_correct = [0 for i in range(len(class_lut))]
    
    race_total = [0 for i in range(len(race_lut))]
    class_total = [0 for i in range(len(class_lut))]

    for i in range(len(story_lst)):
        race_clf = Pipeline([('vect', CountVectorizer(stop_words='english')),
                             ('tfidf', TfidfTransformer()),
                             ('clf', LinearSVC(loss='hinge', class_weight='balanced'))])
                             # ('clf', SGDClassifier(loss='hinge', tol=None, max_iter=1000))])
        class_clf = Pipeline([('vect', CountVectorizer(stop_words='english')),
                              ('tfidf', TfidfTransformer()),
                              ('clf', LinearSVC(loss='hinge', class_weight='balanced'))])
                             # ('clf', SGDClassifier(loss='hinge', tol=None, max_iter=1000))])

        race_pipeline = race_clf.fit(story_lst[:i]+story_lst[i+1:], race_lst[:i]+race_lst[i+1:])
        class_pipeline = class_clf.fit(story_lst[:i]+story_lst[i+1:], class_lst[:i]+class_lst[i+1:])

        if race_lst[i] == race_pipeline.predict([story_lst[i]])[0]:
            race_correct[race_lst[i]] += 1
        race_total[race_lst[i]] += 1
        if class_lst[i] == class_pipeline.predict([story_lst[i]])[0]:
            class_correct[class_lst[i]] += 1
        class_total[class_lst[i]] += 1

    race_acc = [float(race_correct[i])/race_total[i] for i in range(len(race_correct))]
    class_acc = [float(class_correct[i])/class_total[i] for i in range(len(class_correct))]

    return race_correct, class_correct, race_total, class_total, race_acc, class_acc#, np.mean(race_acc), np.mean(class_acc)

def grid_search():
    f = open('data_lst', 'rb')
    data = pickle.load(f)
    f.close()

    story_lst = [d[0] for d in data]    

    race_lst = [race_dict[d[1]] for d in data]
    class_lst = [class_dict[d[2]] for d in data]
    
    race_correct = [0 for i in range(len(race_lut))]
    class_correct = [0 for i in range(len(class_lut))]
    
    race_total = [0 for i in range(len(race_lut))]
    class_total = [0 for i in range(len(class_lut))]



    params = {}
    # 'clf__class_weight': [None, 'balanced']} -- lowers performance on grid search metric but maybe better in general?
    # {'vect__ngram_range': [(1,1),(1,2),(1,3)]} -- (1,2), (1,3) better under some configurations
    # {'clf__kernel': ['rbf', 'linear', 'poly', 'sigmoid']} -- linear
    # binary=True, remove tfidf?

    #{'vect__ngram_range': [(1,1),(1,2)],
    # 'clf__alpha': [1e-2, 1e-3, 1e-4]}

    race_clf = Pipeline([('vect', CountVectorizer(analyzer=stemmed_words)),
                         ('tfidf', TfidfTransformer()),
                         ('clf', LinearSVC(loss='hinge', class_weight='balanced'))])
    class_clf = Pipeline([('vect', CountVectorizer(analyzer=stemmed_words)),
                          ('tfidf', TfidfTransformer()),
                          ('clf', LinearSVC( loss='hinge', class_weight='balanced'))])

    gs_race_clf = GridSearchCV(race_clf, params, n_jobs=-1)
    gs_class_clf = GridSearchCV(class_clf, params, n_jobs=-1)

    gs_race_clf.fit(story_lst, race_lst)
    gs_class_clf.fit(story_lst, class_lst)

    return gs_race_clf, gs_class_clf


    
