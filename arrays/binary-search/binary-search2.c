int search(int* nums, int numsSize, int target){
    int low = 0;
    int high = numsSize;
    
    while(low < high){
        int index = low+(high - low)/2;
        if(*(nums+index)<target){
            low = index+1;
        }
        else if(*(nums+index)>target){
            high = index;
        }
        else
            return index;
    }
    
    return -1;
}

