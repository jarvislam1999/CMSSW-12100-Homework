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
        '''

        # REPLACE pass WITH YOUR CODE
        data = util.load_numpy_array(dir_path, "data.csv")
        parameters = util.load_json_file(dir_path, "parameters.json")
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
        '''

        # REPLACE pass WITH YOUR CODE
        self.pred_vars = pred_vars
        self.dep_var = dataset.dependent_var
        self.beta = util.linear_regression(dataset.data[0][:, pred_vars],\
            dataset.data[0][:, self.dep_var])
        self.R2 = self.calculate_R2(dataset.data[0])
        self.adj_R2 = self.R2 - (1 - self.R2)*\
        (len(self.pred_vars)/(len(dataset.data[0]) - len(self.pred_vars) - 1))
        
    def calculate_R2(self, dataset_):
        return 1 - (((dataset_[:, self.dep_var] - util.apply_beta(self.beta, dataset_[:, self.pred_vars])\
            ) ** 2).sum()/((dataset_[:, self.dep_var] - dataset_[:, self.dep_var].mean()) ** 2).sum())
    
    def __str__(self):
        '''
        Format model as a string
        '''

        # Replace this return statement with one that returns a more
        # helpful string representation
        return "CRIME_TOTALS ~ {} + {} * {}\n R2: {}".format(self.beta[0], self.dataset.labels[self.pred_vars[0]],\
            self.beta[1], self.R2)

    ### Additional methods here

    def __repr__(self):
        '''
        Format model as a string
        '''

        # Replace this return statement with one that returns a more
        # helpful string representation
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
    return max([Model(dataset, [i,j]) for i in dataset.predictor_vars \
    for j in range(i+1, len(dataset.predictor_vars))], key = R2_value)


def R2_value(model):
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
    predictor_vars = dataset.predictor_vars[:]
    model_list =[Model(dataset, dataset.predictor_vars)]
    
    for K in range(len(dataset.predictor_vars) - 1, 0, -1):
        models = [Model(dataset, predictor_vars[0:i] + predictor_vars[i+1:len(predictor_vars)])\
         for i in range(0,len(predictor_vars))]
        #max_model = max(models, R2_value)
        model_list.insert(0, max(models, key = R2_value))
        # print(max(models, key = R2_value))
        del predictor_vars[models.index(max(models, key = R2_value))]

    # Replace [] with the list of models
    return model_list

def adj_r2_value(model):
    return model.adj_R2

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
    return max(backward_selection(dataset), key = adj_r2_value)


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
    return model.calculate_R2(dataset.data[1])

