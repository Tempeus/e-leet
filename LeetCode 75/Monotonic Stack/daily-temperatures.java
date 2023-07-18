class Solution {
    public int[] dailyTemperatures(int[] temperatures) {
            int[] answer = new int[temperatures.length];
            Stack<Integer> monoTONIC = new Stack<Integer>();

            for(int i = temperatures.length -1; i >= 0; i--){
                while(!monoTONIC.isEmpty() && temperatures[monoTONIC.peek()] <= temperatures[i]){
                    monoTONIC.pop();
                }
                if(monoTONIC.isEmpty()){
                    monoTONIC.push(i);
                    answer[i] = 0;
                }
                else{
                    int previous = monoTONIC.peek();
                    monoTONIC.push(i);
                    answer[i] = previous - i;
                }
            }
            return answer;
        }
}