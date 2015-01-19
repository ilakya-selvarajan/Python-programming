class Person:

    def __init__(self,first_name,last_name):
        self.first_name=first_name
        self.last_name=last_name

    def __str__(self):
        return self.first_name+" "+self.last_name




class AddressBook:

    def __init__(self):
        #print "Hi, I'm AddressBook init"
        self.people=[]

    def add(self,person):
        self.people.append(person)

    def lookup(self, last_name):
##        return [person for person in self.people if person.last_name==last_name]
        result=[]
        for person in self.people:
            if person.last_name==last_name:
                result.append(person)
        if result==[]:
            raise ValueError("No such person")
        assert len(result)>0, result
        return result
        
class FAddressBook(AddressBook):
    
    def __init__(self):
        AddressBook.__init__(self)
       # print "Hi, I'm FAddressBook init"
        self.by_last_name={} #{last_name:[Person(),...]}
        self.by_first_name={} #{first_name:[Person()...]}

    def lookup_last_name(self, last_name):
        try:
            return self.by_last_name[last_name]
        except KeyError:
            return None

    def lookup_first_name(self, first_name):
        try:
            return self.by_first_name[first_name]
        except KeyError:
            return None

    def add(self, person):
        if person.last_name in self.by_last_name and person.first_name in self.by_first_name:
                print "Name already exists"
        else:
            try:
                (self.by_last_name[person.last_name]).append(person)
                print person.first_name,person.last_name, "added"
            except KeyError:
                self.by_last_name[person.last_name] = [person]
                print person.first_name,person.last_name, "added"
            try:
                (self.by_first_name[person.first_name]).append(person)
                #print person.first_name,person.last_name, "added"
            except KeyError:
                self.by_first_name[person.first_name] = [person]
                #print person.first_name,person.last_name, "added"

    def remove(self, person):
        if person.last_name in self.by_last_name:
            list1=self.by_last_name[person.last_name]
            for c in list1:
                if c.last_name==person.last_name and c.first_name==person.first_name:
                    index1=list1.index(c)
                    list1.pop(index1)
                    if len(list1)==0:
                        del self.by_last_name[person.last_name]

        if person.first_name in self.by_first_name:
            list2=self.by_first_name[person.first_name]
            for c in list2:
                if c.last_name==person.last_name and c.first_name==person.first_name:
                    index2=list2.index(c)
                    list2.pop(index2)
                if len(list2)==0:
                        del self.by_first_name[person.first_name]
                #index1=list1.index('person.last_name')
                #list2=self.by_first_name[person.first_name]
                #index2=list2.index('person.first_name')
                #print index1
            print person, "deleted"
        else:
            print "Name not found in dictionary"
            
        

    #add lookup by first name

    

a_book=FAddressBook()
a_book.add(Person("Ilakya","RamMohan"))
a_book.add(Person("Ilakya","Selvarajan"))
#print a_book.lookup_first_name("Ilakya")
value='z'
print "Address Book!"
print "Please press 'a' to add name,"
print "Enter 'b' to lookup name"
print "Enter 'c' to delete name"
print "Enter 'e' to exit"
while value!='e':
    value=raw_input("\nPress 'a','b','c' or 'e':")
    if value=='a':
        first_name=raw_input("Enter the first name: ")
        last_name=raw_input("Enter the second name: ")
        first_name=first_name.capitalize()
        last_name=last_name.capitalize()
        a_book.add(Person(first_name,last_name))
        
    if value=='b':
        print "Do you want to search by first or last name?"
        
        value1=raw_input("please type 'first' or 'second': ")
        while value1!='first' and value1!='second':
            value1=raw_input("please type 'first' or 'second':")
        if value1=='first':
            first=raw_input("Enter the first name: ")
            first=first.capitalize()
            try:
                for person in a_book.lookup_first_name(first):
                    print "A name",person, "exists!"
            except  TypeError:
                print "Name not found"
        if value1=='second':
            second=raw_input("Enter the second name: ")
            second=second.capitalize()
            try:
                for person in a_book.lookup_last_name(second):
                    print "A name",person, "exists!"
            except  TypeError:
                print "Name not found"
        
            
    if value=='c':
        first_name=raw_input("Enter the first name:")
        last_name=raw_input("Enter the second name:")
        first_name=first_name.capitalize()
        last_name=last_name.capitalize()
        a_book.remove(Person(first_name, last_name))
    if value=='e':
        break




