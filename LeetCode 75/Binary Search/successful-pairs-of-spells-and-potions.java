class Solution {
    public int[] successfulPairs(int[] spells, int[] potions, long success) {
        Arrays.sort(potions);
        int n = spells.length;
        int m = potions.length;
        int[] cars = new int[n];
        for(int i = 0; i < n; i++){
            int spell = spells[i];
            int min_ran = 0;
            int max_ran = m - 1;
            while(min_ran <= max_ran){
                int mid = max_ran + (min_ran - max_ran) / 2;
                long product = (long) spell * potions[mid];
                if (product < success) min_ran = mid + 1;
                else max_ran = mid - 1;
            } 
            cars[i] = m - min_ran;
        }        
        return cars;
    }
}