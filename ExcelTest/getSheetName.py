#  -*- coding:gbk -*-  
  
import openpyxl  
  

wb1 = openpyxl.load_workbook('E:\����-��Ŀ�ĵ�\������Ŀ\����׼��\ԭʼ�ĵ�\����̩������һ����Ŀ_����_2B��̨�����ռ�ģ��_V1.0_180111.xlsx')  
wb2=openpyxl.load_workbook(r'E:\����-��Ŀ�ĵ�\������Ŀ\����׼��\ԭʼ�ĵ�\����̩������һ����Ŀ_����_2C��̨�����ռ�ģ��_V1.0_180111.xlsx')
wb3=openpyxl.load_workbook(r'E:\����-��Ŀ�ĵ�\������Ŀ\����׼��\ԭʼ�ĵ�\����̩������һ����Ŀ_����_WMS(2B)�����ռ�ģ��_V1.0_180111.xlsx')
wb4= openpyxl.load_workbook(r'E:\����-��Ŀ�ĵ�\������Ŀ\����׼��\ԭʼ�ĵ�\����̩������һ����Ŀ_����_WMS(2C)�����ռ�ģ��_V1.0_180111.xlsx')
  
#��ȡworkbook�����еı��  
print ("//////////////////////////////////2B��̨�����ռ�ģ��")
sheets = wb1.get_sheet_names()  
  
for i in sheets:
    print i
    
print ("//////////////////////////////////2C��̨�����ռ�ģ��")
sheets = wb2.get_sheet_names()  
  
for i in sheets:
    print i
    
print ("//////////////////////////////////WMS(2B)�����ռ�ģ��")
sheets = wb3.get_sheet_names()  
  
for i in sheets:
    print i 
    
print ("//////////////////////////////////WMS(2C)�����ռ�ģ��")
sheets = wb4.get_sheet_names()  
  
for i in sheets:
    print i    
#ѭ����������sheet  
#for i in range(len(sheets)):  
#    sheet= wb.get_sheet_by_name(sheets[i])  
      
#   print('\n\n��'+str(i+1)+'��sheet: ' + sheet.title+'->>>')  
  
#    for r in range(1,sheet.max_row+1):  
#        if r == 1:  
#            print('\n'+''.join([str(sheet.cell(row=r,column=c).value).ljust(17) for c in range(1,sheet.max_column+1)] ))  
#        else:  
#            print(''.join([str(sheet.cell(row=r,column=c).value).ljust(20) for c in range(1,sheet.max_column+1)] ))  