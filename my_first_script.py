from math import *
import json
with open('parallelepipeds.json','r') as f:
  data=json.load(f)
pict = """
MY FIRST SKRIPT

    /------/
   /      /|
  /      / |
 /------/  |
 |      |  /
 |      | /
 |______|/

I LOVE PYTHON
"""
print(pict)
def charac(paralel:dict):
  a_=int(paralel[f'figure_{i}']['a'])
  b_=int(paralel[f'figure_{i}']['b'])
  c_=int(paralel[f'figure_{i}']['c'])
  diagon=(a_**2+b_**2+c_**2)**0.5
  volume=a_*b_*c_
  area=2*a_*b_+ 2*b_*c_ + 2*a_*c_
  alpha=degrees(acos(a_/(diagon)))
  beta=degrees(acos(b_/(diagon)))
  gamma=degrees(acos(c_/(diagon)))
  radius=(diagon)/2
  volume_described_sphere=(4*pi*radius**3)/3
  return {'diag':str(diagon),'volume':str(volume),'surface_area':str(area),'alpha':str(alpha),'beta':str(beta),'gamma':str(gamma),'radius_described_sphere':str(radius),
          'volume_described_sphere': str(volume_described_sphere)}
characteristics={}
sumdiag=0
sumvol=0
sumsurfac=0
sumalpha=0
sumbetta=0
sumgamma=0
sumrad=0
sumvolsph=0
lenn=len(data)
for i in range(1,len(data)+1):
  characteristics[f'figure_{i}']=charac(data)
  sumdiag+=float(characteristics[f'figure_{i}']['diag'])
  sumvol+=float(characteristics[f'figure_{i}']['volume'])
  sumsurfac+=float(characteristics[f'figure_{i}']['surface_area'])
  sumalpha+=float(characteristics[f'figure_{i}']['alpha'])
  sumbetta+=float(characteristics[f'figure_{i}']['beta'])
  sumgamma+=float(characteristics[f'figure_{i}']['gamma'])
  sumrad+=float(characteristics[f'figure_{i}']['radius_described_sphere'])
  sumvolsph+=float(characteristics[f'figure_{i}']['volume_described_sphere'])
with open('characteristics.json','w') as fp:
  json.dump(characteristics,fp,indent=4)
print(f'Total number of figures: {len(data)}')
print()
statistics={"avg_diag": str(sumdiag/len(characteristics)),
        "avg_volume": str(sumvol/len(characteristics)) ,
        "avg_surface_area":str(sumsurfac/lenn) ,
        "avg_alpha": str(sumalpha/lenn),
        "avg_beta": str(sumbetta/lenn),
        "avg_gamma": str(sumgamma/lenn),
        "avg_radius_described_sphere": str(sumrad/lenn),
        "avg_volume_described_sphere": str(sumvolsph/lenn)}
print('Средняя диагональ = '+str(sumdiag/len(characteristics)))
print('Средний объём = '+str(sumvol/len(characteristics)))
print('Средняя площадь = '+str(sumsurfac/lenn))
print('Средний угол альфа = '+str(sumalpha/lenn))
print('Средний угол бета = '+str(sumbetta/lenn))
print('Средний угол гамма = '+str(sumgamma/lenn))
print('Средний радиус описанной окружности =' +str(sumrad/lenn))
print('Средний объём описанной окружности = '+str(sumvolsph/lenn))
with open('statistics.json','w') as fp:
  json.dump(statistics,fp,indent =4 )