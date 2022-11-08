import base64
import os
import pdb
import shutil

from github import Github
from github import InputGitTreeElement

user = "Srilekha476"
token = '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'

# login with user and token
g = Github(user, token)
repo = g.get_user().get_repo('Srilekhag476')
pdb.set_trace()
# folder name
folder_path = 'C:\\Users\\raju\\PycharmProjects\\pythonProject18\\test'

file_names = os.listdir(folder_path)
# print(file_list+file_names)

# commit message for github
commit_message = 'python commit'
master_ref = repo.get_git_ref('heads/main')
master_sha = master_ref.object.sha
base_tree = repo.get_git_tree(master_sha)
element_list = list()
for i, entry in enumerate(file_names):
    print('entry', entry)
    full_file_path = folder_path+'\\'+entry
    with open(full_file_path) as input_file:
        data = input_file.read()
    # if entry.endswith('.png'):
    #     data = base64.b64encode(data)
    element = InputGitTreeElement(folder_path + '\\' + entry, '100755', 'blob', '9323dff6fc3883b2097f77c817b0bbd5bfd4cd81')
    element_list.append(element)
    # print(element_list.append(element)
    print(element_list)
    # committing files to github
tree = repo.create_git_tree(element_list, base_tree)
parent = repo.get_git_commit(master_sha)
commit = repo.create_git_commit(commit_message, tree, [parent])
print(commit)
master_ref.edit(commit.sha)


