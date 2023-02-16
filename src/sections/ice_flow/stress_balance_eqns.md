# Stress balance equations
In ice sheets and glaciers, the forces associated with acceleration (= mass $\times$ acceleration) are small compared to all the other forces involved. This is essentially because the speed of the ice only changes very slowly. In these circumstances, Newton's second law $\Sigma F_i=ma$ simplifies to $\Sigma F_i = 0$, meaning that all the forces acting on each portion of the ice must add up to zero.

We will use this idea to derive a set of partial differential equations which describe how the different components of the stress tensor relate to each other. 

## The setup

Consider a cube with density $\rho$, sides with length $\delta x$, $\delta y$, and $\delta z$, and volume $V = \delta x \delta y \delta x$:

![image](https://user-images.githubusercontent.com/33917430/201834366-79cc03de-220d-4775-b9be-eb4973d6af16.png)

The cube's stress state can be described through the stress tensor $\underline{\underline{\sigma}}$, where the normal and shear stress components are denoted by $\sigma_{ij}$ and $\tau_{ij}$, respectively, such that: 

$$\underline{\underline{\sigma}}=\begin{bmatrix}
   \sigma_{xx} & \tau_{xy} &\tau_{xz} \\
   \tau_{yx} & \sigma_{yy} & \tau_{yz}\\
   \tau_{zx}&\tau_{zy}&\sigma_{zz}
\end{bmatrix}$$

## The forces acting on the cube

Let's now consider the forces associated with these different stress components and with gravity. We will consider the forces acting in each of the three directions in turn, starting with the $z$ direction. Note that here we consider forces as positive upwards and we are considering the forces acting *on* the cube. So, a force acting to push the cube upwards is considered positive and a force acting to push the cube downwards is considered negative.  

![image](https://user-images.githubusercontent.com/33917430/201834410-3954ce95-2b78-44d5-a583-6573990e96b8.png)


### Gravity

The force of gravity is simply the volume of the cube times its density times the acceleration due to gravity, $g$:

$$
\rho g \delta x \delta y \delta x
$$

## The vertical forces acting on the $z$ faces
Next we will look at the forces acting on the two faces with normals in the $z$ direction (the top and bottom of the cube). The normal stress $\sigma_{zz}$  acts to stretch the material vertically, so at the bottom face the material around the cube is pulling the cube down - according to our sign convention this is $-\sigma_{zz}$. To get the force associated with this stress we simply multiply it by the area over which is acts:  

$$
-\sigma_{zz} \delta x \delta y
$$

At the top of the cube the stress is (in general) slightly different than $\sigma_{zz}$ in magnitude because we have moved a distance $\delta z$ from the bottom face. Using the same procedure we have used in several previous derivations, we express this difference using the $z$ derivative of $\sigma_{zz}$:

$$
\sigma_{zz}+\frac{\partial\sigma_{zz}}{\partial z}\delta z.
$$

Note that this is a positive stress because at this face the material around the cube is pulling the cube upwards.

Multiplying by the area over which this stress acts gives the force at the upper face of the cube:

$$
\left(\sigma_{zz}+\frac{\partial\sigma_{zz}}{\partial z}\delta z\right)\delta y \delta x.
$$

### The vertical forces acting on the $x$ faces
At the other four faces shear stresses act in the $z$ direction. We apply the same procedure to the left face to get the force acting there:

$$
-\tau_{xz}\delta z \delta y
$$

In general, positive horizontal shear stress involves the right side of any interface pulling up and the left side pulling down. So in the case of the left face of our cube, positive shear pulls downwards on the cube, so that's why the expression above is negative. 

On the right face the force is 

$$
\left(\tau_{xz}+\frac{\partial\tau_{xz}}{\partial x}\delta x\right)\delta z \delta y
$$

### The vertical forces acting on the  $y$ faces
Applying the same approach to the $y$ faces gives

$$
-\tau_{yz}\delta z \delta x
$$

and

$$
\left(\tau_{yz}+\frac{\partial\tau_{yz}}{\partial y}\delta y\right)\delta z \delta x.
$$

## Summing all the forces
Summing the forces defined in the six expressions above and equating the sum to zero gives


$$
0 = -\rho g\delta x \delta y \delta z-\sigma_{zz}\delta y \delta x + \left(\sigma_{zz}+\frac{\partial\sigma_{zz}}{\partial z}\delta z\right)\delta y \delta x \\
-\tau_{yz}\delta z \delta x + \left(\tau_{yz}+\frac{\partial\tau_{yz}}{\partial y}\delta y\right)\delta z \delta x\\
-\tau_{xz}\delta z \delta y + \left(\tau_{xz}+\frac{\partial\tau_{xz}}{\partial x}\delta x\right)\delta z \delta y
$$

which simplifies to:

$$0 = -\rho g + \frac{\partial \sigma_{zz}}{\partial z}+\frac{\partial \tau_{yz}}{\partial y}+\frac{\partial \tau_{xz}}{\partial x}$$

Performing a similar analysis in the $x$- and $y$-directions yields:

$$
0 =  \frac{\partial \sigma_{xx}}{\partial x}+\frac{\partial \tau_{yx}}{\partial y}+\frac{\partial \tau_{zx}}{\partial z}
$$

$$
0 = \frac{\partial \sigma_{yy}}{\partial y}+\frac{\partial \tau_{xy}}{\partial x}+\frac{\partial \tau_{zy}}{\partial z}.
$$

Together, these three equations form the static stress balance equations, also known as Stokes equations.




