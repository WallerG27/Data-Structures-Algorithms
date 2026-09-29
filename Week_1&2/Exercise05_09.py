
#Suppose that the tuition for a university is $10,000 this year and increases 5% every year.
# Write a program that computes the tuition in ten years and the total cost of four years’
# worth of tuition starting ten years from now.

tuition = 10000
count = 1
while count <= 10:
    tuition = tuition * 1.05;
    count += 1
    
print("Tuition in ten years is", tuition)

sum = tuition
for i in range(2, 5):
    tuition = tuition * 1.05
    sum += tuition
    
print("The four-year total tuition in ten years is", sum)
