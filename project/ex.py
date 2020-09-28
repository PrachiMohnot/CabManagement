import pickle as p
file=open('dealer.txt','wb')
dict={}
p.dump(dict,file)
file.close()