def find_most_occ_char(input): 
   
    wc = Counter(input) 
  
    s = max(wc.values()) 
    i = wc.values()
      
    print wc.items()[i] 
    
if __name__ == "__main__": 
    input = 'geeksforgeeks'
    find_most_occ_char(input) 
