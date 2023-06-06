class Logger
  #Ruby's fields are private. attr_accessor makes them public
  attr_accessor :messages
  def initialize()
    @messages = {}
  end

  def should_print_message(timestamp, message)
    if messages[message] == nil
      messages[message] = timestamp
      return true
    else
      last = messages[message]
      if timestamp - last >= 5
        messages[message] = timestamp
        return true
      else
        return false
      end
    end
  end
end
