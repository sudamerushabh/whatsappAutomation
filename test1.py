

test_file = open("test.txt", "r+")
num_lines = sum(1 for line in open("test.txt"))
testObj = []

print(num_lines)

for i in range(1, num_lines+1):
    testObj.append(test_file.readlines(i))

print(testObj)

testObj1 = []
for i in range(0, len(testObj)):
    testObj1.append(testObj[i][0])

t = list(map(lambda s: s.strip(), testObj1))

print(t)
test_file.close()
