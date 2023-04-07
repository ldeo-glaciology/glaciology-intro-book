# Two other ice flow models

So far in this chapter we started from the full stokes stress balance equations and applied the shallow ice approximation (SIA) to derive the simplest widely-used ie sheet model. 

Below we describe the derivation of two other commonly used ice-flow models the 'higher-order' Blatter-Pattyn (BP) model, and the shallow shelf approximation (SSA) model. 

## Full stokes to BP
The Blatter-Pattyn (BP) model is considered higher-order than the SIA and SSA because it retains more of the terms in the stress balance equations that those models. The following derivation of the BP model comes from the [documentation of the Community Ie Sheet model](https://cism.github.io/data/cism_documentation_v2_1.pdf).

Starting with the stokes equations
$$
\frac{\partial \sigma_{xx}}{\partial x}+\frac{\partial \tau_{yx}}{\partial y}+\frac{\partial \tau_{zx}}{\partial z} = 0
$$
 

$$
\frac{\partial \sigma_{yy}}{\partial y}+\frac{\partial \tau_{xy}}{\partial x}+\frac{\partial \tau_{zy}}{\partial z} = 0,
$$


$$
\frac{\partial \tau_{xz}}{\partial x} + \frac{\partial \tau_{yz}}{\partial y}+\frac{\partial \sigma_{zz}}{\partial z} = \rho g
$$

 we will ignore the $y$ dimension for simplicity, leaving:

$$
\frac{\partial \sigma_{xx}}{\partial x}+\frac{\partial \tau_{zx}}{\partial z} = 0
$$

$$
\frac{\partial \sigma_{zz}}{\partial z}+\frac{\partial \tau_{xz}}{\partial x} = \rho g
$$

Motivated by the fact that ice sheets, streams and shelves are much wider than they are thick, we neglect the horizontal gradient of vertical shear stresses - the 'so-called' bridging stresses - leaving

$$
\frac{\partial \sigma_{xx}}{\partial x}+\frac{\partial \tau_{zx}}{\partial z} = 0
$$

$$
\frac{\partial \sigma_{zz}}{\partial z} = \rho g.
$$

We define the deviatoric stress as 

$$
\tau_{xx} = P + \sigma_{xx},
$$

$$
\tau_{zz} = P + \sigma_{zz}, 
$$

where $P$ is the pressure. Substituting these into the stress balance equations gives:

$$
\frac{\partial \tau_{xx}}{\partial x}+\frac{\partial \tau_{zx}}{\partial z} - \frac{\partial P}{\partial x} = 0
$$

$$
\frac{\partial \tau_{zz}}{\partial z} - \frac{\partial P}{\partial z} = \rho g.
$$

Next we rearrange the $z$-direction stress balance equation (the second equation above) as

$$
\frac{\partial P}{\partial z} = -\rho g + \frac{\partial \tau_{zz}}{\partial z}
$$

and integrate vertically between the surface ($z=s$) and some height $z$:

$$
\int^0_P dP = -\rho g \int^s_z dz + \int^0_{\tau_{zz}} \frac{\partial \tau_{zz}}{\partial z} dz,
$$

where we have imposed boundary conditions at the surface of zero pressure $P$ and zero deviatoric vertical normal stress \tau_{zz}. Evaluating the integrals and rearranging, 

$$
P = \rho g(s-z) + \tau_{zz}
$$

which states that the total vertical normal stress $(P - \tau_{zz})$ is equal to the hydrostatic stress $(\rho g(s-z))$.

Substituting this into the $x$-direction stress balance equation gives

$$
\frac{\partial \tau_{xx}}{\partial x}+\frac{\partial \tau_{zx}}{\partial z} = \frac{\partial}{\partial x}\left(\rho g(s-z) + \tau_{zz}\right)
$$

$$
\frac{\partial \tau_{xx}}{\partial x}+\frac{\partial \tau_{zx}}{\partial z} = \rho g\frac{\partial s}{\partial x}+ \frac{\partial \tau_{zz}}{\partial x}
$$

Here we assume that ice is incompressible 

$$
\frac{\partial u}{\partial x} + \frac{\partial w}{\partial z} = 0 
$$

where $u$ is the horizontal velocity and $w$ is the vertical velocity. 

Additionally assuming that the stresses and strains are aligned gives 

$$
\tau_{zz} = -\tau_{xx}
$$

Substituting this into the stress balance equation above gives

$$
\frac{\partial \tau_{xx}}{\partial x}+\frac{\partial \tau_{zx}}{\partial z} = \frac{\partial s}{\partial x} - \frac{\partial \tau_{xx}}{\partial x}
$$

or, rearranging, 

$$
2\frac{\partial \tau_{xx}}{\partial x}+\frac{\partial \tau_{zx}}{\partial z} = \rho g \frac{\partial s}{\partial x} 
$$

Next we bring in Glen's flow law to describe the rheology of the ice

$$
\dot{\epsilon_{ij}} = A \tau_{ij}^n
$$

where $\dot{\epsilon_{ij}}$ are the components of the strain rate tensor, $A$ is a flow parameter, $n$ is the flow exponent, and $\tau_E$ is the effective stress. The inverse form of the flow law is more useful for use here. 

Rearranging the equation above gives

$$
\dot{\epsilon_{ij}}^{\frac{1}{n}} = A^{\frac{1}{n}} \tau_{ij}
$$

then

$$ 
\tau_{ij}= A^{-\frac{1}{n}} \dot{\epsilon_{ij}}^{\frac{1}{n}}. 
$$

Then we define the effective viscosity as

$$
\eta = \frac{1}{2}  A^{-\frac{1}{n}} \epsilon_E^{\frac{1}{n}-1}, 
$$

where $\epsilon_E$ is the effective strain rate, in this case  defined by

$$
\epsilon_E^2 = \epsilon_{xx}^2 + \epsilon_{xz}^2
$$

The the inverse flow law is therefore 

$$ 
\tau_{ij}= 2 \eta \dot{\epsilon_{ij}}.
$$

Subsituting this into the stress balance equation gives

$$
4\frac{\partial }{\partial x}  (\eta \epsilon_{xx}) +2 \frac{\partial }{\partial z} (\eta \epsilon_{zx}) = \rho g \frac{\partial s}{\partial x} 
$$

Finally we will need the relationship between strain rates and velocity gradients: 

$$
\dot{\epsilon}_{ij} = \frac{1}{2}\left(\frac{\partial \underline{u}_i}{\partial \underline{x}_j} + \frac{\partial \underline{u}_j}{\partial \underline{x}_i}\right),
$$
where $\underline{u}$ is velocity field $(u, v, w)$ components and $\underline{x}$ are the three coordinates $x$, $y$, and $z$. 
For our two remaining strain rates this gives

$$ 
\dot{\epsilon}_{xx} = \frac{\partial u}{\partial x}
$$

and

$$
\dot{\epsilon}_{zx} = \frac{1}{2}\left(\frac{\partial w}{\partial x} + \frac{\partial u}{\partial z}\right)
$$

Consistent with neglecting bridging stresses at the start of the derivation, we now neglect $\frac{\partial w}{\partial x}$, leaving 

$$
\dot{\epsilon}_{zx} = \frac{1}{2}\frac{\partial u}{\partial z} 
$$

Substituting these expressions for $\dot{\epsilon}_{xx}$ and $\dot{\epsilon}_{zx}$ into the stress balance equation gives the Blatter-Pattyn model

$$
4\frac{\partial }{\partial x}  \left(\eta \frac{\partial u}{\partial x} \right)+ \frac{\partial }{\partial z} \left(\eta \frac{\partial u}{\partial z} \right) = \rho g \frac{\partial s}{\partial x} 
$$



## BP to SSA
In this section we make apply further simplifying assumptions to the BP above to derive a Shallow Shelf approximation model, which is applicable in locations where basal shear stress is relatively small compared to the longitudinal stresses and the driving stress. 

## BP to SIA
For completeness and to compliment the derivation of the SIA on the previous page, in this section we derive the SIA from the BP equation. 

