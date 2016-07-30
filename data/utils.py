#!/usr/bin/env python2.7

ENGLISH_STOPWORDS = {
    "a", "an", "the",
    "be", "'s", "been",
    "being", "was", "were",
    "here", "there", "do",
    "how", "i", "i'd",
    "i'll", "i'm", "i've",
    "me", "my", "myself",
    "can", "could", "did",
    "do", "does", "doing",
    "must", "should", "would",
     "you", "you'd", "you'll",
    "you're", "you've", "your",
    "yours", "yourself", "yourselves",
     "he", "he'd", "he'll",
    "he's", "her", "here",
    "here's", "hers", "herself",
    "him", "himself", "his",
    "she", "she'd", "she'll",
    "she's", "it", "it's",
    "its", "itself", "we",
    "we'd", "we'll", "we're",
    "we've", "their", "theirs",
    "them", "themselves", "then",
    "there", "there's", "they",
    "they'd", "they'll", "they're",
    "they've", "let", "let's",
    "this", "that", "these",
    "those", "what", "what's",
    "which", "how", "how's",
    "but"
}

def is_stopword(w):
    return w in ENGLISH_STOPWORDS
