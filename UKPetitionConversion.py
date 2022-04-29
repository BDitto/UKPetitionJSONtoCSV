import pandas as pd, urllib.request as web, json

# ---------------------------------
#UK Parliment JSON to CSV converter
version = "v1.220427.2"
#Last Updated: 27 April 2022
#---------------------------------
#This script is provided AS IS for the purposes of converting UK Parlimentary Petition data to a CSV format readable in most data packages (Excel, SAS, Tableu, Google Data Studio etc). This file will create 3 csv files in directory:
#
#       Signatures by Country
#       Signatures by Region
#       Signatures by Constituency
#
# Field titles shall be saved as presentend by the UK Parlimentary Petitions data source
#
# No garuntees are expressed or implied by the author in making this script available.
# This script is made available under GNU General Public License v3.0 license
#
# This script requires and utalises PANDAS which can be found at https://github.com/pandas-dev/pandas and is distributed under BSD 3-Clause License found here: https://github.com/pandas-dev/pandas/blob/main/LICENSE
#
# The author makes ABSOLUTELY NO claims of affilitation with or of rights to the PANDAS project(s) but thanks them for their continued work for the good of the data science community.
#
# Please remember to credit this script in your final outputs also
#
# Please see README at github.com/BDitto/UKPetitionJSONtoCSV for further guidence on how to utalise this script

def UKPetitionJSONtoCSV(automate = 0,pettitionID = 0, outputName = "", CountryOutput = 1, RegionOutput = 1, constituencyOutput = 1, verbose = 1):

    #set verbose terminal logging:

    if automate == 0:
        #verbose logging is always enabled where automation is not utalised in order to ensure clear script progression feedback
        verbose = 1

    if verbose == 1:
        print("\n Verbose logging enabled: UK Parlimnet JSON to CSV converter " + version + "\n")


    #retrieve petition from user manually

    if automate == 0:
        retloop = 0
        while retloop != "1":
            print("Please enter/paste the pettition ID for the pettition you wish to convert (ie the last part of the pettition URL)")
            petURL = input("ID = ")
            print("\n --------------------------------- \n"
                  "retrieving"
                  "\n --------------------------------- \n")

            #load data
            js = json.load(web.urlopen("https://petition.parliament.uk/petitions/"+ str(petURL) +".json"))


            print("this petition ID return the title:\n"
                  "\"" +js["data"]["attributes"]["action"]+"\" \n")

            answer = "begin"
            while answer != "1" and answer != "0":
                print("Is this correct? \n Yes [1] \n no [0] \n")
                answer = str(input(""))
                print(answer)

            retloop = answer

    #auto retrieve petition
    if automate == 1:
        if verbose == 1:
            print("Loading Pettition")
        js = json.load(web.urlopen("https://petition.parliament.uk/petitions/" + str(pettitionID) + ".json"))
        if verbose == 1:
            print("petition Title:\n"
                  "\"" + js["data"]["attributes"]["action"] + "\" \n")

    #request manual output name:
    if automate == 0:
        print("Enter Output name: \n (This will be used to label output files)")
        outputName = input("")

    if automate == 1:
        if verbose == 1:
            print("\n output prefixed with " + outputName)

    #convert JSON to Data Frames and export

    if verbose ==1:
        print("\n Begging Conversion and Saving Output \n")

    if CountryOutput == 1:
        countryDF = pd.DataFrame(js["data"]["attributes"]["signatures_by_country"])
        countryDF.to_csv(str(outputName) + "_By_Country.csv", index=False)
        if verbose == 1:
            print("Country Conversion Complete")
            print("individuals from " + str(
                len(countryDF)) + " countries signed this peition. For binning purposes, there are " + str(
                len(countryDF["signature_count"].unique())) + " unique values \n\n")

    if RegionOutput == 1:
        region = pd.DataFrame(js["data"]["attributes"]["signatures_by_region"])
        region.to_csv(str(outputName) + "_by_region.csv", index=False)
        if verbose == 1:
            print("Region Conversion Complete")
            print("individuals from " + str(len(region)) + " regions signed this peition. For binning purposes, there are " + str(len(region["signature_count"].unique())) + " unique values \n\n")

    if constituencyOutput== 1:
        constituency = pd.DataFrame(js["data"]["attributes"]["signatures_by_constituency"])
        constituency.to_csv(str(outputName) + "_By_constituency.csv", index=False)
        if verbose == 1:
            print("Constituency Conversion Complete")
            print("individuals from " + str(len(constituency)) + " constituencys signed this peition. For binning purposes, there are " + str(len(constituency["signature_count"].unique())) + " unique values \n\n ")

    if verbose == 1:
        print(" \n\n script complete")
