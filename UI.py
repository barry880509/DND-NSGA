#!/usr/bin/env python
# coding: utf-8

# In[55]:


import numpy as np
import pandas as pd
from sklearn.datasets import make_regression
from sklearn import metrics
import random
import string
from decimal import getcontext, Decimal
import csv
import math
from tkinter import *
import tkinter.font as tkFont
from PIL import Image,ImageTk
import matplotlib.pyplot as plt
from math import pi
from PIL import Image, ImageTk


# In[56]:


def refresh():
    mylistbox.delete(0, END)
    if factionvalue.get()==1:
        mytarget=["力量檢定","敏捷檢定","體質檢定","智力檢定","智慧檢定","魅力檢定","物理攻擊力","魔法攻擊力","物理防禦力","魔法防禦力","麻痺抗性","睡眠抗性","中毒抗性","精神抗性","攀爬機率","跳躍機率","擺脫束縛","游泳","迴避","跑步","負重","隱藏","觀察","致盲","擊暈","精準打擊","說服","穩定傷勢","察言觀色","表演","融入人群","特技動作","奧術法術","法術詠唱速度","估價"]
    if factionvalue.get()==2:
        mytarget=["力量檢定","敏捷檢定","體質檢定","智力檢定","智慧檢定","魅力檢定","物理攻擊力","魔法攻擊力","物理防禦力","魔法防禦力","麻痺抗性","睡眠抗性","中毒抗性","精神抗性","破門機率","攀爬機率","跳躍機率","擺脫束縛","游泳","迴避","議價","跑步","負重","隱藏","觀察","致盲","擊暈","精準打擊","說服","威嚇","穩定傷勢","察言觀色","欺騙機率","表演","融入人群","特技動作","奧術法術","法術詠唱速度","估價"]
    if factionvalue.get()==3:
        mytarget=["力量檢定","敏捷檢定","體質檢定","智力檢定","智慧檢定","魅力檢定","物理攻擊力","魔法攻擊力","物理防禦力","魔法防禦力","麻痺抗性","睡眠抗性","中毒抗性","精神抗性","破門機率","攀爬機率","跳躍機率","擺脫束縛","游泳","迴避","偷竊","議價","搶奪","跑步","負重","隱藏","觀察","致盲","擊暈","精準打擊","說服","威嚇","穩定傷勢","察言觀色","欺騙機率","表演","融入人群","特技動作","奧術法術","法術詠唱速度","估價"]
    if factionvalue.get()==4:
        mytarget=["力量檢定","敏捷檢定","體質檢定","智力檢定","智慧檢定","魅力檢定","物理攻擊力","魔法攻擊力","物理防禦力","魔法防禦力","麻痺抗性","睡眠抗性","中毒抗性","精神抗性","破門機率","攀爬機率","跳躍機率","擺脫束縛","游泳","迴避","議價","跑步","負重","隱藏","觀察","致盲","擊暈","精準打擊","說服","穩定傷勢","察言觀色","表演","融入人群","特技動作","奧術法術","法術詠唱速度","估價"]
    if factionvalue.get()==5:
        mytarget=["力量檢定","敏捷檢定","體質檢定","智力檢定","智慧檢定","魅力檢定","物理攻擊力","魔法攻擊力","物理防禦力","魔法防禦力","麻痺抗性","睡眠抗性","中毒抗性","精神抗性","破門機率","攀爬機率","跳躍機率","擺脫束縛","游泳","迴避","偷竊","議價","搶奪","跑步","負重","隱藏","觀察","致盲","擊暈","精準打擊","說服","威嚇","穩定傷勢","察言觀色","欺騙機率","表演","融入人群","特技動作","奧術法術","法術詠唱速度","估價"]
    if factionvalue.get()==6:
        mytarget=["力量檢定","敏捷檢定","體質檢定","智力檢定","智慧檢定","魅力檢定","物理攻擊力","魔法攻擊力","物理防禦力","魔法防禦力","麻痺抗性","睡眠抗性","中毒抗性","精神抗性","破門機率","攀爬機率","跳躍機率","擺脫束縛","游泳","迴避","偷竊","議價","搶奪","跑步","負重","隱藏","觀察","致盲","擊暈","精準打擊","說服","威嚇","穩定傷勢","察言觀色","欺騙機率","表演","融入人群","特技動作","奧術法術","法術詠唱速度","估價"]
    if factionvalue.get()==7:
        mytarget=["力量檢定","敏捷檢定","體質檢定","智力檢定","智慧檢定","魅力檢定","物理攻擊力","魔法攻擊力","物理防禦力","魔法防禦力","麻痺抗性","睡眠抗性","中毒抗性","精神抗性","破門機率","攀爬機率","跳躍機率","擺脫束縛","游泳","迴避","偷竊","議價","搶奪","跑步","負重","隱藏","觀察","致盲","擊暈","精準打擊","說服","威嚇","穩定傷勢","察言觀色","欺騙機率","表演","融入人群","特技動作","奧術法術","法術詠唱速度","估價"]
    if factionvalue.get()==8:
        mytarget=["力量檢定","敏捷檢定","體質檢定","智力檢定","智慧檢定","魅力檢定","物理攻擊力","魔法攻擊力","物理防禦力","魔法防禦力","麻痺抗性","睡眠抗性","中毒抗性","精神抗性","破門機率","攀爬機率","跳躍機率","擺脫束縛","游泳","迴避","偷竊","議價","搶奪","跑步","負重","隱藏","觀察","致盲","擊暈","精準打擊","說服","威嚇","穩定傷勢","察言觀色","欺騙機率","表演","融入人群","特技動作","奧術法術","法術詠唱速度","估價"]
    if factionvalue.get()==9:
        mytarget=["力量檢定","敏捷檢定","體質檢定","智力檢定","智慧檢定","魅力檢定","物理攻擊力","魔法攻擊力","物理防禦力","魔法防禦力","麻痺抗性","睡眠抗性","中毒抗性","精神抗性","破門機率","攀爬機率","跳躍機率","擺脫束縛","游泳","迴避","偷竊","議價","搶奪","跑步","負重","隱藏","觀察","致盲","擊暈","精準打擊","說服","威嚇","穩定傷勢","察言觀色","欺騙機率","表演","融入人群","特技動作","奧術法術","法術詠唱速度","估價"]
    
    for item in mytarget:
        mylistbox.insert("end", item)


