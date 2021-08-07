# 1. Two Sum
# @param {Integer[]} nums
# @param {Integer} target
# @return {Integer[]}
def two_sum(nums, target)
    seen = Hash.new
    nums.each_with_index do |val, index|
        prev_index = seen[target - val]
        return [prev_index, index] if prev_index.nil?
        seen[val] = index
    end
end