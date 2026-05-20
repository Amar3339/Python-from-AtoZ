# implement an exponential backoff stragety that doubles the wait time between retries,starting from 1 sec but stop after 5 tries

import time
wait_time=1
max_retries=5
attempt=0
while attempt<max_retries:
    print("attempt",attempt+1,"wait time",wait_time)
    time.sleep(wait_time)
    wait_time*=2
    attempt+=1
    
    