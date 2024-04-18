
demog_ind = [1,1,1,1,1]
demog_par_score = [4,8,4,2,2]

def demog_score (df):
    score = 0
    if df['Gender'] == 'M':
        score+=4
    if df['SES']== 'Medium-High':
        score+=8
    if df['Urban']==1:  
        score+=4 
    if df['Season']=='Autumn':
        score+=2 
    if df['Smoking']==1:
        score+=2 
    return score

parent_ind = [1,1,1,1]
parent_par_score = [2.5,2.5,5,1]

def parent_score (df):
    score = 0
    if df['Maternal atopic']==1:
        score+=2.5  
    if df['Paternal atopic']==1:
        score+=2.5 
    if df['AD_parents']==1:
        score+=5 
    if df['Antibiotics.prg']==1:
        score+=1.5     
    return score


sib_ind = [1,1,1]
sib_par_score = [6,4,10]

def sibling_score (df):
    score = 0
    if df['First_Born']==1: 
        score+=6  
    if df['AD_sbiling']==1:
        score+=4
    if df['prec_sibling']>0:
        score+=10
    return score



def max_score (param_ind, param_score) :
    max_val = sum(x*y for x, y in list(zip(param_ind, param_score)))
    return max_val

def total_score (df, c):
    score = demog_score(df) + parent_score (df) + sibling_score (df)
    final_score = (score/(max_score(demog_ind,demog_par_score)+max_score(parent_ind,parent_par_score)+max_score(sib_ind,sib_par_score)))+c
    return final_score


def Risk (score):
    val=[]
    if score<=0.35:
        val='Low' 
    elif score<=0.5:
        val='Medium'
    else :
        val='High'       
    return val    
