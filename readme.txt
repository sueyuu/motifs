please unzip all zip files first
because the github repostiory will be too large if we put all the training/validation folders in
so we only put multi source training/validation data here for demonstration

because pairwise distance calculation of original training set takes hours to run
we use only several sample cases here, in smoothed_multi_train_test
(we already save all the pairwise dtw distance for multi source training data in masked_arr_both_multi.npz)
first run calculate_pairwise_dist to get pairwise distance matrix

then use smoothed_multi_train and masked_arr_both_multi.npz, which are the original training set and the result of all pairwise distance of original training set
then run motif_training to get motifs algorithm pickles with different hyperparameters
(we already have all of the results in the folder)

then run motif_validation to see motif numbers and outlier numbers for selecting final algorithm we want
finally run pca_model_for_centers for compressing 2d returned barycenters result to 1d for further evaluation

some of the result files like npz and pkl are already in the folder

you can put the results elsewhere in case being overwritten when testing the code