"""
Module defining a base class implementing simple Bayesian inference for a
univariate model, using quadrature for integration.

Created Feb 27, 2015 by Tom Loredo
2018-03-08 Modified for Py-3, updated for BDA18
2020-02-26 Updated for BDA20
"""

import numpy as np
from numpy import *
from matplotlib.pyplot import plot


class UnivariateBayesianInference(object):
    """
    Implement Bayesian inference for a univariate model, using quadrature for
    integrals.
    """

    def __init__(self, param_grid, prior, lfunc=None, logprob=False):
        """
        Calculate the posterior distribution over a grid in parameter space.

        Either the likelihood or the log-likelihood may be specified.

        Parameters
        ----------
        param_grid : float array
            Array of parameter values; assumed equally spaced

        prior : float or function
            Prior PDF for the param, as a constant for flat prior, or
            a function that can evaluate the PDF on an array; if
            logprob == True, prior is interpreted as the log density

        lfunc : function
            Function that can evaluate the likelihood on an array; if
            logprob == True, lfunc is interpreted as the log likelihood

        logprob : boolean
            If False, prior and lfunc are interpreted as providing the actual
            prioir PDF and likelihood function; if True, they are interpreted
            as providing the log prior PDF and log likelihood function
        """
        self.param_grid = param_grid
        self.delta = param_grid[1] - param_grid[0]
        self.logprob = logprob

        # Evaluate prior and likelihood over the grid.  These will be
        # the log values if logprob=True.
        if callable(prior):
            self.prior_pdf = prior(param_grid)
        else:
            self.prior_pdf = prior * ones_like(param_grid)
        self.like = lfunc(param_grid)

        # Handle the logprob=True case.
        if self.logprob:
            # Subtract off the max to avoid possible underflow everywhere.
            # Note this affects the marginal likelihood so it needs to be
            # taken into account if the marginal likelihood is used directly,
            # e.g., to compute a Bayes factor.  So save the max values.
            self.max_log_prior = self.prior_pdf.max()
            self.prior_pdf = exp(self.prior_pdf - self.max_log_prior)
            self.max_log_like = self.like.max()
            self.like = exp(self.like - self.max_log_like)

        # Bayes's theorem, using the trapezoid rule for the marginal likeilhood:
        numer = self.prior_pdf * self.like
        self.mlike = np.trapz(numer, dx=self.delta)
        self.post_pdf = numer / self.mlike

    def plot(self, ls='b-', lw=3, **kwds):
        """
        Plot the posterior PDF using the current axes.
        """
        plot(self.param_grid, self.post_pdf, ls, lw=lw, **kwds)
