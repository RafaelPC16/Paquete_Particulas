# Definimos la clase en donde agregaremos los valores importantes de cada partícula como su carga, masa, spin y qué tipo 
# de partícula es.
class Particle():
    def __init__(self, nombre, carga, masa, spin, tipo, momento_magnetico, vida_media):
        self.n = nombre
        self.c = carga
        self.m = masa
        self.s = spin
        self.t = tipo
        self.mm = momento_magnetico
        self.v = vida_media
# Creamos una función la cual nos arrojará toda la información que querramos saber de la partícula que esté en la clase.
    def properties(self):
        str_properties = f'particula: {self.n}\n' + f'tipo: {self.t}\n' + (
            f'carga: {str(self.c)} e\n' +
            f'masa: {str(self.m)} MeV/c^2\n' +
            f'spin: {str(self.s)}' +
            f'momento_magnetico: {str(self.mm)}' + 
            f'vida_media: {str(self.v)}'
        )
        print(str_properties)

# Definimos a los leptones
electron = Particle(nombre = 'electrón',carga = -1, masa = 0.511, spin = '\u00B1 1/2', tipo = 'Lepton', momento_magnetico = 1159.65e-6, vida_media = 6.6e28)
muon = Particle(nombre = 'muon',carga = -1, masa = 105.65, spin = '\u00B1 1/2', tipo = 'Lepton', momento_magnetico = 11659205e-10, vida_media = 2.19e-6)
Tau = Particle(nombre = 'Tau',carga = -1, masa = 1776.93, spin = '\u00B1 1/2', tipo = 'Lepton', momento_magnetico = 0.024, vida_media = 290e-15)
e_neutrino = Particle(nombre = 'Neutrino electrón',carga = 0, masa = '<0.8', spin = '\u00B1 1/2', tipo = 'Lepton', momento_magnetico = 0.064e-10, vida_media = 300)
m_neutrino = Particle(nombre = 'Neutrino muón', carga = 0, masa = '<0.8', spin = '\u00B1 1/2', tipo = 'Lepton', momento_magnetico = 0.064e-10, vida_media = 7e9)
t_neutrino = Particle(nombre = 'Neutrino tau',carga = 0, masa = '<0.8', spin = '\u00B1 1/2', tipo = 'Lepton', momento_magnetico = 0.064e-10, vida_media = 15.4)

# Definimos a los Quarks
up = Particle(nombre = 'Quark up',carga = 2/3, masa = '2.16', spin = '+1/2', tipo = 'Quark', momento_magnetico = 0, vida_media = 0)
down = Particle(nombre = 'Quark down',carga = -1/3, masa = '4.70', spin = '-1/2', tipo = 'Quark', momento_magnetico = 0, vida_media = 0)
strange = Particle(nombre = 'Quark strange',carga = -1/3, masa = '93.5', spin = '0', tipo = 'Quark', momento_magnetico = 0, vida_media = 0)
charm = Particle(nombre = 'Quark charm',carga = 2/3, masa = '1273', spin = '+1/2', tipo = 'Quark', momento_magnetico = 0, vida_media = 0)
top= Particle(nombre = 'Quark up',carga = 2/3, masa = '172.57', spin = '0', tipo = 'Quark', momento_magnetico = 0, vida_media = 0)
bottom = Particle(nombre = 'Quark up',carga = -1/3, masa = '4183', spin = '+1/2', tipo = 'Quark', momento_magnetico = 0, vida_media = 0)

# Definimos a los Bosones
foton = Particle(nombre = 'Fotón',carga = 0, masa = '<1x10^{-18}', spin = 1, tipo = 'Boson', momento_magnetico = 0, vida_media = 0)
gluon = Particle(nombre = 'Gluón',carga = 0, masa = 0, spin = 1, tipo = 'Boson', momento_magnetico = 0, vida_media = 0)
W = Particle(nombre = 'W',carga = '\u00B1 1', masa = '80369.2', spin = 1 , tipo = 'Boson', momento_magnetico = 0, vida_media = 0)
Z = Particle(nombre = 'Z',carga = 0, masa = '91900', spin = 1, tipo = 'Boson', momento_magnetico = 0, vida_media = 0)
Higgs = Particle(nombre = 'Bosón de Higgs',carga = 0, masa = '125200', spin = 0, tipo = 'Boson', momento_magnetico = 0, vida_media = 0)

