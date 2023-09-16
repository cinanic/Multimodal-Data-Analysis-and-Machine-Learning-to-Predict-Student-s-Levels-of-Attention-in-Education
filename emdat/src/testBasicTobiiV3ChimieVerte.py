"""
UBC Eye Movement Data Analysis Toolkit (EMDAT), Version 3
Created on 2015-08-15

Sample code to run EMDAT for a given experiment.

@author: Sebastien Lalle (creator)
Institution: The University of British Columbia.
"""

from BasicParticipant import *
from EMDAT_core.Participant import export_features_all, write_features_tsv
from EMDAT_core.ValidityProcessing import output_Validity_info_Segments, output_percent_discarded, output_Validity_info_Participants

# user list
ul = [ i for i in range(1,26)]
ul = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]



# user ids
uids = ul
# time offsets from start of the recording
alogoffset = [ 0 for i in range(1,26)]
alogoffset = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

# Read participants
ps = read_participants_Basic(user_list = ul, pids = uids, log_time_offsets = alogoffset, datadir = params.EYELOGDATAFOLDER,
                             prune_length = None,
                             #aoifile = "./sampledata/AOIs/general.aoi",
                             require_valid_segs = False,
                             auto_partition_low_quality_segments = False)

if params.DEBUG or params.VERBOSE == "VERBOSE":
    # explore_validation_threshold_segments(ps, auto_partition_low_quality_segments = False)
    output_Validity_info_Segments(ps, auto_partition_low_quality_segments_flag = False, validity_method = 3)
    output_percent_discarded (ps, r'C:\Users\Sina\Desktop\Stage V2\Sripts\emdat\src\outputfolder\smi_disc.csv')
    output_Validity_info_Segments(ps, auto_partition_low_quality_segments_flag = False, validity_method = 2,threshold_gaps_list = [100, 200, 250, 300], output_file = "C:\Users\Sina\Desktop\Stage\chimieverte\attention_detection_eyetracking_stage_smail\emdat\src\outputfolder\tobiiv3_Seg_val.csv" ) 
    output_Validity_info_Participants(ps, include_restored_samples = True, auto_partition_low_quality_segments_flag = False)


# WRITE features to file
#if params.VERBOSE != "QUIET":#
#    print#
#    print "Exporting:\n--General:", params.featurelist
#write_features_tsv(ps, './outputfolder/tobiiv3_sample_features_test.tsv', featurelist=params.featurelist, id_prefix=False)

aoi_feat_names = (map(lambda x:x, params.aoigeneralfeat))
if params.VERBOSE != "QUIET":
     print()
     print("Exporting features:\n--General:", params.featurelist, "\n--AOI:", aoi_feat_names)#, "\n--Sequences:", params.aoisequencefeat
write_features_tsv(ps, r'C:\Users\Sina\Desktop\Stage V2\Sripts\emdat\src\output\chimieverte_features_10.tsv',featurelist = params.featurelist,
            aoifeaturelabels = params.aoifeaturelist, id_prefix = True)
