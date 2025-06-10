please unzip all zip files first
because the github repostiory will be too large if we put all the training/validation folders in
so we only put multi source training/validation data here for demonstration
first run calculate_pairwise_dist to get pairwise distance matrix
we already save all the pairwise dtw distance for multi source training data in masked_arr_both_multi.npz
then run motif_training to get motifs algorithm pickles with different hyperparameters
we already have them in the repostiory
then run motif_validation to see motif numbers and outlier numbers for selecting final algorithm we want
finally run pca_model_for_centers for compressing 2d returned barycenters result to 1d for further evaluation

some of the result files like npz and pkl are already in the folder

you can put the results elsewhere in case being overwritten when testing the code