import {MyStack} from './Stack.js'

class MaxStack{
    // Constructor
    constructor(){
        this.maxStack = new MyStack()
        this.mainStack = new MyStack()
    }

    // Removes and returns value from maxStack
    pop(){
        this.maxStack.pop()
        return this.mainStack.pop()
    }

    // Pushes values into maxStack
    push(value){
        this.mainStack.push(value)
        if ((this.maxStack.is_empty() || this.maxStack.top() < value))
            this.maxStack.push(value)
        else
            this.maxStack.push(this.maxStack.top())
    }

    // Returns maximum value from newStack in O(1) Time
    maxRating(){
        if (!(this.maxStack.is_empty()))
            return this.maxStack.top()
    }
}