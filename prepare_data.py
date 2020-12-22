"""
Prepares the NoisyNER data. Merges the original dataset with
the new noisy label sets and creates train/dev/test splits.
"""

def load_estner():
    """ Load the original Estonian NER dataset and return both
        the full instances as well as only its
        features (token + additional features)
    """
    filepath = "data/estner.cnll"
    try:
        with open(filepath) as in_file:
            instances = in_file.readlines()
    except FileNotFoundError:
        raise Exception("Could not find the original dataset at " \
                        f"{filepath}. Have you followed the instructions"\
                        " and downloaded and extracted this file?")
    
    # remove original label
    instances = [instance.strip().split("\t") for instance in instances]
    features = [instance[:-1] for instance in instances] 
    return instances, features

def load_noisyner_labelset(labelid):
    """ Load a NoisyNER label set (labelid in range [1,7])
    """
    filepath = f"data/only_labels/NoisyNER_labelset{labelid}.labels"
    with open(filepath) as in_file:
        labels = in_file.read().splitlines()
    return labels
    
def merge_features_labels(features, labels):
    """ Merge the original Estonian NER features with the NoisyNER
        labels.
    """
    # The features include sentence separation markers (empty features)
    # which the labels do not have. Merging keeping the sentence 
    # separation marker
    
    new_instances = []
    label_idx = 0
    for instance_features in features:
        if len(instance_features) == 0:
            new_instances.append("") # sentence separation marker
        else:
            assert(label_idx < len(labels)), "Number of features does "\
                                             "not match number of labels"
            new_instance = instance_features + [labels[label_idx]]
            new_instances.append(new_instance)
            label_idx += 1
            
    assert label_idx == len(labels), "Number of features does "\
                                             "not match number of labels"
    return new_instances

def split_instances(instances):
    """ Split the whole dataset into train/dev/test based on
        a 80/10/10 split on the tokens (sentence separation
        markers are ignored for the counting for the splits)
    """
    train = instances[:185708]
    dev = instances[185708:208922]
    test = instances[208922:]
    return train, dev, test

def write_instances(instances, filepath):
    """ Write an NER dataset to file in the CoNLL format.
    """
    column_separator = "\t"
    with open(filepath, "w") as out_file:
        for instance in instances:
            out_file.write(column_separator.join(instance))
            out_file.write("\n")
            
def main():
    instances, features = load_estner()  
    
    # split for clean data
    train, dev, test = split_instances(instances)
    write_instances(train, f"data/estner_clean_train.tsv")
    write_instances(dev, f"data/estner_clean_dev.tsv")
    write_instances(test, f"data/estner_clean_test.tsv")
    
    # noisy label sets
    for labelid in range(1,8):
        labels = load_noisyner_labelset(labelid)
        instances = merge_features_labels(features, labels)
        train, dev, test = split_instances(instances)
        write_instances(instances, f"data/NoisyNER_labelset{labelid}_all.tsv")
        write_instances(train, f"data/NoisyNER_labelset{labelid}_train.tsv")
        write_instances(dev, f"data/NoisyNER_labelset{labelid}_dev.tsv")
        write_instances(test, f"data/NoisyNER_labelset{labelid}_test.tsv")

if __name__ == "__main__":
    main()
