from load_csv import load
import matplotlib.pyplot as plt


def main():
    data_expectancy = load("life_expectancy_years.csv")
    income_perc = load("income_per_person_gdppercapita\
_ppp_inflation_adjusted.csv")
    try:
        if data_expectancy is None or income_perc is None:
            raise AssertionError("Program failed loading data")
        print(data_expectancy['country'])
        # set country as index
        # loc only the 1900 column
        # merge the two dataframes using concat (ensure the index is the same)
        merged_data = data_expectancy[['country', '1900']].merge(income_perc[['country', '1900']], on='country')
        # clean the rows that have NaN values
        # plot the data (look at subject x axis, it seems exponential)
    except AssertionError as e:
        print(e)

if __name__ == '__main__':
    main()
