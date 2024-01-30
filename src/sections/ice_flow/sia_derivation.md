
# The Shallow Ice Approximation model  
Finally we are ready to derive our simple equation of ice flux, which will be combined with the depth-averaged mass balance equation to make our ice-sheet model. 

We will use the so-called 'shallow ice approximation' to simplify the stress balance equations, 

$$
\frac{\partial \sigma_{xx}}{\partial x}+\frac{\partial \tau_{yx}}{\partial y}+\frac{\partial \tau_{zx}}{\partial z} = 0\\
$$


$$
\frac{\partial \tau_{xy}}{\partial x} + \frac{\partial \sigma_{yy}}{\partial y} +\frac{\partial \tau_{zy}}{\partial z} = 0
$$


$$
\frac{\partial \tau_{xz}}{\partial x}+\frac{\partial \tau_{yz}}{\partial y}+\frac{\partial \sigma_{zz}}{\partial z} = \rho g
$$

which we derived previously to produce an expression for the depth-integrated ice flux $q$ in one horizontal dimension, $q$, defined by  

$$
q = \int^H_0 u(z) dz.
$$

where $z$ is the vertical coordinate measured from the ice base, $H$ is the ice thickness  and $u$ is the horizontal ice velocity. $q$ is the volume of ice flowing horizontally past a location per unit time, per unit width across flow.

The depth integral in the expression above is a hint that this is a depth-integrated ice-flow model, meaning that the final model will consider the stresses, fluxes, and velocities in a depth integrated/averaged sense, which does not resolve variations in these properties with depth. (Although some of the equations that we see along the way can be used to compute some of these as functions of $z$.)

Note that in the stress balance equations above, we have three equations and nine unknowns - we cannot solve this system of equations without more information. In the a 'full-stokes' ice-sheet model this information comes from the rheology. In our case,s we will make simplifications until we have two equations and two unknowns. 


## Reduce to two dimensions, $x$ and $z$
The first step is drop the $y$ dimension. We are just considering how properties vary in $x$ and $z$, so all terms in the stress balance that include a $y$ are assumed to be zero: 

$$
\frac{\partial \sigma_{xx}}{\partial x}+\frac{\partial \tau_{zx}}{\partial z} = 0\\
$$

$$
\frac{\partial \tau_{xz}}{\partial x}+\frac{\partial \sigma_{zz}}{\partial z} = \rho g
$$

You can think of this as an assumption that the ice is a vertical slice of ice with zero thickness in the $y$ direction, or (probably more helpfully) you can think of it as an assumption that the ice has infinite across-flow width and no properties vary in that across-flow direction. The latter assumption is a good one in some real-world scenarios, so it seems reasonable to make this assumption here to simplify the maths. 

## Substitute in deviatoric stress
As defined previously, the deviatoric stress is the component of the stress tensor that varies with direction. It is related to the total stress by

$$
\underline{\underline{\tau}}=\underline{\underline{\sigma}}-\sigma_m\underline{\underline{I}}
$$

where the mean stress $\sigma_m = \frac{1}{3}(\sigma_{xx}+\sigma_{yy}+\sigma_{zz})$ and $\underline{\underline{I}}$ is the identity tensor. Element-wise this means 

$$
\sigma_{xx} = \tau_{xx} + \sigma_{m}
$$

$$
\sigma_{zz} = \tau_{zz} + \sigma_{m}
$$

and therefore

$$
\frac{\partial \sigma_{xx}}{\partial x} = \frac{\partial \tau_{xx}}{\partial x} + \frac{\partial \sigma_{m}}{\partial x}
$$

$$
\frac{\partial \sigma_{zz}}{\partial z} = \frac{\partial \tau_{zz}}{\partial z} + \frac{\partial \sigma_{m}}{\partial z}
$$

Substituting these two expressions into the stress balance equation gives

$$
\frac{\partial \tau_{xx}}{\partial x} + \frac{\partial \sigma_{m}}{\partial x}+\frac{\partial \tau_{zx}}{\partial z} = 0\\
$$

$$
\frac{\partial \tau_{xz}}{\partial x}+\frac{\partial \tau_{zz}}{\partial z}+\frac{\partial \sigma_{m}}{\partial z} = \rho g
$$


## Drop stress terms - the 'Shallow Ice Approximation'
Next, we make *part of* what is called the 'Shallow Ice Approximation.' Based on the assumption that the ice is much wider than it is tall (i.e. the aspect ratio is very large), we neglect the variation of stresses in the $x$ direction. We also assume the vertical stress is hydrostatic (i.e. $\frac{\partial \tau_{zz}}{\partial z} =0$).


