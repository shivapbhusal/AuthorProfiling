# AuthorProfiling
Author profiling and identification is a practical application of text mining. It involves training the classifier using the existing text with authorship information and using the classifier to identify the author of the new text. Different authors have different styles of writing, and the style can be distinguished based on the attributes such as length of sentences, noun-verb ratio, the frequency of certain words etc.

This project consits of two components: the Profiler Engine and the Classification Engine. 

# Running the project 
## Dependencies:
* Python 3.0 or higher 

## Running the profiler engine:

```python
python src/main.py
```
## Running the classifier engine
```python
python src/kNN.py

```
## Running the Unit tests
```python
python tests/profilerTest.py

```

# Guidelines for contribution 
* Fork the project 
* Make meaningful changes 
* Send a pull request
* Git commit message: Use imperative setences to write your commit message. 
For eg. "add unit tests", "fix issue x", etc. 
Make sure your commit message is shorter than 50 characters. 

# Acknowledgement

* Parsing English: https://explosion.ai/blog/parsing-english-in-python
* Dikens, James Joyce
* Most common English words
* https://stackoverflow.com/questions/2288953/separate-word-lists-for-nouns-verbs-adjectives-etc
* http://users.dsic.upv.es/~prosso/resources/RangelRosso_NLPCS13.pdf
* List of 150 prepositions: https://www.englishclub.com/grammar/prepositions-list.htm

# Contributors
* [Shiva Bhusal](https://github.com/shivapbhusal)
* [ Abhinaya Patthi](https://github.com/abhipatthi)