# In[57]:


def calbest():
    startchar = []
    atknum=[]
    dognum=[]
    barnum=[]
    doornum=[]

    lv = int(levelup.get())
    startstr = int(STR_entry.get())
    startdex = int(DEX_entry.get())
    startcon = int(CON_entry.get())
    startint = int(INT_entry.get())
    startwis = int(WIS_entry.get())
    startcha = int(CHA_entry.get())
    #----------------------------------------------------------------------------------------------------------------------
    
    #種族
    if racevalue.get()==1:
        startdex = startdex+2
    
    elif racevalue.get()==2:
        startcha = startcha+2
        
    elif racevalue.get()==3:
        startstr = startstr+1
        startdex = startdex+1
        startcon = startcon+1
        startint = startint+1
        startwis = startwis+1
        startcha = startcha+1
        
    elif racevalue.get()==4:
        startdex = startdex+2
        
    elif racevalue.get()==5:
        startcon = startcon+2
        
    elif racevalue.get()==6:
        startint = startint+2
        
    elif racevalue.get()==7:
        startint = startint+1
        startcha = startcha+2
        
    elif racevalue.get()==8:
        startstr = startstr+2
        startcha = startcha+1
        
    elif racevalue.get()==9:
        startstr = startstr+2
        startcon = startcon+1
        
    #職業
    if jobvalue.get()==1:
        addn = lv/2
    elif jobvalue.get()==2:
        addn = lv/2
    elif jobvalue.get()==3:
        addn = lv/2
    elif jobvalue.get()==4:
        addn = lv/2
    elif jobvalue.get()==5:
        addn = lv/2
    elif jobvalue.get()==6:
        addn = lv/2
    elif jobvalue.get()==7:
        addn = lv/2
    elif jobvalue.get()==8:
        addn = lv/2
    elif jobvalue.get()==9:
        addn = lv/2

    #----------------------------------------------------------------------------------------------------------------------
  
    targetdic = {   "力量檢定":[1.0,0.0,0.0,0.0,0.0,0.0],
                    "敏捷檢定":[0.0,1.0,0.0,0.0,0.0,0.0],
                    "體質檢定":[0.0,0.0,1.0,0.0,0.0,0.0],
                    "智力檢定":[0.0,0.0,0.0,1.0,0.0,0.0],
                    "智慧檢定":[0.0,0.0,0.0,0.0,1.0,0.0],
                    "魅力檢定":[0.0,0.0,0.0,0.0,0.0,1.0],
                    "物理攻擊力":[1.8,1.0,0.6,0.0,0.0,0.0],
                    "物理防禦力":[1.4,0.8,1.2,0.0,0.0,0.0],
                    "魔法攻擊力":[0.0,0.0,0.0,2.0,1.0,0.0],
                    "魔法防禦力":[0.0,1.0,1.8,0.8,0.0,0.0],
                    "麻痺抗性":[0.0,0.0,2.0,0.0,0.0,0.0],
                    "睡眠抗性":[0.0,0.0,1.0,1.2,1.6,0.0],
                    "中毒抗性":[0.0,0.0,2.0,0.0,0.0,0.0],
                    "精神抗性":[0.0,0.0,0.0,1.6,2.0,0.0],
                    "破門機率":[2.0,0.0,0.0,0.0,0.0,0.0],
                    "攀爬機率":[1.8,0.8,0.0,0.0,0.0,0.0],
                    "跳躍機率":[1.8,0.8,0.0,0.0,0.0,0.0],
                    "擺脫束縛":[2.0,0.0,0.0,0.0,0.0,0.0],
                    "游泳":[1.8,0.8,0.0,0.0,0.0,0.0],
                    "迴避":[0.0,1.8,0.8,0.0,1.0,0.0],
                    "偷竊":[0.0,1.8,0.0,0.0,0.8,0.0],
                    "議價":[0.0,0.0,0.0,0.0,0.8,1.4],
                    "搶奪":[1.4,1.0,0.0,0.0,0.2,0.0],
                    "跑步":[0.2,0.2,0.1,0.0,0.0,0.0],
                    "負重":[15.0,0.0,0.0,0.0,0.0,0.0],
                    "隱藏":[0.0,1.4,0.0,0.8,0.0,0.0],
                    "觀察":[0.0,1.2,0.0,0.0,1.0,0.0],
                    "致盲":[0.0,2.0,0.0,0.0,0.0,0.0],
                    "擊暈":[1.0,0.8,0.0,0.0,0.0,0.0],
                    "精準打擊":[0.0,2.0,0.0,0.0,1.0,0.0],
                    "說服":[0.0,0.0,0.0,0.0,0.8,2.0],
                    "威嚇":[0.0,0.0,1.0,0.0,0.8,1.8],
                    "穩定傷勢":[0.0,0.0,0.0,0.0,2.0,0.0],
                    "察言觀色":[0.0,0.0,0.0,1.0,2.0,0.0],
                    "欺騙機率":[0.0,0.0,0.0,0.8,0.0,1.8],
                    "表演":[0.0,0.8,0.0,0.0,0.8,1.8],
                    "融入人群":[0.0,0.0,0.0,0.8,0.8,1.8],
                    "特技動作":[0.0,1.8,0.0,0.8,0.6,0.0],
                    "奧術法術":[0.0,0.0,0.0,1.8,0.8,0.0],
                    "法術詠唱速度":[0.0,0.8,0.0,1.8,0.0,0.0],
                    "估價":[0.0,0.0,0.0,1.8,0.8,0.0] }
    
    index = mylistbox.curselection()
    pp=0
    
    targ=[]
    for i in index:
        tttg=""
        tttg = mylistbox.get(i)
        targ.append(tttg)
        pp=pp+1
    targetratio1=targetdic[targ[0]]
    targetratio2=targetdic[targ[1]]
    #----------------------------------------------------------------------------------------------------------------------
    
    startnum=[]
    bbb=[]
    record=[]

    for i in range(0,100):
        ggg=[]
        for lvv in range(0,lv):

            bbb=(random.choice([1,2,3,4,5,6]),random.choice([1,2,3,4,5,6]),random.choice([1,2,3,4,5,6]),random.choice([1,2,3,4,5,6]),random.choice([1,2,3,4,5,6]))
            ggg.extend(bbb)
        for lvv in range(0,int(addn)):
            
            bbb=(random.choice([1,2,3,4,5,6]),)
            ggg.extend(bbb)
        startnum.append(ggg)

    startnum=pd.DataFrame(startnum)
    colu = []
    for i in range(1,(lv*5)+1+int(addn)):
        colu.append(i)
    startnum.columns = colu

    finalchar =[]
    aaa=[]
    kkk = startnum
    for i in range(0,100):
    
        startstr1 = startstr
        startdex1 = startdex
        startcon1 = startcon
        startint1 = startint
        startwis1 = startwis
        startcha1 = startcha
        for j in range(1,(lv*5+int(addn))):
            if kkk.iloc[i][j] == 1:
                startstr1=startstr1+1
            elif kkk.iloc[i][j] == 2:
                startdex1=startdex1+1
            elif kkk.iloc[i][j] == 3:
                startcon1=startcon1+1
            elif kkk.iloc[i][j] == 4:
                startint1=startint1+1
            elif kkk.iloc[i][j] == 5:
                startwis1=startwis1+1
            elif kkk.iloc[i][j] == 6:
                startcha1=startcha1+1
        aaa=(startstr1,startdex1,startcon1,startint1,startwis1,startcha1)
        finalchar.append(aaa)
    finalchar=pd.DataFrame(finalchar)


    target1 = []
    target2 = []
    for i in range(0,100):
        t1=0
        t2=0
        for j in range(0,6):
            t1 = finalchar.iloc[i][j]*targetratio1[j] + t1
            t2 = finalchar.iloc[i][j]*targetratio2[j] + t2
        target1.append(t1)
        target2.append(t2)


    target1=pd.DataFrame(target1)
    target2=pd.DataFrame(target2)
    target1.columns = ['t1']
    target2.columns = ['t2']
    df=[]
    df=pd.DataFrame(df)
    df= pd.concat([startnum,target1], axis=1)
    df= pd.concat([df,target2], axis=1)

    df.sort_values(by=['t1'], inplace=True,ascending=[False])
    df.to_csv('test.csv', index=False)
    df = pd.read_csv("test.csv")
    control_number1 = pd.read_csv("control1.csv")
    df = pd.concat([df,control_number1], axis=1)
    
    df.sort_values(by=['t2'], inplace=True,ascending=[False])
    df.to_csv('test.csv', index=False)
    df = pd.read_csv("test.csv")
    control_number2 = pd.read_csv("control2.csv")
    df = pd.concat([df,control_number2], axis=1)
    
    total = df['control_number1']+df['control_number2']#1
    total= pd.DataFrame(total)
    total.columns = ['Final_preds']
    df = pd.concat([df,total], axis=1)

    df.sort_values(by=['Final_preds'], inplace=True,ascending=[True])
    df.to_csv('test.csv', index=False)
    df = pd.read_csv("test.csv")
    control_number = pd.read_csv("control.csv")
    df2 = pd.concat([df,control_number], axis=1)

    control_table=[]
    control_table =df2
    control_table.to_csv('control_table.csv', index=False)
    ans=control_table
    score=[]
    yyk = []
    yyk = control_table.iloc[0:9,:]
    score = pd.DataFrame(score)
    score = pd.concat([score,yyk], axis=0)
    o=0
    while o <40:
        ans = ans.drop(columns=['t1'])
        ans = ans.drop(columns=['t2'])
        ans = ans.drop(columns=['control_number1'])
        ans = ans.drop(columns=['control_number2'])
        ans = ans.drop(columns=['Final_preds'])
        ans = ans.drop(columns=['control_number'])
        df2=ans
        df = pd.concat([ans, df2], axis=0)
        for i in range(2,100):
            bbb=[]
            for j in range(0,(lv*5)):
                bbb.append(j)
            random.shuffle(bbb)
            bbb = pd.DataFrame(bbb)
            b_1 = bbb.iloc[1,0]
            ggg=[]
            bbb=[]
            for lvv in range(0,lv):
                bbb=(random.choice([1,2,3,4,5,6]),random.choice([1,2,3,4,5,6]),random.choice([1,2,3,4,5,6]),random.choice([1,2,3,4,5,6]),random.choice([1,2,3,4,5,6]))
                ggg.extend(bbb)
            for lvv in range(0,int(addn)):
            
                bbb=(random.choice([1,2,3,4,5,6]),)
                ggg.extend(bbb)
            cc = ggg
            df.iloc[i,b_1] = cc[b_1]
        for i in range(101,199):
            bbb=[]
            for j in range(0,(lv*5)):
                bbb.append(j)
            random.shuffle(bbb)
            bbb = pd.DataFrame(bbb)
            b_1 = bbb.iloc[1,0]
            g = df.iloc[i,b_1]
            df.iloc[i,b_1] = df.iloc[i+1,b_1]
            df.iloc[i+1,b_1] = g
        df.reset_index(drop=True, inplace=True)
        df.columns = colu
        finalchar =[]
        aaa=[]
        kkk = df
        for i in range(0,200):
            startstr1 = startstr
            startdex1 = startdex
            startcon1 = startcon
            startint1 = startint
            startwis1 = startwis
            startcha1 = startcha
            for j in range(1,(lv*5)+int(addn)):
                if kkk.iloc[i][j] == 1:
                    startstr1=startstr1+1
                elif kkk.iloc[i][j] == 2:
                    startdex1=startdex1+1
                elif kkk.iloc[i][j] == 3:
                    startcon1=startcon1+1
                elif kkk.iloc[i][j] == 4:
                    startint1=startint1+1
                elif kkk.iloc[i][j] == 5:
                    startwis1=startwis1+1
                elif kkk.iloc[i][j] == 6:
                    startcha1=startcha1+1
            aaa=(startstr1,startdex1,startcon1,startint1,startwis1,startcha1)
            finalchar.append(aaa)
        finalchar=pd.DataFrame(finalchar)
        target1 = []
        target2 = []
        for i in range(0,200):
            t1=0
            t2=0
            for j in range(0,6):
                t1 = finalchar.iloc[i][j]*targetratio1[j] + t1
                t2 = finalchar.iloc[i][j]*targetratio2[j] + t2
            target1.append(t1)
            target2.append(t2)
        target1=pd.DataFrame(target1)
        target2=pd.DataFrame(target2)
        target1.columns = ['t1']
        target2.columns = ['t2']
        df=[]
        df=pd.DataFrame(df)
        df= pd.concat([kkk,target1], axis=1)
        df= pd.concat([df,target2], axis=1)
        
        df.sort_values(by=['t1'], inplace=True,ascending=[False])
        df.to_csv('test.csv', index=False)
        df = pd.read_csv("test.csv")
        control_number3 = pd.read_csv("control3.csv")
        df = pd.concat([df,control_number3], axis=1)

        df.sort_values(by=['t2'], inplace=True,ascending=[False])
        df.to_csv('test.csv', index=False)
        df = pd.read_csv("test.csv")
        control_number4 = pd.read_csv("control4.csv")
        df = pd.concat([df,control_number4], axis=1)
        
        total = df['control_number1'] + df['control_number2']#2
        total= pd.DataFrame(total)
        total.columns = ['Final_preds']
        df = pd.concat([df,total], axis=1)

        df.sort_values(by=['Final_preds'], inplace=True,ascending=[True])
        df.to_csv('test.csv', index=False)
        df = pd.read_csv("test.csv")
        control_number = pd.read_csv("control-2.csv")
        df2 = pd.concat([df,control_number], axis=1)
        ct = pd.read_csv("control_table.csv")
        df3 = df2.iloc[0:100,:]
        ct=pd.concat([ct,df3])
        ct.sort_values(by=['control_number'], inplace=True,ascending=[True])
        ct.to_csv('control_table.csv', index=False)
        ct= pd.read_csv("control_table.csv")
        ans = ct.iloc[0:100,:]
        preans = ans
        preans=pd.DataFrame(preans)
        preans.sort_values(by=['control_number'], inplace=True,ascending=[True])
        preans.to_csv('ans.csv', index=False)
        jj= []
        jj=preans.iloc[0:9,:]
        score= pd.concat([score,jj], axis=0)
        o=o+1
        
        
    score=pd.DataFrame(score)
    score.to_csv('score-10NSGA.csv', index=False)

    
    #--------------------------------------------------------------------------------------------------
    

    
    finalshow = pd.read_csv('score-10NSGA.csv')
    finalshow = pd.DataFrame(finalshow)
    finalshow=finalshow.drop(columns=['control_number1'])
    finalshow=finalshow.drop(columns=['control_number2'])
    finalshow=finalshow.drop(columns=['Final_preds'])

    finalshow.drop_duplicates(subset = ['t1','t2'],keep='first', inplace=True)
    finalshow.to_csv('score-10NSGA.csv', index=False)
    finalshow = pd.read_csv('score-10NSGA.csv')
    finalshow.sort_values(by=['control_number'], inplace=True,ascending=[True])
    finalshow.to_csv('score-10NSGA.csv', index=False)
    finalshow = pd.read_csv('score-10NSGA.csv')

    

    ansss = finalshow.iloc[0:10,:]
    faa = 0
    ind = 0
    fff = 0

    resultSTR = []
    resultDEX = []
    resultCON = []
    resultINT = []
    resultWIS = []
    resultCHA = []
        
    for i in range(0,10):
        startstr1 = startstr
        startdex1 = startdex
        startcon1 = startcon
        startint1 = startint
        startwis1 = startwis
        startcha1 = startcha
        for j in range(1,(lv*5)+int(addn)):
            if ansss.iloc[i][j] == 1:
                startstr1=startstr1+1
            elif ansss.iloc[i][j] == 2:
                startdex1=startdex1+1
            elif ansss.iloc[i][j] == 3:
                startcon1=startcon1+1
            elif ansss.iloc[i][j] == 4:
                startint1=startint1+1
            elif ansss.iloc[i][j] == 5:
                startwis1=startwis1+1
            elif ansss.iloc[i][j] == 6:
                startcha1=startcha1+1
        resultSTR.append(str(startstr1))
        resultDEX.append(str(startdex1))
        resultCON.append(str(startcon1))
        resultINT.append(str(startint1))
        resultWIS.append(str(startwis1))
        resultCHA.append(str(startcha1))
        
        tot=0
        iii=0
        for iii in range(0,10):
            tot = tot + int(resultSTR[i])
        avaSTR = int(tot/10)
        tot=0
        iii=0
        for iii in range(0,10):
            tot = tot + int(resultDEX[i])
        avaDEX = int(tot/10)
        tot=0
        iii=0
        for iii in range(0,10):
            tot = tot + int(resultCON[i])
        avaCON = int(tot/10)
        tot=0
        iii=0
        for iii in range(0,10):
            tot = tot + int(resultINT[i])
        avaINT = int(tot/10)
        tot=0
        iii=0
        for iii in range(0,10):
            tot = tot + int(resultWIS[i])
        avaWIS = int(tot/10)
        tot=0
        iii=0
        for iii in range(0,10):
            tot = tot + int(resultCHA[i])
        avaCHA = int(tot/10)
        
        
   

    #--------------------------------------------------------------------------------------------------

    new = Toplevel()
    load = Image.open('ElbYw-IXYAAvsa6.png')
    back = ImageTk.PhotoImage(load)
    img = Label(new, image=back)
    img.place(x=0,y=0)
    
    race_frame=LabelFrame(new, padx=15, pady=18, bd=5, relief='ridge', font=25)
    race_frame.grid(row=0, column=0, padx=5, pady=10)
    word=Label(race_frame, text='STR: '+resultSTR[0], font="Helvetica 19 bold").grid()
    word=Label(race_frame, text='DEX: '+resultDEX[0], font="Helvetica 19 bold").grid()
    word=Label(race_frame, text='CON: '+resultCON[0], font="Helvetica 19 bold").grid()
    word=Label(race_frame, text='INT: '+resultINT[0], font="Helvetica 19 bold").grid()
    word=Label(race_frame, text='WIS: '+resultWIS[0], font="Helvetica 19 bold").grid()
    word=Label(race_frame, text='CHA: '+resultCHA[0], font="Helvetica 19 bold").grid()
    race1_frame=LabelFrame(new,padx=15, pady=18, bd=5, relief='ridge', font=25)
    race1_frame.grid(row=0, column=1, padx=5, pady=10)
    word=Label(race1_frame, text='STR: '+resultSTR[1], font="Helvetica 19 bold").grid()
    word=Label(race1_frame, text='DEX: '+resultDEX[1], font="Helvetica 19 bold").grid()
    word=Label(race1_frame, text='CON: '+resultCON[1], font="Helvetica 19 bold").grid()
    word=Label(race1_frame, text='INT: '+resultINT[1], font="Helvetica 19 bold").grid()
    word=Label(race1_frame, text='WIS: '+resultWIS[1], font="Helvetica 19 bold").grid()
    word=Label(race1_frame, text='CHA: '+resultCHA[1], font="Helvetica 19 bold").grid()
    race2_frame=LabelFrame(new, padx=15, pady=18, bd=5, relief='ridge', font=25)
    race2_frame.grid(row=0, column=2, padx=5, pady=10)
    word=Label(race2_frame, text='STR: '+resultSTR[2], font="Helvetica 19 bold").grid()
    word=Label(race2_frame, text='DEX: '+resultDEX[2], font="Helvetica 19 bold").grid()
    word=Label(race2_frame, text='CON: '+resultCON[2], font="Helvetica 19 bold").grid()
    word=Label(race2_frame, text='INT: '+resultINT[2], font="Helvetica 19 bold").grid()
    word=Label(race2_frame, text='WIS: '+resultWIS[2], font="Helvetica 19 bold").grid()
    word=Label(race2_frame, text='CHA: '+resultCHA[2], font="Helvetica 19 bold").grid()
    race3_frame=LabelFrame(new, padx=15, pady=18, bd=5, relief='ridge', font=25)
    race3_frame.grid(row=0, column=3, padx=5, pady=10)
    word=Label(race3_frame, text='STR: '+resultSTR[3], font="Helvetica 19 bold").grid()
    word=Label(race3_frame, text='DEX: '+resultDEX[3], font="Helvetica 19 bold").grid()
    word=Label(race3_frame, text='CON: '+resultCON[3], font="Helvetica 19 bold").grid()
    word=Label(race3_frame, text='INT: '+resultINT[3], font="Helvetica 19 bold").grid()
    word=Label(race3_frame, text='WIS: '+resultWIS[3], font="Helvetica 19 bold").grid()
    word=Label(race3_frame, text='CHA: '+resultCHA[3], font="Helvetica 19 bold").grid()
    race4_frame=LabelFrame(new, padx=15, pady=18, bd=5, relief='ridge', font=25)
    race4_frame.grid(row=0, column=4, padx=5, pady=10)
    word=Label(race4_frame, text='STR: '+resultSTR[4], font="Helvetica 19 bold").grid()
    word=Label(race4_frame, text='DEX: '+resultDEX[4], font="Helvetica 19 bold").grid()
    word=Label(race4_frame, text='CON: '+resultCON[4], font="Helvetica 19 bold").grid()
    word=Label(race4_frame, text='INT: '+resultINT[4], font="Helvetica 19 bold").grid()
    word=Label(race4_frame, text='WIS: '+resultWIS[4], font="Helvetica 19 bold").grid()
    word=Label(race4_frame, text='CHA: '+resultCHA[4], font="Helvetica 19 bold").grid()
    race5_frame=LabelFrame(new, padx=15, pady=18, bd=5, relief='ridge', font=25)
    race5_frame.grid(row=0, column=5, padx=5, pady=10)
    word=Label(race5_frame, text='STR: '+resultSTR[5], font="Helvetica 19 bold").grid()
    word=Label(race5_frame, text='DEX: '+resultDEX[5], font="Helvetica 19 bold").grid()
    word=Label(race5_frame, text='CON: '+resultCON[5], font="Helvetica 19 bold").grid()
    word=Label(race5_frame, text='INT: '+resultINT[5], font="Helvetica 19 bold").grid()
    word=Label(race5_frame, text='WIS: '+resultWIS[5], font="Helvetica 19 bold").grid()
    word=Label(race5_frame, text='CHA: '+resultCHA[5], font="Helvetica 19 bold").grid()
    race6_frame=LabelFrame(new, padx=15, pady=18, bd=5, relief='ridge', font=25)
    race6_frame.grid(row=0, column=6, padx=5, pady=10)
    word=Label(race6_frame, text='STR: '+resultSTR[6], font="Helvetica 19 bold").grid()
    word=Label(race6_frame, text='DEX: '+resultDEX[6], font="Helvetica 19 bold").grid()
    word=Label(race6_frame, text='CON: '+resultCON[6], font="Helvetica 19 bold").grid()
    word=Label(race6_frame, text='INT: '+resultINT[6], font="Helvetica 19 bold").grid()
    word=Label(race6_frame, text='WIS: '+resultWIS[6], font="Helvetica 19 bold").grid()
    word=Label(race6_frame, text='CHA: '+resultCHA[6], font="Helvetica 19 bold").grid()
    race7_frame=LabelFrame(new, padx=15, pady=18, bd=5, relief='ridge', font=25)
    race7_frame.grid(row=0, column=7, padx=5, pady=10)
    word=Label(race7_frame, text='STR: '+resultSTR[7], font="Helvetica 19 bold").grid()
    word=Label(race7_frame, text='DEX: '+resultDEX[7], font="Helvetica 19 bold").grid()
    word=Label(race7_frame, text='CON: '+resultCON[7], font="Helvetica 19 bold").grid()
    word=Label(race7_frame, text='INT: '+resultINT[7], font="Helvetica 19 bold").grid()
    word=Label(race7_frame, text='WIS: '+resultWIS[7], font="Helvetica 19 bold").grid()
    word=Label(race7_frame, text='CHA: '+resultCHA[7], font="Helvetica 19 bold").grid()
    race8_frame=LabelFrame(new, padx=15, pady=18, bd=5, relief='ridge', font=25)
    race8_frame.grid(row=0, column=8, padx=5, pady=10)
    word=Label(race8_frame, text='STR: '+resultSTR[8], font="Helvetica 19 bold").grid()
    word=Label(race8_frame, text='DEX: '+resultDEX[8], font="Helvetica 19 bold").grid()
    word=Label(race8_frame, text='CON: '+resultCON[8], font="Helvetica 19 bold").grid()
    word=Label(race8_frame, text='INT: '+resultINT[8], font="Helvetica 19 bold").grid()
    word=Label(race8_frame, text='WIS: '+resultWIS[8], font="Helvetica 19 bold").grid()
    word=Label(race8_frame, text='CHA: '+resultCHA[8], font="Helvetica 19 bold").grid()
    race9_frame=LabelFrame(new, padx=15, pady=18, bd=5, relief='ridge', font=25)
    race9_frame.grid(row=0, column=9, padx=5, pady=10)
    word=Label(race9_frame, text='STR: '+resultSTR[9], font="Helvetica 19 bold").grid()
    word=Label(race9_frame, text='DEX: '+resultDEX[9], font="Helvetica 19 bold").grid()
    word=Label(race9_frame, text='CON: '+resultCON[9], font="Helvetica 19 bold").grid()
    word=Label(race9_frame, text='INT: '+resultINT[9], font="Helvetica 19 bold").grid()
    word=Label(race9_frame, text='WIS: '+resultWIS[9], font="Helvetica 19 bold").grid()
    word=Label(race9_frame, text='CHA: '+resultCHA[9], font="Helvetica 19 bold").grid()
    race10_frame=LabelFrame(new, text="平均結果", padx=15, pady=18, bd=5, relief='ridge', font="Helvetica 20 bold")
    race10_frame.grid(row=0, column=9, padx=5, pady=10)
    word=Label(race10_frame, text='STR: '+str(avaSTR), font="Helvetica 19 bold").grid()
    word=Label(race10_frame, text='DEX: '+str(avaDEX), font="Helvetica 19 bold").grid()
    word=Label(race10_frame, text='CON: '+str(avaCON), font="Helvetica 19 bold").grid()
    word=Label(race10_frame, text='INT: '+str(avaINT), font="Helvetica 19 bold").grid()
    word=Label(race10_frame, text='WIS: '+str(avaWIS), font="Helvetica 19 bold").grid()
    word=Label(race10_frame, text='CHA: '+str(avaCHA), font="Helvetica 19 bold").grid()



