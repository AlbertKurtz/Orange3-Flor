import numpy

from orangecontrib.xrdanalyzer.controller.fit.fit_parameter import FitParametersList

class FitGlobalParameters(FitParametersList):

    fit_initialization = None
    background_parameters = None
    instrumental_parameters = None
    lab6_tan_correction = None
    size_parameters = None
    strain_parameters = None
    free_input_parameters = None
    free_output_parameters = None

    n_max_iterations = 10
    convergence_reached = False

    def __init__(self,
                 fit_initialization = None,
                 background_parameters = None,
                 instrumental_parameters = None,
                 lab6_tan_correction = None,
                 size_parameters = None,
                 strain_parameters = None):
        super().__init__()

        self.fit_initialization = fit_initialization
        self.background_parameters = background_parameters
        self.instrumental_parameters = instrumental_parameters
        self.lab6_tan_correction = lab6_tan_correction
        self.size_parameters = size_parameters
        self.strain_parameters = strain_parameters
        self.free_input_parameters = FreeInputParameters()
        self.free_output_parameters = FreeOutputParameters()

        self.n_max_iterations = 10
        self.convergence_reached = False

    def set_n_max_iterations(self, value=10):
        self.n_max_iterations = value

    def get_n_max_iterations(self):
        return self.n_max_iterations

    def set_convergence_reached(self, value=True):
        self.convergence_reached = value

    def is_convergence_reached(self):
        return self.convergence_reached == True

    def space_parameters(self):
        return FitSpaceParameters(self)

    def get_parameters(self):
        parameters = []

        if not self.fit_initialization is None:
            parameters.extend(self.fit_initialization.get_parameters())

        if not self.background_parameters is None:
            parameters.extend(self.background_parameters.get_parameters())

        if not self.instrumental_parameters is None:
            parameters.extend(self.instrumental_parameters.get_parameters())

        if not self.lab6_tan_correction is None:
            parameters.extend(self.lab6_tan_correction.get_parameters())

        if not self.size_parameters is None:
            parameters.extend(self.size_parameters.get_parameters())

        if not self.strain_parameters is None:
            parameters.extend(self.strain_parameters.get_parameters())

        return parameters

    def tuple(self):
        tuple = []

        if not self.fit_initialization is None:
            tuple.extend(self.fit_initialization.tuple())

        if not self.background_parameters is None:
            tuple.extend(self.background_parameters.tuple())

        if not self.instrumental_parameters is None:
            tuple.extend(self.instrumental_parameters.tuple())

        if not self.lab6_tan_correction is None:
            tuple.extend(self.lab6_tan_correction.tuple())

        if not self.size_parameters is None:
            tuple.extend(self.size_parameters.tuple())

        if not self.strain_parameters is None:
            tuple.extend(self.strain_parameters.tuple())

        return tuple

    def append_to_tuple(self, parameters, boundaries):

        if not self.fit_initialization is None:
            parameters, boundaries = self.fit_initialization.append_to_tuple(parameters, boundaries)

        if not self.background_parameters is None:
            parameters, boundaries = self.background_parameters.append_to_tuple(parameters, boundaries)

        if not self.instrumental_parameters is None:
            parameters, boundaries = self.instrumental_parameters.append_to_tuple(parameters, boundaries)

        if not self.lab6_tan_correction is None:
            parameters, boundaries = self.lab6_tan_correction.append_to_tuple(parameters, boundaries)

        if not self.size_parameters is None:
            parameters, boundaries = self.size_parameters.append_to_tuple(parameters, boundaries)

        if not self.strain_parameters is None:
            parameters, boundaries = self.strain_parameters.append_to_tuple(parameters, boundaries)

        return parameters, boundaries

    def to_text(self):
        
        text = "FIT GLOBAL PARAMETERS\n"
        text += "###################################\n\n"
        
        if not self.fit_initialization is None:
            text += self.fit_initialization.to_text()

        if not self.background_parameters is None:
            text += self.background_parameters.to_text()
            
        if not self.instrumental_parameters is None:
            text += self.instrumental_parameters.to_text()
            
        if not self.lab6_tan_correction is None:
            text += self.lab6_tan_correction.to_text()

        if not self.size_parameters is None:
            text += self.size_parameters.to_text()

        if not self.strain_parameters is None:
            text += self.strain_parameters.to_text()
        
        text += "\n###################################\n"

        text += self.free_input_parameters.to_text()
        text += self.free_output_parameters.to_text()

        return text

    def evaluate_functions(self):
        if self.has_functions() or self.free_output_parameters.get_parameters_count() > 0:
            python_code = "import numpy\nfrom numpy import *\n\n"

            python_code += self.free_input_parameters.to_python_code()

            python_code += self.get_available_parameters()

            parameters_dictionary_fit, code_fit = self.get_functions_data()
            parameters_dictionary_out, code_out = self.free_output_parameters.get_functions_data()

            python_code += code_fit
            python_code += code_out

            parameters_dictionary = {}
            parameters_dictionary.update(parameters_dictionary_fit)
            parameters_dictionary.update(parameters_dictionary_out)

            exec(python_code, parameters_dictionary)

            self.set_functions_values(parameters_dictionary)
            self.free_output_parameters.set_functions_values(parameters_dictionary)

    def duplicate(self):
        fit_global_parameters = FitGlobalParameters(fit_initialization=None if self.fit_initialization is None else self.fit_initialization.duplicate(),
                                   background_parameters=None if self.background_parameters is None else self.background_parameters.duplicate(),
                                   instrumental_parameters=None if self.instrumental_parameters is None else self.instrumental_parameters.duplicate(),
                                   lab6_tan_correction=None if self.lab6_tan_correction is None else self.lab6_tan_correction.duplicate(),
                                   size_parameters=None if self.size_parameters is None else self.size_parameters.duplicate(),
                                   strain_parameters=None if self.strain_parameters is None else self.strain_parameters.duplicate())

        fit_global_parameters.free_input_parameters = self.free_input_parameters.duplicate()
        fit_global_parameters.free_output_parameters = self.free_output_parameters.duplicate()

        return fit_global_parameters

