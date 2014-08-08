from euler import *
import time

#start timer
start = time.time()

#question number
questionno = 32

#print the problem
print_problem(questionno)

#
# Solution
#

# return True if pandigital string containing numbers 1 - limit
def is_pandigital(string, limit = 9):

    if ( len(string) != limit ):
        return False

    if( '0' in string ):
        return False

    if(len("".join(set(string))) != limit ):
        return False

    return True


pandigital_products = []
limit = 9

# make assumptions about the range of products and work backwards
for product in range(4012,9876):

    product_str = str(product)

    # skip products containing zeroes
    if( '0' in product_str ):
        continue

    # skip products with duplicate digits
    if( len(product_str) != len( ''.join(set(product_str)) ) ):
        continue

    # loop though [0 ~ product] to find potential factors
    for i in range(product, 1, -1):
        
        multiplier_str = ''

        # check if it is a factor and pandigital
        if( is_factor(product, i) and is_pandigital(str(product) + str(i) + str(product/i)) ):

            # number is pandigital so add to list
            pandigital_products.append(product)

print '-----------------------------------------------------------------------'
print 'Solution:'
print '-----------------------------------------------------------------------'
print "Answer: %s" % sum(set(pandigital_products))
print "\n"+"Execution time: %s" % (time.time()-start) 
print '\n'