# In[ ]:





# In[58]:


root = Tk()
root.title("DND點數分配器")
root.iconbitmap('1.ico')
load = Image.open('1030391.jpg')
back = ImageTk.PhotoImage(load)
img = Label(root, image=back)
img.place(x=0,y=0)
root.geometry("1600x900")


# In[59]:


f1 = tkFont.Font(family='microsoft yahei', size=40, weight='bold')
f2 = tkFont.Font(family='times', size=15, slant='italic', weight='bold')
f3 = tkFont.Font(family='times', size=19, slant='italic')

racevalue=IntVar()
racevalue.set(1)
race_frame=LabelFrame(root, text="種族", padx=15, pady=18, bd=5, relief='ridge', font=f1, height = 100, width = 200, fg='gray')
race_frame.grid(row=0, column=0, padx=20, pady=200)
Radiobutton(race_frame, text="精靈", variable=racevalue, value=1, font="Helvetica 19 bold").grid(sticky='w')
Radiobutton(race_frame, text="半精靈", variable=racevalue, value=2, font="Helvetica 19 bold").grid(sticky='w')
Radiobutton(race_frame, text="人類", variable=racevalue, value=3, font="Helvetica 19 bold").grid(sticky='w')
Radiobutton(race_frame, text="半身人", variable=racevalue, value=4, font="Helvetica 19 bold").grid(sticky='w')
Radiobutton(race_frame, text="矮人", variable=racevalue, value=5, font="Helvetica 19 bold").grid(sticky='w')
Radiobutton(race_frame, text="半獸人", variable=racevalue, value=6, font="Helvetica 19 bold").grid(sticky='w')
Radiobutton(race_frame, text="龍裔", variable=racevalue, value=7, font="Helvetica 19 bold").grid(sticky='w')
Radiobutton(race_frame, text="魔人", variable=racevalue, value=8, font="Helvetica 19 bold").grid(sticky='w')
Radiobutton(race_frame, text="地株", variable=racevalue, value=9, font="Helvetica 19 bold").grid(sticky='w')


