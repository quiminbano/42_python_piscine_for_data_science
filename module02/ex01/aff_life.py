from load_csv import load
import matplotlib.pyplot as plt


def main():
    database = load("life_expectancy_years.csv")
    try:
        if database is None:
            raise AssertionError("")
        extracted_data = database[database['country'] == 'Finland']
        if extracted_data.shape[0] == 0:
            raise AssertionError("Country not found")
        extracted_data.set_index('country', inplace=True)
        extracted_data = extracted_data.transpose()
        extracted_data.plot()
        plt.title("Finland Life expectancy Projections")
        plt.xlabel("Year")
        plt.ylabel("Life expectancy")
        plt.show()
    except (KeyError, AssertionError) as e:
        print(e)


if __name__ == '__main__':
    main()