These are serious simplifications. They mean that our model will not be applicable to places where the bed slope varies rapidly, places where the bed is very slippery, at grounding lines, in ice shelves, or at ice divides. In all these cases, the terms we are about to neglect are likely to be very important and should not be ignored. We would need to retain some (or all) of these terms in the stress balance to have a hope of realistically simulating ice flow in those places. Nonetheless, neglecting them here can help us to understand the basics of ice sheet flow and we can come back to more sophisticated models later. 

Neglecting the variation of stresses in the $x$ direction and $\frac{\partial \tau_{zz}}{\partial z}$ in the stress balance equations leaves

$$
 \frac{\partial \sigma_{m}}{\partial x}+\frac{\partial \tau_{zx}}{\partial z} = 0\\
$$

$$
\frac{\partial \sigma_{m}}{\partial z} = \rho g
$$

We started with three equations and nine unknowns. The simplifications above have reduced the model to two equations and two unknowns. Therefore, as long as we have boundary conditions, we can solve this system of equations to get the stresses, then use the result with Glen's flow law to get ice flux. 

## Integrate the $z$ equation vertically 
Our first challenge is to combine these equations to get an expression for $\tau_{zx}$. The first step is to integrate the $z$-direction stress balance equation vertically. Integrating both sides gives

$$
\int^0_{\sigma_m} d \sigma_m = \rho g \int^H_z dz
$$

where we have used the limits of integration to impose a boundary condition at the upper surface, $z=H$, of $\sigma_m(z=H) = 0$.

Evaluating the integrals gives

$$
\sigma_m = -\rho g (H-z)
$$

i.e. as expected, the mean normal stress is negative (compressive) and increasing with depth from the surface at a rate proportional to the strength of gravity and the density of ice.

## Differentiate horizontally
Next we differentiate this expression horizontally to get

$$
\frac{\partial \sigma_{m}}{\partial x} =- \rho g \frac{\partial H}{\partial x}
$$

Substituting this into the $x$-direction stress balance equation shows

<!--dtau_zxdz-->
$$
\frac{\partial \tau_{zx}}{\partial z} = \rho g \frac{\partial H}{\partial x}
$$

Noting that $\frac{\partial H}{\partial x}$ is usually negative, this expression suggests that the vertical shear stress $\tau_{zx}$ decreases with $z$. 

## Integrate vertically 
To get an expression for $\tau_{zx}$, we integrate the expression above vertically: 

$$
\int^0_{\tau_{zx}} \frac{\partial \tau_{zx}}{\partial z}dz = \rho g \frac{\partial H}{\partial x} \int^H_z  dz
$$

where we have imposed the boundary condition $\tau_{zx}(z=H) = 0$, i.e.  there is no shear stress exerted by the air on the ice sheet at the surface. 

Evaluating this integral gives

$$
\tau_{zx} = \rho g \alpha  (H-z),
$$

where $\alpha = -\frac{\partial H}{\partial x}$.

This is a solution to the stress balance equations for the vertical shear stress. It says that vertical shear stress is zero at the surface and increases linearly with depth at a rate proportional to the density, the strength of gravity, and the surface slope. To determine how this corresponds to deformation and ultimately the ice flux we need to bring in rheology.  


## Rheology
To derive expressions for deformation we will use a description of ice rheology, Glen's flow law: 

$$
\dot{\epsilon_{ij}} = A\tau_E^{n-1}\tau_{ij}
$$

where $\epsilon_{ij}$ are the elements of the strain rate tensor $\underline{\underline{\epsilon}}$ and $\tau_E$ is the so-called effective stress, defined as the second invariant of the deviatoric stress tensor:

$$
\tau_E^2 = \frac{1}{2}(\tau_{xx}^2+\tau_{yy}^2+\tau_{zz}^2)+\tau_{xz}^2+\tau_{xy}^2+\tau_{yz}^2.
$$

As part of the shallow ice approximation we neglect all terms on the right except $\tau_{xz}^2$. Neglecting $\tau_{yy}^2$, $\tau_{xy}^2$ and $\tau_{yz}^2$ is equivalent to assuming the ice flow is two dimensional. Neglecting $\tau_{xx}^2$ is an additional assumption; previously we neglected the effect of $\frac{\partial \tau_{xx}}{\partial x}$ on the stress balance, but here we are additionally neglecting the effect of $\tau_{xx}$ on ice viscosity, this is equivalent to saying $\frac{\partial u}{\partial x}=0$.

These assumption leave

$$
\tau_E = \tau_{xz}
$$

and therefore 

$$
\dot{\epsilon_{xz}} = A\tau_{xz}^n.
$$

## Strain rates and velocity gradients. 
To relate strain rates to velocity gradients we use the expression:

$$
\dot\epsilon_{xz} = \frac{1}{2}\left(\frac{\partial w}{\partial x} + \frac{\partial u}{\partial z}\right)
$$

We make a final additional simplification associated with the shallow ice approximation - we assume that $\frac{\partial w}{\partial x}$ is much smaller than $\frac{\partial u}{\partial z}$, 

$$
\dot\epsilon_{xz} = \frac{1}{2}\frac{\partial u}{\partial z}.
$$

## Horizontal velocity

Combining our simplified flow law, the stress-balance-based equation for $\tau_{zx}$ and the expression above for $\epsilon_{zx}$ yields an expression for the vertical variation of horizontal velocity:

$$
\frac{\partial u}{\partial z} = 2A \left(\rho g \alpha  (H-z)\right)^n
$$

To determine the horizontal velocity we need to integrate vertically:

$$
\int^u_0 du = 2A \left(\rho g \alpha H \right)^n \int^z_0\left(1-\frac{z}{H}\right)^n dz.
$$

To evaluate the integral we use the substitution $\zeta = 1-\frac{z}{H}$, which is usually referred to as the normalized depth.

Differentiating gives us $\frac{d\zeta}{dz} = -\frac{1}{H}$; $dz = -H d\zeta$. To change the limits in the integral we need $\zeta$ at $z=0$: $\zeta(z=0) = 1$. Using these results in the above equation gives us

$$
\int^u_0 du = -2A \left(\rho g \alpha \right)^n  H^{n+1} \int^\zeta_1\zeta^n dz
$$

Evaluating the integrals, 

$$
u = -2A \left(\rho g \alpha \right)^n  H^{n+1} \left[ \frac{\zeta^{n+1}}{n+1}\right]^\zeta_1 
$$

$$
u =  -2A \left(\rho g \alpha \right)^n  H^{n+1} \left[ \frac{\zeta^{n+1}}{n+1} - \frac{1}{n+1}\right],
$$

and rearranging slightly gives

$$
u(\zeta)=  \frac{2A}{n+1} \left(\rho g \alpha \right)^n  H^{n+1} \left( 1- \zeta^{n+1} \right).
$$

We can get the horizontal velocity at the surface by evaluating this expression at $\zeta = 0$:

$$
u_s = u(0)=  \frac{2A}{n+1} \left(\rho g \alpha \right)^n  H^{n+1},
$$

which shows that

$$
u(\zeta) = u_s \left( 1- \zeta^{n+1} \right).
$$

This highlights how you can think of the velocity as being the product of the surface velocity and a function of depth: $1- \zeta^{n+1}$. This function is often called a 'shape function'. 

## Ice flux
To determine the ice flux 

$$
q = \int^H_0 u(z) dz
$$


we need to integrate the horizontal velocity vertically:

$$
q = \int^H_0 u dz =  \frac{2A}{n+1} \left(\rho g \alpha \right)^n  H^{n+1} \int^H_0\left( 1- \zeta^{n+1} \right) dz.
$$

We will use the same substitution as before. To change the limits in the integral we need $\zeta(z=H) = 0$ and $\zeta(z=0) = 1$. making use of $dz = -H d\zeta$ again we get

$$
q = \int^H_0 u dz =  -\frac{2A}{n+1} \left(\rho g \alpha \right)^n  H^{n+2} \int^0_1\left( 1- \zeta^{n+1} \right) d\zeta.
$$

Evaluating the integral yields

$$
q = -\frac{2A}{n+1} \left(\rho g \alpha \right)^n  H^{n+2} \left[ \zeta- \frac{\zeta^{n+2}}{n+2} \right]^0_1 
$$

$$
q = -\frac{2A}{n+1} \left(\rho g \alpha \right)^n  H^{n+2} \left( (0- 0) - \left(1- \frac{1}{n+2}\right) \right)
$$

$$
q = \frac{2A}{n+1} \left(\rho g \alpha \right)^n  H^{n+2} \left(1- \frac{1}{n+2} \right) .
$$

To simplify we substitute in $\frac{n+2}{n+2} = 1$:

$$
q = \frac{2A}{n+1} \left(\rho g \alpha \right)^n  H^{n+2} \left(\frac{n+2}{n+2}- \frac{1}{n+2} \right) .
$$

$$
q = \frac{2A}{n+1} \left(\rho g \alpha \right)^n  H^{n+2} \left(\frac{n+1}{n+2} \right) .
$$

$$
\boxed{q = \frac{2A}{n+2} \left(\rho g \alpha \right)^n  H^{n+2}} .
$$

This is the final expression for the ice flux in the Shallow Ice Approximation model. 

Note how strongly dependent on the thickness it is: $H^5$, if $n=3$.


