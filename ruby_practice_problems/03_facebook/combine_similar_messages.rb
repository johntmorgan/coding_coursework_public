def combine_messages(messages)
  def generate_key(message)
    key = ""
    (0...message.length() - 1).each do |i|
      diff = message[i + 1].ord() - message[i].ord()
      if diff < 0
        diff += 26
      end
      key += diff.to_s + ","
    end
    return key
  end

  message_group = {}
  (0...messages.length()).each do |i|
    message = messages[i]
    key = generate_key(message)
    p(key)
    if message_group.include?(key)
      message_group[key] += [message]
    else
      message_group[key] = [message]
    end
  end
  return message_group
end


messages = ["lmn", "mno", "azb", "bac", "yza", "bdfg"]
groups = combine_messages(messages)
puts("The Grouped Messages are:\n")
puts( groups.map{ |k,v| "#{v}" }.sort)