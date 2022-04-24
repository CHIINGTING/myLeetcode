char * longestCommonPrefix(char ** strs, int strsSize){
    int min = strlen(strs[0]);
    for (int i = 1; i < strsSize; ++i) {
        min = strlen(strs[i]) < min ? strlen(strs[i]) : min;
    }
    char* subtext = malloc((min+1) * sizeof(char));
    if(strsSize == 0) return ""; 
    else{
        for(int i=0; ; i++)
        {
            for(int j=0;j<strsSize;j++)
            {
                if(i >= strlen(strs[j]) || strs[j][i] != strs[0][i]) {
                    strs[0][i] = '\0';
                    strcpy(subtext, strs[0]);
                    return subtext;
                }
            }
        }
    }
}
