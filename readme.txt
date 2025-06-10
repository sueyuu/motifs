please unzip all zip files first
because the github repostiory will be too large if we put all the training/validation folders in
so we only put multi source training/validation data here for demonstration
first run calculate_pairwise_dist to get pairwise distance matrix
we already save all the pairwise dtw distance for multi source training data in masked_arr_both_multi.npz
then run motif_training to get motifs algorithm pickles with different hyperparameters
we already have them in the repostiory
finally run motif_validation to see motif numbers and outlier numbers for selecting final algorithm we want