import os, sys

from PyQt5.QtWidgets import QMessageBox, QScrollArea, QTableWidget, QApplication
from PyQt5.QtCore import Qt

from silx.gui.plot.PlotWindow import PlotWindow

from Orange.widgets.settings import Setting
from Orange.widgets import gui as orangegui

from orangecontrib.xrdanalyzer.util.widgets.ow_generic_widget import OWGenericWidget
from orangecontrib.xrdanalyzer.util.gui.gui_utility import gui, ShowTextDialog
from orangecontrib.xrdanalyzer.util import congruence

from orangecontrib.xrdanalyzer.model.diffraction_pattern import DiffractionPattern, DiffractionPatternFactory

from orangecontrib.xrdanalyzer.controller.fit.fit_parameter import FitParameter
from orangecontrib.xrdanalyzer.controller.fit.fit_global_parameters import FitGlobalParameters
from orangecontrib.xrdanalyzer.controller.fit.init.fit_initialization import FitInitialization
from orangecontrib.xrdanalyzer.controller.fit.init.crystal_structure import CrystalStructure, Reflection, Simmetry
from orangecontrib.xrdanalyzer.controller.fit.init.fft_parameters import FFTInitParameters

class OWFitInitialization(OWGenericWidget):

    name = "Fit Initialization"
    description = "Define Crystal Structure and FFT Parameters"
    icon = "icons/initialization.png"
    priority = 2

    want_main_area = False

    s_max = Setting(9.0)
    n_step = Setting(8196)

    a = Setting(0.0)
    #b = Setting(0.0)
    #c = Setting(0.0)

    #alpha = Setting(0.0)
    #beta = Setting(0.0)
    #gamma = Setting(0.0)

    simmetry = Setting(4)

    reflections = Setting("")

    fit_global_parameters = None

    inputs = [("Fit Global Parameters", FitGlobalParameters, 'set_data')]
    outputs = [("Fit Global Parameters", FitGlobalParameters)]

    def __init__(self):
        super().__init__(show_automatic_box=True)

        main_box = gui.widgetBox(self.controlArea,
                                 "Fit Initialization", orientation="vertical",
                                 width=self.CONTROL_AREA_WIDTH - 10, height=600)


        fft_box = gui.widgetBox(main_box,
                                 "FFT", orientation="vertical",
                                 width=self.CONTROL_AREA_WIDTH - 30)

        gui.lineEdit(fft_box, self, "s_max", "S_max [nm-1]", labelWidth=250, valueType=float)
        gui.lineEdit(fft_box, self, "n_step", "FFT Steps", labelWidth=250, valueType=float)

        crystal_box = gui.widgetBox(main_box,
                                    "Crystal Structure", orientation="vertical",
                                    width=self.CONTROL_AREA_WIDTH - 30)

        self.cb_simmetry = orangegui.comboBox(crystal_box, self, "simmetry", label="Simmetry", items=Simmetry.tuple(), callback=self.set_simmetry, orientation="horizontal")

        gui.lineEdit(crystal_box, self, "a", "Cell Parameter [nm]", labelWidth=250, valueType=float)

        reflection_box = gui.widgetBox(crystal_box,
                                       "Reflections", orientation="vertical",
                                       width=self.CONTROL_AREA_WIDTH - 50)

        orangegui.label(reflection_box, self, "h, k, l, <intensity_name> int <, min value, max value>")

        self.scrollarea = QScrollArea(reflection_box)
        self.scrollarea.setMaximumWidth(self.CONTROL_AREA_WIDTH - 85)
        self.scrollarea.setMinimumWidth(self.CONTROL_AREA_WIDTH - 85)


        self.text_area = gui.textArea(width=self.CONTROL_AREA_WIDTH - 85, readOnly=False)
        self.text_area.setText(self.reflections)

        self.scrollarea.setWidget(self.text_area)
        self.scrollarea.setWidgetResizable(1)

        reflection_box.layout().addWidget(self.scrollarea, alignment=Qt.AlignHCenter)

        button_box = gui.widgetBox(main_box,
                                   "", orientation="horizontal",
                                   width=self.CONTROL_AREA_WIDTH-25)

        gui.button(button_box,  self, "Send Fit Initialization", height=50, callback=self.send_fit_initialization)



    def set_simmetry(self):
        if not CrystalStructure.is_cube(self.cb_simmetry.currentText()):
            QMessageBox.critical(self, "Error",
                                 "Only Cubic Systems are supported",
                                 QMessageBox.Ok)

            self.simmetry = 4


    def send_fit_initialization(self):
        try:
            if not self.fit_global_parameters is None:
                self.reflections = self.text_area.toPlainText()

                congruence.checkStrictlyPositiveNumber(self.s_max, "S Max")
                congruence.checkStrictlyPositiveNumber(self.n_step, "FFT steps")
                congruence.checkEmptyString(self.reflections, "Reflections")

                crystal_structure = CrystalStructure.init_cube(a=FitParameter(value=self.a, fixed=True),
                                                               simmetry=self.cb_simmetry.currentText())

                crystal_structure.parse_reflections(self.reflections)

                self.fit_global_parameters.fit_initialization.crystal_structure = crystal_structure
                self.fit_global_parameters.fit_initialization.fft_parameters = FFTInitParameters(s_max=self.s_max,
                                                                                                 n_step=self.n_step)

                #ShowTextDialog.show_text("Output", self.fit_global_parameters.fit_initialization.crystal_structure.to_PM2K(), parent=self)

                self.send("Fit Global Parameters", self.fit_global_parameters)

        except Exception as e:
            QMessageBox.critical(self, "Error",
                                 str(e),
                                 QMessageBox.Ok)

            raise e

    def set_data(self, data):
        if not data is None:
            self.fit_global_parameters = data.duplicate()

            if self.is_automatic_run:
                self.send_fit_initialization()



if __name__ == "__main__":
    a = QApplication(sys.argv)
    ow = OWDiffractionPattern()
    ow.show()
    a.exec_()
    ow.saveSettings()
