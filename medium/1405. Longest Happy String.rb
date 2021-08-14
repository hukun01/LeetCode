# 1405. Longest Happy String
# @param {Integer} a
# @param {Integer} b
# @param {Integer} c
# @return {String}
def longest_diverse_string(a, b, c)
    (first, x), (second, y), (third, z) = [[a, 'a'], [b, 'b'], [c, 'c']].sort.reverse
    buckets = [x + x] * (first / 2)
    buckets.push(x) if first % 2 == 1
    num_buckets = buckets.length
    bucket_idx = 0
    [[second, y], [third, z]].each do |count, char|
        (0...count).each do |_|
            buckets[bucket_idx % num_buckets] += char
            bucket_idx += 1
        end
    end

    buckets[...[num_buckets, bucket_idx+1].min].join
end