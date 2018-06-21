'''
Created on 2017.11.30

@author: mgliu
'''
from jira import JIRA

jira = JIRA(server='http://172.16.10.165:8080',basic_auth=('liumougang','123456'))

projects = jira.projects()
test_issue = jira.issue(10127)

#print projects
print (test_issue)

