# pseudodojo_experiments

A repo for storing and exchanging experimental pseudos

standard.txt and stringent.txt list the filenames defining the pseudos 
used for the different tables available on the pseudodojo website.
Note that, in some cases, the same pseudo is included in both tables.

The Ba-sp in this repo is based on Ba-sp-high.in of PD0.4 and should be used both
for the standard and the stringent table of PD v0.5


During the process of computing the oxide verification equations of state, we observed that the results for around 11 of the
PseudoDojo pseudopotentials were not in as good agreement with the all-electron equations of state as other elements from the
same pseudopotential family. This led to an investigation into possible improvements to the pseudopotentials for 

Ba, 
Bi, 
I, 
Pb,
Po, 
Rb, 
Rn, 
S, 
Te, 
Tl, and 
Xe. 


With the exception of S, we found that the accuracy of the pseudopotentials is significantly
improved by including a projector for the f -channel. In the original version, indeed, the local part of the pseudopotential was
not able to reproduce the all-electron scattering properties of the f -channel in the empty region.
