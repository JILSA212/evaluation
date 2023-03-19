import os
import nltk
import matplotlib.pyplot as plt

def edit_distance_score(ref):
    """Calculate the edit distance score for a given reference.
    Args:
        ref (list): A list of reference sentences.
    Returns:
        float: The edit distance score.
    """
    # Calculate edit distance score
    references = [ref]
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
            new_lines.append(line)

        data.append(new_lines)

    # data = data[0]
    # print("Data: ", data)

    edit_distance_score = []
    # print(len(references))
    # print(len(data[0]))

    for i in range(len(files_list)):
        scores = []
        for j in range(len(data[i])):
            # print(references[0][j])
            # print(data[i][j])
            scores.append(nltk.edit_distance(references[0][j], data[i][j]))

            f1 = plt.figure()
            plt.plot(scores)
            plt.title("Edit Distance Score for " + files_list[i].split(".")[0])
            plt.xlabel("Sentence Number")
            plt.ylabel("Edit Distance Score")
            plt.savefig("data/plots/" + files_list[i].split(".")[0] + "_edit_distance.png")
            plt.close(f1)

        edit_distance_score.append(sum(scores)/len(scores))
    f2 = plt.figure()
    # plt.plot(edit_distance_score)
    x = range(len(files_list))
    plt.bar(x, edit_distance_score, tick_label = files_list, width = 0.5, color = ['blue'])
    plt.xticks(rotation=10)
    # plt.show()
    plt.title("Edit Distance for all files")
    plt.xlabel("Sentence Number")
    plt.ylabel("Edit Distance Score")
    plt.savefig("data/plots/all_edit_distance.png")
    plt.close(f2)


    return edit_distance_score