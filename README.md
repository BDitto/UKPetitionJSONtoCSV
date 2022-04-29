# UKPetitionJSONtoCSV
Convert UK Parlimentary Petition data from JSON to CSV format readable in most data packages (Excel, SAS, Tableu, Google Data Studio etc)
--

This script is provided "AS IS" for the purposes of converting UK Parlimentary Petition data to a CSV format readable in most data processing/visualisation packages (Excel, SAS, Tableu, Google Data Studio etc). This file will create 3 csv files in directory:

 - Signatures by Country
 - Signatures by Region
 - Signatures by Constituency

Please note:
- Field titles shall be saved as presentend by the UK Parlimentary Petitions data source and as such may require additional editing/scripting to suit your needs
- This script has been written to be compatible as of April 2022. Pettitions prior to this date may not work with this script without modification. 
 
This script is made available under GNU General Public License v3.0 License, No garuntees are expressed or implied by the author in making this script available.

This script utalises PANDAS which can be found at https://github.com/pandas-dev/pandas and is distributed under BSD 3-Clause License found here: 
https://github.com/pandas-dev/pandas/blob/main/LICENSE

The author makes ABSOLUTELY NO claims of affilitation with or of rights to the PANDAS project(s) but thanks them for their continued work for the good of the data science community.
 
Acknowledgement in final outputs that have used this script are appreciated.


# Usage Guide
--

**Requirements**:
 - This module **Requires internet access** to function and availability of the UK Parlimentary Pettions Website
 - This module requires the ID of the Parlimentary Petition you wish to obtain CSV data from. This can usually be found as the last segment of the Pettition page URL
 - This script requires Pandas to be installed within your python enviroment [ pip install pandas ]

This function is designed to be very simple to use with both a "Manual" and "automated" option available. By default, outputs will be exported to the DIR from which code is being run. 

Manual:
--
In order to use this Function in Manual Mode import this module and call the function without arguments, the script will automaticcaly enable verbose logging and request required information from the user

Automate:
--
To use the Function in Automatic mode please pass the following Arguments

- automate (1, 0)
    - Must be set as 1 for automation
- petitionID (*string*)
    - The pettition ID for the pettition you wish to convert (ie the last part of the pettition URL)
- outputName (*string*)
     - The prefix of output files for easier identification when workingg with multiple petitions
- CountryOutput (1, 0)
     - Enabled/Disable Output data relating to number of signitures recieved from different Countries
- RegionOutput = (1, 0)
     - Enabled/Disable Output data relating to number of signitures recieved from different Regions
- constituencyOutput = (1, 0)
     - Enabled/Disable Output data relating to number of signitures recieved from different Constituencies. 
- verbose = (1, 0)
     - Enabled/Disable Verbose Logging

