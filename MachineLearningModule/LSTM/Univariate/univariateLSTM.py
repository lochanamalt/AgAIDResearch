class UnivariateLSTM:
    def __init__(self, num_epochs: int = 500, optimizer: str ='adam', loss_function: str ='mse',
                 verbose: int = 1, activation_function: str = 'relu') -> None:
        self.num_epochs = num_epochs   
        self.optimizer = optimizer
        self.loss_function = loss_function
        self.verbose = verbose
        self.activation_function = activation_function

    def train(self, training_sequences: list[list], target_values: list[float]):
        # TODO: Function description
        """
        Used to train LSTM
        """    
        raise NotImplementedError("No train function implemented")

    def predict(self, sequence: list):
        # TODO: Function description
        """
        Function to be called to get predicted value after training
        """
        raise NotImplementedError("No predict function implemented")
    