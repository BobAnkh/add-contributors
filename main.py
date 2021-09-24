#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Author       : BobAnkh
# @Github       : https://github.com/BobAnkh
# @Date         : 2020-07-29 00:12:39
# @LastEditors  : BobAnkh
# @LastEditTime : 2021-09-24 16:28:29
# @FilePath     : /add-contributors/main.py
# @Description  : Main script of Github Action
# @Copyright 2020 BobAnkh

import argparse
import base64
import os
import re

import github
import yaml

head = '''<table>
<tr>'''
tail = '''
</tr>
</table>'''


def argument_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-m',
        '--mode',
        help=
        'choose to use local-dev mode or on github action mode. Valid values are \'local\' or \'github\'',
        default='github')
    parser.add_argument(
        '-f',
        '--file',
        help='configuration file to read from when running local-dev mode',
        default='.github/workflows/contributors.yml')
    parser.add_argument('-o',
                        '--output',
                        help='output file when running local-dev mode',
                        default='local-dev.md')
    parser.add_argument('-t', '--token', help='Github Access Token')
    args = parser.parse_args()
    return args


class GithubContributors:
    '''
    Class for data interface of Github

    Use it to get contributors data and file content from Github and write new file content to Github
    '''
    def __init__(self, ACCESS_TOKEN, REPO_NAME, PATH, BRANCH, PULL_REQUEST, COMMIT_MESSAGE, IGNORED_CONTRIBUTORS):
        '''
        Initial GithubContributors

        Args:
            ACCESS_TOKEN (str): Personal Access Token for Github
            REPO_NAME (str): The name of the repository
            PATH (str): The path to the file
            BRANCH (str): The branch of the file
            PULL_REQUEST (str): Pull request target branch, none means do not open a pull request
            COMMIT_MESSAGE (str): Commit message you want to use
        '''
        self.COMMIT_MESSAGE = COMMIT_MESSAGE
        self.PATH = PATH
        self.BRANCH = BRANCH
        self.PULL_REQUEST = PULL_REQUEST
        self.IGNORED_CONTRIBUTORS = IGNORED_CONTRIBUTORS
        self.SHA = ''
        self.contributors_data = []
        self.file_content = ''
        # Use PyGithub to login to the repository
        # References: https://pygithub.readthedocs.io/en/latest/github_objects/Repository.html#github.Repository.Repository
        g = github.Github(ACCESS_TOKEN)
        self.repo = g.get_repo(REPO_NAME)

    def get_data(self):
        # get contributors data
        contributors = self.repo.get_contributors()
        print('[DEBUG]All contributors\' names:')
        for contributor in contributors:
            name = contributor.name
            avatar_url = contributor.avatar_url
            html_url = contributor.html_url
            if name == None:
                name = html_url[19:]
            print(f'[DEBUG]{name}:{html_url}')
            if name in self.IGNORED_CONTRIBUTORS or re.match('apps/', name):
                continue
            self.contributors_data.append({
                'name': name,
                'avatar_url': avatar_url,
                'html_url': html_url
            })
        # get file content
        contents = self.repo.get_contents(self.PATH, self.BRANCH)
        self.PATH = contents.path
        self.SHA = contents.sha
        base = contents.content
        base = base.replace('\n', '')
        self.file_content = base64.b64decode(base).decode('utf-8')

    def write_data(self, content):
        if content == self.file_content:
            pass
        else:
            self.repo.update_file(self.PATH, self.COMMIT_MESSAGE, content,
                                  self.SHA, self.BRANCH)
            print(f'[DEBUG] BRANCH: {self.BRANCH}, PULL_REQUEST: {self.PULL_REQUEST}')
            if self.PULL_REQUEST != '' and self.PULL_REQUEST != self.BRANCH:
                self.repo.create_pull(title=self.COMMIT_MESSAGE, base=self.PULL_REQUEST, head=self.BRANCH, draft=False, maintainer_can_modify=True)

    def read_contributors(self):
        return self.contributors_data

    def read_file_content(self):
        return self.file_content


def set_local_env(env_name: str, env_value: str, prefix='INPUT'):
    '''
    set local env for dev

    Args:
        env_name (str): local env name.
        env_value (str): value of local env name.
        prefix (str, optional): prefix of env variable. Defaults to 'INPUT'.
    '''
    os.environ[prefix + '_{}'.format(env_name).upper()] = env_value


def get_inputs(input_name: str, prefix='INPUT') -> str:
    '''
    Get a Github actions input by name

    Args:
        input_name (str): input_name in workflow file.
        prefix (str, optional): prefix of input variable. Defaults to 'INPUT'.

    Returns:
        str: action_input

    References
    ----------
    [1] https://help.github.com/en/actions/automating-your-workflow-with-github-actions/metadata-syntax-for-github-actions#example
    '''
    return os.getenv(prefix + '_{}'.format(input_name).upper())


