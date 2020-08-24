# Extra credit: Search online for the Python documentation for the len() function.
# It will be on a web page titled “Built-in Functions.” Skim the list of other 
# functions Python has, look up what the round() function does, and experiment 
# with it in the interactive shell.

# Answer:

# len(s)
# Return the length (the number of items) of an object. The argument may be a 
# sequence (such as a string, bytes, tuple, list, or range) or a collection 
# (such as a dictionary, set, or frozen set).
# https://docs.python.org/3/library/functions.html?#len

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
