(page:apres-intro)=
# Autonomous phase-sensitive Radio Echo Sounder

The Autonomous phase-sensitive Radio-Echo Sounder (ApRES) is a frequency-modulated continuous-wave radar. Like all ground-penetrating radar systems, it emits radio waves in to the subsurface and records what is reflected back towards the radar. Reflection typically occurs at discrete locations in the subsurface, which are interpreted as interfaces between materials with different dielectric properties. We refer to these as reflectors.

ApRES is primarily designed to measure changes over time in the separation of sub-surface reflectors. When ApRES is used on an ice sheet, these reflectors can be internal to the ice ('englacial') reflectors or the ice base. Englacial reflections originate from contrasts in the density or chemistry of the ice, while basal reflections originate from the strong contrast between the ice and the underlying sediment, bedrock, or water. 

ApRES has most commonly been used to estimate melt rates at the base of ice shelves (the floating extensions of ice sheets), by tracking the separation between the ice-water interface and the englacial reflectors {cite:p}`brennan_phase-sensitive_2014, Nicholls_Corr_Stewart_Lok_Brennan_Vaughan_2015, vavnkova2022ocean`. ApRES, along with it predecessor, pRES, have also been used to measure englacial deformation on grounded ice {cite:p}`kingslake2014full`) and constrain ice-crystal fabric {cite:p}`brisbourne2019constraining, young2021rapid`.

```{figure} figures/apres_at_JIRP.png
---
name: fig:apres_on_JIRP
---
ApRES being deployed on the Juneau Icefield as part of the Juneau Icefield Research Program (JIRP). Photo credit: Elizabeth Case. 
```



The following page describes the theory behind one aspect of the ApRES system: how the so-called 'coarse' range is computed using fourier transform of  the signal recorded by ApRES. The following page applies this theory to real data collected in Antarctica. 