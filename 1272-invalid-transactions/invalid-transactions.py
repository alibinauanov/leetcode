class Solution(object):
    def invalidTransactions(self, transactions):
        """
        :type transactions: List[str]
        :rtype: List[str]
        """
        groups = defaultdict(list)    # name -> [(time, city, idx), ...]
        invalid_idx = set()

        # Parse & handle amount rule; group compact tuples for easy sorting
        for idx, t in enumerate(transactions):
            name, time, amount, city = t.split(',')
            time = int(time)
            amount = int(amount)
            if amount > 1000:
                invalid_idx.add(idx)
            groups[name].append((time, city, idx))

        # For each person, sort by time (tuple first element) and window-scan 60 mins
        for name, arr in groups.items():
            arr.sort()  # sorts by time automatically
            n = len(arr)
            for i in range(n):
                j = i + 1
                while j < n and arr[j][0] - arr[i][0] <= 60:
                    if arr[i][1] != arr[j][1]:           # different city
                        invalid_idx.add(arr[i][2])
                        invalid_idx.add(arr[j][2])
                    j += 1

        return [transactions[i] for i in sorted(invalid_idx)]