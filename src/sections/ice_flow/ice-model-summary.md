# Modeling using ice models
In this segment, we provide a concise overview of various ice models, detailing their underlying assumptions and the consequential implications. These mathematical expressions play a crucial role in simulating ice flow within computer models. It's essential to ensure a determinant system by balancing the number of equations with the number of unknowns.

## 1. High-Fidelity Models:
### Stokes Flow Model:

The stress balance equations known as the Stokes Equations have 4 variables, the velocity vector and pressure. Note: we make an assumption that the advection term is negligible which is a very resonable assumption 

$$
0 =  \frac{\partial \sigma_{xx}}{\partial x}+\frac{\partial \tau_{yx}}{\partial y}+\frac{\partial \tau_{zx}}{\partial z}
$$

$$
0 = \frac{\partial \sigma_{yy}}{\partial y}+\frac{\partial \tau_{xy}}{\partial x}+\frac{\partial \tau_{zy}}{\partial z}.
$$

$$
0 = -\rho g + \frac{\partial \sigma_{zz}}{\partial z}+\frac{\partial \tau_{yz}}{\partial y}+\frac{\partial \tau_{xz}}{\partial x}
$$

To close these equations we need the mass conservation/ continuity equation

$$
\nabla\cdot\underline{u} = 0
$$

and rheological properties and models like the Glen's flow law which relates strain rate and stress.

These equations are integrated with appropriate boundary conditions to ensure their solvability.

## 2. Intermediate-Fidelity Models:
### Blatter-Pattyn Model (BP Model):


The Blatter-Pattyn (BP) stress conservation equations make simplifying assumptions in the stokes equations. We have two unknowns, the velocity vector $\underbar{u} = (u(x,y,z),v(x,y,z))$ and surface elevation $s$ 

$$
4\frac{\partial }{\partial x}  \left(\eta \frac{\partial u}{\partial x} \right)+ \frac{\partial }{\partial z} \left(\eta \frac{\partial u}{\partial z} \right) = \rho g \frac{\partial s}{\partial x} 
$$

$$
4\frac{\partial }{\partial yx}  \left(\eta \frac{\partial v}{\partial y} \right)+ \frac{\partial }{\partial z} \left(\eta \frac{\partial v}{\partial z} \right) = \rho g \frac{\partial s}{\partial y} 
$$

This is combined with the depth integrated mass balance equation to ensure solvability.


The list of assumptions and their implications on the applicability of the model is as follows:

| Assumption  | Implication | 
|-------|-----|
| 2D assumption, infinite y dimension |   |
| Horizontal gradient of shear stress is small ($\frac{\partial \tau_{xz}}{\partial x}$) |   |
| Integrate $z$ stress equation vertically |   |
| Horizontal gradient of vertical velocity is small ($\frac{\partial w}{\partial x}$) |   |


### Shallow Shelf Approximation (SSA):

The Shallow Shelf Approximation (SSA) is derived from the BP by making further simplifying assumptions. The resulting stress balance equation is as follows:

$$
2 \frac{\partial }{\partial x} \left( A^{-\frac{1}{n}} H\left(\frac{\partial u}{\partial x}\right)^{\frac{1}{n}-1} \frac{\partial u}{\partial x} \right) - \tau_b = \rho g H\frac{\partial s}{\partial x}.
$$

$$
2 \frac{\partial }{\partial y} \left( A^{-\frac{1}{n}} H\left(\frac{\partial v}{\partial y}\right)^{\frac{1}{n}-1} \frac{\partial v}{\partial y} \right) - \tau_b = \rho g H\frac{\partial s}{\partial y}.
$$

This equation has two unknowns, $\underbar{u} = (u(x,y),v(x,y))$ and H.

This is combined with the depth integrated mass balance equation to ensure solvability.


| Assumption  | Implication | 
|-------|-----|
| 2D assumption, infinite y dimension |   |
| Horizontal gradient of shear stress is small ($\frac{\partial \tau_{xz}}{\partial x}$) |   |
| Integrate $z$ stress equation vertically |   |
| Horizontal gradient of vertical velocity is small ($\frac{\partial w}{\partial x}$) |   |
| Vertical shear $\tau_{zx}$ is small |   |
| Integrate $x$ stress equation vertically |   |
| Surface boundary condition of  $\tau_{zx}(s) = 0$ |   |
| assume $\frac{ds}{dx} = \frac{db}{dx} = 0$ |   |
| assume $\dot\epsilon_{E} = \dot\epsilon_{xx}$ |   |
| $\frac{\partial u}{\partial x}$ is uniform in depth|  |

## 3. Lower-Fidelity Models:
### Shallow Ice Approximation (SIA):

The Shallow Ice Approximation is derived from BP by making some more simplifying assumptions. The stress balance equation results in:

$$
u(\zeta)=  \frac{2A}{n+1} \left(\rho g \alpha \right)^n  H^{n+1} \left( 1- \zeta^{n+1} \right)
$$

This equation has H as the only unknown (diagonastic equation).
This is combined with the depth integrated mass balance equation to determine the evolution of ice thickness (prognostic equation).



| Assumption  | Implication | 
|-------|-----|
| 2D assumption, infinite y dimension |   |
| Horizontal gradient of shear stress is small ($\frac{\partial \tau_{xz}}{\partial x}$) |   |
| Integrate $z$ stress equation vertically |   |
| Horizontal gradient of vertical velocity is small ($\frac{\partial w}{\partial x}$) |   |
| Neglect the horizontal extenstional stresses ($\tau_{xx}$)|  |
| Integrate $x$ stress equation vertically| |
| $\frac{\partial u}{\partial x}=0$/$\tau_E = \tau_{xz}$| |
| Assume that $\frac{\partial w}{\partial x}$ is much smaller than $\frac{\partial u}{\partial z}$| |
| Vertically integrate the equation for $\tau_{zx}$ to get $u$ | |

## Depth integrated mass balance equation assumptions

$$
\dot{H} = a -  m - \nabla_h\cdot\underline{q},
$$

where $a$ is the accumulation rate, $m$ is the melting rate and $\nabla_h = <\frac{\partial}{\partial x}, \frac{\partial }{\partial y}>$ . This is derived from the $\nabla\cdot\underline{u} = 0$ by making the following assumptions.


| Assumption  | Implication | 
|-------|-----|
| Integrate vertically  |   |
