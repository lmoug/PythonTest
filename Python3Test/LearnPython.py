# -*- coding:GB2312 -*-

'''
Created on 2017年12月6日

@author: mgliu
'''
# import sys
# word="word"
# sentence="This is a sentence"
# paragraphTest="""This is a paragraph
# haha haha """
# 
# print (word,end = " ")
# print (sentence,end = " ")
# print (paragraphTest)
# print ("-------------------python import mode--------------")
# 
# for i in sys.argv:
#     print (i);
#     
# print ("--------------------python system path---------------")
# print (sys.path)
# 
# #print ("sub str:",sentence[0:8])
# print ("sub str \" %s \" length \" %f \" end" % (sentence[0:8],len(sentence)))
# 
# # a,b,c,d,e=25,25.55,True,False,4+9j
# # print (type(a),type(b),type(c),type(d),type(e))
# # print ("Ru\nboo")
# # print (r"Ru\nboo")
# 
# tup_test=("a","b","c","F","e")
# print (type(tup_test))
# print (tup_test)
# print ("del tup now:")
# 
# print (max(tup_test))
# print (min(tup_test))
# 
# dict001={"a":8,"c":23}
# print (dict001.keys())
# print (dict001["a"])
aa,bb=0,1
print ("initial aa is: %s,bb is:%s"%(aa,bb))
while bb < 5:

    aa,bb=bb,aa+bb

    print (aa,bb)
