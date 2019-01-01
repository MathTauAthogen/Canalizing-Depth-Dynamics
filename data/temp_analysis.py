import json
n=12
ssarr=[]
numattarr=[]
sumattarr=[]
avattarr=[]
for k in range(n+1): 
    with open("num_vars="+str(n)+"_depth="+str(k)+".json") as data:
        loaded=json.load(data)
        ss=[0]*len(loaded)
        numatt=[0]*len(loaded)
        sumatt=[0]*len(loaded)
        avatt=[]
        for i,dds in enumerate(loaded):
            tempss=0
            tempnumatt=0
            tempsumatt=0
            tempavatt=0
            for attbas in dds:
                att=attbas[0]
                if(att==1):
                    tempss+=1
                tempnumatt+=1
                tempsumatt+=att
                avatt.append(att)
            ss[i]=tempss
            numatt[i]=tempnumatt
            sumatt[i]=tempsumatt
        sscnt=[]
        numcnt=[]
        sumcnt=[]
        avcnt=[]
        for j in range(min(ss),max(ss)+1):
            if((ss.count(j)+0.0)/len(loaded)>0):
                sscnt.append([j,(ss.count(j)+0.0)/len(loaded)])
        for j in range(min(numatt),max(numatt)+1):
            if((numatt.count(j)+0.0)/len(loaded)>0):
                numcnt.append([j,(numatt.count(j)+0.0)/len(loaded)])
        for j in range(min(sumatt),max(sumatt)+1):
            if((sumatt.count(j)+0.0)/len(loaded)>0):
                sumcnt.append([j,(sumatt.count(j)+0.0)/len(loaded)])
        for j in range(min(avatt),max(avatt)+1):
            if((avatt.count(j)+0.0)/len(loaded)>0):
                avcnt.append([j,(avatt.count(j)+0.0)/len(loaded)])
        ssarr.append(sscnt)
        numattarr.append(numcnt)
        sumattarr.append(sumcnt)
        avattarr.append(avcnt)
with open("mathematica_data_n.json", "w+") as output:
    json.dump(ssarr,output)
with open("mathematica_data_m.json", "w+") as output:
    json.dump(numattarr,output)
with open("mathematica_data_o.json", "w+") as output:
    json.dump(sumattarr,output)
with open("mathematica_data_p.json", "w+") as output:
    json.dump(avattarr,output)