jobvalue=IntVar()
jobvalue.set(1)
job_frame=LabelFrame(root, text="職業", padx=15, pady=18, bd=5, relief='ridge', font=f1, fg='gray')
job_frame.grid(row=0,column=1, padx=20, pady=200)
Radiobutton(job_frame, text="戰士", variable=jobvalue, value=1, font="Helvetica 19 bold").grid(sticky='w')
Radiobutton(job_frame, text="刺客", variable=jobvalue, value=2, font="Helvetica 19 bold").grid(sticky='w')
Radiobutton(job_frame, text="法師", variable=jobvalue, value=3, font="Helvetica 19 bold").grid(sticky='w')
Radiobutton(job_frame, text="德魯伊", variable=jobvalue, value=4, font="Helvetica 19 bold").grid(sticky='w')
Radiobutton(job_frame, text="牧師", variable=jobvalue, value=5, font="Helvetica 19 bold").grid(sticky='w')
Radiobutton(job_frame, text="遊俠", variable=jobvalue, value=6, font="Helvetica 19 bold").grid(sticky='w')
Radiobutton(job_frame, text="吟遊詩人", variable=jobvalue, value=7, font="Helvetica 19 bold").grid(sticky='w')
Radiobutton(job_frame, text="術士", variable=jobvalue, value=8, font="Helvetica 19 bold").grid(sticky='w')
Radiobutton(job_frame, text="聖騎士", variable=jobvalue, value=9, font="Helvetica 19 bold").grid(sticky='w')

