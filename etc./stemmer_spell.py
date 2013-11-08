def stemmer(word,flex,pos):
    root=''
    #be nim fasele tavajoh konid
    #noun
    asli=word
    shakhsi1=['م','ت','ش']
    shakhsi3=['مان','تان','شان']
    shakhsi2=['ام','ات','اش']
    shakhsi4=['يمان','يتان','يشان']
    rabti1=['م','ي','د']
    rabti2=['يم','يد','ند']
    flag=0
    if word[-2:] in rabti2:
        word=word[:len(word)-2]
    if word in flex:
        i=flex.index(word)
        p=pos[i]
        if p=='N1' or p=='N8':
            flag=1
            return word,flag
    if len(word)==0:
        flag=1
        return asli,flag
    if len(word)>0:
        if word[-1] in rabti1:
            word=word[:len(word)-1]
        
    if word in flex:
        i=flex.index(word)
        p=pos[i]
        
        if p=='N1':
            flag=1
            return word,flag
    if len(word)==0:
        flag=1
        return asli,flag
    aw=word
    cc=0
    if word.endswith('هاي'):
        cc=1
        x=word[:len(word)-3]
        if len(x)>0:
            if x[-1]=='':
                x=x[:len(x)-1]
        if x in flex:
            i=flex.index(x)
            p=pos[i]
            if p=='N1' or p=='N6' or p=='A1':
                flag=1
                return x,flag
        if len(x)==0:
            flag=1
            return asli,flag
    if cc==0:
        word=aw
    
    if word.endswith('ها') or word.endswith('ان') or word.endswith('ات'):
        cc=1
        x=word[:len(word)-2]
        if len(x)>0:
            if x[-1]=='':
                x=x[:len(x)-1]
        if x in flex:
            i=flex.index(x)
            p=pos[i]
            if p=='N1' or p=='N6' or p=='A1':
                flag=1
                return x,flag
        if len(x)==0:
            flag=1
            return asli,flag
    if cc==0:
        word=aw
        
    if word[-4:] in shakhsi4:
        word=word[:len(word)-4]
        if len(word)>0:
            if word[-1]=='':
                word=word[:len(word)-1]
    if len(word)==0:
        flag=1
        return asli,flag    
    if word in flex:
        i=flex.index(word)
        
        p=pos[i]
        if p=='N1':
            flag=1
            return word,flag
    if len(word)==0:
        flag=1
        return asli,flag
    if word[-3:] in shakhsi3:
        word=word[:len(word)-3]
        if len(word)>0:
            if word[-1]=='':
                word=word[:len(word)-1]
    if word in flex:
        i=flex.index(word)
        p=pos[i]
        if p=='N1' or p=='N8':
            flag=1
            return word,flag
    if len(word)==0:
        flag=1
        return asli,flag
    if word[-2:] in shakhsi2:
        word=word[:len(word)-2]
        if len(word)>0:
            if word[-1]=='':
                word=word[:len(word)-1]
    if word in flex:
        i=flex.index(word)
        p=pos[i]
        if p=='N1':
            flag=1
            return word,flag
    if len(word)==0:
        flag=1
        return asli,flag
    if word[-1] in shakhsi1:
        word=word[:len(word)-1]
    if word in flex:
        i=flex.index(word)
        p=pos[i]
        if p=='N1' or p=='N8':
            flag=1
            return word,flag
    if len(word)==0:
        flag=1
        return asli,flag
    asl=asli
    if len(asl)>1:
        
        if asl[-2:]=='يي' or asl[-2:]=='اي':
            asl=asl[:len(asl)-2]
            if asl.endswith('')and asl[-1]!='و':
                asl=asl[:len(asl)-1]
            
    if asl in flex:
        i=flex.index(asl)
        p=pos[i]
        if p=='N1' or p=='N8':
            flag=1
            return asl,flag
    if len(asl)==0:
        flag=1
        return asli,flag
    if len(asl)>0:
        if asl[-1]=='ي':
            asl=asl[:len(asl)-1]
            if asl.endswith('')and word[-1]!='و':
                asl=asl[:len(asl)-1]
    if asl in flex:
        i=flex.index(asl)
        p=pos[i]
        if p=='N1' or p=='N8':
            flag=1
            return asl,flag
    if len(asl)==0:
        flag=1
        return asli,flag
    if len(word)>1:
        
        if word[-2:]=='يي' or word[-2:]=='اي':
            word=word[:len(word)-2]
            if len(word)>0:
                if word[-1]=='':
                    word=word[:len(word)-1]
    if word in flex:
        i=flex.index(word)
        p=pos[i]
        if p=='N1' or p=='N8':
            flag=1
            return word,flag
    if len(word)==0:
        flag=1
        return asli,flag
    if len(word)>0:
        if word[-1]=='ي':
            word=word[:len(word)-1]
            if len(word)>0:
                if word[-1]=='':
                    word=word[:len(word)-1]
    if word in flex:
        i=flex.index(word)
        p=pos[i]
        if p=='N1' or p=='N8':
            flag=1
            return word,flag
    if len(word)==0:
        flag=1
        return asli,flag
    
    
    
    
    #q=word
    if word.endswith('ها') or word.endswith('ان') or word.endswith('ات'):
        
        x=word[:len(word)-2]
        if len(x)>0:
            if x[-1]=='':
                x=x[:len(x)-1]
        if x in flex:
            i=flex.index(x)
            p=pos[i]
            if p=='N1' or p=='N6' or p=='A1':
                flag=1
                return x,flag
        if len(x)==0:
            flag=1
            return asli,flag
    
    if word.endswith('گان'):
        x=word[:len(word)-3]
        x+='ه'
        if x in flex:
            i=flex.index(x)
            p=pos[i]
            
            if p=='N1' or p=='N6' or p=='A0':
                flag=1
                return x,flag
        
    if word.endswith('يان'):
        x=word[:len(word)-3]
        if x in flex:
            i=flex.index(x)
            p=pos[i]
            if p=='N1' or p=='N6' or p=='A0':
                flag=1
                return x,flag
        if len(x)==0:
            flag=1
            return asli,flag


        
        
    #adjective
    if flag==0:
        word=asli
    if word[-1] in rabti1:
        word=word[:len(word)-1]
    if word in flex:
        i=flex.index(word)
        p=pos[i]
        if p=='A0':
            flag=1
            return word,flag
    if len(word)==0:
        flag=1
        return asli,flag
    rab2=['يم','يد','ست']
    if word[-2:] in rab2:
        word=word[:len(word)-2]
    if word in flex:
        i=flex.index(word)
        p=pos[i]
        if p=='A0':
            flag=1
            return word,flag
    if len(word)==0:
        flag=1
        return asli,flag
    if word.endswith('ها') or word.endswith('ان') or word.endswith('ات'):
        
        x=word[:len(word)-2]
        if len(x)>0:
            if x[-1]=='':
                x=x[:len(x)-1]
        if x in flex:
            i=flex.index(x)
            p=pos[i]
            if p=='A0' or p=='A1':
                flag=1
                return x,flag
        if len(x)==0:
            flag=1
            return asli,flag
        
        if x.endswith('ترين'):
            x=x[:len(x)-4]
            if len(x)>0:
                if x[-1]=='':
                    x=x[:len(x)-1]
            if x in flex:
                i=flex.index(x)
                p=pos[i]
                if p=='A0':
                    flag=1
                    return x,flag
            if len(x)==0:
                flag=1
                return asli,flag
        if x.endswith('تر'):
            x=x[:len(x)-2]
            if len(x)>0:
                if x[-1]=='':
                    x=x[:len(x)-1]
            if x in flex:
                i=flex.index(x)
                p=pos[i]
                if p=='A0':
                    flag=1
                    return x,flag
            if len(x)==0:
                flag=1
                return asli,flag

        
        
    if word.endswith('ترين'):
        word=word[:len(word)-4]
        if len(word)>0:
            if word[-1]=='':
                word=word[:len(word)-1]
    if word in flex:
        i=flex.index(word)
        p=pos[i]
        if p=='A0':
            flag=1
            return word,flag
    if len(word)==0:
        flag=1
        return asli,flag
    if word.endswith('تر'):
        word=word[:len(word)-2]
        if len(word)>0:
            if word[-1]=='':
                word=word[:len(word)-1]
    if word in flex:
        i=flex.index(word)
        p=pos[i]
        if p=='A0':
            flag=1
            return word,flag
    if len(word)==0:
        flag=1
        return asli,flag
        
    #adverb
    if flag==0:
        word=asli
    if word.endswith('تر'):
        word=word[:len(word)-2]
        if len(word)>0:
            if word[-1]=='':
                word=word[:len(word)-1]
            
    if word in flex:
        i=flex.index(word)
        p=pos[i]
        if p=='Ad':
            flag=1
            return word,flag
    if len(word)==0:
        flag=1
        return asli,flag

    #verb
    if flag==0:
        word=asli
    shenase1=['م','ي','د']
    shenase2=['ام','اي','يم','يد','ند']
    shenase3=['است','ايم','ايد','اند','است']
    

    if word[-3:] in shakhsi3:
        word=word[:len(word)-3]
        if len(word)>0:
            if word[-1]=='':
                word=word[:len(word)-1]
               
    if len(word)==0:
        flag=1
        return asli,flag  
    if word[-1:] in shakhsi1 and word[-2:] not in shenase2 and word[-3:] not in shenase3:
        
        word=word[:len(word)-1]
        if word.endswith('')and word[-1]!='و':
                word=word[:len(word)-1]
    if len(word)==0:
        flag=1
        return asli,flag
    if word[-3:] in shenase3:
        word=word[:len(word)-3]
        if len(word)>0:
            if word[-1]=='':
                word=word[:len(word)-1]
    if len(word)==0:
        flag=1
        return asli,flag   
    if word in flex:
        co=flex.count(word)
        
        for t in range(len(flex)-1,-1,-1):
            if flex[t]==word:
                p=pos[t]
                  
                if p=='V2' or p=='V1' or p=='A0' or p=='V3' or p=='V5' or p=='V4':
                    flag=1
                    return word,flag
                    break    
    if word[-2:] in shenase2:
        word=word[:len(word)-2]
        if len(word)>0:
            if word[-1]=='':
                word=word[:len(word)-1]
    if len(word)==0:
        flag=1
        return asli,flag
        
    if word in flex:
        co=flex.count(word)
        
        for t in range(len(flex)-1,-1,-1):
            if flex[t]==word:
                p=pos[t]
                  
                if p=='V2' or p=='V1' or p=='A0' or p=='V3' or p=='V5' or p=='V4':
                    flag=1
                    return word,flag
                    break
    if word[-1:] in shenase1:
        word=word[:len(word)-1]
    
    
    if len(word)==0:
        flag=1
        return asli,flag   
    if word in flex:
        co=flex.count(word)
        
        for t in range(len(flex)-1,-1,-1):
            if flex[t]==word:
                p=pos[t]
                  
                if p=='V2' or p=='V1' or p=='A0' or p=='V3' or p=='V5' or p=='V4':
                    flag=1
                    return word,flag
                    break
    word=asli
    
    if word[0]=='ن':
        word=word[1:]
        if word in flex:
            co=flex.count(word)
            
            for t in range(len(flex)-1,-1,-1):
                if flex[t]==word:
                    p=pos[t]
                    if p=='V2' or p=='V1' or p=='V3' or p=='V5' or p=='V4':
                        flag=1
                        return word,flag
                        break
        if len(word)==0:
            flag=1
            return asli,flag
    
    if word[0]=='ب':
        root=word[1:]
        co=flex.count(root)
        
        for t in range(len(flex)-1,-1,-1):
            if flex[t]==root:
                p=pos[t]
                if p=='V2' or p=='V1' or p=='V3' or p=='V5' or p=='V4':
                    flag=1
                    return root,flag
                    break
        if len(root)==0:
            flag=1
            return asli,flag
        
    
    if word[0:2]=='مي':
        word=word[2:]
        if len(word)>0:
            if word[-1]=='':
                word=word[:len(word)-1]
        co=flex.count(word)
            
        for t in range(len(flex)-1,-1,-1):
            if flex[t]==word:
                p=pos[t]
                if p=='V2' or p=='V1' or p=='V3' or p=='V5' or p=='V4':
                    flag=1
                    return word,flag
                    break
    if len(word)==0:
        flag=1
        return asli,flag
    
    if word[-3:] in shakhsi3:
        word=word[:len(word)-3]
        if len(word)>0:
            if word[-1]=='':
                word=word[:len(word)-1]
    if len(word)==0:
        flag=1
        return asli,flag   
    if word[-1:] in shakhsi1 and word[-2:]!='ام' and word[-3:]!='ايم':
        
        word=word[:len(word)-1]
        if len(word)>0:
            if word[-1]=='':
                word=word[:len(word)-1]
    if len(word)==0:
        flag=1
        return asli,flag
    if word[-3:] in shenase3 and len(word)>4:
        word=word[:len(word)-3]
        if len(word)>0:
            if word[-1]=='':
                word=word[:len(word)-1]
    if len(word)==0:
        flag=1
        return asli,flag    
    if word[-2:] in shenase2 and len(word)>3:
        
        word=word[:len(word)-2]
        
        if len(word)>0:
            if word[-1]=='':
                word=word[:len(word)-1]
                
    if len(word)==0:
        flag=1
        return asli,flag
        
    if word in flex:
        co=flex.count(word)
        
        for t in range(len(flex)-1,-1,-1):
            if flex[t]==word:
                p=pos[t]
                if p=='V2' or p=='V1' or p=='V3' or p=='V5' or p=='V4':
                    flag=1
                    return asli,flag
                    break
    if word[-1:] in shenase1 and len(word)>2:
        word=word[:len(word)-1]
        if len(word)>0:
            if word[-1]=='':
                word=word[:len(word)-1]
    
    
    if len(word)==0:
        flag=1
        return asli,flag    
    if word in flex:
        co=flex.count(word)
        
        for t in range(len(flex)-1,-1,-1):
            if flex[t]==word:
                p=pos[t]
                if p=='V2' or p=='V1' or p=='V3' or p=='V5' or p=='V4':
                    flag=1
                    return word,flag
                    break
        
    if word[-1]=='ه':
        word=word[:len(word)-1]
        co=flex.count(word)
        
        for t in range(len(flex)-1,-1,-1):
            if flex[t]==word:
                p=pos[t]
                if p=='V2' or p=='V1' or p=='V3' or p=='V5' or p=='V4':
                    flag=1
                    return word,flag
                    break
    
            
    if word[0]=='ن':
        word=word[1:]
        co=flex.count(word)
        for t in range(len(flex)-1,-1,-1):
            if flex[t]==word:
                p=pos[t]
                if p=='V2' or p=='V1' or p=='V3' or p=='V5' or p=='V4':
                    flag=1
                    return word,flag
                    break
    if len(word)==0:
        flag=1
        return asli,flag
    
    if word[0]=='ب':
        word=word[1:]
    co=flex.count(word)
    
    for t in range(len(flex)-1,-1,-1):
        if flex[t]==word:
            p=pos[t]
            if p=='V2' or p=='V1' or p=='V3' or p=='V5' or p=='V4':
                flag=1
                return word,flag
                break
    if len(word)==0:
        flag=1
        return asli,flag
    if word[0:2]=='مي':
        word=word[2:]
        if len(word)>0:
            if word[-1]=='':
                word=word[:len(word)-1]
        co=flex.count(word)
            
        for t in range(len(flex)-1,-1,-1):
            if flex[t]==word:
                p=pos[t]
                if p=='V2' or p=='V1' or p=='V3' or p=='V5' or p=='V4':
                    flag=1
                    return word,flag
                    break
    if len(word)==0:
        flag=1
        return asli,flag
    if flag==0:
        
        return asli,flag
    
    
    
    
    
        
        
    
    
    

    
