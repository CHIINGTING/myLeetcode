typedef struct { int key; int intersect; UT_hash_handle hh; } Map;

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* twoSum(int* nums, int numsSize, int target, int* returnSize){
    *returnSize = 2;
    Map *map = NULL, *elem, *tmp;
    int *result = malloc(2 * sizeof(int));
    // numsSize
    for (int i = 0; i < numsSize; i++) {
        elem = malloc(sizeof(Map));
        elem->key = nums[i];
        elem->intersect = i;
        HASH_ADD_INT(map, key, elem);
    }
    int *test = malloc(sizeof(int));
    //find value
    for (int i = 0; i < numsSize; i++) {
        elem = NULL;
        *test = target - nums[i];
        HASH_FIND_INT(map, test, elem);
        if (elem) {
            if(i == elem->intersect){
                continue;
            }
            else{
                result[0] = i;
                result[1] = elem->intersect;
                return result;
            }
        }
    }
    return NULL;
}