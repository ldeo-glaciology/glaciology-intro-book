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

The surface velocity is always larger than the depth-averaged velocity, but by a smaller fraction for increasing nonlinear ice rheology. For example, if is linear, $n=1$ and $u_s/\overline{u} = 3/2$, or if $n=3$ and $u_s/\overline{u} = 5/4$. This can be understood mathematically by looking at the horizontal velocity shape function $1- \zeta^{n+1} $. The second term in the shape function controls how much the velocity deviates from the surface velocity. It deviates less for higher $n$ (just consider what the curves of $y=x^{n+1}$ look like between 0 and 1 for different values of $n$). Ths effect can be understood physically by remembering that we showed the that vertical shear stress increases linearly with depth:

$$
\tau_{zx} = -\rho g \alpha  (z-H).
$$

It is the rheology of the ice that determines how this linear increase in $\tau_{zx}$ with depth translates into shear strain. Therefore, it makes sense that in more non-linear ice, the deformation is concentrated where the shear stress is highest -- the bottom -- and the vertical gradient of $u$ is highest there, which is exactly what $1- \zeta^{n+1} $
does for higher $n$. 