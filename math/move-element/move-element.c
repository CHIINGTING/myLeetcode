void moveZeroes(int* nums, int numsSize){
    int zeroProsition = 0;
    for(uint32_t nunZeroProsition=0; nunZeroProsition<numsSize;nunZeroProsition++){
        if(nums[nunZeroProsition] != 0){
            nums[zeroProsition] = nums[nunZeroProsition];
            zeroProsition++;
        }
    }
    for(uint32_t zeroNumber=zeroProsition;zeroNumber<numsSize;zeroNumber++){
        nums[zeroNumber] = 0;
    }
}
//O(N)