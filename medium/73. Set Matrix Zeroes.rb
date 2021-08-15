# 73. Set Matrix Zeroes
# @param {Integer[][]} matrix
# @return {Void} Do not return anything, modify matrix in-place instead.
def set_zeroes(matrix)
    """
    Note that in Ruby we can't let capitalized variables to be assigned when
    the method is called, because capitalized variables are CONSTANTS.

    Also note that to reversely iterate through a range, we can't use
    (bigger..smaller).each, but need to do (smaller..bigger).reverse_each.
    """
    rows = matrix.length
    cols = matrix[0].length
    is_first_col0 = false
    (0...rows).each do |r|
        is_first_col0 = true if matrix[r][0] == 0
        (1...cols).each do |c|
            if matrix[r][c] == 0
                matrix[r][0] = matrix[0][c] = 0
            end
        end
    end

    (0...rows).reverse_each do |r|
        (1...cols).each do |c|
            if matrix[0][c] == 0 or matrix[r][0] == 0
                matrix[r][c] = 0
            end
        end
        matrix[r][0] = 0 if is_first_col0
    end
end