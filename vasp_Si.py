"""
Run some VASP tests to ensure that the VASP calculator works. This
is conditional on the existence of the VASP_COMMAND or VASP_SCRIPT
environment variables

"""
import os
import shutil
from ase.test.vasp import installed

assert installed()

# ***************************************************************************************************

from ase import Atoms
from ase.build import bulk
from ase.io import write
from ase.dft.kpoints import special_paths
from ase.calculators.vasp import Vasp
import numpy as np

# ***************************************************************************************************

import pymatgen as mg
from pymatgen.io.vasp.outputs import BSVasprun, Vasprun
# from pymatgen import Spin
from pymatgen.electronic_structure.plotter import BSPlotter, BSDOSPlotter, DosPlotter
from pymatgen.symmetry.bandstructure import HighSymmKpath

import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
from matplotlib.gridspec import GridSpec
# matplotlib inline

# ***************************************************************************************************

def array_almost_equal(a1, a2, tol=np.finfo(type(1.0)).eps):
    """Replacement for old numpy.testing.utils.array_almost_equal."""
    return (np.abs(a1 - a2) < tol).all()

# ***************************************************************************************************
# Si = bulk('Si', 'fcc', a=3.9, cubic=True)
a0 = 3.9
Si = Atoms('Si', [(0, 0, 0)],
           pbc=True)
b = a0 / 2
Si.set_cell([(0, b, b),
             (b, 0, b),
             (b, b, 0)], scale_atoms=True)

# co = Atoms('CO', positions=[(0, 0, 0), (0, 0, d)],
#              pbc=True)
# co.center(vacuum=5.)
# ***************************************************************************************************

path = special_paths['fcc']

def check_kpoints_line(n, contents):
    """Assert the contents of a line"""
    with open('KPOINTS', 'r') as f:
        lines = f.readlines()
        assert lines[n] == contents

calc = Vasp(system = 'FCC_Si',
            xc = 'PBE',
            encut = 240,
            ismear = 0,
            sigma = 0.1,
            istart = 0,
            nbands = 20,
            lwave = False,
            gamma=False, 
            kpts=(11, 11, 11))

calc.write_kpoints()
check_kpoints_line(2, 'Monkhorst-Pack\n')
check_kpoints_line(3, '11 11 11 \n')

Si.set_calculator(calc)
en = Si.get_potential_energy()
# write('vasp_co.traj', co)
# assert abs(en + 14.918933) < 5e-3

# Secondly, calculate DOS that restart from the previously created VASP output works
if not os.path.exists('DOS'):
   os.mkdir('DOS')

if not os.path.exists('Band'):
   os.mkdir('Band')

files = ['CHG', 'CHGCAR', 'POSCAR', 'INCAR', 'CONTCAR',
         'DOSCAR', 'EIGENVAL', 'IBZKPT', 'OSZICAR',
         'OUTCAR', 'POTCAR', 'vasprun.xml',
         'WAVECAR']
         
for f in files:
    try:
        shutil.copy(f,'DOS')
        shutil.copy(f,'Band')
    except OSError:
        pass

os.chdir('DOS')

Si2 = Si
calc2 = Vasp(system = 'FCC_Si',
#            restart = True,
            xc = 'PBE',
            encut = 240,
            ismear = -5,
            sigma = 0.0,
            nbands = 20,
            icharg = 11,
            lorbit = 11,
            gamma=True,
            kpts=(23, 23, 23))

calc2.write_kpoints()
# check_kpoints_line(2, 'Monkhorst-Pack\n')
# check_kpoints_line(3, '24 24 24 \n')

Si2.set_calculator(calc2)
en2 = Si2.get_potential_energy()

# Thirdly, calculate Band that restart from the previously created VASP output works
os.chdir('../Band')

Si3 = Si
# ***************************************************************************************************
# shutil.copy('../KPOINTS_BAND','KPOINTS')
kpaths = HighSymmKpath(mg.Structure.from_file("CONTCAR")).get_kpoints(1,False)

KPOINTS_BAND = open("./KPOINTS", 'w')

i = 0
print >> KPOINTS_BAND, 'KPOINTS for BandStrucure:' 
print >> KPOINTS_BAND, 20
print >> KPOINTS_BAND, 'Line'
print >> KPOINTS_BAND, 'reciprocal'
for j in kpaths[1]:
    if kpaths[1][i] != '':
        print >> KPOINTS_BAND,kpaths[0][i][0],kpaths[0][i][1],kpaths[0][i][2], kpaths[1][i]
    i=i+1
# for i in kpathsi:
KPOINTS_BAND.close()
# ***************************************************************************************************

calc3 = Vasp(system = 'FCC_Si',
#            restart = True,
            xc = 'PBE',
            encut = 240,
            ismear = 0,
            sigma = 0.1,
            nbands = 20,
            icharg = 11,
            lorbit = 11,
            kspacing = 1)

Si3.set_calculator(calc3)
en3 = Si2.get_potential_energy()

# ***************************************************************************************************

os.chdir('..')

dosrun = Vasprun("DOS/vasprun.xml", parse_dos=True)
dos = dosrun.complete_dos
print("E_Fermi=%f%3s" % (dosrun.efermi, 'eV'))
# print(dos.efermi)

dosplot1 = DosPlotter(sigma=0.05)
dosplot1.add_dos("Total DOS", dos)
plt = dosplot1.get_plot(xlim=(-18, 15))
plt.grid()
plt.savefig("pymatgen_DOS.eps", format="eps")
plt.show()

plt.close()

# bsrun = BSVasprun("Band/vasprun.xml", parse_projected_eigen=True)
bsrun = BSVasprun("Band/vasprun.xml")
bs = bsrun.get_band_structure("Band/KPOINTS")
bsplot = BSPlotter(bs)
plt = bsplot.get_plot(bs)
bsplot.get_plot(ylim=(-18, 15), zero_to_efermi=True)
plt.grid()
plt.savefig("pymatgen_Band.eps", format="eps")
plt.show()

plt.close()

# run = BSVasprun("Band/vasprun.xml", parse_projected_eigen=True)
# dosrun = Vasprun("DOS/vasprun.xml", parse_dos=True)
# dosrun = Vasprun("vasprun.xml", parse_dos=True)
# dos = dosrun.complete_dos

# bs = run.get_band_structure("Band/KPOINTS")
bsdosplot = BSDOSPlotter(
#            bs_projection="elements", 
#            dos_projection="elements", 
            vb_energy_range=18,
            cb_energy_range=15,
            egrid_interval=2.5
)
plt = bsdosplot.get_plot(bs, dos=dos)
# plt = bsdosplot.get_plot(bs)
# plt.show()
plt.savefig("pymatgen_Band-DOS.eps", format="eps")
# plt.savefig("Band_DOS", dpi=100)
plt.show()

plt.close()


# ***************************************************************************************************
# Need tolerance of 1e-14 because VASP itself changes coordinates
# slightly between reading POSCAR and writing CONTCAR even if no ionic
# steps are made.
# assert array_almost_equal(co.positions, co2.positions, 1e-14)

# assert en - co2.get_potential_energy() == 0.
# assert array_almost_equal(calc.get_stress(co), calc2.get_stress(co2))
# assert array_almost_equal(calc.get_forces(co), calc2.get_forces(co2))
# assert array_almost_equal(calc.get_eigenvalues(), calc2.get_eigenvalues())
# assert calc.get_number_of_bands() == calc2.get_number_of_bands()
# assert calc.get_xc_functional() == calc2.get_xc_functional()

# Cleanup
calc.clean()
