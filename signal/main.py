from a import A

ser = [A('loop://%d'%(1)) for i in range(3)] 
[s.tx('Your text') for s in ser]
print([s.rx() for s in ser])