factionvalue=IntVar()
factionvalue.set(1)
faction_frame=LabelFrame(root, text="陣營", padx=15, pady=18, bd=5, relief='ridge', font=f1, fg='gray')
faction_frame.grid(row=0,column=2, padx=20, pady=200)
Radiobutton(faction_frame, text="守序善良", variable=factionvalue, value=1, font="Helvetica 19 bold").pack()
Radiobutton(faction_frame, text="中立善良", variable=factionvalue, value=2, font="Helvetica 19 bold").pack()
Radiobutton(faction_frame, text="混亂善良", variable=factionvalue, value=3, font="Helvetica 19 bold").pack()
Radiobutton(faction_frame, text="守序中立", variable=factionvalue, value=4, font="Helvetica 19 bold").pack()
Radiobutton(faction_frame, text="絕對中立", variable=factionvalue, value=5, font="Helvetica 19 bold").pack()
Radiobutton(faction_frame, text="混亂中立", variable=factionvalue, value=6, font="Helvetica 19 bold").pack()
Radiobutton(faction_frame, text="守序邪惡", variable=factionvalue, value=7, font="Helvetica 19 bold").pack()
Radiobutton(faction_frame, text="中立邪惡", variable=factionvalue, value=8, font="Helvetica 19 bold").pack()
Radiobutton(faction_frame, text="混亂邪惡", variable=factionvalue, value=9, font="Helvetica 19 bold").pack()

