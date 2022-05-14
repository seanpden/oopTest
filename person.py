class Person:
    '''
    A class that has an ID, features, and label.
    '''

    def __init__(self, id, feature, label):
        self.id = id
        self.feature = feature
        self.label = label

    def getall(self):
        '''
        get all attributes
        '''
        print(self.id, self.feature, self.label)
        return self.id, self.feature, self.label

    def getid(self):
        '''
        get ID
        '''
        print(self.id)
        return self.id

    def setid(self, id):
        '''
        set ID value
        '''
        self.id = id

    def getfeature(self):
        '''
        get features
        '''
        print(self.feature)
        return self.feature

    def setfeature(self, feature):
        '''
        set feature value
        '''
        self.feature = feature

    def getlabel(self):
        '''
        get label
        '''
        print(self.label)
        return self.label

    def setlabel(self, label):
        '''
        set label value
        '''
        self.label = label

    def gethardcodePersons(self, n):
        '''
        Initialises a group array, fills it with 'n' persons. \n
        Prints each person
        '''
        group = []
        for i in range(0, n):
            foo = Person("", "", "")
            foo.id = ("id %d" % i)
            foo.feature = ("feature %d" % i)
            foo.label = ("label %d" % i)
            group.append(foo)
        for i in range(0, n):
            group[i].getall()
        return group