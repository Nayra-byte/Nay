student_data = {'id1':{'name':['Sara'],'class':['V'],'subject_interrogation':['english,math,science']},
'id2':{'name':['dylan'],'class':['V'],'subject_interrogation':['english,SST,science']},
 'id3':{'name':['Sara'],'class':['V'],'subject_interrogation':['english,math,art']},  
 'id4':{'name':['diana'],'class':['V'],'subject_interrogation':['english,math,science']},             
                }
result={}
for key,value in student_data.items():
    if value not in result.values():
        result[key]=value
print(result)
