import csv

# parsing the toxic release inventory from wrpdc
# https://data.wprdc.org/dataset/toxic-release-inventory

# create data tracking container prior to iterating through csv
tri_summary = {"incident_count": 0, "location": {},
               "year": {}, "parent_company": {}}

with open("tri_water.csv") as tri_file:
    dreader = csv.DictReader(tri_file)
    # prints the field names
    # print(dreader.fieldnames)
    for record in dreader:
        tri_summary["incident_count"] = tri_summary["incident_count"] + 1
        if record["ZIP_CODE"] not in tri_summary["location"]:
            tri_summary["location"][record["ZIP_CODE"]] = 1
        else:
            tri_summary["location"][record["ZIP_CODE"]] += 1
        if record["REPORTING_YEAR"] not in tri_summary["year"]:
            tri_summary["year"][record["REPORTING_YEAR"]] = 1
        else:
            tri_summary["year"][record["REPORTING_YEAR"]] += 1

    # prints the year and the count of that year
    prev_key = 0
    for y in sorted(tri_summary["year"]):
        print(y, ":", tri_summary["year"][y], end="")
        if prev_key != 0:
            # % change = prev - current / prev
            # TODO something isn't working here
            percent_delta = ((tri_summary["year"][prev_key] -
                              tri_summary["year"][y]) / tri_summary["year"][prev_key]) * 100
            print(", change", percent_delta)
        else:
            print()
        prev_key = y

    # prints the whole data set
    # print(record)
    # just prints the zipcodes with first 5 characters
    # print(record["ZIP_CODE"][0:5])
    # print(record["REPORTING_YEAR"])
    # print(record["CHEM_NAME"])
    # print(record["STANDARDIZED_PARENT_COMPANY"])
