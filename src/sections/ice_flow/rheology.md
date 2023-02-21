# Ice rheology (under construction)

- explain viscous deformation with contrast to elastic deformation
- introduce the power law
- introduce Glen's flow law
- plot of stress vs strain for different values of $n$


## Glen's flow law
Glen's flow law is the most common flow law used to describe the viscous flow of ice in glaciology. So far we have written is as $\dot{\epsilon} = A\tau^n$, without specifying which stress $\tau$ and strain rate $\dot{\epsilon}$ are involved. A more complete formulation is:

$$
\dot{\epsilon_{ij}} = A\tau_E^{n-1}\tau_{ij}
$$

where $\tau_{ij}$ are the elements of the deviatoric stress tensor $\underline{\underline{\tau}}$ and $\tau_E$ is the so-called effective stress, defined as the second invariant of the deviatoric stress tensor as:

$$
\tau_E^2 = \frac{1}{2}(\tau_{xx}^2+\tau_{yy}^2+\tau_{zz}^2)+\tau_{xz}^2+\tau_{xy}^2+\tau_{yz}^2
$$