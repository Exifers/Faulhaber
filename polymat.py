from fractions import Fraction
import copy

def mines(M,N):
    O=[]
    for i in range(len(M)):
        l=[]
        for j in range(len(M[0])):
            l+=[M[i][j]-N[i][j]]
        O+=[l]
    return O

def times(M,a):
    for i in range(len(M)):
        for j in range(len(M[0])):
            M[i][j]*=a
    return M

def call(M,X):
    Y=[]
    for j in range(len(M[0])):
        s=0
        for i in range(len(M)):
           s+=(M[i][j]*X[i])
        Y+=[s]
    return Y

def builtA(m):
    A=[]
    for i in range(m+1):
        l=[]
        for j in range(m+2):
            if i==j or (i+1==j):
                l+=[1]
            else:
                l+=[0]
        A+=[l]
    A[m][m+1]=1
    return A

def builtMp(M):
    for i in range(len(M)):
        M[i]+=[0]
    M+=[[0]*len(M[0])]
    return M

def builtM(Ps):
    M=copy.deepcopy(Ps)
    for i in range(len(M)-1):
        M[i]+=[0]*(len(M[-1])-i-2)
    return M

def writeresults(filename,Ps):
    f=open(filename+".html","w+")
    f.writelines("<link rel=\"stylesheet\" type=\"text/css\" href=\"style.css\">")
    f.writelines("<table>")
    
    for p in Ps:
        l="<tr>"
        for c in p:
            n="<td>"
            if c==Fraction(0):
                n+="0"
            elif c.denominator==1:
                n+=str(c.numerator)
            else:
                n+=str(c.numerator)+"/"+str(c.denominator)
            n+="</td>"
            l+=n
        l=l[:-2]
        l+="</tr>"
        f.writelines(l)
    f.writelines("</table>")
    f.close()

Ps=[[0,1]]
n=70

for m in range(1,n+1):
    A=builtA(m)
    M=builtM(Ps)
    Mp=builtMp(M)    
    Q=mines(A,Mp)
    Qp=times(Q,Fraction(m,m+1))
    P=call(Qp,Ps[-1])
    
    Ps+=[P]

writeresults("res",Ps)