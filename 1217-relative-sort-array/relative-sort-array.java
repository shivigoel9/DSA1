class Solution {
    public int[] relativeSortArray(int[] arr1, int[] arr2) {
        int[] freq = new int[1001];
        for(int num: arr1)
            freq[num]++;
        int idx = 0;
        for(int num: arr2) {
            while(freq[num] > 0) {
                arr1[idx++] = num;
                freq[num]--;
            }
        }
        for(int i=0; i<1001 && idx < arr1.length; i++){
            while(freq[i] > 0){
                arr1[idx++] = i;
                freq[i]--;
            }
        }
        return arr1;
        
    }
}