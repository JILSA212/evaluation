import os
import nltk
nltk.download('wordnet')
import matplotlib.pyplot as plt

def meteor_score(ref):
    """Calculate the METEOR score for a given reference.
    Args:
        ref (list): A list of reference sentences.
    Returns:
        float: The METEOR score.
    """
    # Calculate METEOR score
    
    references = [lines.split() for lines in ref]
    # print("References: ", references)

    files_list = []
    for file in os.listdir("data/results"):
        if file.endswith(".txt"):
            files_list.append(file)

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

    # data = data[0]
    # print("Data: ", data)

    meteor_score = []
    # print(len(references))
    # print(len(data[0]))

    for i in range(len(files_list)):
        scores = []
        for j in range(len(data[i])):
            # print(references[j])
            # print(data[i][j])
            scores.append(nltk.translate.meteor_score.single_meteor_score(references[j], data[i][j]))
        f1 = plt.figure()
        plt.plot(scores)
        # plt.show()
        plt.title("METEOR Score for " + files_list[i].split(".")[0] + " METEOR Score")
        plt.xlabel("Sentence Number")
        plt.ylabel("METEOR Score")
        plt.savefig("data/plots/" + files_list[i].split(".")[0] + "_meteor.png")
        plt.close(f1)

        meteor_score.append(sum(scores)/len(scores))
        # plt.clf()
        # plt.cla()

    f2 = plt.figure()
    # plt.plot(meteor_score)
    x_pos = [i for i, _ in enumerate(files_list)]
    plt.bar(x_pos, meteor_score, color='blue', width=0.5)
    plt.xticks(x_pos, files_list, rotation=10)
    plt.title("METEOR Score for All Files")
    plt.xlabel("File Number")
    plt.ylabel("METEOR Score")
    plt.savefig("data/plots/all_meteor.png")
    plt.close(f2)

    return meteor_score