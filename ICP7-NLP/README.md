# ICP-7

#### Complete the following:
```
Name: Keenan Flynn
Email: kpfxn8@umsystem.edu
```
---
```
Partner Name: Jasmine Thai
Partner Email: jtt9fb@umsystem.edu
Partner ICP-Link: https://github.com/UMKC-APL-PythonDeepLearing/icp_7-JasmineThai-hub
```

```
Video Link: https://youtu.be/Ytg_M9chkfU
```
### SUBMIT PYTHON NOTEBOOK FILE (ipynb files)
<br/>
 
# Write brief explanation here:
For Part 1 of ICP 7,

Our goal for Part 1 was to classify each news into one of 20 categories.

    -we learned how to fetch a dataset (20newsgroup) from sklearn.
    -We learned text preprocessing, tokenizing, and used CountVectorizer to build a dict of features and transfroms documents to feature vectors
    -Then we fit and transformed the count matrix to a tf-idf representation using TfidfTransformer() [better than using just TfidfVectorizer]
    -We used pipeline to make the vectorizer=> transformer => classifier easier to work with
         -For the classifiers, we used SGD (by default it fits a linear support vector machine) and KNN
    -We printed the accuracies and classification reports for each classifier [SGD was better]
       -KNN: 65%
       -SGD/SVM: 85%
    -then, we set the tfidf vectorizer to bigram, fit, transformed and predicted (we used KNN as our classifier) and got a worse accuracy (59%)
    -Finally, we set the tfidf vectorizer stop_words to 'english' fit, transformed and predicted (we used KNN as our classifier) and got a better accuracy (67%)
    
    
For Part 2 of ICP 7:

Our goal was to use NLP algorithms on the story 'Fox and the Crow'.

    -First we scraped the story from the web using a BeautifulSoup html parser. We took all paragraph tags, added the text of these tags to a list, and then spliced the list so that it contained parts of the story only.
    -We joined the list together so that it created 1 long string and then used a sentence tokenizer to split the string into a list of sentences. 
    -We also split the story into words using the wordtokenize() method. This creates a list of words so that we can perform further NLP transformations. 
    -For example, we can pass the list of words into the nltk.pos_tag() to get the part of speech for each word. POS tags help us differentiate between 'duck' as a verb and 'duck' as a noun. 
    -We created a PorterStemmer() object and passed our list of words into the objects stem() method. The method returns a stemmed version of each word.
    -We also created a WordNetLemmatizer() object that uses a lemma() method on our word list. This is similar to stemming but lemmatizing uses a word dictionary to generate the base form of each word.
    -We got a list of trigrams which is a grouping of 3 consecutive words and also used Named Entity Recognition to determine any proper nouns.
    -Finally we plotted word frequency with and without stop words.
    -These are all useful tools for computers to use to be able to understand human language
