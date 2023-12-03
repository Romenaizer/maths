"SYSTEM"
class EXPSystem:
    """
    CLASS NOT FOR PUBLIC USE (calculators):
        THE CLASS IS CREATED IN ORDER TO CREATE THE FUNCTIONS WITH RETURNS
        PUBLIC FUNCTIONS ARE THUS THE ONE WITHOUT PREFIX 'sys_'.
    
    FOR NON-CALCULATORS USERS:
        ABLE TO USE THE CLASS AS YOU WISH.
    """
    def sys_factorial(n:int):
        """
        n! = n*(n-1)*(n-2)*...*1
        """
        if n == 0:
            return 1
        else:
            try:
                for i in range(1, n):
                    n = i*n
                    if len(str(n)) > 4299:
                        n = str(n)[:-3] + '...'
                        break
                return n
            except:
                print("Error - factorial(n) too high. (>4300 digits)")
    
    
    def sys_binomial_coefficient(n:int, k:int):
        """
        n!/k!(n-k)!
        """
        fn = EXPSystem.sys_factorial(n)
        fk = EXPSystem.sys_factorial(k)
        fnk = EXPSystem.sys_factorial(n-k)
        return fn/(fk*fnk)

"PUBLIC (CALCULATORS)"

def factorial(n:int):
    print(EXPSystem.sys_factorial(n))
def binomial_coefficient(n:int, k:int):
    print(EXPSystem.sys_binomial_coefficient(n, k))

