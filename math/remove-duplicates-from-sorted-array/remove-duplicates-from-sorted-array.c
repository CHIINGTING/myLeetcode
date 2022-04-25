/*
1. replace problem -> copy back to origin
2. use map -> check["map number"] if match: ture->false
3. return the match count
*/
int removeDuplicates(int* nums, int numsSize){
    if(numsSize==0){
        return 0;
    }
    int count = 0;
    bool check[202];
    for(int i=0;i<202;i++){
        check[i] = true;
    }
    for(int index = 0; index< numsSize;index++){
        if(check[nums[index]+100]){
            check[nums[index]+100] = false;
            nums[count] = nums[index]; 
            count++;
        }
    }
    return count;
}
