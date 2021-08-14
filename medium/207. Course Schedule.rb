# 207. Course Schedule
# @param {Integer} num_courses
# @param {Integer[][]} prerequisites
# @return {Boolean}
def can_finish(num_courses, prerequisites)
    pre_count = Hash.new(0)
    succs = Hash.new { |h, k| h[k] = [] }
    prerequisites.each do |b, a|
        pre_count[b] += 1
        succs[a].push(b)
    end
    free = Set.new(0...num_courses) - pre_count.keys
    taken = 0
    until free.empty?
        a = free.pop
        taken += 1
        succs[a].each do |b|
            pre_count[b] -= 1
            free.add(b) if pre_count[b] == 0
        end
    end

    taken == num_courses
end

class Set
  def pop
    element = first
    delete(first)
    element
  end
end