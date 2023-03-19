import os
from nltk.translate.bleu_score import sentence_bleu

def bleu_score(ref):
    """Calculate the BLEU score for a given reference.
    Args:
        ref (list): A list of reference sentences.
    Returns:
        float: The BLEU score.
    """
    # Calculate BLEU score
    # print(ref)
    references = [lines.split() for lines in ref]
    # print("References: ", references)

    files_list = []
    for file in os.listdir("data/results"):
        if file.endswith(".txt"):
            files_list.append(file)

    # print("Files: ", files_list)
    data = []

    for file in files_list:
        lines = []
        f = open("data/results/" + file, "r")
        lines.append(f.readlines())
        # print("Lines: ", lines)

        new_lines = []
        for line in lines[0]:
            new_lines.append(line.split())

        data.append(new_lines)

    data = data[0]
    # print("Data: ", data)
    bleu_scores = []
    
    for i in range(len(files_list)):
        scores = []
        for j in range(len(data[i])):
            # print(references[i][j])
            # print(data[i][j])
            scores.append(sentence_bleu(references[i][j], data[i][j]))
        bleu_scores.append(sum(scores)/len(scores))

    return bleu_scores