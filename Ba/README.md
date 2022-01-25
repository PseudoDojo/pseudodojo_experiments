# Info

## Ba-sp.in

This pseudo is based on `Ba-sp-high.in` of the official PD table.
It uses the neutral ground-state as reference configuration but, unlike the official PD version,
it includes two projectors for the f-channel in order to improve the logder.

According to oncvpsp, the cutoff should be around 30 Ha but I would suggest to increase these value
by let's say 10 Ha to be on the safe side.

Hopefully, this version will give better results than the previous version, especially in covalent-like
configurations.

## Ba-sp-2+.in:

This pseudos uses an (almost) 2+ ionization state as reference 
The parameters are similar to Ba-sp-2+.in.
The main difference is that

# n l f
6 0 2.0

is now replaced by:

# n l f
6 0 0.01

so we have 0.01 electrons in the 6s state.

According to oncvpsp, the cutoff should be around 35 Ha so slightly larger than
the previous version because the 5f state gets more localized once the 6s electrons 
are removed. Again, add +10 Ha to be on the safe side. 

Hopefully, this version will give better results for the XO2, XO3 oxides.
