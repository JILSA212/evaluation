import os
import matplotlib.pyplot as plt
from metrices.bleu import bleu_score
from metrices.meteor import meteor_score
from metrices.edit_distance import edit_distance_score

for file in os.listdir("data/reference"):
    if file.endswith(".txt"):
        f = open("data/reference/" + file, "r")
        references = f.readlines()

bleu_scores = bleu_score(references)
print(bleu_scores)

meteor_scores = meteor_score(references)
print(meteor_scores)

edit_distance_scores = edit_distance_score(references)
print(edit_distance_scores)