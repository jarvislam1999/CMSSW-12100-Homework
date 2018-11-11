'''
Polling places: test code for simulate_election_day
'''

import json
import pytest

from regression import DataSet, compute_single_var_models, \
  compute_all_vars_model, compute_best_pair, backward_selection, \
  choose_best_model, validate_model

# DO NOT REMOVE THESE LINES OF CODE
# pylint: disable-msg= invalid-name, missing-docstring, too-many-arguments, line-too-long
# pylint: disable-msg= missing-docstring, too-many-locals, unused-argument, broad-except
# pylint: disable-msg= assignment-from-none

DATASETS = ["city", "stock"]
DATA_DIR = "./data/"

@pytest.fixture(scope="session")
def test_data():
    """
    Fixture for loading the test data and creating the Dataset objects
    """
    test_data_file = DATA_DIR + "test_data.json"
    try:
        with open(test_data_file) as f:
            data = json.load(f)
    except IOError as e:
        pytest.fail("Unable to load test data file in {}".format(test_data_file), e)
    except Exception as e:
        pytest.fail("Unexpected exception: {}".format(e), e)

    for ds in DATASETS:
        data_dir = DATA_DIR + ds
        try:
            ds_obj = DataSet(data_dir)
        except IOError as e:
            pytest.fail("Unable to load dataset in {}".format(data_dir), e)
        except Exception as e:
            pytest.fail("Unexpected exception: {}".format(e), e)

        data[ds]["dataset_object"] = ds_obj

        with open(data_dir + "/data.csv") as f:
            header = f.readline()
            labels = header.strip().split(",")
            data[ds]["labels"] = labels

    return data


def fcompare(prefix, model_str, attribute, got, expected):
    assert got == pytest.approx(expected), prefix + model_str + "Incorrect {} (got {}, expected {})".format(attribute, got, expected)


def ds_labels(test_data, dataset, var_indexes):
    labels = test_data[dataset]["labels"]
    var_labels = [labels[x] for x in var_indexes]
    return var_labels


def model_labels(test_data, dataset, dep_var, pred_vars):
    dep_var_label = ds_labels(test_data, dataset, [dep_var])
    dep_var_label = dep_var_label[0]
    pred_vars_labels = ds_labels(test_data, dataset, pred_vars)
    return dep_var_label, pred_vars_labels


def check_models(test_data, dataset, func, models):
    """
    Given a list of models returned by one of the functions in Tasks 1-4,
    checks whether the correct models were returned
    """
    expected_models = test_data[dataset]["expected"][func]

    prefix = "\nTesting {} on {} dataset\n".format(func, dataset)

    # Check that the function returned the correct number of models
    err_msg = prefix + "Expected {} models, but got {}"
    err_msg = err_msg.format(len(expected_models), len(models))
    assert len(models) == len(expected_models), err_msg

    if None in models:
        pytest.fail(prefix + "The function returned None instead of a Model object")

    # Check that the list of models contains every expected model
    model_pairs = []
    for exp_model in expected_models:

        model = None
        for m in models:
            if m.dep_var == exp_model["dep_var"] and set(m.pred_vars) == set(exp_model["pred_vars"]):
                model = m
                break

        if model is None:
            dep_var_label, pred_vars_labels = model_labels(test_data, dataset,
                                                           exp_model["dep_var"],
                                                           exp_model["pred_vars"])
            pred_vars_labels = ", ".join(pred_vars_labels)
            err_msg = "Expected to find a model with dependent variable {} and predictor variables {}. No such model was returned."
            err_msg = err_msg.format(dep_var_label, pred_vars_labels)
            pytest.fail(prefix + err_msg)

        model_pairs.append((model, exp_model))

    # Check that each model has the correct values
    for model, exp_model in model_pairs:
        dep_var_label, pred_vars_labels = model_labels(test_data, dataset, exp_model["dep_var"], exp_model["pred_vars"])
        pred_vars_labels = ", ".join(pred_vars_labels)
        model_str = "<Model: dep_var={}, pred_vars={}>\n".format(dep_var_label, pred_vars_labels)

        beta0 = model.beta[0]
        exp_beta0 = exp_model["beta"][0]

        fcompare(prefix, model_str, "beta0", beta0, exp_beta0)

        betas = sorted(zip(model.pred_vars, model.beta[1:]))
        exp_betas = sorted(zip(exp_model["pred_vars"], exp_model["beta"][1:]))

        for (pred_var, beta), (exp_pred_var, exp_beta) in zip(betas, exp_betas):
            assert pred_var == exp_pred_var, "Unexpected error in tests. Please notify instructors."

            var_label = ds_labels(test_data, dataset, [pred_var])
            var_label = var_label[0]

            fcompare(prefix, model_str, "beta for " + var_label, beta, exp_beta)

        R2 = model.R2
        exp_R2 = exp_model["R2"]
        fcompare(prefix, model_str, "R2", R2, exp_R2)

        if "adj_R2" in exp_model:
            adj_R2 = model.adj_R2
            exp_adj_R2 = exp_model["adj_R2"]
            fcompare(prefix, model_str, "Adjusted R2", adj_R2, exp_adj_R2)


@pytest.mark.parametrize("dataset", DATASETS)
def test_task1a(test_data, dataset):
    dataset_obj = test_data[dataset]["dataset_object"]

    models = compute_single_var_models(dataset_obj)

    check_models(test_data, dataset, "compute_single_var_models", models)


@pytest.mark.parametrize("dataset", DATASETS)
def test_task1b(test_data, dataset):
    dataset_obj = test_data[dataset]["dataset_object"]

    model = compute_all_vars_model(dataset_obj)

    check_models(test_data, dataset, "compute_all_vars_model", [model])


@pytest.mark.parametrize("dataset", DATASETS)
def test_task2(test_data, dataset):
    dataset_obj = test_data[dataset]["dataset_object"]

    model = compute_best_pair(dataset_obj)

    check_models(test_data, dataset, "compute_best_pair", [model])


@pytest.mark.parametrize("dataset", DATASETS)
def test_task3(test_data, dataset):
    dataset_obj = test_data[dataset]["dataset_object"]

    models = backward_selection(dataset_obj)

    check_models(test_data, dataset, "backward_selection", models)


@pytest.mark.parametrize("dataset", DATASETS)
def test_task4(test_data, dataset):
    dataset_obj = test_data[dataset]["dataset_object"]

    model = choose_best_model(dataset_obj)

    check_models(test_data, dataset, "choose_best_model", [model])


@pytest.mark.parametrize("dataset", DATASETS)
def test_task5(test_data, dataset):
    dataset_obj = test_data[dataset]["dataset_object"]

    best_model = choose_best_model(dataset_obj)

    if best_model is None:
        pytest.fail("When testing Task #5, choose_best_model returned None instead of a Model object")

    testing_R2 = validate_model(dataset_obj, best_model)

    exp_training_R2 = test_data[dataset]["expected"]["validate_model"]["training_R2"]
    exp_testing_R2 = test_data[dataset]["expected"]["validate_model"]["testing_R2"]

    assert best_model.R2 == pytest.approx(exp_training_R2), "Incorrect Training R2"
    assert testing_R2 == pytest.approx(exp_testing_R2), "Incorrect Testing R2"
