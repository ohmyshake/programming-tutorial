#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  4 13:39:53 2022

@author: yf
"""

import numpy as np



PI = np.pi
DEG = 180./PI

def mat(m):
    """ Converts from vector to
        matrix representation
    """
    return np.array(([[m[0], m[3], m[4]],
                      [m[3], m[1], m[5]],
                      [m[4], m[5], m[2]]]))


def vec(M):
    """ Converts from matrix to
        vector representation
    """
    return np.array([M[0,0], 
                     M[1,1],
                     M[2,2],
                     M[0,1],
                     M[0,2],
                     M[1,2]])


### eigenvalue-related functions
    
def lam2lune(lam):
    """
    Converts moment tensor eigenvalues to lune coordinates

    input
    : lam: vector with shape [3]

    output
    : gamma: angle from DC meridian to lune point (-30 <= gamma <= 30)
    : delta: angle from deviatoric plane to lune point (-90 <= delta <= 90)
    : M0: seismic moment, M0 = ||lam|| / sqrt(2)
    """
    # descending sort
    lam = np.sort(lam)[::-1]

    # magnitude of lambda vector (rho of TapeTape2012a p.490)
    lammag = np.linalg.norm(lam)

    # seismic moment
    M0 = lammag/np.sqrt(2.)

    # TapeTape2012a, eqs.21a,23
    # numerical safety 1: if trace(M) = 0, delta = 0
    # numerical safety 2: is abs(bdot) > 1, adjust bdot to +1 or -1
    if np.sum(lam) != 0.:
        bdot = np.sum(lam)/(np.sqrt(3)*lammag)
        np.clip(bdot, -1, 1)
        delta = 90. - np.arccos(bdot)*DEG
    else:
        delta = 0.
    
    # TapeTape2012a, eq.21a
    # note: we set gamma=0 for (1,1,1) and (-1,-1,-1)
    if lam[0] != lam[2]:
        gamma = np.arctan((-lam[0] + 2.*lam[1] - lam[2])
                         /(np.sqrt(3)*(lam[0] - lam[2]))) * DEG
    else:
        gamma = 0.

    return (
        gamma,
        delta,
        M0,
        )


def lune2lam(gamma, delta, M0):
    """ Converts lune coordinates to moment tensor eigenvalues
    """
    beta = 90. - delta

    # magnitude of lambda vectors (TT2012, p.490)
    rho = M0*np.sqrt(2)

    # convert to eigenvalues (TT2012, Eq.20)
    # matrix to rotate points such that delta = 90 is (1,1,1) and delta = -90 is (-1,-1,-1)
    R = np.array([[3.**0.5, 0., -3.**0.5],
                  [-1., 2., -1.],
                  [2.**0.5, 2.**0.5, 2.**0.5]])/6.**0.5

    # Cartesian points as 3 x n unit vectors (TT2012, Eq.20)
    #Pxyz = latlon2xyz(delta,gamma,ones(n,1))
    Pxyz = np.array([np.cos(gamma/DEG)*np.sin(beta/DEG),
                     np.sin(gamma/DEG)*np.sin(beta/DEG),
                     np.cos(beta/DEG)])

    # rotate points and apply magnitudes
    lamhat = np.dot(R.T, Pxyz)
    lam = rho*lamhat

    return rho*lamhat


def eig(M, sort_type=1):
    """
    Calculates eigenvalues and eigenvectors of matrix
    
    sorting of eigenvalues
    1: highest to lowest, algebraic: lam1 >= lam2 >= lam3
    2: lowest to highest, algebraic: lam1 <= lam2 <= lam3
    3: highest to lowest, absolute : | lam1 | >= | lam2 | >= | lam3 |
    4: lowest to highest, absolute : | lam1 | <= | lam2 | <= | lam3 |
    """
    if sort_type not in [1,2,3,4]:
        raise ValueError

    lam,V = np.linalg.eigh(M)

    if sort_type == 1:
        idx = np.argsort(lam)[::-1]
    elif sort_type == 2:
        idx = np.argsort(lam)
    elif sort_type == 3:
        idx = np.argsort(np.abs(lam))[::-1]
    elif sort_type == 4:
        idx = np.argsort(np.abs(lam))
    lsort = lam[idx]
    Vsort = V[:,idx]

    return lsort,Vsort