def generate_contributors_table(contributors_data, COLUMN_PER_ROW, img_width,
                                font_size, head_format, tail_format, shape):
    '''
    Generate the contributors table in html format using a given template

    Args:
        contributors_data (list): a list of dict which contains contributors' name, avatar_url and html_url
        COLUMN_PER_ROW (int): number of contributors per row
        img_width (int): width of img
        font_size (int): font size of name
        head_format (str): html_format for table head
        tail_format (str): html_format for table tail
        shape (str): round for round avatar and square for square avatar

    Returns:
        str: contributors table in html format
    '''
    USER = 0
    HEAD = head_format
    TAIL = tail_format
    cell_width = 1.5 * img_width
    cell_height = 1.5 * img_width
    for contributor in contributors_data:
        name = contributor['name']
        avatar_url = contributor['avatar_url']
        html_url = contributor['html_url']
        if USER >= COLUMN_PER_ROW:
            new_tr = '''\n</tr>\n<tr>'''
            HEAD = HEAD + new_tr
            USER = 0
        if shape == 'round':
            img_style = ' style="border-radius:50%;align-items:center;justify-content:center;overflow:hidden;padding-top:10px"'
        else:
            img_style = ''
        td = f'''
    <td align="center" style="word-wrap: break-word; width: {cell_width}; height: {cell_height}">
        <a href={html_url}>
            <img src={avatar_url} width="{img_width};" {img_style} alt={name}/>
            <br />
            <sub style="font-size:{font_size}px"><b>{name}</b></sub>
        </a>
    </td>'''
        HEAD = HEAD + td
        USER += 1
    HEAD = HEAD + TAIL
    return HEAD


def generate_content(file_content, contributors_table, CONTRIBUTOR, PATH):
    '''
    Generate the whole content with contributors table

    Args:
        file_content (str): content of target file
        contributors_table (str): contributors list
        CONTRIBUTOR (str): where you want to write the contributors list
        PATH (str): the file to write

    Raises:
        Exception: the target file does not have the CONTRIBUTOR section

    Returns:
        str: the whole content with contributors table
    '''
    text = file_content
    text_str = text.split(CONTRIBUTOR)
    if len(text_str) == 1:
        print('[DEBUG]: ', text, '\n[DEBUG]')
        raise Exception("File '" + PATH + "' does not have '" + CONTRIBUTOR +
                        "' section")
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
    end[0] = contributors_table
    text = text_str[0] + CONTRIBUTOR + '\n' + end[0] + end[1]
    return text


def set_env_from_file(file, args, prefix='INPUT'):
    '''
    Set env when use local-dev mode

    Args:
        file (str): path to config file
        args (object): cmdline argument
        prefix (str, optional): prefix of env. Defaults to 'INPUT'.
    '''
    f = open(file, encoding='utf-8')
    y = yaml.safe_load(f)
    for job in y['jobs'].values():
        for step in job['steps']:
            if re.match(r'BobAnkh/add-contributors', step['uses']):
                params = step['with']
                break
    option_params = [
        'REPO_NAME', 'CONTRIBUTOR', 'COLUMN_PER_ROW', 'ACCESS_TOKEN',
        'IMG_WIDTH', 'FONT_SIZE', 'PATH', 'COMMIT_MESSAGE', 'AVATAR_SHAPE', 'IGNORED_CONTRIBUTORS'
    ]
    for param in option_params:
        if param not in params.keys():
            if param == 'ACCESS_TOKEN' and args.token:
                tmp = args.token
            else:
                tmp = input('Please input the value of ' + param + ':')
        elif param == 'ACCESS_TOKEN':
            if re.match(r'\$\{\{secrets\.', params[param]):
                if args.token:
                    tmp = args.token
                else:
                    tmp = input('Please input the value of ' + param + ':')
            else:
                tmp = params[param]
        elif param == 'REPO_NAME' and params[param] == '':
            tmp = input('Please input the value of ' + param + ':')
        else:
            tmp = params[param]
        set_local_env(param, tmp, prefix)


def main():
    args = argument_parser()
    if args.mode == 'local':
        set_env_from_file(args.file, args)
    elif args.mode == 'github':
        pass
    else:
        print("Illegal mode option, please type \'-h\' to read the help")
        os.exit()
    ACCESS_TOKEN = get_inputs('ACCESS_TOKEN')
    REPO_NAME = get_inputs('REPO_NAME')
    if REPO_NAME == '':
        REPO_NAME = get_inputs('REPOSITORY', 'GITHUB')
    CONTRIBUTOR = get_inputs('CONTRIBUTOR') + '\n'
    COLUMN_PER_ROW = int(get_inputs('COLUMN_PER_ROW'))
    IMG_WIDTH = int(get_inputs('IMG_WIDTH'))
    FONT_SIZE = int(get_inputs('FONT_SIZE'))
    PATH = get_inputs('PATH')
    BRANCH = get_inputs('BRANCH')
    if BRANCH == '':
        BRANCH = github.GithubObject.NotSet
    PULL_REQUEST = get_inputs('PULL_REQUEST')
    COMMIT_MESSAGE = get_inputs('COMMIT_MESSAGE')
    AVATAR_SHAPE = get_inputs('AVATAR_SHAPE')
    IGNORED_CONTRIBUTORS = [x.lstrip().rstrip() for x in get_inputs('IGNORED_CONTRIBUTORS').split(',')]
    Contributors = GithubContributors(ACCESS_TOKEN, REPO_NAME, PATH, BRANCH, PULL_REQUEST,
                                      COMMIT_MESSAGE, IGNORED_CONTRIBUTORS)
    Contributors.get_data()
    contributors_table = generate_contributors_table(
        Contributors.read_contributors(), COLUMN_PER_ROW, IMG_WIDTH, FONT_SIZE,
        head, tail, AVATAR_SHAPE)
    content = generate_content(Contributors.read_file_content(),
                               contributors_table, CONTRIBUTOR, PATH)
    if args.mode == 'local':
        with open(args.output, 'w', encoding='utf-8') as f:
            f.write(content)
    else:
        Contributors.write_data(content)


if __name__ == '__main__':
    main()
