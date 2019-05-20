from dynimport import dimport

ttt = dimport("takethetime@pypi")

with ttt("Time this!"):
    print("Hello world!")
