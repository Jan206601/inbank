import math

MINIMUM_PERIOD = 12
MAXIMUM_PERIOD = 60

MINIMUM_AMOUNT = 2000
MAXIMUM_AMOUNT = 10000


class LoanCalculator:

    def get_loan_decision(self, personal_code, amount, period):
        if self.person_has_debt(personal_code):
            return False
        if period > MAXIMUM_PERIOD or period < MINIMUM_PERIOD:
            return False
        if amount > MAXIMUM_AMOUNT or amount < MINIMUM_AMOUNT:
            return False
        maximum = self.get_maximum_amount(personal_code, period)
        return MINIMUM_AMOUNT <= amount <= maximum

    def get_maximum_amount(self, personal_code, period):
        if self.person_has_debt(personal_code):
            return None
        maximum = self.__get_person_credit_modifier(personal_code) * period
        if maximum > MAXIMUM_AMOUNT:
            return MAXIMUM_AMOUNT
        if maximum < MINIMUM_AMOUNT:
            return None
        return math.floor(maximum)

    def get_suitable_period_for_amount(self, personal_code, amount):
        if self.person_has_debt(personal_code):
            return None
        if amount < MINIMUM_AMOUNT:
            return None
        period = amount / self.__get_person_credit_modifier(personal_code)
        if period > MAXIMUM_PERIOD:
            return None
        if period < MINIMUM_PERIOD:
            return MINIMUM_PERIOD
        return math.ceil(period)

    def get_credit_score(self, personal_code, amount, period):
        return (self.__get_person_credit_modifier(personal_code) / amount) * period

    @staticmethod
    def period_in_allowed_range(period):
        return MINIMUM_PERIOD <= period <= MAXIMUM_PERIOD

    @staticmethod
    def amount_in_allowed_range(amount):
        return MINIMUM_AMOUNT <= amount <= MAXIMUM_AMOUNT

    def person_has_debt(self, personal_code):
        return self.__get_person_segment(personal_code) == -1

    def personal_code_known(self, personal_code):
        return self.__get_person_segment(personal_code) is not None

    def __get_person_credit_modifier(self, personal_code):
        if not self.personal_code_known(personal_code):
            raise ValueError("Personal code not found")
        segment = self.__get_person_segment(personal_code)
        return self.__get_segment_credit_modifier(segment)

    @staticmethod
    def __get_person_segment(personal_code):
        if personal_code == "49002010965":
            return -1
        if personal_code == "49002010976":
            return 1
        if personal_code == "49002010987":
            return 2
        if personal_code == "49002010998":
            return 3
        return None

    @staticmethod
    def __get_segment_credit_modifier(segment_number):
        if segment_number == 1:
            return 100
        if segment_number == 2:
            return 300
        if segment_number == 3:
            return 1000
        return 0
