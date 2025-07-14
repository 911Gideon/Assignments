class DateCalculator:
    def __init__(self, year, month, day):
        self.original_year = year
        self.original_month = month
        self.day = day
        self._adjust_date()

    def _adjust_date(self):
        # Adjust month and year for January and February
        if self.original_month == 1 or self.original_month == 2:
            self.month = self.original_month + 12
            self.year = self.original_year - 1
        else:
            self.month = self.original_month
            self.year = self.original_year

    def calculate_day_of_week(self):
        q = self.day
        m = self.month
        Y = self.year
        K = Y % 100
        J = Y // 100

        # Zeller’s formula
        h = (q + (13 * (m + 1)) // 5 + K + (K // 4) + (J // 4) + (5 * J)) % 7

        # Map result to day names
        days = ['Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
        return days[h]


# Example use
date = DateCalculator(1589, 9, 15)
print(f"September 15, 1589 was a {date.calculate_day_of_week()}")