Attributes_frame=LabelFrame(root, text="屬性", padx=15, pady=10, bd=5, font=f1, relief='ridge', fg='gray')
Attributes_frame.grid(row=0,column=3, padx=20, pady=200)
#STR
attribute1 = Label(Attributes_frame, text="STR", font=f3).grid(sticky='w')
num1=IntVar()
STR_entry=Entry(Attributes_frame, font="Helvetica 18 bold", textvariable=num1, fg="yellow", bg='grey')
STR_entry.grid(sticky='w')
#DEX
attribute2 = Label(Attributes_frame, text="DEX", font=f3).grid(sticky='w')
num2=IntVar()
DEX_entry=Entry(Attributes_frame, font="Helvetica 18 bold", textvariable=num2, fg="yellow", bg='grey')
DEX_entry.grid(sticky='w')
#CON
attribute3 = Label(Attributes_frame, text="CON", font=f3).grid(sticky='w')
num3=IntVar()
CON_entry=Entry(Attributes_frame, font="Helvetica 18 bold", textvariable=num3, fg="yellow", bg='grey')
CON_entry.grid(sticky='w')
#INT
attribute4 = Label(Attributes_frame, text="INT", font=f3).grid(sticky='w')
num4=IntVar()
INT_entry=Entry(Attributes_frame, font="Helvetica 18 bold", textvariable=num4, fg="yellow", bg='grey')
INT_entry.grid(sticky='w')
#WIS
attribute5 = Label(Attributes_frame, text="WIS", font=f3).grid(sticky='w')
num5=IntVar()
WIS_entry=Entry(Attributes_frame, font="Helvetica 18 bold", textvariable=num5, fg="yellow", bg='grey')
WIS_entry.grid(sticky='w')
#CHA
attribute6 = Label(Attributes_frame, text="CHA", font=f3).grid(sticky='w')
num6=IntVar()
CHA_entry=Entry(Attributes_frame, font="Helvetica 18 bold", textvariable=num6, fg="yellow", bg='grey')
CHA_entry.grid(sticky='w')

