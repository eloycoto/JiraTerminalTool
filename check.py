#!/usr/bin/env python
# -*- coding: utf-8 -*-

from jira.client import JIRA
from libs.jiraStatus import *
import json
import sys
import getopt

config = {
    'server': '',
    'user': '',
    'Assignee': '',
    'pass': ''
}


def main(argv):
    inputfile = ''
    outputfile = ''
    try:
        opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
    except getopt.GetoptError:
        print 'projects.py -p <project>'
        sys.exit(2)
    print opts
    for opt, arg in opts:
        if opt == '-h':
            print 'projects.py -p <project>'
        if opt == '-p':
            issues = JiraStatus(config)
            issues.getIssues(arg)
            sys.exit()

if __name__ == "__main__":
    # issues = JiraStatus(config)
    # issues.getIssues('wph')
    main(sys.argv[1:])

