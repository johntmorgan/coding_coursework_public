class RequestLimiter

  attr_accessor :requests
  def initialize
    @requests = {}
  end

  def request_approver(timestamp, request)
    if !@requests.include?(request) || timestamp - @requests[request] >= 5
      @requests[request] = timestamp
      puts "Request accepted"
      return true
    else
      puts "Request rejected"
      return false
    end
  end
end

obj = RequestLimiter.new
obj.request_approver(1, "send_message")
obj.request_approver(2, "block")
obj.request_approver(3, "send_message")
obj.request_approver(8, "block")
obj.request_approver(10, "send_message")
obj.request_approver(11, "send_message")