import numpy
import orangecontrib.xrdanalyzer.util.congruence as congruence

data = numpy.array([['Ac', 'Actinium', 89, 227],
                    ['Ag', 'Silver', 47, 107.868],
                    ['Al', 'Aluminum', 13, 26.98154],
                    ['Am', 'Americium', 95, 243],
                    ['Ar', 'Argon', 18, 39.948],
                    ['As', 'Arsenic', 33, 74.9216],
                    ['At', 'Astatine', 85, 210],
                    ['Au', 'Gold', 79, 196.9665],
                    ['B', 'Boron', 5, 10.81],
                    ['Ba', 'Barium', 56, 137.33],
                    ['Be', 'Beryllium', 4, 9.01218],
                    ['Bi', 'Bismuth', 83, 208.9804],
                    ['Bk', 'Berkelium', 97, 247],
                    ['Br', 'Bromine', 35, 79.904],
                    ['C', 'Carbon', 6, 12.011],
                    ['Ca', 'Calcium', 20, 40.08],
                    ['Cd', 'Cadmium', 48, 112.41],
                    ['Ce', 'Cerium', 58, 140.12],
                    ['Cf', 'Californium', 98, 251],
                    ['Cl', 'Chlorine', 17, 35.453],
                    ['Cm', 'Curium', 96, 247],
                    ['Co', 'Cobalt', 27, 58.9332],
                    ['Cr', 'Chromium', 24, 51.996],
                    ['Cs', 'Cesium', 55, 132.9054],
                    ['Cu', 'Copper', 29, 63.546],
                    ['Dy', 'Dysprosium', 66, 162.50],
                    ['Er', 'Erbium', 68, 167.26],
                    ['Es', 'Einsteinium', 99, 254],
                    ['Eu', 'Europium', 63, 151.96],
                    ['F', 'Fluorine', 9, 18.998403],
                    ['Fe', 'Iron', 26, 55.847],
                    ['Fm', 'Fermium', 100, 257],
                    ['Fr', 'Francium', 87, 223],
                    ['Ga', 'Gallium', 31, 69.735],
                    ['Gd', 'Gadolinium', 64, 157.25],
                    ['Ge', 'Germanium', 32, 72.59],
                    ['H', 'Hydrogen', 1, 1.0079],
                    ['He', 'Helium', 2, 4.0026],
                    ['Hf', 'Hafnium', 72, 178.49],
                    ['Hg', 'Mercury', 80, 200.59],
                    ['Ho', 'Holmium', 67, 164.9304],
                    ['I', 'Iodine', 53, 126.9045],
                    ['In', 'Indium', 49, 114.82],
                    ['Ir', 'Iridium', 77, 192.22],
                    ['K', 'Potassium', 19, 39.0983],
                    ['Kr', 'Krypton', 36, 83.80],
                    ['La', 'Lanthanum', 57, 138.9055],
                    ['Li', 'Lithium', 3, 6.94],
                    ['Lr', 'Lawrencium', 103, 260],
                    ['Lu', 'Lutetium', 71, 174.96],
                    ['Md', 'Mendelevium', 101, 258],
                    ['Mg', 'Magnesium', 12, 24.305],
                    ['Mn', 'Manganese', 25, 54.9380],
                    ['Mo', 'Molybdenum', 42, 95.94],
                    ['N', 'Nitrogen', 7, 14.0067],
                    ['Na', 'Sodium', 11, 22.98977],
                    ['Nb', 'Niobium', 41, 92.9064],
                    ['Nd', 'Neodymium', 60, 144.24],
                    ['Ne', 'Neon', 10, 20.17],
                    ['Ni', 'Nickel', 28, 58.71],
                    ['No', 'Nobelium', 102, 259],
                    ['Np', 'Neptunium', 93, 237.0482],
                    ['O', 'Oxygen', 8, 15.9994],
                    ['Os', 'Osmium', 76, 190.2],
                    ['P', 'Phosphorous', 15, 30.97376],
                    ['Pa', 'Proactinium', 91, 231.0359],
                    ['Pb', 'Lead', 82, 207.2],
                    ['Pd', 'Palladium', 46, 106.4],
                    ['Pm', 'Promethium', 61, 145],
                    ['Po', 'Polonium', 84, 209],
                    ['Pr', 'Praseodymium', 59, 140.9077],
                    ['Pt', 'Platinum', 78, 195.09],
                    ['Pu', 'Plutonium', 94, 244],
                    ['Ra', 'Radium', 88, 226.0254],
                    ['Rb', 'Rubidium', 37, 85.467],
                    ['Re', 'Rhenium', 75, 186.207],
                    ['Rh', 'Rhodium', 45, 102.9055],
                    ['Rn', 'Radon', 86, 222],
                    ['Ru', 'Ruthenium', 44, 101.07],
                    ['S', 'Sulfur', 16, 32.06],
                    ['Sb', 'Antimony', 51, 121.75],
                    ['Sc', 'Scandium', 21, 44.9559],
                    ['Se', 'Selenium', 34, 78.96],
                    ['Si', 'Silicon', 14, 28.0855],
                    ['Sm', 'Samarium', 62, 150.4],
                    ['Sn', 'Tin', 50, 118.69],
                    ['Sr', 'Strontium', 38, 87.62],
                    ['Ta', 'Tantalum', 73, 180.947],
                    ['Tb', 'Terbium', 65, 158.9254],
                    ['Tc', 'Technetium', 43, 98.9062],
                    ['Te', 'Tellurium', 52, 127.60],
                    ['Th', 'Thorium', 90, 232.0381],
                    ['Ti', 'Titanium', 22, 47.90],
                    ['Tl', 'Thallium', 81, 204.37],
                    ['Tm', 'Thulium', 69, 168.9342],
                    ['U', 'Uranium', 92, 238.029],
                    ['Unh', 'Unnilhexium', 106, 263],
                    ['Unp', 'Unnilpentium', 105, 260],
                    ['Unq', 'Unnilquadium', 104, 260],
                    ['Uns', 'Unnilseptium', 107, 262],
                    ['V', 'Vanadium', 23, 50.9415],
                    ['W', 'Tungsten', 74, 183.85],
                    ['Xe', 'Xenon', 54, 131.30],
                    ['Y', 'Yttrium', 39, 88.9059],
                    ['Yb', 'Ytterbium', 70, 173.04],
                    ['Zn', 'Zinc', 30, 65.38],
                    ['Zr', 'Zirconium', 40, 91.22]])

