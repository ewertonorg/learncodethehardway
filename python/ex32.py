the_count = [1, 2, 3, 4, 5]
fruits = ['apples','oranges','pears','apricots']
change = [1,'pennies',2 ,'dimes',3,'quartes']

#this first kind of for-loop goes through a list
for number in the_count:
    print "This is count %d" % number

#same above    
for fruit in fruits:
    print "A fruit of types: %s" % fruit

#also we can go through mixed lists too
#notice we have to use %r since we don't know what's in it
for i in change:
	print "I got %r" % i

#we can also build lists first start with an empty one
elements = []

#then use range function to do 0 to 5 counts
for i in range(0, 6):
    print "Adding %d to the list." % i
    elements.append(i)


#now we can print them out too
for i in elements:
    print "Elment was: %d" % i    	
