class Solution {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<>();
        if(s.length()%2 != 0){
            return false;
        }
        for (char c: s.toCharArray()){
            if (c == '{' || c == '(' || c == '['){
                stack.push(c);
            }
            else{
                if(stack.isEmpty()){
                    return false;
                }
                if(c == ']'){
                    if(stack.peek() == '['){
                        stack.pop();
                    }else {
                        return false;
                    }  
                }
                else if(c == '}'){
                    if(stack.peek() == '{'){
                        stack.pop();
                    }else {
                        return false;
                    }  
                }
                else if(c == ')' ){
                     if(stack.peek() == '('){
                        stack.pop();
                    }else {
                        return false;
                    }  
                }
            }
        }
        if(stack.isEmpty()){
            return true;
        }
        return false;
    }
}
