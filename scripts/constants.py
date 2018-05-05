import os
from os import sep as SEP

# Folders
PROJECT_PATH = os.path.normpath(os.getcwd() + os.sep + os.pardir)

SCRIPTS_FOLDER = "scripts"
SCRIPTS_PATH = PROJECT_PATH + SEP + SCRIPTS_FOLDER

DATA_FOLDER = "data"
DATA_PATH = PROJECT_PATH + SEP + DATA_FOLDER

# Scripts
TOKENIZER = "tokenizer.perl"
TOKENIZER_PATH = SCRIPTS_PATH + SEP + "tools" + SEP + TOKENIZER

# Train files
RAW_TRAIN = "raw_train.json"
RAW_TRAIN_PATH = DATA_PATH + SEP + RAW_TRAIN

TOKENIZED_TRAIN = "tokenized_train.json"
TOKENIZED_TRAIN_PATH = DATA_PATH + SEP + TOKENIZED_TRAIN

EMBEDDED_TRAIN = "emb_train.json"
EMBEDDED_TRAIN_PATH = DATA_PATH + SEP + EMBEDDED_TRAIN


# Embeddings
BIN_EMBEDDING = "wiki.simple.bin"
BIN_EMBEDDING_PATH = DATA_PATH + SEP + BIN_EMBEDDING

'''
RAW_EMBEDDING = "wiki-news-300d-1M-subword.vec"
RAW_EMBEDDING_PATH = DATA_PATH + SEP + RAW_EMBEDDING

EMBEDDING = "embedding.npy"
EMBEDDING_PATH = DATA_PATH + SEP + EMBEDDING

VOCABULARY = "vocabulary.npy"
VOCABULARY_PATH = DATA_PATH + SEP + VOCABULARY
'''
