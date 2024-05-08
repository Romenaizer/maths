"SYSTEM"
class BASICSystem:
    """
    CLASS NOT FOR PUBLIC USE (calculators):
        THE CLASS IS CREATED IN ORDER TO CREATE THE FUNCTIONS WITH RETURNS
        PUBLIC FUNCTIONS ARE THUS THE ONE WITHOUT PREFIX 'sys_'.
    
    FOR NON-CALCULATORS USERS:
        ABLE TO USE THE CLASS AS YOU WISH.
    """
    inf = float('inf')

    def sys_sum(sequence_func, from_n: int, to):
        """
        SUM = a + b + c ...
        """
        SUM = 0
        n = from_n
        while n <= to:
            SUM += sequence_func(n)
            n += 1
        return SUM