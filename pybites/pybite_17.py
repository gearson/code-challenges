# Write a function called friends_teams that takes a list of friends, a team_size 
# (type int, default=2) and order_does_matter (type bool, default False).

# Return all possible teams. Hint: if order matters (order_does_matter=True), 
# the number of teams would be greater.

#%%
import itertools
from itertools import permutations, combinations

friends = 'Deniz Rebecca Sieglinde Max Kirry Rob Fanny Hao Lisa David Leslie'.split()

def friends_teams(friends, team_size=2, order_does_matter=True):
    if order_does_matter==True:
        teams = list(combinations(friends, team_size))
        print(teams)
    else:
        teams = list(permutations(friends, team_size))
        print(teams)

if __name__ == '__main__':
    friends_teams(friends)

#%%
# pybite solutions
def friends_teams(friends, team_size=2, order_does_matter=False):
    if order_does_matter:
        func = itertools.permutations
    else:
        func = itertools.combinations
    return func(friends, team_size)

list(friends_teams(friends))

#%%
