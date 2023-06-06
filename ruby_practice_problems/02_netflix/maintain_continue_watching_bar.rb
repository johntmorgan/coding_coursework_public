
# O(1) time
# O(n) space - size of FreqStack

class FreqStack
  attr_accessor :freq, :group, :max_freq
  def initialize(max_freq=0)
    @freq = {}
    @group = {}
    @max_freq = max_freq
  end

  def push(show_name)
    if @freq[show_name] != nil
      @freq[show_name] += 1
    else
      @freq[show_name] = 1
    end

    f = @freq[show_name]
    @max_freq = f if f > @max_freq
    if @group[f] != nil
      @group[f].push(show_name)
    else
      @group[f] = [show_name]
    end
  end

  def pop()
    show = ""
    if @max_freq > 0
      show = @group[@max_freq].pop()
      @freq[show] -= 1
      if @group[@max_freq].length() == 0
        @max_freq -=1
      end
    end
    return show
  end
end

#Driver Code
obj = FreqStack.new
obj.push("Queen's Gambit")
obj.push("Teen Wolf")
obj.push("Queen's Gambit")
puts("...User navigates to the browser...")
puts("Continue Watching : " + obj.pop().to_s)
puts()
obj.push("Teen Wolf")
obj.push("Bigderton")
puts("...User navigates to the browser...")
puts("Continue Watching : " + obj.pop().to_s)
puts()
obj.push("Queen's Gambit")
obj.push("Teen Wolf")
obj.push("Bigderton")
for i in (0...7)
    puts("...User navigates to the browser...")
    puts("Continue Watching : " + obj.pop().to_s)
    puts()
end