def get_z_from_element(element="Si"):
    return int(data[numpy.where(data[:, 0] == element)[0], 2][0])

def get_element_from_z(z = 10):
    return data[numpy.where(data[:, 2] == str(z))[0], 0][0]


# ----------------------------------------------------
# DATA STRUCTURES
# ----------------------------------------------------

class AtomicCoordinate:
    x = 0
    y = 0
    z = 0

    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def tuple(self):
        return numpy.array([x, y, z])


class AtomVelocity:
    v_x = 0
    v_y = 0
    v_z = 0

    def __init__(self, v_x=0, v_y=0, v_z=0):
        self.v_x = v_x
        self.v_y = v_y
        self.v_z = v_z

    def tuple(self):
        return numpy.array([v_x, v_y, v_z])

class Atom:
    z_element = 0
    coordinates = None
    velocity = None
    id = 0
    coordination_number = 0
    nearest_neighbours = None

    def __init__(self,
                 z_element=1,
                 coordinates = AtomicCoordinate(),
                 velocity = AtomVelocity(),
                 id = 1,
                 coordination_number = 0):
        self.z_element = z_element
        self.coordinates = coordinates
        self.velocity = velocity
        self.id = id
        self.set_coordination_number(coordination_number)

    def set_coordination_number(self, coordination_number):
        congruence.checkPositiveNumber(coordination_number, "Coordination Number")

        self.coordination_number = coordination_number

        if self.coordination_number > 0:
            self.nearest_neighbours = numpy.zeros(self.coordination_number)
        else:
            self.nearest_neighbours = None

    def set_nearest_neighbour(self, index, id):
        self.__check_nearest_neighbour_congruence()

        if index + 1 > self.coordination_number:
            raise ValueError("Nearest Neighbour Index out of range")

        self.nearest_neighbours[index] = id

    def get_nearest_neighbour(self, index):
        self.__check_nearest_neighbour_congruence()

        if index + 1 > self.coordination_number:
            raise ValueError("Nearest Neighbour Index out of range")

        return self.nearest_neighbours[index]

    def tupla(self):
        return numpy.array([self.z_element,
                            self.coordinates.x,
                            self.coordinates.y,
                            self.coordinates.z,
                            self.velocity.v_x,
                            self.velocity.v_y,
                            self.velocity.v_z,
                            self.id,
                            self.coordination_number,
                            self.nearest_neighbours])


    def __check_nearest_neighbour_congruence(self):
        if self.coordination_number == 0:
            if not self.nearest_neighbours is None:
                raise AttributeError("Nearest Neighbours list (n=" +
                                     str(self.nearest_neighbours.size) +
                                     ") is incosistent with Coordination Number (" +
                                     str(self.coordination_number) + ")")
        else:
            if self.nearest_neighbours is None:
                raise AttributeError("Nearest Neighbours list (None) is incosistent with Coordination Number (" +
                                     str(self.coordination_number) + ")")

            elif self.nearest_neighbours.size != self.coordination_number:
                raise AttributeError("Nearest Neighbours list (n=" +
                                     str(self.nearest_neighbours.size) +
                                     ") is incosistent with Coordination Number (" +
                                     str(self.coordination_number) + ")")