class FitSpaceParameters:
    def __init__(self, fit_global_parameters):
        s_max   = fit_global_parameters.fit_initialization.fft_parameters.s_max
        n_steps = fit_global_parameters.fit_initialization.fft_parameters.n_step

        self.ds = s_max/(n_steps - 1)
        self.dL = 1 / (2 * s_max)

        self.L_max = (n_steps - 1) * self.dL
        self.L = numpy.linspace(self.dL, self.L_max + self.dL, n_steps)



from orangecontrib.xrdanalyzer.controller.fit.fit_parameter import FitParameter, FreeInputParameters, FreeOutputParameters, Boundary
from orangecontrib.xrdanalyzer.controller.fit.init.fit_initialization import FitInitialization
from orangecontrib.xrdanalyzer.controller.fit.init.crystal_structure import CrystalStructure, Reflection
from orangecontrib.xrdanalyzer.controller.fit.init.fft_parameters import FFTInitParameters
from orangecontrib.xrdanalyzer.controller.fit.instrument.background_parameters import ChebyshevBackground
from orangecontrib.xrdanalyzer.controller.fit.instrument.instrumental_parameters import Caglioti, Lab6TanCorrection
from orangecontrib.xrdanalyzer.controller.fit.microstructure.size import SizeParameters, Distribution, Shape
from orangecontrib.xrdanalyzer.controller.fit.microstructure.strain import InvariantPAHLaueGroup14, InvariantPAH

if __name__ == "__main__":

    fit_global_parameters = FitGlobalParameters()

    fit_global_parameters.free_input_parameters.set_parameter("A", 10)
    fit_global_parameters.free_input_parameters.set_parameter("C", 20)

    parameter_prefix = Caglioti.get_parameters_prefix()
    fit_global_parameters.instrumental_parameters = Caglioti(a=FitParameter(parameter_name=parameter_prefix + "a", value=0.5, boundary=Boundary(min_value=-10, max_value=10)),
                                                             b=FitParameter(parameter_name=parameter_prefix + "b", value=0.001, boundary=Boundary(min_value=0, max_value=10)),
                                                             c=FitParameter(parameter_name=parameter_prefix + "c", function=True, function_value="numpy.exp(A +C)"),
                                                             U=FitParameter(parameter_name=parameter_prefix + "U", function=True, function_value="numpy.exp(-(A +C))"),
                                                             V=FitParameter(parameter_name=parameter_prefix + "V", value=0.001, fixed=True),
                                                             W=FitParameter(parameter_name=parameter_prefix + "W", value=-0.001, fixed=True))

    parameter_prefix = InvariantPAH.get_parameters_prefix()
    fit_global_parameters.strain_parameters = InvariantPAHLaueGroup14(aa=FitParameter(parameter_name=parameter_prefix + "aa", value=2.0, boundary=Boundary(min_value=0, max_value=10)),
                                                                      bb=FitParameter(parameter_name=parameter_prefix + "bb", value=3.0, boundary=Boundary(min_value=0, max_value=10)),
                                                                      e1=FitParameter(parameter_name=parameter_prefix + "e1", function=True, function_value=parameter_prefix + "aa + " + parameter_prefix + "bb"),
                                                                      e6=FitParameter(parameter_name=parameter_prefix + "e6", function=True, function_value=parameter_prefix + "aa**2 + " + parameter_prefix + "bb**2"))


    fit_global_parameters.free_output_parameters.set_formula("out1 = caglioti_U + numpy.abs(caglioti_W)")

    fit_global_parameters.evaluate_functions()

    print(fit_global_parameters.to_text())

    '''
    free_p = FreeInputParameters()

    free_p.set_parameter("A", 10)
    free_p.set_parameter("C", 20)

    free_parameters_python_text = free_p.to_python_code()


    parameter = FitParameter(parameter_name="param1", function=True, function_value="numpy.exp(A +C)")

    out = {parameter.parameter_name : numpy.nan}

    exec("import numpy\n\n" + free_parameters_python_text + parameter.to_python_code(), out)

    parameter.set_value(float(out[parameter.parameter_name]))

    print("OUTPUT", parameter.value)
    '''
