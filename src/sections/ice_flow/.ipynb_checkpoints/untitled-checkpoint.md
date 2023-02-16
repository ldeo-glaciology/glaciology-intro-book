# Backgroundon vector calculus
Before we get going on deriving a model of cie sheet flow we will go over some fundamentals of vector calculus:
- scalar and vector fields
- the del operator
- gradients and divergence

## Fields

Fields are functions or variables that have a value defined at every point in space or time. Common fields in glaciology are temperature $T$, velocity $\underline{u}$, stress $\sigma$. These vary in the three spatial dimensions $x$, $y$, and $z$, and in time $t$.

### Scalar fields
Scalar fields are fields that only need one value in each location in space and time to define them. Examples are temperature $T$, ice-surface slope $S$, age $A$, and speed. 

We denote a scalar field simply as $T(x,y,z,t)$.

### Vector fields
Vector fields are more complicated. At each point in space and time, rather than just a scalar quantity we have a vector pointing in a specific direction in space. Therefore at each point in space and time, we require as many values as we have spatial dimensions. 

Examples of vector fields in glaciology are velocity $\underline{u}$, and the gradient of the ice-surface.

We denote vector fields with an underline as usually (at least when we first define them) write out their components, e.g.,

$$
\underline{u} = (u, v, w)
$$

These are typical symbols for the three velocity components used in glaciology, with $u$ as the horizontal component of velocity in direction of the large scale flow of the ice sheet (i.e. along the $x$ axis), $v$ being the horizontal component perpendicular to this (i.e. along the $y$ axis), and $w$ being the vertical component (i.e. along the $z$ axis). Note the potential for confusion between the vector field $\underline{u}$ and its $x$-component $u$.

Each of the components are functions of space and time, so we could write the whole thing out verbosely as

$$
\underline{u}(x,y,z,t) = (u(x,y,z,t), v(x,y,z,t), w(x,y,z,t)).
$$

## The del operator
The del operator is a vector of differential operators. A differential operator can operate on functions and the result of the operation is a derivative of the function. 

We can also think of it as a vector that has one component for each spatial dimension. So, for example, if we are considering a two-dimensional model del has two components corresponding to these two directions. 

Each component is the differential operator corresponding to differentiation *in the corresponding direction*. So in two dimensions del is defined as 

$\underline{\nabla} = \left(\frac{\partial}{\partial x} , \frac{\partial}{\partial y} \right)$

This notation with a comma in the middle is used to denote the two components of the vector $\frac{\partial}{\partial x}$ and $\frac{\partial}{\partial y}$. Individually, these two components can each act on a scalar field and when they do they compute how rapidly the scalar field varies (i.e. its gradient) in the corresponding direction. 

For example, if our ice sheet surface elevation is defined by the scalar field $h(x,y)$ (i.e. is it a function of our two coordinates $x$ and $y$), then the two components of del can individually act on $h$ giving us the gradients of $h$ in the two directions:  $\frac{\partial h}{\partial x}$ and $\frac{\partial h}{\partial y}$. The gradients are themselves scalar fields because they vary in $x$ and $y$. 

### Grad

Instead of having each component of del operate on our scalar field individually, we can simply write $\underline{\nabla} h$, which is the same as writing 

$\underline{\nabla}h = \left(\frac{\partial h}{\partial x} , \frac{\partial h}{\partial y} \right)$

The gradients of $h$ in each direction (which, remember, are scalar fields) have been inserted in as the two components of the *vector* field $\underline{\nabla}h$. 
In other words, $\underline{\nabla}h$ is a vector field in which the $x$-component is $\frac{\partial h}{\partial x}$ and the $y$-component is $\frac{\partial h}{\partial y}$. 
This is referred to as the grad operator. 

### Divergence
Del is also useful for analyzing vector fields. One way to apply it to a vector field is to use the dot product. 
The dot product is the sum of the products of the components of two vectors. 
For example, for two vectors $\underline{A}$ and $\underline{B}$, each with components in the $x$ and $y$ direction denoted with subscripts ($A_x$, $A_y$, $B_x$, and $B_y$), the dot product is 

$$
\underline{A} \cdot \underline{B} = A_x B_x + A_y B_y
$$

Let's use a 2-D velocity field for our vector field $\underline{u} = (u,w)$.


Remembering that the $x$ and $y$ components of del are $\frac{\partial h}{\partial x}$ and $\frac{\partial h}{\partial y}$, we can write down 

$$
\underline{\nabla} \cdot \underline{u} = \left(\frac{\partial u}{\partial x} + \frac{\partial v}{\partial y} + \frac{\partial w}{\partial z} \right)
$$

This is called the divergence of the velocity field. Later we will show using mass conservation that it is proportional to the rate of change of porosity, $\phi$:

$$
\frac{\partial \phi}{\partial t} = (1- \phi) \underline{\nabla} \cdot \underline{u} 
$$

We usually assume that porosity is zero everywhere. In other words, we assume that in a bulk sense the ice is incompressible. This means that we can usually assume 

$$
\underline{\nabla} \cdot \underline{u} =0, 
$$

which is really useful in many ice sheet modelling and data analysis tasks. 