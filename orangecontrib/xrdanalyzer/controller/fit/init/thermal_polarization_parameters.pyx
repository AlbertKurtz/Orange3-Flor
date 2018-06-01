try:
    import orangecontrib.xrdanalyzer.util.test_recovery
    is_recovery = False
except:
    is_recovery = True

if not is_recovery:
    from orangecontrib.xrdanalyzer.util import congruence
    from orangecontrib.xrdanalyzer.controller.fit.fit_parameter import Boundary, FitParameter, FitParametersList
else:
    from orangecontrib.xrdanalyzer.recovery.util import congruence
    from orangecontrib.xrdanalyzer.recovery.controller.fit.fit_parameter import Boundary, FitParameter, FitParametersList


class ThermalPolarizationParameters(FitParametersList):

    debye_waller_factor = None
    use_lorentz_polarization_factor = True

    def __init__(self,
                 debye_waller_factor = FitParameter(parameter_name="B", value=1e-1, boundary=Boundary(min_value=0.0)),
                 use_lorentz_polarization_factor = False):
        self.debye_waller_factor = debye_waller_factor
        self.use_lorentz_polarization_factor = use_lorentz_polarization_factor

    @classmethod
    def get_parameters_prefix(cls):
        return "tp_"

    def duplicate(self):
        return ThermalPolarizationParameters(debye_waller_factor=self.debye_waller_factor,
                                             use_lorentz_polarization_factor=self.use_lorentz_polarization_factor)

    def to_text(self):
        text = "THERMAL/POLARIZATION PARAMETERS\n"
        text += "-----------------------------------\n"
        text += "B      : " + "" if self.debye_waller_factor is None else self.debye_waller_factor.to_text() + "\n"
        text += "use LP : " + str(self.use_lorentz_polarization_factor) + "\n"
        text += "-----------------------------------\n"

        return text