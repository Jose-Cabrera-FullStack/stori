# Connect the service with external services from infrastructure. (S3, Other APIs, etc.)
import csv
import pandas
# Extract data from csv file
# Path: stori/temp/stori_transaction_data.csv
# Format:
# "Id,Date,Transaction"
# "0,7/15,+60.5"
# "1,7/28,-10.3"
# "2,8/2,-20.46"
# "3,8/13,+10"

# TODO: check if use pandas or numpy for this


class StoriAdapter:

    @staticmethod
    def extract_data_from_csv(file_path: str) -> list:
        """ Extract data from csv file. """

        with open(file_path, 'r') as csv_file:
            df = pandas.read_csv(csv_file,sep=',')

            return df
