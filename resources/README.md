## About this directory:
for starters, you need to download the OpenSubtitles corpus from https://opus.nlpl.eu/OpenSubtitles.php

Make sure to use the bottom table to download the corpus in Moses format (Bottom-left triangle). This will give you a file called `OpenSubtitles.en-fa.en` and `OpenSubtitles.en-fa.fa` which are the English and Persian files respectively.

The `clean_dataset` is available here, and it's the 10,000 line dataset that's been hand-made for this project.
## OpenSubtitle Corpus info

 Corpus Name: OpenSubtitles
     Package: OpenSubtitles in Moses format
     Website: http://opus.nlpl.eu/OpenSubtitles-v2018.php
     Release: v2018
Release date: Tue Apr  3 23:47:52 EEST 2018

This corpus is part of OPUS - the open collection of parallel corpora
OPUS Website: http://opus.nlpl.eu

Please cite the following article if you use any part of the corpus in your own work: P. Lison and J. Tiedemann, 2016, OpenSubtitles2016: Extracting Large Parallel Corpora from Movie and TV Subtitles. In Proceedings of the 10th International Conference on Language Resources and Evaluation (LREC 2016)

This is a new collection of translated movie subtitles from http://www.opensubtitles.org/.IMPORTANT: If you use the OpenSubtitle corpus: Please, add a link to http://www.opensubtitles.org/ to your website and to your reports and publications produced with the data! I promised this when I got the data from the providers of that website!  This is a slightly cleaner version of the subtitle collection using improved sentence alignment and better language checking.
We also provide sentence alignments between alternative subtitle uploads. This produces a lot of repeated material and, therefore, we do not provide data sets that are compiled into plain text or TMX format. Instead, you can download the standoff annotation of the sentence alignment from the form at the top-level website. There are links to [alt] in the other files column of the search result if they exist.OpenSubtitles also includes intra-lingual sentence alignments between alternative subtitle uploads in the same language. To access those files, search for resources with the same source and target language using the form on the top-level website. The intra-lingual links are divided into different categories (listed in the column other files in the search result):  insert: Sentence pairs that differ only by some inserted text on one side other: Other types of sentence pairs; probably paraphrases and/or stylistically different subtitles. pct: Sentence pairs that differ only in punctuation characters. spell: Sentence pairs that differ in a few characters only that looks suspiciously like misspellings.  For more information, please look at  J. Tiedemann, 2016, Finding Alternative Translations in a Large Corpus of Movie Subtitles. In Proceedings of the 10th International Conference on Language Resources and Evaluation (LREC 2016)(and, please, cite the paper as well).
