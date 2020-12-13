import sys

#set open filename as f
f = open("TAinput_Review.txt")
#set reading line as lines
lines = f.readlines()



#make array on the list.
array = []

#make sum, mean, median as 0
sum = 0
mean = 0
median = 0

#make for loop for the split the each lines of files.
for i in lines:
    a = map(float, i.split())
    array+=a

#make nums for list of length of array
nums = array[1:len(array)]

#make sum
for i in nums:
    sum+=i
sum = "%0.2f" % round(sum,2)
#f is for the decimal point
#round is for rounds

#make mean
mean = float(sum)/array[0]
mean = "%0.2f" % round(mean,3)

#make median
length = len(nums)
nums = sorted(nums)

if length%2 != 0:
    median = nums[int(length/2)]
else:
    median = (nums[int(length/2)-1] + nums[int(length/2)])/2
median = "%0.2f" % round(median,2)

print("Sum: "+str(sum))
print("Mean: "+str(mean))
print("Median: " + str(median))

#close the python file
f.close()