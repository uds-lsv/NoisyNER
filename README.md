# NoisyNER dataset
A dataset for evaluation of noisy label methods

## About
NoisyNER is a dataset for the evaluation of methods to handle noisy labels when training machine learning models. It is from the NLP/Information Extraction domain and was created through a realistic distant supervision technique. Some highlights and interesting aspects of the data are:
- Seven sets of labels with differing noise patterns to evaluate different noise levels on the same instances
- Full parallel clean labels available to compute upper performance bounds or study scenarios where a small amount of gold-standard data can be leveraged
- Skewed label distribution (typical for Named Entity Recognition tasks)
- For some label sets: noise level higher than the true label probability
- Sequential dependencies between the labels

For more details on the dataset and its creation process, please refer to our publication [LINK TO FOLLOW].

## Instructions

1. Clone this repository 
2. Download the original Estonian NER dataset from https://doi.org/10.15155/1-00-0000-0000-0000-00073L
2. Extract the downloaded .zip file and save the "estner.cnll" file in the "data" subdirectory
3. Run ``python prepare_data.py`` with Python3

You will then find in the "data" directory all the dataset files.

## Structure

For each of the 7 noisy label sets, we provide the full dataset (with the file ending \*\_all.tsv) as well as an 80/10/10 train/dev/test split (with the file ending \*\_train.tsv/\*\_dev.tsv/\*\_test.tsv). The splits for the original, clean dataset are estner_clean_{train,dev,test}.tsv.

All files are tsv files with the same structure. The structure follows the CoNLL standard for NER datasets. Each line corresponds to one word or token. The first column gives the actual token. The last column gives the label. The two middle columns give additional, grammatical features which used to be leveraged by NLP methods but are often ignored by modern neural methods.

## Contact Sources & Citations

For more details, please refer to our publication [LINK TO FOLLOW]. If you have any questions or if you run into any issues, feel free to contact us.

When you work with this dataset, please consider citing us as

>
> CITATION TO FOLLOW
>

This noisy label dataset is based on an existing NER dataset for Estonian. Please cite this work as well. 

The original dataset and the clean labels are from

>Laur, S. (2013). 
>Nimeüksuste korpus. Center of Estonian Language Resources. 
>https://doi.org/10.15155/1-00-0000-0000-0000-00073L

```
@inproceedings{tkachenko-etal-2013-named,
    title = "Named Entity Recognition in {E}stonian",
    author = "Tkachenko, Alexander  and  Petmanson, Timo  and  Laur, Sven",
    booktitle = "Proceedings of the 4th Biennial International Workshop on {B}alto-{S}lavic Natural Language Processing",
    year = "2013",
    publisher = "Association for Computational Linguistics",
    url = "https://www.aclweb.org/anthology/W13-2412",
}
```
The original dataset is licensed under CC-BY-NC. We provide our noisy labels under CC-BY 4.0.


