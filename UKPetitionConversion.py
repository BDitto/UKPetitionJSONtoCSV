import pandas as pd, urllib.request as web, json

#script information
print("\n --------------------------------- \n "
      "UK Parlimnet JSON to CSV converter v0.220422" 
      "\n --------------------------------- \n"
      " This script is provided \"AS IS\" for the purposes of converting UK Parlimentary Petition data to a CSV format readable in most data packages (Excel, SAS, Tableu, Google Data Studio etc). This file will create 3 csv files in directory:\n"
      "\n Signatures by Country\n"
      "\n Signatures by Region\n"
      "\n Signatures by Constituency\n"
      "\n Field titles shall be saved as presentend by the UK Parlimentary Petitions data source"
      "\n \n No garuntees are expressed or implied by the author in making this script available. \n \n This script is made available under Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0) License \n Please remember to credit this script in your final outputs also\n --------------------------------- \n")


#retrieve petition

retloop = 0
while retloop != "1":
      print("Please enter/paste the pettition ID for the pettition you wish to convert (ie the last part of the pettition URL)")
      petURL = input("ID = ")
      print("\n --------------------------------- \n"
            "retrieving"
            "\n --------------------------------- \n")

      #load data
      js = json.load(web.urlopen("https://petition.parliament.uk/petitions/"+ str(petURL) +".json"))
      #print(js["data"]["attributes"].keys())


      print("this petition ID return the title:\n"
            "\"" +js["data"]["attributes"]["action"]+"\" \n")

      answer = "begin"
      while answer != "1" and answer != "0":
            print("Is this correct? \n Yes [1] \n no [0] \n")
            answer = str(input(""))
            print(answer)

      retloop = answer

#request output name:
print("Enter Output name: \n (This will be used to label output files)")
PetitionID = input("")

#load keys to verify file and simplyfy coding later as a reference point for keys
#print(js["data"]["attributes"].keys())


#convert JSON to Data Frame
countryDF = pd.DataFrame(js["data"]["attributes"]["signatures_by_country"])
constituency =  pd.DataFrame(js["data"]["attributes"]["signatures_by_constituency"])
region =  pd.DataFrame(js["data"]["attributes"]["signatures_by_region"])


#Optional choice to add UK apprend to consituency for google data studio inport
#constituency['name'] = constituency['name'] + ", UK"

#save country dataframes
countryDF.to_csv(PetitionID + "_By_Country.csv", index=False)
constituency.to_csv(PetitionID + "_By_constituency.csv", index=False)
region.to_csv(PetitionID + "_by_region.csv", index=False)

print("\n --------------------------------- \n"
      "individuals from " + str(len(constituency)) + " constituencys signed this peition. For binning purposes, there are " + str(len(constituency["signature_count"].unique())) + " unique values \n\n "
      "individuals from " + str(len(region)) + " regions signed this peition. For binning purposes, there are " + str(len(region["signature_count"].unique())) + " unique values \n\n"
      "individuals from " + str(len(countryDF)) + " countries signed this peition. For binning purposes, there are " + str(len(countryDF["signature_count"].unique())) + " unique values \n"
      "\n --------------------------------- \n")

print(" \n\n --script complete--")
