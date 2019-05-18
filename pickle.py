import pickle
import keyword
data={'pos':[100,200], 'pockets' :['keys', 'knife', 'gun', 'stone'], 'items' : ['rope', 'hammer', 'food', 'house', 'estate', 'guard', 'fence', 'cabinet', 'bed', 'zoo', 'farm', 'computer', 'ball', 'kids']}
def save():
    save_file=open('save.dat', 'wb')
    pickle.dump(data, save_file)
    save_file.close()
    for i in data:
        print(data[i])
save()
print(data)
print(keyword.kwlist)
