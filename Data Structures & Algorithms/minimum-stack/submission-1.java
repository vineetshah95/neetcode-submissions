class MinStack {
    
    Stack<Integer> mainStack;
    Stack<Integer> minStack;
    public MinStack() {
        mainStack = new Stack<>();
        minStack = new Stack<>();
    }
    
    public void push(int val) {
        // push in Main stack
        // if min Stack empty 
        //     push in min stack 
        // else if val < minStack.peek()
        //     push in MinStack
        // else 
        //     push min.peek() in minStack 
        mainStack.push(val);
        if(minStack.isEmpty()){
            minStack.push(val);
        }
        else if(val < minStack.peek()){
            minStack.push(val);
        } 
        else{
            minStack.push(minStack.peek());
        }

    }
    
    public void pop() {
        mainStack.pop();
        minStack.pop();
    }
    
    public int top() {
        return mainStack.peek();
    }
    
    public int getMin() {
        return minStack.peek();
    }
}
