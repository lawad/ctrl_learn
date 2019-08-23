class Something:
    def __init__(self):
        self.reset()
        
    def reset(self):
        self.d_1 = {'b': {'c':1, 'd':2}, 'a': 1, 'f': 0}
        self.d_1_orig = {'b': {'c':1, 'd':2}, 'a': 1, 'f': 0}

        self.d_2 = {'b': {'c':10, 'e':20}, 'g':2}

        self.d_expected = {'a':1, 
                 'b': {'c':10, 'd':2, 'e':20}, 
                 'f': 0,
                 'g':2}

    def success(self, f_test):
        self.reset()
        return f_test(self.d_1, self.d_2) == self.d_expected and self.d_1 == self.d_1_orig
    

def f(d_1, d_2):
    for k in d_1:
        if k in d_2:
            if not (isinstance(d_1[k], dict) and isinstance(d_2[k], dict)):
                d_1[k] = d_2[k]
            else:
                f(d_1[k], d_2[k])

    for k in d_2:
        if k not in d_1:
            d_1[k] = d_2[k]
            
    return d_1


def f2(d_1, d_2):
    d_3 = d_1
    f(d_3, d_2)
    return d_3


if __name__=='__main__':
    s = Something()
    print(f"test f result {s.success(f)}")
    print(f"test f2 result {s.success(f2)}")