num7=IntVar()
v=StringVar()
LEVEL_frame=LabelFrame(root, text="目標", padx=12, pady=8, bd=5, relief='ridge', font=f1, fg='gray')
LEVEL_frame.grid(row=0,column=4, padx=20, pady=200)
targer=Label(LEVEL_frame, text="目標提升等級").grid(sticky='w')
levelup=Entry(LEVEL_frame, font="Helvetica 18 bold", textvariable=num7, fg="yellow", bg='green')
levelup.grid(sticky='w')
selecttarget=Label(LEVEL_frame, text="目標(建議至多2項)").grid(sticky='w')
mylistbox=Listbox(LEVEL_frame, font="Helvetica 19 bold", selectmode=MULTIPLE, bg='black', fg='white', selectbackground='red',listvariable=v, height=10, width=18)#, yscrollcommand=myscrollbar.set
mylistbox.grid()
lol=Label(LEVEL_frame, text="  ").grid()

frame5=LabelFrame(root, text="功能", padx=20, pady=8, bd=5, relief='ridge', font=f1, fg='gray')
frame5.grid(row=0,column=5, padx=25, pady=150)
a=Label(frame5, text="  ").grid()
myButton2=Button(frame5, text="目標更新", command=refresh, fg="lime",bg="blue", height=4, width=10, font="Helvetica 20 bold").grid()
b=Label(frame5, text="  ").grid()
c=Label(frame5, text="  ").grid()
myButton=Button(frame5, text="執行", command=calbest, fg="yellow",bg="green", height=4, width=10, font="Helvetica 20 bold").grid()
e=Label(frame5, text="  ").grid()
d=Label(frame5, text="  ").grid()


# In[60]:


root.mainloop()

