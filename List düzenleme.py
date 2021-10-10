def make_list_flat (l):
    flist = []
    flist.extend ([l]) if (type (l) is not list) else [flist.extend (make_list_flat (e)) for e in l]
    return flist

lst = [[1, 'a', ['cat'], 2], [[[3]], 'dog'], 4, 5]
flist = make_list_flat(lst)
flist.reverse()
print(flist)