var containsNearbyDuplicate = function(nums, k) {
    const window = new Set();

    for (let i = 0; i < nums.length; i++) {
        if (window.has(nums[i])) return true;

        window.add(nums[i]);

        // 윈도우 크기를 k로 유지
        if (window.size > k) {
            window.delete(nums[i - k]);
        }
    }

    return false;
};
