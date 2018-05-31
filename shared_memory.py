import multiprocessing 

#child Process
def compute_square(numbers, q):
    
    for  n in numbers:
        q.put(n*n)
    

    
if __name__ == "__main__":

    #The parent first writes into the numbers array  
    numbers = [2,3,5]
    for i in range (0,3):
        print("The Parent Process writes: " , numbers[i])
       
    #creating the share memory queue
    #This kind of queue is found in the shared memory not the process memory
    q = multiprocessing.Queue()
    
    #here we are creating a new process
    p = multiprocessing.Process(target=compute_square, args=(numbers, q))

    p.start()
    p.join() #waiting for the parent process to write
    print()
    print(".............................")
    print()
    while q.empty() is False:
        print("The Parent reads the squared value from child: " , q.get())

