export class MyStack{
    constructor(){
        this.stack_list = []
    }

    is_empty(){
        return this.stack_list.length == 0
    }

    top(){
        if (this.is_empty())
            return null
        return this.stack_list[this.stack_list.length-1]
    }

    size(){
        return this.stack_list.length
    }

    push(value){
        this.stack_list.push(value)
    }

    pop(){
        if (this.is_empty())
            return null
        return this.stack_list.pop()
    }
}