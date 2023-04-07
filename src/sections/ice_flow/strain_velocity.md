# Strain rate and velocity fields
Normal strain is deformation which changes the length of a material element. It is defined as the fractional change in length in a particular direction. For example, if the length of a piece of ice is $L$ in the $x$ direction, then the strain in the $x$ direction is

$$
\epsilon_{xx} = \frac{\Delta L}{L}.
$$


The rate of change of strain (the strain rate) is denoted $\dot{\epsilon}$ and this is related to gradients in the velocity field as follows

$$
\dot{\epsilon}_{xx} = \frac{\partial u}{\partial x}.
$$


## Proof of this strain rate - velocity relationship  

Consider a segment of ice within a glacier that is $L$ long in the $x$ direction. It sits in a velocity field $\underline{u}(x) = u(x)$ which only varies in the $x$ direction. Let's define $x=0$ at the left side of the block. Arbitrarily, we say that the velocity at the left side of the block is $u$. Because the block is in a velocity field, the ends of the block move at different speeds. 

After a time $\Delta t$, the left side of the block has moved from $x=0$ to $x = u\Delta t$. 

The right side of the block moves at a velocity of $u + L\frac{\partial u}{\partial x}$. To understand this, consider that the spatial gradient inthe velocity ($\partial u/\partial x$) expresses how much $u$ increases for every meter you shift in the $x$ direction. So the difference in the velocity between the left of the block and the right is simply this gradient times the length of the block $L$. This approach is valid as long as we consider the distance $L$ small enough that $u$ varies linearly. 

In $\Delta t$ the right side of the block has moved $\Delta t(u + L\frac{\partial u}{\partial x})$. It started at $x = L$, so its new position is $L + \Delta t(u + L\frac{\partial u}{\partial x})$


Now, if the left side is at  $x = u\Delta t$ and the right side of the block is  at $x = L+ \Delta t(u + L\frac{\partial u}{\partial x})$, the new length of the block is 
$$
L + \Delta t(u + L\frac{\partial u}{\partial x}) - \Delta t u = L + \Delta t L\frac{\partial u}{\partial x}
$$

and the change in length is

$$
\Delta L = L + \Delta t L\frac{\partial u}{\partial x} - L = \Delta t L\frac{\partial u}{\partial x}.
$$

Rearranging shows that the strain in a time $\Delta t$ is

$$
\epsilon_{xx} = \Delta t \frac{\partial u}{\partial x}.
$$

Dividing through by the time gives us the relationship between the strain rate and gradient in velocity,

$$
\dot{\epsilon}_{xx} = \frac{\partial u}{\partial x}.
$$

## A general relationship

Doing the same exercise for shear strain shows that a general equation for this relationship is 

$$
\dot{\epsilon}_{ij} = \frac{1}{2}\left(\frac{\partial \underline{u}_i}{\partial \underline{x}_j} + \frac{\partial \underline{u}_j}{\partial \underline{x}_i}\right),
$$

where $\underline{u}$ is velocity field $(u, v, w)$ components and $\underline{x}$ are the three coordinates $x$, $y$, and $z$. 