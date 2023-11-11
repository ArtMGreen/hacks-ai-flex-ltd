
## 1. Installation

### 1.1 Libraries
```
pip install -r requirements.txt
pip install git+https://github.com/boudinfl/pke.git@69337af9f9e72a25af6d7991eaa9869f1322dd72

python -m nltk.downloader universal_tagset
python -m spacy download en_core_web_sm 
```
### 1.2 Download and extract zip of Sense2vec wordvectors that are used for generation of multiple choices.
```
wget https://github.com/explosion/sense2vec/releases/download/v1.0.0/s2v_reddit_2015_md.tar.gz
tar -xvf  s2v_reddit_2015_md.tar.gz
```


### NLP models used

For maintaining meaningfulness in Questions, Questgen uses Three T5 models. One for Boolean Question generation, one for MCQs, FAQs, Paraphrasing and one for answer generation.
