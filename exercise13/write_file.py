pelican = open("pelican.txt", "a")
pelican.write("A wonderful bird is the pelican")
pelican.write("\nHis bill holds more than his belican")

pelican.writelines(["\nHe can take in his beak,\n", "Enough food for a week,\n", "But I'm damned if I see how the helican.\n"])

pelican.close()
# print(pelican)

pelican = open("pelican.txt", "r")
print(pelican.read())
