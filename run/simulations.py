import pandas as pd
import os
import glob
import time

print("Remember to delete results folder and enable noise! Also note: you may reach your results faster to run multiple tabs of this script")
print("")
runs = int(input("How many simulations would you like to run? "))

start = time.time()

for i in range(runs):
    print('Run no: ' + str(i))
    os.system('python solve_regular.py')

end = time.time()

print()
print(f"Total time taken is {(end - start) / 60:.2f} minutes")
