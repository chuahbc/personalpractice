# Extra credit: Look up the round() and abs() functions on the 
# internet, and find out what they do. Experiment with them in 
# the interactive shell.




#  round(number[, ndigits])

# Return number rounded to ndigits precision after the decimal point. If ndigits 
# is omitted or is None, it returns the nearest integer to its input.

# For the built-in types supporting round(), values are rounded to the closest 
# multiple of 10 to the power minus ndigits; if two multiples are equally close, 
# rounding is done toward the even choice (so, for example, both round(0.5) and 
# round(-0.5) are 0, and round(1.5) is 2). Any integer value is valid for ndigits 
# (positive, zero, or negative). The return value is an integer if ndigits is omitted 
# or None. Otherwise the return value has the same type as number.

# For a general Python object number, round delegates to number.__round__.

# Note :
# The behavior of round() for floats can be surprising: for example, round(2.675, 2) 
# gives 2.67 instead of the expected 2.68. This is not a bug: it’s a result of the fact 
# that most decimal fractions can’t be represented exactly as a float. See Floating 
# Point Arithmetic: Issues and Limitations for more information. 



# abs(x)

# Return the absolute value of a number. The argument may be an integer or a floating 
# point number. If the argument is a complex number, its magnitude is returned. If x 
# defines __abs__(), abs(x) returns x.__abs__().

# print(abs(2-4))
# >> 2