#Creamos una función que permita conocer la carga total de un sistema conformado por varias partículas contenidas en la clase.
def carga_total(particles):
  tot = 0
  for p in particles:
    if isinstance(p, Particle):
      tot += p.c
    else:
      print(p, ' esto no pertenece a la clase Particle')
  return tot

import numpy as np


class StandardModelParticle:
    def __init__(self, name, symbol, mass, charge, spin, type_of_particle, is_antiparticle=False):
        """
        Clase que representa una partícula del modelo estándar.
        
        :param name: Nombre de la partícula.
        :param symbol: Símbolo de la partícula.
        :param mass: Masa de la partícula en MeV/c^2.
        :param charge: Carga de la partícula en unidades de la carga del electrón.
        :param spin: Espín de la partícula.
        :param type_of_particle: Tipo de partícula, como 'fermion' o 'boson'.
        :param is_antiparticle: Booleano que indica si es la antipartícula.
        """
        self.name = name
        self.symbol = symbol
        self.mass = mass
        self.charge = charge
        self.spin = spin
        self.type_of_particle = type_of_particle
        self.is_antiparticle = is_antiparticle

    def info(self):
        """Devuelve una descripción de la partícula."""
        return (f"{self.name} ({self.symbol}) - Masa: {self.mass} MeV/c^2, Carga: {self.charge}, "
                f"Espín: {self.spin}, Tipo: {self.type_of_particle}, Antipartícula: {self.is_antiparticle}")

"""Clase Rotation del paquete pyforce"""

import numpy as np
from .three_vector import ThreeVector

class Rotation:
    def __init__(self, angle, axis):
        """
        Inicializa una rotación 3D dado un ángulo y un eje de rotación.
        :param angle: Ángulo de rotación en radianes.
        :param axis: Eje de rotación como un ThreeVector.
        """
        if not isinstance(axis, ThreeVector):
            raise ValueError("El eje debe ser un ThreeVector")
        
        # Normaliza el eje de rotación
        norm = np.linalg.norm(axis.vector)
        if norm == 0:
            raise ValueError("El eje de rotación no puede ser el vector cero")
        
        axis_normalized = axis.vector / norm
        cos_a = np.cos(angle)
        sin_a = np.sin(angle)

        # Matriz de rotación utilizando la fórmula de Rodrigues
        self.rotation_matrix = np.array([
            [cos_a + axis_normalized[0]**2 * (1 - cos_a),
             axis_normalized[0] * axis_normalized[1] * (1 - cos_a) - axis_normalized[2] * sin_a,
             axis_normalized[0] * axis_normalized[2] * (1 - cos_a) + axis_normalized[1] * sin_a],

            [axis_normalized[1] * axis_normalized[0] * (1 - cos_a) + axis_normalized[2] * sin_a,
             cos_a + axis_normalized[1]**2 * (1 - cos_a),
             axis_normalized[1] * axis_normalized[2] * (1 - cos_a) - axis_normalized[0] * sin_a],

            [axis_normalized[2] * axis_normalized[0] * (1 - cos_a) - axis_normalized[1] * sin_a,
             axis_normalized[2] * axis_normalized[1] * (1 - cos_a) + axis_normalized[0] * sin_a,
             cos_a + axis_normalized[2]**2 * (1 - cos_a)]
        ], dtype=complex)

    def apply(self, vector):
        """Aplica la rotación al ThreeVector dado."""
        if not isinstance(vector, ThreeVector):
            raise ValueError("El vector debe ser una instancia de ThreeVector")
        rotated_vector = self.rotation_matrix @ vector.vector
        return ThreeVector(*rotated_vector)

    def __repr__(self):
        return f"Rotation(rotation_matrix=\n{self.rotation_matrix})"