# ----------------------------------------------------
# PERSISTENCY MANAGAMENT
# ----------------------------------------------------


class AtomList:

    atom_list = None

    def __init__(self, n_atoms=0):
        if n_atoms > 0:
            self.atom_list = numpy.full(n_atoms, None)
        else:
            self.atom_list = None

    def add_atom(self, atom=Atom()):
        if atom is None: raise ValueError("Atom is None")
        if not isinstance(atom, Atom): raise ValueError("atom should be of type Atom")

        if self.atom_list is None:
            self.atom_list = numpy.array([atom])
        else:
            self.atom_list.append(atom)

    def set_atom(self, index=0, atom=Atom()):
        self.__check_atom_list()

        self.atom_list[index] = atom

    def set_atoms(self, atom_list=numpy.full(0, None)):
        self.atom_list = atom_list

    def atoms_count(self):
        return 0 if self.atom_list is None else len(self.atom_list)

    def get_atom(self, index):
        self.__check_atom_list()
        return self.atom_list[index]

    def matrix(self):
        matrix = numpy.full(self.atoms_count(), None)

        for index in range(0, self.atoms_count()):
            matrix[index] = self.get_atom(index).tupla()

        return matrix

    def __check_atom_list(self):
        if self.atom_list is None:
            raise AttributeError("Atom List is not initialized")


# ----------------------------------------------------
# "PRIVATE" CLASSES (python de i sa morti cani)
# ----------------------------------------------------


class AtomListFileMultipleArrays(AtomList):

    def __init__(self, file_name=""):
        super(AtomListFileMultipleArrays, self).__init__(n_atoms=0)

        self.__initialize_from_file(file_name)

    def __initialize_from_file(self, file_name):
        with open(file_name, 'r') as xyzfile: lines = xyzfile.readlines()
        n_atoms = int(lines[0])

        if n_atoms > 0:
            self.atom_list = numpy.full(n_atoms, None)

            for i in numpy.arange(2, n_atoms+2):
                line = lines[i].split()

                atom = Atom(z_element=get_z_from_element(line[0]),
                            coordinates=AtomicCoordinate(x=float(line[1]),
                                                         y=float(line[2]),
                                                         z=float(line[3])))

                self.set_atom(index=i-2, atom=atom)

class AtomListFileNumpy(AtomList):

    def __init__(self, file_name=""):
        super(AtomListFileNumpy, self).__init__(n_atoms=0)

        self.__initialize_from_file(file_name)

    def __initialize_from_file(self, file_name):
        dt = numpy.dtype([('element', numpy.unicode, 32),
                          ('x', numpy.float32),
                          ('y', numpy.float32),
                          ('z', numpy.float32)])

        element, x, y, z = numpy.loadtxt(file_name, dtype=dt, unpack=True, skiprows=2)
        n_atoms = len(element)

        if n_atoms > 0:
            self.atom_list = numpy.full(n_atoms, None)

            for index in range(0, n_atoms):
                atom = Atom(z_element=get_z_from_element(element[index][2:-1]),
                            coordinates=AtomicCoordinate(x=x[index],
                                                         y=y[index],
                                                         z=z[index]))

                self.set_atom(index=index, atom=atom)

import os

class AtomListFactory:

    @classmethod
    def create_atom_list_from_file(cls, file_name):
        filename, file_extension = os.path.splitext(file_name)

        if file_extension == ".xyz":
            return AtomListFileMultipleArrays(file_name=file_name)
        elif file_extension == ".np":
            return AtomListFileNumpy(file_name=file_name)
        else:
            raise ValueError("File Extension not recognized")