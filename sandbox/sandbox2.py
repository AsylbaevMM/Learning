


class Repo():
    def __init__(self,number, parent = None):
        self.number = number
        self.parent = parent
        self.childs = []
        self.childs_count = 0
        if parent is not None:
            parent.childs.append(self)
            self.parent.add_child()

    def find_longer(self):
        if self.childs:
            max(self.childs, key = lambda x: x.childs_count).find_longer()
        else:
            print(self.number)

    def add_child(self):
        self.childs_count += 1
        if self.parent is not None:
            self.parent.add_child()
    
repos = [Repo(0)]

for i in range(int(input())):
    repos.append(Repo(i+1, repos[int(input())]))

repos[0].find_longer()