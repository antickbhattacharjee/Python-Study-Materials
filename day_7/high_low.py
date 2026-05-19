myp={'a':(4,3),'b':(1,2),'c':(5,1)}
high=[0,0]
init=0
for a in range(2):
    init=0
    for b in myp.keys():
        val=myp[b][a]
        if init==0:
            high[a]=val
            init=1
        elif val>high[a]:
            high[a]=val
            
    print("Max at index(myp,",a,")=",high[a])