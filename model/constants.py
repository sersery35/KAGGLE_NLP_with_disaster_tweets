from tensorboard.plugins.hparams import api as hp

metrics = [hp.Metric("accuracy", display_name="Accuracy"),
           hp.Metric("precision", display_name="Precision"),
           hp.Metric("recall", display_name="Recall"),
           hp.Metric("f1", display_name="F1 Score")]

glove_url = {
    '6B': 'https://nlp.stanford.edu/data/glove.6B.zip',
    'twitter.27B': 'https://nlp.stanford.edu/data/glove.twitter.27B.zip'
}
