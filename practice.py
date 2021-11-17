class Countries:
    num_of_countries = 0
    pop_rate = 2
    def __init__(self, name, leader, pop, size):
        self.name = name
        self.leader = leader
        self.pop = pop
        self.size = size
        Countries.num_of_countries += 1

    def pop_incr(self):
        self.pop = int(self.pop *self.pop_rate)  
        

        
country1 = Countries("Nigeria", "muhammadu", 400,374)
country2 = Countries("Barbados", "Kante", 200, 648)
country3 = Countries("Ghana", "Kennedy", 45557,74)
country4 = Countries("Fiji", "Ernest", 111,112)

print(Countries.num_of_countries)
print(country4.leader)
print(country2.pop_incr())
