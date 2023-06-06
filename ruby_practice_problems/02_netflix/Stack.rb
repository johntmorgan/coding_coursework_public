class MyStack
    # Ruby's field are always private. attr_accessor makes them public
    attr_accessor :stack_list
    def initialize()
        @stack_list = []
    end

    def is_empty()
        return @stack_list.length() == 0
    end

    def top()
        if is_empty()
            return nil
        end
        return @stack_list[-1]
    end

    def size()
        return @stack_list.length()
    end

    def push(value)
        @stack_list.push(value)
    end

    def pop()
        if is_empty()
            return nil
        end
        return @stack_list.pop()
    end
end