__author__ = 'jarvis'

class Permutations:
    def __init__(self, string):
        self.used = [False]*len(string)
        self.out = []
        self.inp = string
        self.hashtable = {0:" " , 1:" ", 2:""}

    def permute(self):
        if(len(self.out) == len(self.inp)):
            print self.out
            return

        for i in range(len(self.inp)):
            if self.used[i] :
                continue

            self.out.append(self.inp[i])
            self.used[i] = True
            self.permute()
            self.used[i] = False
            self.out = self.out[:-1]

    def combine(self):
        num = 1 << len(self.inp)
        for i in range(num):
            temp = i
            out = []
            last = []
            while temp > 0:
                if temp & 1 is 1:
                    out.append(1)
                else:
                    out.append(0)
                temp = temp >> 1
            for j in range(len(out)):
                if out[j] == 1:
                    last.append(self.inp[j])
            print last
obj = Permutations('abc')
obj.combine()





