# JARVIS LAM - CS 12100
import numpy as np
import util

from sklearn.model_selection import train_test_split


class DataSet(object):
    '''
    Class for representing a data set.
    '''

    def __init__(self, dir_path):
        '''
        Constructor
        Inputs:
            dir_path: (string) path to the directory that contains the
              file

        Initializing five public variables:
        name: name of dataset
        predictor_vars: list of all predictor variables
        dependent_var: dependent variable
        labels: label of predictor variables and dependent variable
        data: a list with two elements, the first being the training data 
        and the second being the testing data
        '''

        # REPLACE pass WITH YOUR CODE

        # Read CVS and JSON files
        data = util.load_numpy_array(dir_path, "data.csv")
        parameters = util.load_json_file(dir_path, "parameters.json")
        # Initializing attributes
        self.name = parameters["name"]
        self.predictor_vars = parameters["predictor_vars"]
        self.dependent_var = parameters["dependent_var"]
        self.labels = data[0]
        self.data = train_test_split(data[1], train_size = parameters["training_fraction"],\
            test_size = None, random_state = parameters["seed"])


class Model(object):
    '''
    Class for representing a model.
    '''

    def __init__(self, dataset, pred_vars):
        '''
        Construct a data structure to hold the model.
        Inputs:
            dataset: an dataset instance
            pred_vars: a list of the indices for the columns used in
              the model.
        Initializing six public attributes:
        dataset: dataset for the model
        pred_vars: subset of all predictors that will be used for the model
        dep_var: dependent variable
        beta: all the linear coefficients after fitting the data
        R2: R-squared for the training data
        adj_R2: adjusted R-squared for the training data
        '''

        # REPLACE pass WITH YOUR CODE
        self.dataset = dataset # Must include since it's required for the str method
        self.pred_vars = pred_vars
        self.dep_var = dataset.dependent_var
        self.beta = util.linear_regression(dataset.data[0][:, pred_vars],\
            dataset.data[0][:, self.dep_var])
        self.R2 = self.calculate_R2(0)
        self.adj_R2 = self.R2 - (1 - self.R2)*\
        (len(self.pred_vars)/(len(dataset.data[0]) - len(self.pred_vars) - 1))

        
    def calculate_R2(self, test):
        '''
        Calculate R2 for either the training or testing data

        Input:
        dataset_: an array or matrix containing the training or testing data
        test: an integer indicating whether it's the train or test data
        1 is for testing, 0 is for training
        Output:
        A float containing R-squared value
        '''
        assert test == 0 or test == 1
        dataset_ = self.dataset.data[test] # Assign training or testing data
        # Calculate R2 according to the fomula in the PA
        numerator = ((dataset_[:, self.dep_var] - util.apply_beta(self.beta, dataset_[:, self.pred_vars])\
            ) ** 2).sum()
        denominator = ((dataset_[:, self.dep_var] - dataset_[:, self.dep_var].mean()) ** 2).sum()
        return 1 - numerator/denominator

    
    def __str__(self):
        '''
        Format model as a string
        '''

        # Replace this return statement with one that returns a more
        # helpful string representation
        s = '{} '.format(self.beta[0]) # Initialize string
        for beta in range(1, len(self.beta)): # Fill string with betas
            s += '+ {} * {} '.format(self.beta[beta], self.dataset.labels[self.pred_vars[beta - 1]])
        return "{} ~ ".format(self.dataset.labels[self.dep_var])+ s + "\n R2: {}".format( self.R2)

    ### Additional methods here


    def __repr__(self):
        '''
        Method for printing object
        '''

        return "Dataset name: {}, Prediction variables: {}".format(self.dataset.name, self.pred_vars)


def compute_single_var_models(dataset):
    '''
    Computes all the single-variable models for a dataset

    Inputs:
        dataset: (DataSet object) a dataset

    Returns:
        List of Model objects, each representing a single-variable model
    '''

    # Replace [] with the list of models
    return [Model(dataset, [i]) for i in dataset.predictor_vars]


def compute_all_vars_model(dataset):
    '''
    Computes a model that uses all the predictor variables in the dataset

    Inputs:
        dataset: (DataSet object) a dataset

    Returns:
        A Model object that uses all the predictor variables
    '''

    # Replace None with a model object
    return Model(dataset, dataset.predictor_vars)


def compute_best_pair(dataset):
    '''
    Find the bivariate model with the best R2 value

    Inputs:
        dataset: (DataSet object) a dataset

    Returns:
        A Model object for the best bivariate model
    '''

    # Replace None with a model object
    # Loop through nested for loops for the best R2 model, the key is defined
    # in the function below
    return max([Model(dataset, [i,j]) for i in dataset.predictor_vars \
    for j in range(i+1, len(dataset.predictor_vars))], key = R2_value)


def R2_value(model):
    '''
    Return R-squared value of a Model object to be used as key

    Input: 
    model: a Model object
    Output: Its R2 attribute
    '''
    return model.R2


def backward_selection(dataset):
    '''
    Given a dataset with P predictor variables, uses backward selection to
    compute the best models for every value of K between 1 and P.

    Inputs:
        dataset: (DataSet object) a dataset

    Returns:
        A list (of length P) of Model objects. The first element is the
        model where K=1, the second element is the model where K=2, and so on.
    '''
    # create a modifiable copy of the predictors
    predictor_vars = dataset.predictor_vars[:]
    # Initializing output list
    model_list =[Model(dataset, dataset.predictor_vars)]
    # Filling the list by decreasing values of K
    for K in range(len(dataset.predictor_vars) - 1, 0, -1):
        # Create list of possible models for a particular K
        models = [Model(dataset, predictor_vars[0:i] + predictor_vars[i+1:len(predictor_vars)])\
         for i in range(0,len(predictor_vars))]
        # Get the max R -squared model and insert it into output list
        model_list.insert(0, max(models, key = R2_value))
        # Delete this ma model's predictor from the list of predictors
        del predictor_vars[models.index(max(models, key = R2_value))]

    # Replace [] with the list of models
    return model_list


def choose_best_model(dataset):
    '''
    Given a dataset, choose the best model produced
    by backwards selection (i.e., the model with the highest
    adjusted R2)

    Inputs:
        dataset: (DataSet object) a dataset

    Returns:
        A Model object
    '''

    # Replace None with a model object
    # Return the model with the highest adj_R2 value, a.k.a with
    # the best K, key is defined below
    return max(backward_selection(dataset), key = adj_R2_value)


def adj_R2_value(model):
    '''
    Return adjusted R-squared value of a Model object to be used as key

    Input: 
    model: a Model object
    Output: Its adj_R2 attribute
    '''
    return model.adj_R2


def validate_model(dataset, model):
    '''
    Given a dataset and a model trained on the training data,
    compute the R2 of applying that model to the testing data.

    Inputs:
        dataset: (DataSet object) a dataset
        model: (Model object) A model that must have been trained
           on the dataset's training data.

    Returns:
        (float) An R2 value
    '''

    # Replace 0.0 with the correct R2 value
    # Using calculate_R2 function from the Model class, 
    # pass in 1 for testing data
    return model.calculate_R2(1) 

