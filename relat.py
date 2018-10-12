from datetime import datetime

class nonRelatNode(Exception):
    def __init__(self,message):
        super().__init__()
        self.expression = "nonRelatNode"
        self.message = "The nodes you are trying to relate are not relatNode."

class fileModified(Exception):
    def __init__(self,message):
        super().__init__()
        self.expression = "File Error"
        self.message = "File has been modified therefore non-readable."

class relatNode():
    """ This is a class to represent choice makers."""
    def __init__(self,name,color):
        self.name = name
        self.color = color

    def me():
        q = "N{0}({1})N".format(self.name,self.color)


class relat():
    """This is a class to represent relationships between choice makers."""
    def __init__(self,first,second,color,weigth):
        if type(first).__name__ == "relatNode" and type(second).__name__ == "relatNode":
            raise nonRelatNode()
        self.first = first
        self.second = second
        self.weigth = weigth
        self.color = color

    def me():
        q = "R{0}-{4}({5})->{1}R".format(self.first.name,self.second.name,self.weigth,self.color)
        return q

class fileManager():
    """This class is for managing files and parsing them"""
    def __init__(self):
        self.saveThis = "!!DO NOT MODIFY THIS FILE (Created by ReLaT)!!"

    def __savePrep(*k):
        self.saveThis += [str(datetime.today()) + " " + str(datetime.time(datetime.now()))]
        for i in k:
            self.saveThis += [i.me()]
        return "\n".join(self.saveThis)

    def __postOpen(x):
        x = x.split('\n')[1:-1]
        time  = x[0]
        lisOfObjects = []
        for i in x:
            if i[0] == 'N':
                i = i[1:-1]
                i = i.split('(')
                i[1] = i[1].replace(")",'')
                n = relatNode(i[0],i[1])
                lisOfObjects += [n]
            elif i[0] == 'R':
                i = i[1:-1]
                i = i.split("(")
                firstName = i[0].split("-")[0]
                weigth = i[0].split("-")[1]
                color = i[1].split(")->")[0]
                secondName = i[1].split(")->")[1]
                r = relat(firstName,secondName,color,weigth)
                lisOfObjects += [r]
            else:
                raise fileModified
        return listOfObjects


    def save(listOfNodeOrRelats, fName):
        toSave = self.__savePrep(listOfNodeOrRelats)
        file = open(fName,'w+')
        file.write(toSave)
        file.close()
        return True

    def open(fName):
        data = open(fName,'r+').read()
        return self.__postOpen(data)
