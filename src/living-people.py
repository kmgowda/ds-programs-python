import random

MIN = 1900
MAX = 2015

class person:
    def __init__(self, birth, death):
        self.birth = birth
        self.death = death
    
    def get_birth(self):
        return self.birth
    
    def get_death(self):
        return self.death 
 
def get_population_delta(people):
    population = [0]*(MAX-MIN+2)
    for p in people:
        birth = p.get_birth()-MIN
        population[birth]+=1
        
        death = p.get_death()-MIN
        population[death+1]-=1
    return population

def get_maxalive(population):
    currentlylive = 0
    maxlive = 0
    year = 0
    index = 0
    for item in population:
        currentlylive += item
        if currentlylive > maxlive:
            maxlive = currentlylive
            year = index
        index+=1
    return maxlive, MIN+year

def add_people(N):
    people= list()
    for i in range(N):
        birth = random.randint(MIN,MAX-1)
        death = random.randint(birth,MAX)
        people.append(person(birth,death))
    return people    

def print_people(people):
    print("Details of people")
    index = 1
    for p in people:
        print("person %d:  birth:%d   death %d " %(index,p.get_birth(), p.get_death()))
        index+=1

if __name__=="__main__":
    print("Python program to list the year in which maximum people lived")
    N =int(input("How many people?"))
    people = add_people(N)
    population = get_population_delta(people)
    maxlive, year =  get_maxalive(population)
    print_people(people)     
    print("The maximum people %d lived in the year %d" %(maxlive, year))  
        
               