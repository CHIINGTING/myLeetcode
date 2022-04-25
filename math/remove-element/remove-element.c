/*
remove the val in *nums -> put the nums replace the origin *nums
left k nums in *nums 
return k 

*/
int removeElement(int* nums, int numsSize, int val){
    if(numsSize == 0){
        return 0;
    }
    int count = 0;
    for(int index=0;index<numsSize;index++){
        if(nums[index] != val){
            nums[count] = nums[index];
            count += 1;
        }
        
    }
    return count;
}
