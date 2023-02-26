# Driving stress 

Ice-sheet flow is driven by gravity. Specifically it is a quantity called the  driving stress that drives flow:

$$
\tau_d = - \rho g H \frac{\partial H}{\partial x},
$$

where $\rho$ is the density of ice ($~9.17 \text{ kg m}^{-3}$), $g$ is gravitational acceleration ( ~9.8 $\text{m s}^{-2}$), $H$ is the ice thickness, $x$ is the horizontal coordinate oriented in teh ice flow direction. 

## Derivation.

Consider a column of ice that extends from the ice-sheet bed to the surface and has length $\delta x$ in the $x$ direction and length $\delta y$ in the $y$ directon perpendicula to flow. We will assume that the bed is flat. The pressure at each elevation $z$ is given by

$$
P = \rho g (H-z),
$$

where $P$ is the pressure, and $z$ is the vertical coordinate  (increasing upward). The equation above comes from integrating the hydrostatic pressure equation 

$$
\frac{d P}{d x} = -\rho g z.
$$

(todo: replace this figure, add figure caption)

![image](https://user-images.githubusercontent.com/90412051/196259608-df6514b0-1267-4b05-8365-447518651a39.png)

To calculate the force acting on one side of the ice column (blue arrow), with thickness $H$, we can consider that force = pressure $\times$ area. However, ppressure $p$ depends on $z$, so we need to integrate over the thickness of the ice, rather than just multiply by the area.   We will call the force on the left-hand side of the column $F_1$:

$$
F_1 = \delta y\int_0^H P(z)  dz
$$

$$
F_1 = \delta y\int_0^H \rho g (H-z)  dz = \delta y \rho g \left[Hz - \frac{z^2}{2}\right] = \delta y \rho g \left[H^2 - \frac{H^2}{2}\right] 
$$

$$
F_1 = \frac{1}{2}\delta y \rho g H^2 
$$

Note that in this calculation, we have assumed constant $\rho$ and g, and that air pressure is negligible compared to ice pressure.

The more relevant quantity to consider here is not just the force acting on one side of the ice column, but rather the difference between the forces on either side. If we imagine that the ice column is part of an ice sheet with a surface slope of $\frac{dH}{dx}$, and has thickness $\partial x$ in the x-direction, then the force acting on the opposite side of the ice column can be calculated as follows:

$$
F_2  = \frac{1}{2}\delta y \rho g H^2 + \delta x \frac{d}{dx}\left(\frac{1}{2}\delta y \rho g H^2 \right)
$$

$$
\Delta F = F_1 - F_2 = \frac{1}{2}\delta y \rho g H^2 - \left(\frac{1}{2}\delta y \rho g H^2 + \delta x \frac{d}{dx}\left(\frac{1}{2}\delta y \rho g H^2\right)\right)
$$

$$
\Delta F = -\frac{1}{2}\delta x \delta y \rho g \frac{\partial H^2}{\partial x}
$$ 

We can now invoke the chain rule to rewrite this as

$$
\Delta F = -\frac{1}{2}\delta x \delta y \rho g \left(2 H \frac{\partial H}{\partial x}\right) = -\delta x \delta y\rho g  H \frac{\partial H}{\partial x}
$$

This is the stres imbalance integrated over the is ice thickness and across a width $\delta y$ perpendicular to flow. We define the driving stress as the force imbalance per unit area of the bed:

$$
\tau_d = \frac{\Delta F}{A} = \frac {\Delta F}{\partial x \partial y}
$$

$$
\tau_d = - \rho g H \frac{\partial H}{\partial x}
$$

This makes sense intuitively; there is more driving stress where the ice is thicker (higher $H$) and steeper (higher $\frac{\partial H}{\partial x}$).

We can generalize this to two dimensions as follows:

$$
\underline{\tau_d} = - \rho g H \left(\frac{\partial H}{\partial x} \hat{i} + \frac{\partial H}{\partial y} \hat{j}\right) = - \rho g H \vec{\nabla} H
$$

The driving stress field will point in the direction in which the slope changes the fastest.

We can also generalize this to account for cases when the be topography is not flat:

$$
\tau_d = - \rho g H \frac{\partial h}{\partial x}
$$

where $h$ is the ice surface height. 