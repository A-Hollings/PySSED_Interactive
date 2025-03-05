<b>PySSED version 1.1</b>

This version accompanies "The Nearby Evolved Stars Survey (NESS) V: properties of volume-limited samples of Galactic evolved stars" (McDonald et al., in review, MNRAS). Original reference: McDonald et al., 2024, RASTI, 3, 89.

PySSED should work out of the box using Python3 src/pyssed.py (see requirements.txt). However, if you need to add more filters, you will also need to download the model data files. Documentation, including detailed installation instructions, can be found in doc/Pyssed_manual.pdf.

To run the NESS models as in the MNRAS paper, you will need to change the programme setup to change the default filters to the NESS filters. In brief, run:

<tt>cd src/</tt><br>
Edit the NESS setup file so that <tt>RecomputeModelGrid = 1</tt>
<tt>
python3 makemodel.py bt-settl setup.ness
python3 pyssed.py single "Betelgeuse" simple setup.ness
source shorten-model.scr
</tt>
Edit the NESS setup file so that <tt>RecomputeModelGrid = 0</tt><br>
Then run your command, e.g.: <tt>python3 pyssed.py list "ness.sources" simple setup.ness</tt><br>
The same process can be used to add other filters - see manual for full details.
</tt>
