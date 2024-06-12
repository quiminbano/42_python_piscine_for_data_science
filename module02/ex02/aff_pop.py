from load_csv import load
import matplotlib.pyplot as plt


def convert_population(pop: str):
    """This function converts a string that represents a number in human
readable format and converts it into a float number"""
    if isinstance(pop, str) is False:
        return pop
    if len(pop) == 0:
        raise AssertionError("The data is empty")
    to_convert = 0.0
    if 'k' in pop:
        to_convert = (float(pop.replace('k', '')) * 1e3)
    elif 'K' in pop:
        to_convert = (float(pop.replace('K', '')) * 1e3)
    elif 'M' in pop:
        to_convert = (float(pop.replace('M', '')) * 1e6)
    else:
        to_convert = float(pop)
    to_convert = (to_convert / 1e6)
    return to_convert


def main():
    """This function extract information about the population projections
of Finland and France and plot it"""
    data = load("population_total.csv")
    list_help = ['Finland', 'France']
    try:
        if data is None:
            raise AssertionError("Error trying processing the data")
        selected_data = data[data['country'].isin(list_help)]
        selected_data.set_index('country', inplace=True)
        selected_data = selected_data.transpose()
        selected_data['Finland'] = \
            selected_data['Finland'].apply(convert_population)
        selected_data['France'] = \
            selected_data['France'].apply(convert_population)
        selected_data.plot()
        plt.title("Population projections")
        y_ticks = plt.gca().get_yticks()
        plt.gca().set_yticks(y_ticks)
        plt.gca().set_yticklabels([f"{int(iter)}M" for iter in y_ticks])
        plt.xlabel("Year")
        plt.ylabel("Population")
        plt.show()

    except (AssertionError, KeyError) as e:
        print(e)


if __name__ == '__main__':
    main()
