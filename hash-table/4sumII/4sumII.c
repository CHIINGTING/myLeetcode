typedef struct { int key; int value; UT_hash_handle hh; } Map;

int fourSumCount(int* nums1, int nums1Size, int* nums2, int nums2Size, int* nums3, int nums3Size, int* nums4, int nums4Size){
    Map *map = NULL,*elem;
    for(int i=0;i<nums1Size;i++){
        for(int j=0;j<nums2Size;j++){
            int iKey = nums1[i] + nums2[j];
            HASH_FIND_INT(map, &iKey, elem);
            if(elem == NULL){
                elem = malloc(sizeof(Map));
                elem->key = iKey;
                elem->value = 1;
                HASH_ADD_INT(map, key, elem);
            }
            else{
                elem->value++;
            }
        }
    }
    int answer=0;
    for(int i=0;i<nums3Size;i++){
        for(int j=0;j<nums4Size;j++){
            int iKey = (-1)*(nums3[i] + nums4[j]);
            HASH_FIND_INT(map, &iKey, elem);
            if(elem){
                answer += elem->value;
            }
        }
    }
    return answer;
}
  