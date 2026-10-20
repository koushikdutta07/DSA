class Solution {
public:
    int countDigits(int num) {
        int temp=num;
        int output=0;
        while(temp>0){
            int digit = temp%10;
            if (num%digit==0) {
                output++;
            }
            temp=temp/10;
        }
        return output++;
    }
};