with open("output.txt", "r", encoding='utf-8') as file:
    for line in file:
        pass
# I'd love to sum all total words in output.txt file because server kicks me out after +- 1000 (can't blame them) joined urls, but I cant
#find the right way to isolate numbers from the file and sum them.
#I thought the code for this would be somewhat like this, I tried a lot of options but still can't isolate the numbers

#edit 
  #the code below returned only numbers, I still have to figure out how to sum them

with open("output.txt", "r", encoding='utf-8') as file:
    for line in file:
        words = line.find("total words")
        if words == 0:
            num = line.split(": ")[1]
            print(num.strip())
            
           
        
#edit2
  # i figured it out!
    with open("output.txt", "r", encoding='utf-8') as file:
    output = []
    for line in file:
        words = line.find("total words")
        if words == 0:
            num = line.split(": ")[1]
            x = num.strip()
            output.append(x)


str(sum(int(num)for num in output))

print(output)
print("Total is: " + str(sum(int(num)for num in output)) + '.')
#result
  #['2', '1', '49']
  #Total is: 52
#
    
