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

The inverse flow law is therefore 

$$ 
\tau_{ij}= 2 \eta \dot{\epsilon_{ij}}.
$$

Substituting this into the stress balance equation gives

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
In this section we apply further simplifying assumptions to the BP above to derive a Shallow Shelf approximation model, which is applicable in locations where basal shear stress is relatively small compared to the longitudinal stresses and the driving stress. 

The SSA model is a depth integrated model, which applies when internal vertical shear $\epsilon_{zx}$ is small. 

Integrating the BP equation above gives

$$
4 \int^s_b\frac{\partial }{\partial x}  \left(\eta \frac{\partial u}{\partial x} \right) dz + \int^s_b\frac{\partial }{\partial z} \left(\eta \frac{\partial u}{\partial z} \right) dz= \rho g \frac{\partial s}{\partial x}  \int^s_b dz.
$$

The integral on the right evaluates to $s-b = H$. Recognizing that $\eta \frac{\partial u}{\partial z} = \tau_{zx}$ (see a few steps up in the BP derivation above), the second term on the left is equal to 

$$
\int^s_b\frac{\partial }{\partial z} \left(\eta \frac{\partial u}{\partial z} \right) dz = \int^s_b \frac{\partial \tau_{zx}}{\partial z}  dz,
$$

which evaluates to 

$$
\int^s_b \frac{\partial \tau_{zx}}{\partial z}  dz = 0 - \tau_b,
$$

where $\tau_b$ is the vertical shear stress at the base of the ice, we have imposed the surface boundary condition of  $\tau_{zx}(s) = 0$. We also assumed $\frac{\partial \tau_{zx}}{\partial z} = 0$ within the ice. 

To evaluate the first term on the left we use the Leibniz integration rule to move the integral inside the first derivative. 

The Leibniz integration rule says that for some function $f(x,z)$ and limits of integration $b$ and $s$,

$$
\frac{d}{dx} \int^s_b f(x,z) dz =  f(x,s) \frac{ds}{dx} -  f(x,b) \frac{db}{dx} + \int^s_b \frac{\partial}{\partial x} f(x,z) dz.
$$

Applying this rule to the first term on the right of the stress balance equation and assuming $\frac{ds}{dx} = \frac{db}{dx} = 0$, gives

$$
4 \int^s_b\frac{\partial }{\partial x}  \left(\eta \frac{\partial u}{\partial x} \right) dz  = 4 \frac{\partial }{\partial x}  \int^s_b \left(\eta \frac{\partial u}{\partial x} \right) dz.
$$

Assuming that $\frac{\partial u}{\partial x} $ is uniform in depth, this becomes

$$
4 \frac{\partial }{\partial x}  \int^s_b \left(\eta \frac{\partial u}{\partial x} \right) dz = 4 \frac{\partial }{\partial x} \left(  \int^s_b\eta \, dz \frac{\partial u}{\partial x} \right) 
$$

FInally, defining the depth-averaged viscosity as

$$
\overline{\eta} = \frac{1}{H} \int^s_b\eta \, dz,
$$

$$
4 \frac{\partial }{\partial x} \left(  \int^s_b\eta \, dz \frac{\partial u}{\partial x} \right)  = 4 \frac{\partial }{\partial x} \left(  \overline{\eta} H\frac{\partial u}{\partial x} \right). 
$$

Bring all three expressions together gives

$$

4 \frac{\partial }{\partial x} \left(  \overline{\eta} H\frac{\partial u}{\partial x} \right) - \tau_b = \rho g H\frac{\partial s}{\partial x} .
$$

This is one commonly used form of the SSA. Another is found by substituting in an expression for the depth-averaged effective viscosity, which is simply 

$$
\overline{\eta} = \frac{1}{2}  A^{-\frac{1}{n}} \epsilon_{xx}^{\frac{1}{n}-1} =  \frac{1}{2}  A^{-\frac{1}{n}} \left(\frac{\partial u}{\partial x}\right)^{\frac{1}{n}-1} 
$$

if we assume $\epsilon_{E} = \epsilon_{xx}$ and that this does not vary with depth.

Substituting this into the SSA equation gives 

$$
2 \frac{\partial }{\partial x} \left( A^{-\frac{1}{n}} H\left(\frac{\partial u}{\partial x}\right)^{\frac{1}{n}-1} \frac{\partial u}{\partial x} \right) - \tau_b = \rho g H\frac{\partial s}{\partial x}.
$$

## BP to SIA
For completeness and to compliment the derivation of the SIA on the previous page, in this section we derive the SIA from the BP equation, 

$$
4\frac{\partial }{\partial x}  \left(\eta \frac{\partial u}{\partial x} \right)+ \frac{\partial }{\partial z} \left(\eta \frac{\partial u}{\partial z} \right) = \rho g \frac{\partial s}{\partial x}. 
$$

The first step is to neglect the horizontal extenstional stresses, the first term on the left. Again we recognize that $\eta \frac{\partial u}{\partial z} = \tau_{zx}$, leaving

$$
\frac{\partial \tau_{zx}}{\partial z} = \rho g \frac{\partial s}{\partial x}. 
$$

From now on the derivation is the same as the derivation on this [page](sia_derivation), equation ({eq}`dtau_zxdz`.

We integrate vertically, then substitute in Glen's flow law and the relationship between velocity gradients and strain rates. Then intergrate vertically again to obtain an expression for $u(z)$, then integrate vertically again to get an expression for the depth-integrated flux per unit width, $q$.  