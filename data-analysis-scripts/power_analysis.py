import statistics as stat

rapl_idle = 12.6
machine_idle = 62.4

source_folder = "/Users/msavasci/Desktop/Courses/Spring23/COMPSCI621/Project_Final_Report/"

dest_folder = "/Users/msavasci/Desktop/Courses/Spring23/COMPSCI621/Project_Final_Report/"

# measurement = "rapl-power-measurements"
measurement = "wall-power-measurements"

tool = "evosuite"

dest_file = f"{dest_folder}{measurement}-{tool}.txt"

files = [f"{source_folder}{measurement}/{tool}/{tool}-AllPathsFromSourceToTarget.csv",
         f"{source_folder}{measurement}/{tool}/{tool}-Anagrams.csv",
         f"{source_folder}{measurement}/{tool}/{tool}-BinaryTree.csv",
         f"{source_folder}{measurement}/{tool}/{tool}-Blowfish.csv",
         f"{source_folder}{measurement}/{tool}/{tool}-CursorLinkedList.csv",
         f"{source_folder}{measurement}/{tool}/{tool}-DES.csv",
         f"{source_folder}{measurement}/{tool}/{tool}-FFT.csv",
         f"{source_folder}{measurement}/{tool}/{tool}-FibonacciHeap.csv",
         f"{source_folder}{measurement}/{tool}/{tool}-HorspoolSearch.csv",
         f"{source_folder}{measurement}/{tool}/{tool}-LeftistHeap.csv",
         f"{source_folder}{measurement}/{tool}/{tool}-LFUCache.csv",
         f"{source_folder}{measurement}/{tool}/{tool}-LRUCache.csv",
         f"{source_folder}{measurement}/{tool}/{tool}-MazeRecursion.csv",
         f"{source_folder}{measurement}/{tool}/{tool}-SinglyLinkedList.csv",
         f"{source_folder}{measurement}/{tool}/{tool}-StrassenMatrixMultiplication.csv"
         ]

total = 0

for f in files:
    with open(f, "r") as file:
        temp_list = file.read().split(",")

    my_data = [float(i) for i in temp_list]

    print("Average of %s: %.2f" %(f.split("-")[3].split(".")[0], stat.mean(my_data)), file=open(dest_file, 'a'))

    total = total + stat.mean(my_data)


print("\nAverage of %s tool: %.2f" %(tool, total/len(files)), file=open(dest_file, 'a'))