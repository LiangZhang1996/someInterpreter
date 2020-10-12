
# returns True if, and only if, string s is a valid variable name
def is_atom(s):
    if not isinstance(s, str):
        return False
    if s == "":
        return False
    return is_letter(s[0]) and all(is_letter(c) or c.isdigit() for c in s[1:])

def is_letter(s):
    return len(s) == 1 and s.lower() in "_abcdefghijklmnopqrstuvwxyz"

def is_valid_kb(head):
    '''
    head = []
    atoms = []
    for d in data:
        s = d.split(' ')
        s[-1] = s[-1].split('\n')[0]
        head.append(s[0])
        atoms.append([j for j in s[1:] if j!='<--' and j!='&'])
    '''
    # read the head
    k = len(head)
    num = 0
    for i in range(k-1):
        if head[i] in head[i+1:]:
            num += 1
    if num == 0:
        return True
    else:
        return False


def load(fname):
    data1 = []
    sdata = str()
    with open(fname, 'r') as f:
        data = f.readlines()
    
    for d in data:
        if d == '\n':
            pass
        else:
            data1.append(d)
            sdata += '   '+d
    # get head and atoms 
    head = []
    atoms = []
    for d in data1:
        s = d.split(' ')
        s[-1] = s[-1].split('\n')[0]
        head.append(s[0])
        atoms.append([j for j in s[1:] if j!='<--' and j!='&'])
    # is valid kb
    if is_valid_kb(head):
        print(sdata)
        print('\n   %s new rule(s) added' % len(data1))
    else:
        print('Error: %s is not a valid knowledge base' % fname)
    
    return data1, head, atoms


def tell(atoms, meomory):
    key =  True
    if atoms == []:
        key = False
        print('Error: tell needs at least one atom')
    else :
        for at in atoms:
            if not is_atom(at):
                print('Error: "%s" is not a valid atom' % at)
                key = False
                break
    if key:
        if meomory != []:
            for at in atoms:
                if at in meomory:
                    print('   atom "%s" already known to be true' %at)
                else:
                    meomory.append(at)
                    print('   "%s" added to KB' %at)
        else:
            for at in atoms:
                meomory.append(at)
                print('   "%s" added to KB' %at)

    return meomory

def infer_all(head_meomory, head_atoms_meomory, meomory, Nmeomory):
    # get the known part

    for at in meomory:
        for ham in head_atoms_meomory:
            for k in ham:
                if at in k and at not in Nmeomory['known']:
                    Nmeomory['known'].append(at)
    
    for i in Nmeomory['inferred']:
        if i not in Nmeomory['known']:
            Nmeomory['known'].append(i)
    Nmeomory['inferred'] = []

    # get the inferred part
    for ss in range(3):
        for l in range(len(head_atoms_meomory)):
            ham = head_atoms_meomory[l]
            key = len(ham)
            num = [0 for i in range(key)] 

            for i in range(key):
                for at in ham[i]:
                    if at in Nmeomory['known'] or at in Nmeomory['inferred']:
                        num[i]+=1
        
                if num[i]==len(ham[i]) and head_meomory[l][i] not in Nmeomory['known'] and  head_meomory[l][i] not in Nmeomory['inferred']:
                    Nmeomory['inferred'].append(head_meomory[l][i])


    if Nmeomory['inferred']==[]:
        print('  Newly infered atoms:')
        print('\t<none>')
    else:
        print('  Newly infered atoms:')
        slist = str()
        for i in Nmeomory['inferred']:
            slist += i+', ' 
        slist = slist.strip(', ')
        print('\t',slist)
    
    if Nmeomory['known']==[]:
        print('  Atoms already known to be true:')
        print('\t<none>')
    else:
        print('  Atoms already known to be true:')
        slist = str()
        for i in Nmeomory['known']:            
            slist += i+', ' 
        slist = slist.strip(', ')
        print('\t',slist)


def myInterpreter():
    meomory = []
    Nmeomory = {'inferred':[],'known':[]}
    head_meomory = []
    head_atoms_meomory = []
    commads = {'load':load,'tell':tell,'infer_all':infer_all}
    while True:
        In = input('kb>')
        In = In.split(' ')
        In = [s for s in In if s!='']
        if In[0] not in commads.keys():
            print('Error: unknown command "%s"' %In[0] )
        else:
            if In[0]=='load':
                _, head, atoms = load(In[1])
                head_meomory.append(head)
                head_atoms_meomory.append(atoms)

            if In[0]=='tell':
                meomory = tell(In[1:], meomory)
            if In[0]=='infer_all':
                infer_all(head_meomory, head_atoms_meomory, meomory, Nmeomory)


if __name__ == '__main__':
    myInterpreter()
