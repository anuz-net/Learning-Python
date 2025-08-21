word_list = ['crab', 'grab', 'bathtub' 'ant']
new_list=[]

for word in word_list:
    if len(word)<5 and word[-1]=='b':
        new_list.append(word)
        
new_list.sort(reverse=True)
print(new_list)
