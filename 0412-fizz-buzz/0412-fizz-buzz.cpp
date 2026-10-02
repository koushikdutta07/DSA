class Solution {
public:
    vector<string> fizzBuzz(int n) {
        vector<string> v(n);
        int in=1;
        for (int i=0;i<v.size();i++){
            if (in%5==0 and in%3==0) v[i]="FizzBuzz";
            else if (in%5==0) v[i]="Buzz";
            else if (in%3==0) v[i]="Fizz";
            else v[i]=to_string(in);
            in++;
        }
        return v;
    }
};