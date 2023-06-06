# O(n) time and space

def service_time(n, logs)
  stack = []
  serv_times = [0] * n
  serv = logs[0].split(":")
  stack.push(serv[0].to_i)
  time = serv[2].to_i
  for i in (0..logs.length() - 1)
    serv = logs[i].split(':')
    if serv[1].include? "start"
      if stack
        serv_times[stack[-1]] += serv[2].to_i - time
      end
      stack.push(serv[0].to_i)
      time = serv[2].to_i
    else
      serv_times[stack[-1]] += serv[2].to_i - time + 1
      stack.pop()
      time = serv[2].to_i + 1
    end
  end
  return serv_times
end


p(service_time(2, ["0:start:0","0:start:2","0:end:5","1:start:6","1:end:6","0:end:7"]))