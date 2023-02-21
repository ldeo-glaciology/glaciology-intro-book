# Deviatoric stress
Given a mean (normal) stress defined as $\sigma_m = \frac{1}{3}(\sigma_{xx}+\sigma_{yy}+\sigma_{zz})$, the deviatoric stress tensor, $\underline{\underline{\tau}}$, is defined as $\underline{\underline{\tau}}=\underline{\underline{\sigma}}-\sigma_m\underline{\underline{I}}$ such that:

$$
\underline{\underline{\tau}} = \begin{bmatrix}
   \sigma_{xx}-\sigma_m & \tau_{xy} &\tau_{xz} \\
   \tau_{yx} & \sigma_{yy}-\sigma_m & \tau_{yz}\\
   \tau_{zx}&\tau_{zy}&\sigma_{zz}-\sigma_m
\end{bmatrix}
$$

Note that only the normal stresses $\sigma_{ij}$ differ between $\underline{\underline{\tau}}$ and $\underline{\underline{\sigma}}$ -- shear stresses $\tau_{ij}$ are the same. 

$\sigma_m$ is the component of the stress that does not vary with direction (i.e. its isotropic). It tries to change the volume of our material. Removing it from the total stress $\underline{\underline{\sigma}}$ leaves only the component of stress that does vary with direction, $\underline{\underline{\tau}}$, which tries to change the shape of our material.

$\underline{\underline{\tau}}$ is particularly useful for glaciology because we can often assume that ice is incompressible, so to a first approximation, $\sigma_m$ does not affect flow, whereas $\underline{\underline{\tau}}$ does. It is $\underline{\underline{\tau}}$ which appears in ice flow laws.  