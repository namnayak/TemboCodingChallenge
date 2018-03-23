# Without changing the provided lists and dictionaries, create a script that cycles
# through all the parents and prints to the terminal the proper activities for
# their child's age group. When there are no more activities for that parent,
# print "curriculum complete!" and move on to the next parent.
#
# (Make sure your script accounts for any edge cases in the provided variables!)

#Full name of parent required
#If child name is provided bt not age, then prints age of child not provided in the list
#Given the constraint on data type and data set, i have assumed that duplicate entry for parents list can exist. for more accurate information a id key must be present in the data type to identify the person uniquely since name and age can't be uniquely
#Since there is a possibility that a parent has more than 1 child, there will be more than one entry for the same parent in the parents list, which will be considered as a different element since we have any id or key to validate if the duplicate parent entry corresponds to the same person
#Conditions to handle input having empty activities or multiple comma seperated values included

import datetime

parents = [
    {'parent': 'Henry', 'child': {'name': 'Calvin', 'age': 2}},
    {'parent': 'Ada', 'child': {'name': 'Lily', 'age': 3}},
    {'parent': 'Emilia', 'child': {'name': 'Petra', 'age': 1}},
    {'parent': 'Biff', 'child': {'name': 'Biff Jr', 'age': 4}},
    {'parent': 'Milo', 'child': {}}
]

curriculum = [
    {
        'age': 1,
        'activity': [
            'Try singing a song together.',
            'Point and name objects.'
            ]
    },
    {
        'age': 2,
        'activity': [
            'Go outside and feel surfaces.',
            'Draw with crayons.',
            'Play with soundmaking toys or instruments.',
            'Look at family pictures together.'
            ]
    },
    {
        'age': 3,
        'activity': [
            'Build with blocks.',
            'Try a simple puzzle.',
            'Read a story together.'
            ]
    }
]

# Want to really shine and show us your chops?  Work in some of these stretch
# goals using any tools or libraries you see fit.
# - Personalize the message output to make it more friendly.
# - Allow users to input new activities & parents before executing the script.
# - Print one activity at a time per parent and continue cycling through until
#   all parents have recieved all their activities.

def getInfo():
    noinfo = ''
    info = ''
    download = raw_input("Do you want to save the results in a file for future references?(Y/N)")
    for parent in parents:
        try:
            pname = parent['parent']
            if pname:
                cobj = parent['child']
                if cobj:
                    cname = ''
                    if 'name' in cobj.keys():
                        cname = ' ' + cobj['name']
                    try:
                        if cobj['age']:
                            cage = cobj['age']
                            flag = 0
                            for curr in curriculum:
                                if curr['age'] == cage:
                                    if curr['activity']:
                                        activity = curr['activity']
                                        info+= 'Hello {0}, you have the following activities for your child{1} aged {2}:\n'.format(pname, cname, cage)
                                        for c in range(len(activity)):
                                            info+= '{0}. {1}\n'.format(c+1,activity[c])
                                        info+= "Curriculum Complete!\n"
                                        flag = 1
                                        break
                        else:
                            noinfo += 'Hello {0}, age of your child is not provided in the list.\n'.format(pname)
                    except:
                        noinfo += 'Hello {0}, age of your child is not provided in the list.\n'.format(pname)
                else:
                    noinfo += 'Hello {0}, there are no activities for you as you do not have a child listed.\n'.format(pname)
                    flag = 1
                if not flag:
                    noinfo += 'Hello {0}, there are no activities for your child{1} aged {2}.\n'.format(pname, cname, cage)
        except:
            pass
    print info
    print noinfo
    if 'y' in download.lower():
        filename = 'Results_' + str(datetime.datetime.now().strftime("%Y%m%d%H%M%S")) + '.txt'
        f = open(filename, 'w+')
        f.write(info)
        f.write(noinfo)
        f.close()
        print 'Result saved in file', filename


def inputData():
    parent = raw_input("Do you want to enter parent and child information?Y/N")
    while 'y' in parent.lower():
        p = raw_input("Enter parent full name:")
        c = raw_input("Enter child full name:")
        a = raw_input("Enter child age:")
        dict = {}
        if c:
            dict['name'] = c
        if a.isdigit() and a>0:
            dict['age'] = int(a)
        if p:
            parents.append({'parent':p, 'child':dict})
        parent = raw_input("Do you want to enter any more parent and child information?Y/N")

    act = raw_input("Do you want to enter curriculum?Y/N")
    while 'y' in act.lower():
        a = raw_input("Enter curriculum age group:")
        cur = raw_input("Enter one or more curriculum seperated by comma:")
        flag = 0
        cur = cur.split(',')
        activities = []
        for c in cur:
            if c:
                activities.append(c)
        if activities and a.isdigit() and a>0:
            for c in curriculum:
                if c['age'] == int(a):
                    c['activity'].extend(activities)
                    flag = 1
                    break
            if not flag:
                curriculum.append({'age':int(a), 'activity':activities})
        act = raw_input("Do you want to enter any more curriculum information?Y/N")

if __name__ == '__main__':
    input_var = raw_input("Do you want to enter any information?Y/N")
    if 'y' in input_var.lower():
        inputData()
    getInfo()
