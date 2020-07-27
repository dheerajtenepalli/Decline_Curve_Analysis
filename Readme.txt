# Decline Curve Analysis Version 1.0
#
# Purpose:
#	1.Convert codebase to Python.
#	2.Fit decline curves.
#   3.Set up an evaluation pipeline to compare hyperbolic, exponential, harmonic, and hyperbolic-to-exponential fittings. 
#	4.Outlier analysis using several machine learing algorithms.    
#	5.Unit Testing. 
#	6.Visualization of results.
#
# Date: 25-Feb-2019
#
# Programming language: Python 3.6.3 or Python 3.6.7
#
# Implementation by
# 	1.Reddy Dheeraj Tenepalli
#--------------------------------------------------------------------------
# Python is an open source, object oriented, interactive, cross platform,
# scripting language with extensive libraries for data analysis and
# plotting. 
#--------------------------------------------------------------------------
# Resources:
#   Python: www.python.org (core language resources)
#   SciPy and NumPy: www.scipy.org (scientific, numerical, and plotting)
#--------------------------------------------------------------------------
# Revisions:
#	1. 27-Feb-2019   -- Added Harmonic, exponential and hyperbolic fitting capabilities.
#	2. 02-March-2019 -- Added hyperbolic-to-exponential fitting capability.
#	3. 04-March-2019 -- Added Outlier filtering capability.
#	4. 05-March-2019 -- Implemented an evaluation pipeline on held out cross validation data.
#	5. 08-March-2019 -- Added Unit testing with code coverage of 97% and support for Multiprocessing to optimize for performance.
#    
#--------------------------------------------------------------------------
# Standards followed:
# 	1. Pep 8 format
#	2. Also the code is tab seperated to optimize for Memory.
