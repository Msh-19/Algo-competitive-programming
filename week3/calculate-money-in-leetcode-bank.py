class Solution:
      def totalMoney(self, n: int) -> int:
        total_money, weeks_count, daily_sum = 0, 0, 0

        for day in range(1, n + 1):
            if day % 7 == 1:
                weeks_count += 1
                daily_sum = weeks_count
            else:
                daily_sum += 1

            total_money += daily_sum

        return total_money
        