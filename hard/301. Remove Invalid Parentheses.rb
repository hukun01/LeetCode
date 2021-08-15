# 301. Remove Invalid Parentheses
# @param {String} s
# @return {String[]}
def remove_invalid_parentheses(s)
    """
    Same as the Python solution 1/2.
    """
    q = Queue.new
    q.push(s)
    used = Set.new
    found = false
    ans = []
    until q.empty? or found
        (0...q.length).each do |_|
            node = q.pop
            next if used.include?(node)
            used.add(node)
            if is_valid(node)
                found = true
                ans.push(node)
            end

            node.chars.each_with_index do |val, idx|
                next unless '()'.include?(val)
                new = node[0...idx] + node[idx+1..-1]
                q.push(new)
            end
        end
    end

    ans
end
def is_valid(s)
    left = 0
    s.chars.each do |c|
        if c == '('
            left += 1
        elsif c == ')'
            if left > 0
                left -= 1
            else
                return false
            end
        end
    end

    left == 0
end