from git import Repo
import matplotlib.pyplot as plt
import os
import datetime
import sys

def countTexWordsInFile(filename):
    count = 0
    with open(filename, "r") as fid:
        lines = fid.readlines()
        for line in lines:
            words = line.split(" ")
            count += len(words)
    return(count)

def countTexWordsInDirectory(loc):
    total_tex_words = 0
    for entry in os.scandir(loc):
        if entry.is_file() and (entry.path.endswith(".tex")):
            file_word_count = countTexWordsInFile(entry.path)
            total_tex_words += file_word_count
        elif entry.is_dir():
            total_tex_words += countTexWordsInDirectory(entry.path)
    return(total_tex_words)

def trackTexWordsInRepository(repo,name_of_main_branch):
    counts = []
    dates = []
    for commit in repo.iter_commits(name_of_main_branch):
        repo.git.checkout(commit.hexsha)
        counts.append(countTexWordsInDirectory(repo_path))
        dates.append(datetime.datetime.fromtimestamp(commit.committed_date))

    repo.git.checkout(name_of_main_branch)
    return(counts,dates)

repo_path = os.path.join(sys.argv[1])
main_branch_name = sys.argv[2]
repo = Repo(repo_path)

counts,dates = trackTexWordsInRepository(repo,main_branch_name)

plt.figure()
plt.plot(dates,counts)
plt.xlabel("Date")
plt.ylabel("Number of Words")
plt.title("Word Count")
plt.show()
