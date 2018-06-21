#coding=utf-8
'''
Created on 2017��11.30

@author: mgliu
'''
from jira import JIRA
import time

jira_test = JIRA(server='http://172.16.10.165:8080',basic_auth=('liumougang','123456'))

'''
customfield_10005':'20',第二周，优先级0
customfield_10005':'21',第三周，优先级1
customfield_10005':'22',第四周，优先级2
customfield_10005':'23',第五周,优先级3
customfield_10005':'24',第六周,优先级4
customfield_10005':'25',第七周,优先级5
'''
issuse_week2=[
"PDA端实现-入库-PDA采购入库任务列表-(修改)"
,"PDA端实现-入库-PDA采购入库任务商品详情-(修改)"
,"PDA端实现-入库-PDA采购入库保存-(修改)"
,"PDA端实现-入库-PDA上架任务列表-(修改)"
,"PDA端实现-入库-PDA上架状态更改-(修改)"
,"PDA端实现-入库-PDA上架提交-(修改)"
,"PDA端实现-出库-PDA销售出库任务列表-(修改)"
,"PDA端实现-出库-PDA销售出库任务商品详情-(修改)"
,"PDA端实现-出库-PDA销售出库-(修改)"
,"PDA端实现-出库-PDA出库任务列表查询-(修改)"
,"PDA端实现-出库-PDA出库单商品详情-(修改)"    
    ]

issuse_week3=[
"PDA端实现-门店管理-门店收货列表查询-(新增)"
,"PDA端实现-门店管理-门店收货商品查询-(新增)"
,"PDA端实现-门店管理-门店收货提交-(新增)"
,"PDA端实现-门店管理-门店库存查询-(新增)"   
    ]

issuse_week4=[
"PDA端实现入库-PDA入库任务列表查询-(修改)"
,"PDA端实现入库-PDA入库单商品详情-(修改)"
,"PDA端实现出库-PDA销售出库统计-(修改)"
,"PDA端实现移位管理-待上架商品列表-(修改)"
,"PDA端实现移位管理-商品上架-(修改)"    
    ]

issuse_week5=[
 "PDA端实现-入库-PDA采购入库统计-(修改)"
,"PDA端实现-出库-PDA预售出库统计-(新增)"
,"PDA端实现-出库-PDA预售出库任务列表-(新增)"
,"PDA端实现-出库-PDA预售出库任务商品详情-(新增)"
,"PDA端实现-出库-PDA预售出库-(新增)"
    ]

issuse_week6=[
"PDA端实现-店中店盘点-PDA新增店中店盘点单-(新增)"
,"PDA端实现-店中店盘点-PDA店中店盘点单确认-(新增)"
,"PDA端实现-仓库盘点-PDA盘点单列表查询-(修改)"
,"PDA端实现-仓库盘点-PDA盘点单保存-(修改)"
,"PDA端实现-移位管理-商品下架查询-(修改)"
,"PDA端实现-移位管理-商品下架-(修改)"

   ]

issuse_week7=[
    
"PDA端实现-入库-PDA退货入库统计-(新增)"
,"PDA端实现-入库-PDA退货入库任务列表-(新增)"
,"PDA端实现-入库-PDA退货入库任务商品详情-(新增)"
,"PDA端实现-入库-PDA退货入库保存-(新增)"
,"PDA端实现-入库-PDA调拨入库统计-(新增)"
,"PDA端实现-入库-PDA调拨入库任务列表-(新增)"
,"PDA端实现-入库-PDA调拨入库任务商品详情-(新增)"
,"PDA端实现-入库-PDA调拨入库保存-(新增)"
,"PDA端实现-出库-PDA调拨出库统计-(修改)"
,"PDA端实现-出库-PDA调拨出库任务列表-(修改)"
,"PDA端实现-出库-PDA调拨出库任务商品详情-(修改)"
,"PDA端实现-出库-PDA调拨出库-(修改)"
,"PDA端实现-报损管理-PDA报损单提交-(修改)"
,"PDA端实现-报损管理-PDA报损单列表查询-(修改)"
,"PDA端实现-报损管理-PDA报损单详情-(修改)"
,"PDA端实现-报损管理-PDA报损单状态查询-(修改)"
,"PDA端实现-门店管理-门店收货查询-(新增)"
,"PDA端实现-库存查询-库存货架查询-(修改)"
,"PDA端实现-库存查询-库存商品查询-(修改)"
,"PDA端实现-设置-软件版本查询-(修改)"
    
   ]

for issue_temp in issuse_week2:
    issue_dict= {
        'project': {'key': 'WMSMWONE'},
        'summary': issue_temp,
        'description': issue_temp,
        'issuetype': {'name': 'Task'},
        'priority': {'name':'Major'},

        'reporter':{'name':'liumougang'},
        'customfield_10005':'20',
    }

    new_issue = jira_test.create_issue(fields=issue_dict)

    print (new_issue)
    time.sleep(1)

for issue_temp in issuse_week3:
    issue_dict= {
        'project': {'key': 'WMSMWONE'},
        'summary': issue_temp,
        'description': issue_temp,
        'issuetype': {'name': 'Task'},
        'priority': {'name':'Major'},

        'reporter':{'name':'liumougang'},
        'customfield_10005':'21',
    }

    new_issue = jira_test.create_issue(fields=issue_dict)

    print (new_issue)
    time.sleep(1)


for issue_temp in issuse_week4:
    issue_dict= {
        'project': {'key': 'WMSMWONE'},
        'summary': issue_temp,
        'description': issue_temp,
        'issuetype': {'name': 'Task'},
        'priority': {'name':'Major'},

        'reporter':{'name':'liumougang'},
        'customfield_10005':'22',
    }

    new_issue = jira_test.create_issue(fields=issue_dict)

    print (new_issue)
    time.sleep(1)

    
for issue_temp_wk5 in issuse_week5:
    issue_dict= {
        'project': {'key': 'WMSMWONE'},
        'summary': issue_temp_wk5,
        'description': issue_temp_wk5,
        'issuetype': {'name': 'Task'},
        'priority': {'name':'Major'},

        'reporter':{'name':'liumougang'},
        'customfield_10005':'23',
    }

    new_issue = jira_test.create_issue(fields=issue_dict)

    print (new_issue)
    time.sleep(1)
    
for issue_temp_wk6 in issuse_week6:
    issue_dict= {
        'project': {'key': 'WMSMWONE'},
        'summary': issue_temp_wk6,
        'description': issue_temp_wk6,
        'issuetype': {'name': 'Task'},
        'priority': {'name':'Major'},

        'reporter':{'name':'liumougang'},
        'customfield_10005':'24',
    }

    new_issue = jira_test.create_issue(fields=issue_dict)

    print (new_issue)
    time.sleep(1)
    
    
for issue_temp_wk7 in issuse_week7:
    issue_dict= {
        'project': {'key': 'WMSMWONE'},
        'summary': issue_temp_wk7,
        'description': issue_temp_wk7,
        'issuetype': {'name': 'Task'},
        'priority': {'name':'Major'},
        'reporter':{'name':'liumougang'},
        'customfield_10005':'25',
    }

    new_issue = jira_test.create_issue(fields=issue_dict)

    print (new_issue)
    time.sleep(1)