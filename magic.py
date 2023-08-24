class employee:
    name = "Karan"
    def __len__(s):
            i = 0
            for c in s.name:
                i += 1
            return i
    
    def __str__(s):       #execute 1st
         return f"The name of the employee is {s.name} str"
    
    def __repr__(s):      #execute if str is not initialized
         return f"The name of the employee is {s.name} repr"
    
    def __call__(s):
         print("hey i am karan")