class Solution {
    public int evalRPN(String[] tokens) {
        int result = 0;
        Stack<Integer> stack = new Stack<>();
        for(String s: tokens){
            System.out.println(s);
            if(s.equals("+")){
                stack.push(stack.pop()+stack.pop());
            }
            else if(s.equals("-")){
                int a = stack.pop();
                int b = stack.pop();
                stack.push(b-a);
            }
            else if(s.equals("*")){
                stack.push(stack.pop()*stack.pop());
            }
            else if(s.equals("/")){
                int a = stack.pop();
                int b = stack.pop();
                stack.push(b/a);
            }
            else{
                stack.push(Integer.parseInt(s));
            }
        }
        return stack.pop();
        
    }
}

/*

1
2

*/