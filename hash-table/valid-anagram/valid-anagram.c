#define CHAR_SET_SIZE ('z' - 'a' + 1)
bool isAnagram(char * s, char * t){
    if (strlen(s) != strlen(t)) { return false; }
    int check[CHAR_SET_SIZE];
    memset(check, 0, sizeof(check));
    while(*s){
        check[ *(s++) - 'a'] +=1;
    }
    while(*t){
        check[ *(t++) - 'a'] -=1;
    }
    for(int i = 0; i<26;i++){
        if(check[i]!=0){
            return false;
        }
    }
    return true;
}