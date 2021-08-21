# coding=utf8
import xml.etree.ElementTree as ET
import re
f_DI=open("DI.txt",mode='w')
f_AI=open("AI.txt",mode='w')
f_CO=open("CO.txt",mode='w')
fout=[f_DI,f_AI,f_CO]
tree = ET.parse("source.xml")
root = tree.getroot()
rootNode=tree.getroot()

count=0

for i in root:
    #author = re.findall('DI',i)
    if re.findall('DI',str(i.attrib)) and re.findall('Worksheet',str(i.tag)):
        #print(i.tag)
        for j in i:
            if re.findall('Table',str(j.tag)):
                #print(j.tag)
                for k in j:
                    if re.findall('Row',str(k.tag)):
                        if len(k)>10:
                            data_p=k[0][0].text+' '
                            while True:
                                data_p+=' '
                                if len(data_p)>10:break

                            data_p+=k[1][0].text+' '
                            while True:
                                data_p+=' '
                                if len(data_p)>20:break

                            data_p+=k[5][0].text
                            while True:
                                data_p+=' '
                                if len(data_p)>30:break

                            if data_p:
                                print(data_p)
                                print(len(data_p))
                                fout[0].write(data_p)
                                fout[0].write('\n')
    if re.findall('AI',str(i.attrib)) and re.findall('Worksheet',str(i.tag)):
        #print(i.tag)
        for j in i:
            if re.findall('Table',str(j.tag)):
                #print(j.tag)
                for k in j:
                    if re.findall('Row',str(k.tag)):
                        if len(k)>10:
                            data_p=k[0][0].text+' '
                            while True:
                                data_p+=' '
                                if len(data_p)>20:break

                            data_p+=k[1][0].text+' '
                            while True:
                                data_p+=' '
                                if len(data_p)>40:break

                            data_p+=k[5][0].text
                            while True:
                                data_p+=' '
                                if len(data_p)>60:break

                            if data_p:
                                print(data_p)
                                print(len(data_p))
                                fout[1].write(data_p)
                                fout[1].write('\n')
    if re.findall('CO',str(i.attrib)) and re.findall('Worksheet',str(i.tag)):
        #print(i.tag)
        for j in i:
            if re.findall('Table',str(j.tag)):
                #print(j.tag)
                for k in j:
                    if re.findall('Row',str(k.tag)):
                        if len(k)>10:
                            data_p=k[0][0].text+' '
                            while True:
                                data_p+=' '
                                if len(data_p)>20:break

                            data_p+=k[1][0].text+' '
                            while True:
                                data_p+=' '
                                if len(data_p)>40:break

                            data_p+=k[5][0].text
                            while True:
                                data_p+=' '
                                if len(data_p)>60:break

                            if data_p:
                                print(data_p)
                                print(len(data_p))
                                fout[2].write(data_p)
                                fout[2].write('\n')

'''
for c in root.findall('Worksheet'):
print(root[4][1].attrib)
'''
