# namespace declaration
__import__("pkg_resources").declare_namespace(__name__)


###################################################################
# DO NOT TOUCH THIS CODE -- BEGIN
###################################################################
import threading

def synchronized_method(method):

    outer_lock = threading.Lock()
    lock_name = "__"+method.__name__+"_lock"+"__"

    def sync_method(self, *args, **kws):
        with outer_lock:
            if not hasattr(self, lock_name): setattr(self, lock_name, threading.Lock())
            lock = getattr(self, lock_name)
            with lock:
                return method(self, *args, **kws)

    return sync_method

class Singleton:

    def __init__(self, decorated):
        self._decorated = decorated

    @synchronized_method
    def Instance(self):
        try:
            return self._instance
        except AttributeError:
            self._instance = self._decorated()
            return self._instance

    def __call__(self):
        raise TypeError('Singletons must be accessed through `Instance()`.')

    def __instancecheck__(self, inst):
        return isinstance(inst, self._decorated)

###################################################################
# DO NOT TOUCH THIS CODE -- END
###################################################################

###################################################################
# RECOVERY FROM FAILED INSTALLATIONS WITH CYTHON

from Orange.canvas import resources
import shutil

try:
    import orangecontrib.xrdanalyzer.controller.fit.wppm_functions
except:
    wonder_dir = resources.package_dirname("orangecontrib.xrdanalyzer")

    try:
        shutil.copyfile(wonder_dir + "/recovery/controller/fit/wppm_functions.py"             , wonder_dir + "/controller/fit/wppm_functions.py"        )
        shutil.copyfile(wonder_dir + "/recovery/controller/fit/fitters/fitter_minpack.py"     , wonder_dir + "/controller/fit/fitters/fitter_minpack.py")
        shutil.copyfile(wonder_dir + "/recovery/controller/fit/fitters/fitter_minpack_util.py", wonder_dir + "/controller/fit/fitters/fitter_minpack_util.py")
    except:
        pass