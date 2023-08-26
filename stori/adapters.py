import pandas as pd


class StoriAdapter:

    @staticmethod
    def extract_data_from_csv(file_path: str = "./temp/stori_transaction_data.csv") -> pd.DataFrame:
        """ Extract data from csv file.
        Format:
            Id,Date,Transaction
            0,7/15,+60.5
            1,7/28,-10.3
            2,8/2,-20.46
            3,8/13,+10
        """

        with open(file_path, 'r') as csv_file:
            datafrmae = pd.read_csv(csv_file, sep=',')
            return datafrmae
