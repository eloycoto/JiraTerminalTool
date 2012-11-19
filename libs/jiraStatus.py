#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# 
from jira.client import JIRA
import json
import sys

class JiraStatus:
    jira = False
    jiraConfig = False

    __color = {
        'red': '\033[91m',
        'green': '\033[92m',
        'blue': '\033[94m',
        'header': '\033[95m',
        'end': '\033[0m',
    }

    def __init__(self, config):
        options = {
            'server': config['server']
        }
        self.jiraConfig = config
        self.jira = JIRA(options, basic_auth=(config['user'], config['pass']))

    def getIssues(self, project):
        if project is False:
            raise JiraError("What project?")
        query = '''
            project = "%s"
            AND Assignee="%s"
            AND (status="open" OR status="In progress")
            ''' % (project,self.jiraConfig['Assignee'])
        try:
            data = self.jira.search_issues(query)
        except:
            return False

        return self.__parseResult(data)
   
    def __parseResult(self, issues):
        if issues is False:
            raise JiraError('No existen incidencias')
        for data in issues:
            color = 'red' if data.fields.issuetype.name == 'Bug' else 'green'
            self.__getColors(color,data.key+"\t"+
                            data.fields.issuetype.name+"\t\t"+
                            data.fields.summary)
            
    def __getColors(self, color, data):
        print self.__color[color] + data + self.__color['end']
