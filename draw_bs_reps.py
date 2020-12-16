#DSS2100 Final Assignment 
#Alex Horkan 19461736

# import packages
import pandas as pd
import numpy as np

# definine draw bootstrap replicas function 
def draw_bs_reps(data, func, size=1):
    """Draw bootstrap replicas"""
    
    # initialise replicates array
    bs_reps = np.empty(size)
    
    # generate replicates
    for i in range(size):
        # generate bootstrap sample
        bs_sample = np.random.choice(data, size=len(data))
        
        # compute replicate
        bs_data = func(bs_sample)
        
        # assign replicate to replicates array
        bs_reps[i] = bs_data
    
    # return replicates array
    return bs_reps

# main guard with assignment specific code
if __name__=='__main__':
    # ignore first 4 rows of metadata in the csv file
    fish_data = pd.read_csv('gandhi_et_al_bouts.csv',skiprows=4)
    
    # select wild type zebrafish from the dataset
    bout_lengths_wt = fish_data[fish_data.genotype == 'wt'].bout_length
    
    # select mutant zebrafish from the dataset
    bout_lengths_mut = fish_data[fish_data.genotype == 'mut'].bout_length
    
    # Compute mean active bout length
    mean_wt = np.mean(bout_lengths_wt)
    mean_mut = np.mean(bout_lengths_mut)
    
    # Draw bootstrap replicates
    bs_reps_wt = draw_bs_reps(bout_lengths_wt, np.mean, size=10000)
    bs_reps_mut = draw_bs_reps(bout_lengths_mut, np.mean, size=10000)
    
    # Compute 95% confidence intervals
    conf_int_wt = np.percentile(bs_reps_wt, [2.5, 97.5])
    conf_int_mut = np.percentile(bs_reps_mut, [2.5, 97.5])
    
    # Print the results
    print("""
    Wild type zebrafish: mean length = {0:.3f} min., confidence interval = [{1:.1f}, {2:.1f}] min.
    Mutant zebrafish: mean = {3:.3f} min., confidence interval = [{4:.1f}, {5:.1f}] min.
    """.format(mean_wt, *conf_int_wt, mean_mut, *conf_int_mut))
