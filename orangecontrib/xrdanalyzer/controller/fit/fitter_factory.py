from orangecontrib.xrdanalyzer.controller.fit.fitters.fitter_scipy import FitterScipy
from orangecontrib.xrdanalyzer.controller.fit.fitters.fitter_lmfit import FitterLmfit
from orangecontrib.xrdanalyzer.controller.fit.fitters.fitter_pm2k import FitterPM2K

import orangecontrib.xrdanalyzer.util.congruence as congruence

class FitterName:
    SCIPY = "scipy"
    LMFIT = "lmfit"
    MINPACK  = "minpack"

    @classmethod
    def tuple(cls):
        return [cls.MINPACK, cls.SCIPY, cls.LMFIT]

class FitterFactory():

    @classmethod
    def create_fitter(cls, fitter_name=FitterName.LMFIT, fitting_method=None):
        congruence.checkEmptyString(fitter_name, "Fitter Name")

        if fitter_name == FitterName.MINPACK:
            return FitterPM2K()
        elif fitter_name == FitterName.SCIPY:
            return FitterScipy()
        elif fitter_name == FitterName.LMFIT:
            return FitterLmfit(fitting_method=fitting_method)
