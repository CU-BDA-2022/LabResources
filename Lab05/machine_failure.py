"""
Posterior probability for production line failure based on counts of defective
widgets.

Based on an example in DeGroot & Schervish, *Probability and Statistics* (2002);
see example 2.3.9, p. 74.

Created 2015-02-05 by Tom Loredo
2018-02-22:  Modified for BDA 2018 Lab05
2020-02-06:  Modified for BDA 2020 Lab03
2022-02-25:  Modified for BDA 2022 Lab05
"""

from numpy.testing import assert_approx_equal
from numpy import *


class MachineFailure:
    """
    Compute the probability that a widget production line is in a failure
    mode, based on counts of defective widgets and knowledge of defect
    rates (as probabilities) in nominal and failure modes, and the historical
    failure mode probability.
    """

    def __init__(self, defect_rate_nom, defect_rate_fail, p_failure):
        """
        Setup a machine failure inference case (with data initialized
        to zero cases).

        Parameters
        ----------
        defect_rate_nom : float
            Defect rate for the machine in nominal operating mode
        defect_rate_fail : float
            Defect rate for the machine when in failure mode
        p_failure : float
            Probability for failure mode on startup
        """
        self.dr_n = defect_rate_nom
        self.dr_f = defect_rate_fail
        self.p_fail = p_failure
        self.n_f, self.N = 0, 0  # number of failures, total number of cases

    def update_data(self, N, n_f):
        """
        Update the defect rate data.

        Parameters
        ----------
        N : int
            Number of widgets produced in a new batch
        n : int
            Number of defective widgets in the batch
        """
        self.N += N
        self.n_f += n_f

    def like_nom_fail(self):
        """
        Return the likelihoods for (nominal, failed) machine states.
        """
        l_nom = self.dr_n**self.n_f * (1.-self.dr_n)**(self.N-self.n_f)
        l_fail = self.dr_f**self.n_f * (1.-self.dr_f)**(self.N-self.n_f)
        return l_nom, l_fail

    def post_failed(self):
        """
        Return the posterior probability that the machine has failed.
        """
        l_nom, l_fail = self.like_nom_fail()
        p_good = 1. - self.p_fail
        return self.p_fail*l_fail / \
            (self.p_fail*l_fail + p_good*l_nom)

    def log_like_nom_fail(self):
        """
        Return the log likelihoods for (nominal, failed) machine states.
        """
        ll_nom = self.n_f*log(self.dr_n) + (self.N-self.n_f)*log(1.-self.dr_n)
        ll_fail = self.n_f*log(self.dr_f) + (self.N-self.n_f)*log(1.-self.dr_f)
        return ll_nom, ll_fail

    def post_failed_ll(self):
        """
        Return the posterior probability that the machine has failed.

        The calculation uses the log likelihood, factoring out the failure
        likelihood.
        """
        ll_nom, ll_fail = self.log_like_nom_fail()
        p_nom = 1. - self.p_fail
        return self.p_fail / \
            (self.p_fail + p_nom*exp(ll_nom - ll_fail))

    def __str__(self):
        """
        Return a string representation of the current state.
        """
        s = 'MachineFailure instance:\n'
        s += '  Failure mode probability: {:.3f}\n'.format(self.p_fail)
        s += '  Defect rates (nominal, failed):  {:.3f}, {:.3f}\n'.format(
            self.dr_n, self.dr_f)
        s += '  Current data (N, n_f):  {}, {}'.format(self.N, self.n_f)
        return s

# Always good to have tests!


def test_DS_case():
    """
    Duplicate the result from DeGroot & Schervish example 2.3.9.
    """
    mf_DS = MachineFailure(.01, .4, .1)
    mf_DS.update_data(6,2)
    p_f = mf_DS.post_failed()
    assert_approx_equal(1.-p_f, 0.04, significant=2)


def test_inc_all():
    """
    Check that we get the same result incrementing the data, or
    analyzing it all at once.
    """
    mf_inc = MachineFailure(.01, .4, .1)
    mf_inc.update_data(10, 1)
    mf_inc.update_data(40, 0)
    p_f_inc = mf_inc.post_failed()
    mf_all = MachineFailure(.01, .4, .1)
    mf_all.update_data(50, 1)
    p_f_all = mf_all.post_failed()
    assert p_f_all == p_f_inc  # should be *exactly* equal


def test_l_ll():
    """
    Check that the likelihood and log likelihood calculations match.
    """
    mf = MachineFailure(.01, .1, .05)
    mf.update_data(50, 1)
    assert_approx_equal(mf.post_failed(), mf.post_failed_ll())


if __name__ == '__main__':
    # DeGroot & Schervish example:
    mf_DS = MachineFailure(.01, .4, .1)
    mf_DS.update_data(6, 2)
    print(mf_DS)
    print('D&S ex. 2.3.9, P(failed|D) =', mf_DS.post_failed())
    print()

    # Case presented in Lab03 slides:
    mf1 = MachineFailure(.01, .1, .05)
    mf1.update_data(10, 1)
    print(mf1)
    print('Notebook example, 1 defect in 10, P(failed|D) =', mf1.post_failed())
    mf1.update_data(40, 0)
    print('Update to 1 in 50:', mf1.post_failed())
    print()

    mf2 = MachineFailure(.01, .1, .05)
    mf2.update_data(50, 1)
    print(mf2)
    print('All at once:', mf2.post_failed())
