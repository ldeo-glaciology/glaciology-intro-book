# Building on the Shallow Ice Approximation

On previous page we derived expressions for the horizontal ice velocity as function of depth $\zeta$ and depth-integrated flux. As a slight aside, on this page we build on these results to derive expressions for the depth-averaged velocity and the vertical velocity as a function of $\zeta$.

## Horizontal velocity
To summarize the previous page, we showed that the horizontal velocity as a function of depth $\zeta$ is 

$$
u(\zeta)=  \frac{2A}{n+1} \left(\rho g \alpha \right)^n  H^{n+1} \left( 1- \zeta^{n+1} \right),
$$

where $A$ is th. flow parameter in Glen's flow law (the power-law, shear thinning rheology assumed for ice), $n$ is the flow-law exponent, $\rho$ is the ice density, $g$ is the acceleration due to gravity, $\alpha$ is the surface slope, $H$ is the ice thickness, and $\zeta$ is the dimensionless depth coordinate defined as $\zeta = 1-z/H$.

We can get the horizontal velocity at the surface by evaluating this expression at $\zeta = 0$:

$$
u_s = u(0)=  \frac{2A}{n+1} \left(\rho g \alpha \right)^n  H^{n+1},
$$

which shows that

$$
u(\zeta) = u_s \left( 1- \zeta^{n+1} \right).
$$

## Mean velocity
We can compute the mean velocity from this by integrating vertically and dividing by $H$:

$$
\overline{u} = \frac{2A}{n+2} \left(\rho g \alpha \right)^n  H^{n+1}. 
$$

```{note}
On the previous page we integrated vertically to get the depth-integrated flux $q$, so you could also obtain the expression above by simply dividing our expression for $q$ by $H$.
```

This looks very similar the surface velocity. In fact, according the shallow ice approximation, the surface velocity and the depth-averaged velocity have a very simple relationship:

$$
\frac{u_s}{ \overline{u}} = \frac{n+2}{n+1}.
$$

The surface velocity is always larger than the depth-averaged velocity, but by a smaller fraction for increasing nonlinear ice rheology. For example, if is linear, $n=1$ and $u_s/\overline{u} = 3/2$, or if $n=3$ and $u_s/\overline{u} = 5/4$. This can be understood mathematically by looking at the horizontal velocity shape function $1- \zeta^{n+1} $. The second term in the shape function controls how much the velocity deviates from the surface velocity. It deviates less for higher $n$ (just consider what the curves of $y=x^{n+1}$ look like between 0 and 1 for different values of $n$). This effect can be understood physically by remembering that we showed the that vertical shear stress increases linearly with depth:

$$
\tau_{zx} = -\rho g \alpha  (z-H).
$$

It is the rheology of the ice that determines how this linear increase in $\tau_{zx}$ with depth translates into shear strain. Therefore, it makes sense that in more non-linear ice, the deformation is concentrated where the shear stress is highest -- the bottom -- and the vertical gradient of $u$ is highest there, which is exactly what $1- \zeta^{n+1} $
does for higher $n$. 


## Vertical velocity
Another extension from our expression for horizontal velocity:

$$
u(x, \zeta)=  u_s(x) \left( 1- \zeta^{n+1} \right),
$$

 is to compute the vertical velocity as function of depth. This is often referred to as the Lliboutry function. Here we explicitly noting that $u_s$ and therefore $u$ are functions of $x$. We will use the general mass continuity equation 

 $$
    \nabla\cdot\underline{u} =   \frac{\partial u}{\partial x} + \frac{\partial w}{\partial z} = 0,
 $$

 where $w$ is the vertical velocity, $u$ is the horizontal velocity, $x$ is the horizontal coordinate, and $z$ is the vertical. As our velocity expression is in terms of normalized depth, $\zeta = 1-z/H$, we want the expression above in terms of $\zeta$. Differentiating the definition of $\zeta$ provides

$$ 
\frac{\partial \zeta}{\partial z} = -\frac{1}{H} 
$$

and applying the chain rule gives

$$
\frac{\partial w}{\partial z} = \frac{\partial w}{\partial \zeta} \frac{\partial \zeta}{\partial z} = -\frac{1}{H} \frac{\partial w}{\partial \zeta}.
$$


Therefore, from the mass continuity equation

$$ 
\frac{\partial u}{\partial x} - \frac{1}{H} \frac{\partial w}{\partial \zeta} = 0.
$$
 
