#%%
text = """
One really nice feature of Python is polymorphism: using the same operation
on different types of objects.
Let's talk about an elegant feature: slicing.
You can use this on a string as well as a list for example
'pybites'[0:2] gives 'py'.
 The first value is inclusive and the last one is exclusive so
here we grab indexes 0 and 1, the letter p and y.
  When you have a 0 index you can leave it out so can write this as 'pybites'[:2]
but here is the kicker: you can use this on a list too!
['pybites', 'teaches', 'you', 'Python'][-2:] would gives ['you', 'Python']
and now you know about slicing from the end as well :)
keep enjoying our bites!
"""

#%%
def slice_and_dice_lc(text):
    results = [line.split()[-1].rstrip('!.') 
               for line in text.strip().splitlines() 
               if line.lstrip()[0].islower()]
    return results

%timeit slice_and_dice_lc(text)

#%%
def slice_and_dice(text):
    results = []
    for line in text.strip().splitlines():
        line = line.lstrip()
        if line[0].islower():
            words = line.split()[-1].rstrip('!.')
            results.append(words)
    return results

%timeit slice_and_dice(text)

