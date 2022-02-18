#!/usr/bin/env python
# coding: utf-8

# # SciPy's probability distributions, ufuncs, and unit testing

# In[1]:


import numpy as np
from numpy import *
import scipy
from scipy import stats, integrate


prior = stats.beta(1, 1)  # flat prior as a "frozen" beta object
alphas = linspace(0., 1., 200)

def like(alpha, n, ntot):
    """
    Likelihood function for `alpha`, the success probability in a binomial
    sampling dist'n for `n` successes in `ntot` trials.
    """
    return stats.binom.pmf(n, ntot, alpha)

n, ntot = 8, 12  # n successes in ntot trials

# Save the likelihood values for use in posterior.
lvals = like(alphas, n, ntot)  # note alphas is an array

# Marginal likelihood calculation:
mlike = integrate.trapz(prior.pdf(alphas)*lvals, alphas)
print('Marg. likelihood:', mlike)


# Compute the posterior.

ppdf = prior.pdf(alphas)*lvals/mlike

# Check the normalization:
print('Posterior norm:', integrate.trapz(ppdf, alphas))


# We could get the likelihoods with an explicit loop.

def like_loop(alphas, n, ntot):
    """
    Likelihood function for `alphas`, a sequence of success probabilities 
    for binomial sampling dist'ns for `n` successes in `ntot` trials.
    
    This computes the likelihood via explicit looping over the values
    in `alphas`.
    """
    lvals = empty_like(alphas)
    for i in range(len(alphas)):
        lvals[i] = stats.binom.pmf(n, ntot, alphas[i])
    return lvals

llvals = like_loop(alphas, n, ntot)
print(llvals - lvals)


alphas = linspace(0., 1., 100000)

# A naive test of normalization:

alphas = linspace(0., 1., 200)
pivals = prior.pdf(alphas)
lvals = like(alphas, n, ntot)
mlike = integrate.trapz(pivals*lvals, alphas)
ppdf = pivals*lvals/mlike

# assert integrate.trapz(ppdf, alphas) == 1.


# In[ ]:


# Account for roundoff:

import numpy.testing as npt

# get_ipython().run_line_magic('pinfo', 'npt.assert_allclose')


# In[ ]:


# Use the default of 0 absolute tolerance, 1e-7 relative tolerance:
# npt.assert_allclose(integrate.trapz(ppdf, alphas), 1.)


# Unit testing *frameworks* typically require tests to be written as Python functions or class methods (often with a particular naming convention).  The framework supports automated discovery and running of tests, as well as providing some advanced testing capability.

# In[ ]:


def test_norm():
    """
    Test normalization of the posterior (using global quantities).
    """
    npt.assert_allclose(integrate.trapz(ppdf, alphas), 1.)

# test_norm()


# In[ ]:


def test_sym():
    """
    Test symmetry of the posterior for a symmetric test case.
    """
    alphas = linspace(0., 1., 200)
    pivals = prior.pdf(alphas)
    lvals = like(alphas, 5, 10)
    mlike = integrate.trapz(pivals*lvals, alphas)
    ppdf = pivals*lvals/mlike
    npt.assert_allclose(integrate.trapz(ppdf[:100], alphas[:100]), integrate.trapz(ppdf[100:], alphas[100:]))

# test_sym()


# In[ ]:


# Double-check that last one!
alphas = linspace(0., 1., 200)
pivals = prior.pdf(alphas)
lvals = like(alphas, 5, 10)
mlike = integrate.trapz(pivals*lvals, alphas)
ppdf = pivals*lvals/mlike

print(integrate.trapz(ppdf[:100], alphas[:100]))
print(integrate.trapz(ppdf[100:], alphas[100:]))
