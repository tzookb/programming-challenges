def rot13(secret_messages)

    res = secret_messages.map do |secret_messagesLine|
    
        secret_messagesLine = secret_messagesLine.split("").map do |x|

            if /^[a-z]$/ === x
                ((x.ord + 13 - 'a'.ord) % 26 + 'a'.ord).chr
            elsif /^[A-Z]$/ === x
                ((x.ord + 13 - 'A'.ord) % 26 + 'A'.ord).chr
            else
                x
            end
        end
        
        secret_messagesLine.join("")
    end

    res
    
end