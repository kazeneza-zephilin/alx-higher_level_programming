import sys
#import calculator_1
#including file path in pythonpath
path = sys.path.append("~/Downloads/hidden_4.pyc")
module_names = dir(path)
filted_names = sorted([name for name in module_names if not name.startswith("__")])

for name in filted_names:
    print(name)
    
    

