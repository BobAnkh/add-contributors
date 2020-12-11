#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author       : BobAnkh
# @Github       : https://github.com/BobAnkh
# @Date         : 2020-07-29 00:12:39
# @LastEditors  : Please set LastEditors
# @LastEditTime : 2020-12-07 10:31:41
# @FilePath     : /add-contributors/main.py
# @Description  : Main script of Github Action
# @Copyright 2020 BobAnkh

import base64
import os
import re

import github

head = '''<table>
<tr>'''
tail = '''
</tr>
</table>'''


def github_login(ACCESS_TOKEN, REPO_NAME):
    '''
    Use PyGithub to login to the repository

    Args:
        ACCESS_TOKEN (string): github Access Token
        REPO_NAME (string): repository name

    Returns:
        github.Repository.Repository: object represents the repo

    References:
    ----------
    [1]https://pygithub.readthedocs.io/en/latest/github_objects/Repository.html#github.Repository.Repository
    '''
    g = github.Github(ACCESS_TOKEN)
    repo = g.get_repo(REPO_NAME)
    return repo


def get_inputs(input_name):
    '''
    Get a Github actions input by name

    Args:
        input_name (str): input_name in workflow file

    Returns:
        string: action_input

    References
    ----------
    [1] https://help.github.com/en/actions/automating-your-workflow-with-github-actions/metadata-syntax-for-github-actions#example
    '''
    return os.getenv('INPUT_{}'.format(input_name).upper())


def generate_contributors(repo, COLUMN_PER_ROW, img_width, font_size,
                          head_format, tail_format, shape):
    '''
    Generate the contributors list using a given template

    Args:
        repo (github.Repository.Repository): object represents the repo
        COLUMN_PER_ROW (int): number of contributors per row
        img_width (int): width of img
        font_size (int): font size of name
        head_format (string): html_format for table head
        tail_format (string): html_format for table tail
        shape (string): round for round avatar and square for square avatar

    Returns:
        string: contributors list
    '''
    USER = 0
    HEAD = head_format
    TAIL = tail_format
    cell_width = 1.25 * img_width
    cell_height = 2 * img_width
    contributors = repo.get_contributors()
    for contributor in contributors:
        name = contributor.name
        avatar_url = contributor.avatar_url
        html_url = contributor.html_url
        if re.match('https://github.com/apps/', html_url):
            continue
        if name == None:
            name = html_url[19:]
        if USER >= COLUMN_PER_ROW:
            new_tr = '''\n</tr>\n<tr>'''
            HEAD = HEAD + new_tr
            USER = 0
        if shape == 'round':
            img_style = ' style="border-radius:50%;align-items:center;justify-content:center;overflow:hidden;"'
        else:
            img_style = ''
        td = f'''
    <td align="center" style="word-wrap: break-word; width: {cell_width}; height: {cell_height}; color: green">
        <a href={html_url}>
            <img src={avatar_url} style="padding-top: 30px" width="{img_width};" {img_style} alt={name}/>
            <br />
            <sub style="font-size:{font_size}px"><b>{name}</b></sub>
            <sub></sub>
            <br />
        </a>
    </td>'''
        HEAD = HEAD + td
        USER += 1
    HEAD = HEAD + TAIL
    return HEAD


def write_contributors(repo, contributors_list, path, commit_message, CONTRIB, BRANCH=github.GithubObject.NotSet):
    '''
    Write contributors list to file if it differs

    Args:
        repo (github.Repository.Repository): object represents the repo
        contributors_list (string): contributors list
        path (string): the file to write
        commit_message (string): commit message
        CONTRIB (string): where you want to write the contributors list
    '''
    contents = repo.get_contents(path, BRANCH)
    base = contents.content
    base = base.replace('\n', '')
    text = base64.b64decode(base).decode('utf-8')
    text_str = text.split(CONTRIB)
    if len(text_str) == 1:
        print('[DEBUG]: ', text, '\n[DEBUG]')
        raise Exception("File '" + path + "' does not have '" + CONTRIB +"' section")
    if re.match(r'\n+', text_str[1]):
        lf_num = re.match(r'\n+', text_str[1]).span()[1]
        text_str[1] = text_str[1][lf_num:]
    else:
        lf_num = 0
        print('[DEBUG-lr_num]: ', text_str[1])
    if re.match(head, text_str[1]):
        end = text_str[1].split(tail)
        end[0] = end[0] + tail
    else:
        end = ['', '\n' * (lf_num + 1) + text_str[1]]
    if end[0] != contributors_list:
        end[0] = contributors_list
        text = text_str[0] + CONTRIB + '\n' + end[0] + end[1]
        repo.update_file(contents.path, commit_message, text, contents.sha, BRANCH)
    else:
        pass

def main():
    ACCESS_TOKEN = get_inputs('ACCESS_TOKEN')
    REPO_NAME = get_inputs('REPO_NAME')
    CONTRIBUTOR = get_inputs('CONTRIBUTOR') + '\n'
    COLUMN_PER_ROW = int(get_inputs('COLUMN_PER_ROW'))
    IMG_WIDTH = int(get_inputs('IMG_WIDTH'))
    FONT_SIZE = int(get_inputs('FONT_SIZE'))
    PATH = get_inputs('PATH')
    if re.match(r'.*:.*', PATH):
        BRANCH = re.sub(r':.*', '', PATH)
        PATH = re.sub(r'.*:', '', PATH)
    else:
        BRANCH = github.GithubObject.NotSet
    COMMIT_MESSAGE = get_inputs('COMMIT_MESSAGE')
    AVATAR_SHAPE = get_inputs('AVATAR_SHAPE')
    repo = github_login(ACCESS_TOKEN, REPO_NAME)
    CONTRIBUTORS_LIST = generate_contributors(repo, COLUMN_PER_ROW, IMG_WIDTH,
                                              FONT_SIZE, head, tail,
                                              AVATAR_SHAPE)
    write_contributors(repo, CONTRIBUTORS_LIST, PATH, COMMIT_MESSAGE,
                       CONTRIBUTOR, BRANCH)


if __name__ == '__main__':
    main()
