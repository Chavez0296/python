import math

num = 9;
fullName = "Luis Chavez";
print(math.sqrt(num));
print(fullName);
print(fullName.index("L"));
hello = "Hello";
world =  "World";
print(hello,world, sep="-");
print(hello,world,end="!\n");
print(fullName);

#string formatting

price = 10;
item = "chips";
print("The %s costs %d dollars." % (item,price));

itemDict = {"item": "chips", "cost": 4};
print("The %(item)s costs %(cost)3.2f dollars" % itemDict); 
