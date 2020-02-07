import random

def my_version_of_bogoSort(lijst):

    isnotsorted = True
    while isnotsorted:
        isnotsorted = False

        randomlist = random.sample(range(0, len(lijst)), len(lijst))
        indexnumber = 1
        lijst = [lijst[i] for i in randomlist]  # list wordt willekeurig herordend via de index-nummers van randomlist

        while indexnumber < len(lijst):
            if lijst[indexnumber] < lijst[indexnumber - 1]:
                isnotsorted = True
                break
            indexnumber += 1

    return lijst


lijst = random.sample(range(0, 8), 8)

print('Before sorting: '+str(lijst))
print('After sorting: '+str(my_version_of_bogoSort(lijst)))