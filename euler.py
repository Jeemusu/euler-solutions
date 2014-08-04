#--- print the problem text ---------------------------------------------------
def print_problem(questionno):
    #import question
    filepath = "questions/%s.txt" % questionno
    with open (filepath, "r") as myfile:
        data=myfile.read()

    print '\n'
    print '-----------------------------------------------------------------------'
    print 'Problem:'
    print '-----------------------------------------------------------------------'
    print data + '\n'   


#--- print content of list ----------------------------------------------------
def is_multiple_of(n, k):
    if n % k == 0:
        return True


#--- print content of list ----------------------------------------------------
def print_r(obj):
    """
    Print an array 

    """
    # Dict
    if isinstance(obj, dict):
        for k, v in sorted(obj.items()):
            print u'{0}: {1}'.format(k, v)

    # List or tuple            
    elif isinstance(obj, list) or isinstance(obj, tuple):
        for x in obj:
            print x

    # Other
    else:
        print object
        
#--- generate prime numbers in range n-----------------------------------------
def prime_sieve(n):

    sieve = [True] * (n/2)
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i/2]:
            sieve[i*i/2::i] = [False] * ((n-i*i-1)/(2*i)+1)
    return [2] + [2*i+1 for i in xrange(1,n/2) if sieve[i]]

#--- test if n is prime (upto 1373653)-----------------------------------------
def _try_composite(a, d, n, s):
    if pow(a, d, n) == 1:
        return False
    for i in range(s):
        if pow(a, 2**i * d, n) == n-1:
            return False
    return True # n  is definitely composite
 
def is_prime(n):
    if n in _known_primes or n in (0, 1):
        return True
    if any((n % p) == 0 for p in _known_primes):
        return False
    d, s = n - 1, 0
    while not d % 2:
        d, s = d >> 1, s + 1
    # Returns exact according to http://primes.utm.edu/prove/prove2_3.html
    if n < 1373653: 
        return not any(_try_composite(a, d, n, s) for a in (2, 3))
    # otherwise
    return False

_known_primes = [2, 3]
_known_primes += [x for x in range(5, 1000, 2) if is_prime(x)]
