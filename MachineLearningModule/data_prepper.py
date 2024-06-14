from DataStructures.plot import Plot
from Helpers.utility import get_plot
from numpy import array


class DataPrepper:
    def __init__(self, plots: list[Plot]) -> None:
        self.data_set = plots

    def get_univariate_set(
        self, variety_index: int, replication_variety: int, target_variate: str
    ) -> list:
        """
        Get a list of values of given variety, block, and target variate
        variety_index (int): Variety index describing the variety plot
        replication_variety (int): Number representing the block for a plot
        target_variate (str): The variate type to target in the plot
        returns (list): list of target variate values
        """
        plot = get_plot(variety_index, replication_variety, self.data_set)
        univariate_set = []
        for dp in plot.data_points:
            value = getattr(dp.vi_state, target_variate, None)
            if value is None:
                value = getattr(dp.conditions_state, target_variate, None)
            if value is not None:
                univariate_set.append(value)
        return univariate_set

    # https://machinelearningmastery.com/how-to-develop-lstm-models-for-time-series-forecasting/
    @staticmethod
    def split_sequence(sequence, n_steps):
        X, y = list(), list()
        for i in range(len(sequence)):
            # find the end of this pattern
            end_ix = i + n_steps
            # check if we are beyond the sequence
            if end_ix > len(sequence) - 1:
                break
            # gather input and output parts of the pattern
            seq_x, seq_y = sequence[i:end_ix], sequence[end_ix]
            X.append(seq_x)
            y.append(seq_y)
        return array(X), array(y)

    @staticmethod
    def split_sequence_target_yield(sequence: list, n_steps: int, yeild: float):
        """
        Split the data into sets of length n_steps and have their target always be yeild
        sequence (list): Univariate list of numbers
        n_steps (int): Length of sets that will be fed to the LSTM model
        yeild (float): The target yield amount that the model is meant to predict towards
        """
        sets = []
        target_outputs = []
        for i, _ in enumerate(sequence):
            end_i_set = i + n_steps
            if end_i_set > len(sequence):
                break
            seq_set, seq_target_ouput = sequence[i:end_i_set], yeild
            sets.append(seq_set)
            target_outputs.append(seq_target_ouput)
        return array(sets), array(target_outputs)