Differentiating our expression for $u(x, \zeta)$ with respect to $x$ gives 

$$
   \frac{\partial u}{\partial x} =  \frac{\partial u_s}{\partial x} \left( 1- \zeta^{n+1} \right) - u_s \frac{\partial \zeta}{\partial x} (n+1) \zeta^n.
$$

Here we assume that $H$ is not a function of $x$, so $\partial \zeta/\partial x = 0$. Putting this into the expression above leaves

$$
    \frac{\partial u}{\partial x} =  \frac{\partial u_s}{\partial x} \left( 1- \zeta^{n+1} \right). 
$$

Based on the mass continuity equation

$$
\frac{\partial u_s}{\partial x} \left( 1- \zeta^{n+1} \right) = \frac{1}{H} \frac{\partial w}{\partial \zeta}.
$$

Rearranging this gives

$$
\frac{\partial w}{\partial \zeta} = H \frac{\partial u_s}{\partial x} \left( 1- \zeta^{n+1} \right).
$$

Now we need to integrate vertically to get $w(\zeta)$. First we put in the limits of integration to define the boundary conditions. At the base, $\zeta = 1$ and $w=w_b$. 

$$
\int^w_{w_b} dw = H \frac{\partial u_s}{\partial x} \int^\zeta_1\left( 1- \zeta^{n+1} \right)
$$

Evaluating the integrals gives

$$
w - w_b = H \frac{\partial u_s}{\partial x} \left[\zeta - \frac{\zeta^{n+2}}{n+2} \right]^\zeta_1 = H \frac{\partial u_s}{\partial x} \left[\zeta - \frac{\zeta^{n+2}}{n+2} - 1 + \frac{1}{n+2} \right].
$$

Noting that 

$$
- 1 + \frac{1}{n+2} = - \frac{n+2}{n+2} + \frac{1}{n+2}  = \frac{-n-2+1}{n+2} = -\frac{n+1}{n+2} 
$$

gives

$$
w - w_b = H \frac{\partial u_s}{\partial x} \left[\zeta - \frac{\zeta^{n+2}}{n+2} -\frac{n+1}{n+2}  \right].
$$

We can define the vertical velocity at the surface ($\zeta=0$) as 

$$
w_s - w_b = - H \frac{\partial u_s}{\partial x} \frac{n+1}{n+2}.
$$

we can divide our expression for simplify our expression $w - w_b$ by dividing to 

$$
w - w_b = (w_s - w_b) \left(1 -\frac{n+2}{n+1}\zeta  + \frac{1}{n+1}\zeta^{n+2} \right).
$$

These are the expressions for the vertical velocity as a function of depth $\zeta$ and the vertical velocity at the surface. 

Perhaps easier to understand is the case when $w_b = 0$, i.e. the ice is not melting or being accreted at the base:

$$
w_s = - H \frac{\partial u_s}{\partial x} \frac{n+1}{n+2},
$$


$$
w = w_s \left(1 -\frac{n+2}{n+1}\zeta  + \frac{1}{n+1}\zeta^{n+2} \right).
$$

Consider the first of the above two expressions. The thickness$H$ and the flow exponent $n$ are positive, so the vertical velocity has the opposite sign to horizontal strain rate at the surface. This makes sense because the horizontal extension should result in vertical compression. In a place where $w_b=0$ this corresponds to a negative (i.e. downward) vertical velocity: think of a spring, initially stretched vertically, is slowly released - if the bottom end is held static (i.e. $w_b=0$) the whole spring is slowly moving downwards, albeit at spatially varying rates. 

Now consider the seccond expression above. At the surface $\zeta=0$ and $w=w_s$ as required. The expression in the brackets is a so called shape function. The value of the flow exponent controls its shape. In the case when $n$ is very large, approximating a plastic rheology,

$$
w = w_s \left(1 -\zeta  \right).
$$

In this case, the vertical velocity varies uniformly from $w_s$ at the surface to zero at the base. This is because all the vertical shear is concentrated in a very small layer at the bed and the horizontal strain rate $\frac{\partial u_s}{\partial x}$ is uniform throughout the thickness of the ice. 

As $n$ decreases and the ice behaves less plastically, and more viscously, the vertical shear spreads out through the thickness of the ice and the vertical velocity profile become nonlinear. 

