The **Mumberg vectors** are a set of *Saccharomyces cerevisiae* expression
plasmids that combine standardized promoter cassettes with the pRS shuttle
vector backbone to provide finely tunable constitutive expression over a
broad dynamic range. 

In this system, weak (**CYC1**), medium (**ADH1**) and
strong (**TEF**, **GPD**) promoters are fused to a common **CYC1 terminator**
and a multiple-cloning array derived from pBluescript/pBIISK, offering
several unique restriction sites for flexible cloning. These expression
cassettes were inserted into both **CEN/ARS** and **2µ** versions of the pRS
vectors carrying **HIS3**, **TRP1**, **LEU2** or **URA3** markers, yielding a
family of 32 plasmids that support controlled expression of heterologous
proteins in many different genetic backgrounds of *S. cerevisiae*.
**PubMed:**
[Yeast vectors for the controlled expression of heterologous proteins in
different genetic backgrounds (PMID: 7737504)](https://pubmed.ncbi.nlm.nih.gov/7737504/)




These plasmids were made from the pRS series of yeast vectors.

a XhoI - KpnI fragment of the ScCYC1 terminator was cloned using the same sites in pRS416 resulting in p416CYC1t

PCR generated SacI - XbaI promoter fragments of ScTDH3pr, ScTEF1pr, ScADH1pr and ScCYC1pr promoters were cloned using the same sites resulting in:

p416GPD sequenced SacI,XbaI,XhoI,KpnI are unique
p416TEF sequenced SacI,XbaI,XhoI,KpnI are unique
p416ADH
p416CYC sequenced SacI,XbaI,KpnI are unique
The SacI - KpnI promoter-terminator fragment was transferred to other pRS vectors using a strategy that is undisclosed in the paper.

ScTDH3pr-ScCYC1t
ScTEF1pr-ScCYC1t
ScADH1pr-ScCYC1t
ScCYC1pr-ScCYC1t
Probably SacI - KpnI were used. In the case of pRS423 and pRS425, there are two KpnI sites, so maybe a partial cut was used?

```
                                         this part is the opposite 
                                         direction in the paper 
                                         (the version below is correct)
                                         <--------------->
mcs:
                    7 SpeI      19 SmaI     31 EcoRI    43 HindIII           64 XhoI
              1 XbaI      13 BamHI    25 PstI     37 EcoRV    49 ClaI  58 SalI
              |     |     |     |     |     |     |     |     |        |     |     
SacI-PROMOTER-TCTAGAACTAGTGGATCCCCCGGGCTGCAGGAATTCGATATCAAGCTTATCGATACCGTCGACCTCGAG-CYC1-TERM-KpnI





Suggested primers for recombination cloning

>primer_fw
ACTAGTGGATCCCCCGGGCTGCAGA...
>primer_rev
TATCGATAAGCTTGATATCGAATTC...

            XbaI SpeI BamHI SmaI PstI EcoRI EcoRV HindIII ClaI SalI XhoI

p413 HIS3   XbaI SpeI BamHI SmaI      EcoRI EcoRV         ClaI SalI XhoI
p414 TRP1   XbaI SpeI BamHI SmaI PstI EcoRI               ClaI SalI XhoI
p415 LEU2   XbaI SpeI BamHI SmaI PstI             HindIII      SalI XhoI
p416 URA3   XbaI SpeI BamHI SmaI      EcoRI       HindIII ClaI SalI XhoI

p423 HIS3        SpeI BamHI SmaI      EcoRI EcoRV         ClaI SalI XhoI
p424 TRP1        SpeI BamHI SmaI PstI EcoRI               ClaI SalI XhoI
p425 LEU2        SpeI BamHI SmaI PstI             HindIII      SalI XhoI
p426 URA3        SpeI BamHI SmaI      EcoRI       HindIII ClaI SalI XhoI

```






