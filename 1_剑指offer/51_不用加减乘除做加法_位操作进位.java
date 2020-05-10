class Solution {
    public int add(int a, int b) {
        while(b!=0){
            int c = (a&b)<<1; // 括号必须
            a ^= b;
            b = c;
        }
        return a;
    }
}