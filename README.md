*****
Tweets Preprocessor
*****


Preprocessor is a preprocessing library for tweet data written in
Python. When building Machine Learning systems based on tweets and text data like twitter sentiment analysis, topic modelling, etc.,
preprocessing is required. This is required because of quality of the data as well as dimensionality reduction purposes. 

This library makes it easy to clean the tweets so you don't have to write the same helper functions over and over again ever time.

Features
========

Currently supports cleaning :

-  URLs
-  Hashtags
-  Mentions
-  Emojis
-  Smileys
-  Length constraint
-  remove tweets containing few specific keywords like birthday,congratulations,etc.
-  ``.csv`` and ``.xlsx`` file support

``Python 3.9+ on Windows``. 

Usage
=====

Basic cleaning:
---------------

.. code:: python
    
    >>># Import Preprocess from your library
    >>>from tweets_preprocess import Preprocess
    >>>import pandas as pd
    >>>import numpy as np

    >>># Instantiate a Preprocess object
    >>>data = pd.read_excel(r"D:\Ipac_new\My_Python_Lib\tweet_preprocess\sample.xlsx")
    >>>data['pre_text'] = ""
    
    >>>rem = ["happy birthday","birthday","congratulations","rip","thank you","congrats","thanks"]  ## sample keywords
    >>>length = 35 
    >>>p = Preprocess(data,'Text',rem,length)
    >>>d = p.process()

    >>>data['pre_text'] = pd.Series(d)

    >>>d1 = data.loc[data['pre_text']!='']
    >>>#save cleaned tweets to csv file
    d1.to_csv('pre-data.csv')
    
    
 Example:   
 Raw Tweet: 'Tweet Preprocessor is #awesome 👍 https://github.com/anusha-ipac/tweets_preprocess'   
 Cleaned Tweet: 'Preprocessor is'   
 
 Removed hashtags, emojis, URLs from the raw tweet and returned clean tweet.   
 Removes tweets containing specific keywords.

Processing files:
-----------------

Preprocessor currently supports processing ``.csv`` and ``.xlsx``
formats. 

Installation
============

Using pip:

.. code:: bash

    $ pip install tweets-preprocess


Using manual installation:

.. code:: bash

    $ python setup.py build
    $ python setup.py install

