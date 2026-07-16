import thinker as tk
def calculater():
    try:
        result = eval(entry.get)
        entry.delete(0, tk.END )
        entry.insert(tk.END, str(result))
    except:
        entry.delete(0, tk.END)   
        entry.insert(0, "Error") 

root = tk.TK()
root.title("Calc")   
     
entry = tk.Entry(root, width=20, font=('Arial', 18) )   
entry.pack() 

btnc=["1","2","3","+","4","5","6","7","8","9","*","C","0","=","/"]
frame= tk.frame(root)
frame.pack()

for i,b in enumerate(btns):
    cmd=lambda x=b:(entry.delete(0, tk.END) if x=='C' else (calculate() if x=='=' else entry.insert(tk.END, x)))
    tk.Button(frame, text=b, width=5, command=cmd).grid(row=i//4, column=i%4)

root.mainloop()    

