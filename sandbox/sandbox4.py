


class Server:
    links_count = -1
    def __init__(self, x, y, num):
        self.__class__.links_count += 1
        self.num = num
        self.x = x
        self.y = y
        self.closest_server = None
        self.links = set()

    def get_way(self, server):
        return (self.x - server.x)**2 + (self.y - server.y)**2
    
    def find_closest_server(self, servers):


        if servers:
            smallest = self.get_way(servers[-1])
            self.closest_server = servers[-1]  
            self.closest_server.links.add(self) 
            #servers = servers.copy()
            for i in servers:
                if i is not self and self.__class__.links_count:
                    if self.get_way(i) < smallest:
                        smallest = self.get_way(i)
                        self.closest_server.links.discard(self)
                        
                        if self.closest_server.closest_server is not self:
                            self.closest_server = i
                            self.closest_server.links.add(self) 
                        servers.remove(i)

    def __repr__(self):
        if self.closest_server:
            return f"s {self.num} - > s {self.closest_server.num}"
        return ''
    

class PC:
    def __init__(self, x, y, num):
        self.num = num
        self.x = x
        self.y = y
        self.closest_server = None

    def get_way(self, server):
        return (self.x - server.x)**2 + (self.y - server.y)**2

    def find_closest_server(self, servers):
        smallest = self.get_way(servers[-1])
        self.closest_server = servers[-1]  
        self.closest_server.links.add(self) 
        
        for i in servers:
            if i is not self:
                if self.get_way(i) < smallest:
                    smallest = self.get_way(i)
                    self.closest_server.links.discard(self)
                    self.closest_server = i    
                    self.closest_server.links.add(self) 
                    
    
    def __repr__(self):
        return f"s {self.closest_server.num} - > c {self.num}"

pcs_list = []
servs_list = []

pcs, servs = [int(i) for i in input().split()]
for i in range(pcs):
    pcs_list.append(PC(*[int(j) for j in input().split()], i+1))

for i in range(servs):
    servs_list.append(Server(*[int(j) for j in input().split()], i+1))

for i in pcs_list:
    i.find_closest_server(servs_list)

for i in sorted(servs_list, key = lambda x: len(x.links))[:-1]:
    i.find_closest_server(list(filter(lambda x: x is not i, servs_list)))


links_count = sum(list(map(lambda x: len(x.links), servs_list)))

ways_long = 0
for i in servs_list:
    ways_long += sum(map(lambda x: x.get_way(x.closest_server), i.links))


print(links_count, ways_long, end = '')
print('\n'.join(repr(i) for i in servs_list))
print('\n'.join(repr(i) for i in pcs_list))



    