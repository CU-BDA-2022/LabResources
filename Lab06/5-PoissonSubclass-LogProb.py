"""
Plot Poisson rate posterior PDFs as a demo of the UnivariateBayesianInference
class, here using the log prior and log likelihood, to avoid overflows when
the number of counts is large.

Created 2022-03-04 by Tom Loredo
"""

import numpy as np
import scipy
import matplotlib as mpl
from matplotlib.pyplot import *
from numpy import *
from scipy import stats, special, integrate

from univariate_bayes import UnivariateBayesianInference


ion()


# This is an alternate definition of PoissonRateInference vs. the one in
# 4-PoissonBinomialSubclasses.py, internally using log probabilities to
# avoid overflows in large-n cases.


class PoissonRateInference(UnivariateBayesianInference):
    """
    Bayesian inference for a Poisson rate.
    """

    def __init__(self, intvl, n, log_prior, r_l, r_u, nr=200):
        """
        Define a posterior PDF for a Poisson rate.

        Parameters
        ----------
        intvl : float
            Interval for observations

        n : int
            Counts observed

        log_prior : const or function
            Prior PDF for the rate, as a (log) constant for flat prior, or
            a function that can evaluate the log prior PDF on an array

        r_u : float
            Upper limit on rate for evaluating the PDF
        """
        self.intvl = intvl
        self.n = n
        self.r_l, self.r_u = r_l, r_u
        self.nr = nr
        self.rvals = linspace(r_l, r_u, nr)

        # Pass the info to the base class initializer.
        super().__init__(self.rvals, log_prior, self.llfunc, logprob=True)

    def llfunc(self, rvals):
        """
        Evaluate the Poisson log likelihood function on a grid of rates.
        """
        r_intvl = self.intvl * rvals
        return self.n*log(r_intvl) - r_intvl


#-------------------------------------------------------------------------------
# 1st 2 curves:  Poisson, const & exp'l priors, (n,T) = (16, 2)

# Limits for PDF calculation and plotting.  These will often *not* correspond
# to the prior range.  They should reflect where the *posterior* needs to be
# computed, which will typically be over a smaller range than the prior range.
r_l, r_u = .001, 20.

# Note r_l is not 0.  log(0) causes a warning; the result remains correct if
# we use r_l=0 (Python understands that exp(-Inf) is zero), but it's safest
# to steer clear of underflows/overflows when possible.


# Explicitly create an empty fig, so we can customize the size.
pfig1 = figure(figsize=(8,5))

# Flat prior case; note the explicit lower bound, near 0 but not at 0:
prior_l, prior_u = 0.001, 1e5
flat_pdf = 1. / (prior_u - prior_l)
n, T = 16, 2
pri1 = PoissonRateInference(T, n, log(flat_pdf), r_l, r_u)
pri1.plot(alpha=.5)

# Exp'l prior:
scale = 10.
gamma1 = stats.gamma(1, scale=scale)  # a=1 is exp'l dist'n


def log_exp_pdf(rvals):
    return log(gamma1.pdf(rvals))


pri2 = PoissonRateInference(T, n, log_exp_pdf, r_l, r_u)
pri2.plot(ls='g--')


# Label the axes; be sure to show the units!
# Note: If we're always going to be using the PRI class for rates per
# second, we could overload the base class `plot` method to handle this.
# See the BinomialInference class for an example.
xlabel(r'Rate (s$^{-1}$)')
ylabel('Posterior PDF for rate (s)')
title('Poisson rate estimation')


#-------------------------------------------------------------------------------
# 2nd 2 curves:  Poisson, const & exp'l priors, (n,T) = (160, 20)

# This is the case that fails with an overflow in 1-PoissonRate-Procedural.py.

# We'll use the same compute/plot range as above, just so that the posteriors
# may be compared over the same abscissa.  But we'll use more points on the
# abscissa, since the posterior is now more concentrated.

n, T = 160, 20
pfig2 = figure(figsize=(8,5))

pri1 = PoissonRateInference(T, n, log(flat_pdf), r_l, r_u, 500)
pri1.plot(alpha=.5)

pri2 = PoissonRateInference(T, n, log_exp_pdf, r_l, r_u, 500)
pri2.plot(ls='g--')
