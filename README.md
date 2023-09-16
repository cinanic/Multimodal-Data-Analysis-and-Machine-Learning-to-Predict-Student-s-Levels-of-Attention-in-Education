# Sina internship project

## Content of the repo (to be run in this order):

### [`Logs/`](Logs/)

- To run: `Logs.ipynb` : Align each Keyboard/Mouse action is related to each panopto event to find at each tobii time participant watching each moment of the video.
- **Input:**
  -'Tobii Data Export MouseKeyboard.csv' : Keyboard and Mouse events added action coulmn that we know each event makes what action.
  -'panopto_logs_filtered.csv': Panopto data that tell us at each moment of the video Participants play to watch and they watch for what duration.
  -'chimieverte2023_Participant_timestamps.csv': To find out the end time of the video in tobii.
- **Output:** 'panopto_data_updated_P01.csv' to 'panopto_data_updated_P25'.csv in the "new panopto" folder

- to run: 'QCM to Tobii time.ipynb' : To find each QCM end appearance and 20 seconds window size in tobii time.
- **Input:** 'panopto_data_updated_P01.csv' to 'panopto_data_updated_P25'.csv in the "new panopto" folder
- **Output:** 'P01_output.csv' to 'P05_output'.csv in the "QCM to Tobii time" folder


### [`preprocess and cleanup/`](preprocess and cleanup/)

- To run: `preprocess and cleanup.ipynb` : To preprocess and cleanup the eye trakcing data
- **Input:** the raw eye tracking data ; the start and end timestamps of the user study steps
- **Output:**   - `data_out/data_RecoveryDataEyeTracker/`: he eye tracking data filtered with only the data recorded during the main video watching task, only eye tracking data samples kept (mouse/keyboard/system removed), with a data recovering process to interpolate short period of lost data.

### [`emdat/`](emdat/)
Use of the EMDAT library to generate the summative eye tracking features 
- To tun: `python testBasicTobiiV3ChimieVerte.py` (requires Python 2.7)
- **Input** (in data_RecoveryDataEyeTracker): The recovered eye tracking data ; Segmet files (for each window sizes, exists in "data_RecoveryDataEyeTracker10" to "data_RecoveryDataEyeTracker30" you can modify segments by Untitled.ipynb in "data_RecoveryDataEyeTracker")
- **Output:** The set of eye tracking metrics computed for each segment and each participants, currently in: `output/chimieverte_features_10.tsv` to `output/chimieverte_features_30.tsv` for each window size

### [`new open face/`](new open face/)

- To run: `OpenFace fatures.ipynb` : Calculate summative features for each MCQ 
- **Input** (in open face data): data generated from OpenFace library (p1.csv to p25.csv)
- **Output:** openface10.tsv to openface30.tsv for each window size

- To run: `y gaze angle.ipynb` : to see gaze angle is below, up or on the screen 
- **Input** (in open face data): data generated from OpenFace library (p1.csv to p25.csv); the raw eye tracking data
- **Output:** (in tobii with eye angle):Participant1.tsv to Participant25.tsv for each participant

### [`emdat and openface clean up/`](emdat and openface clean up/)

- To run: `Emdat.ipynb` : To remove unwanted columns and rows from eytracker data for and keep all emdat features and each feature seprately 
- **Input** (it is output of the emdat): chimieverte_features_10.tsv to chimieverte_features_30.tsv
- **Output:** modified_EMDAT10.tsv to modified_EMDAT30.tsv; fixation10.tsv to fixation30.tsv; angles10.tsv to angles30.tsv; pupil10.tsv to pupil30.tsv; distance10.tsv to distance30.tsv

- To run: `openface.ipynb` : To remove unwanted columns and rows from webcam data for and keep all openface features and each feature seprately
- **Input** (in new open face): summative features we got from open face data for each window size in new open face
- **Output:** : modified_openface10.tsv to modified_openface30.tsv; AU10.tsv to AU30.tsv; gaze10.tsv to gaze30.tsv; pose10.tsv to pose30.tsv

- To run: `Merge.ipynb` : To have all needed eyetracker and webcam features in one tsv file.
- **Input** : modified_openface10.tsv and modified_EMDAT10.tsv (same for all window sizes)
- **Output:** : merged_data10.tsv to merged_data30.tsv

### [`Classification/`](Classification/)

- To run: `eyetracker classification .ipynb` : classification of all features of eytracker extracted from emdat (seprately or all together) 
- To run: `decision fusion - eyetracker.ipynb` : decision fusion of eyetracker features (voting classifier)
- **Input** (in emdat and openface clean up): all outputs of Emdat.ipynb in emdat and openface clean up
- **Output:** results in the folder name tobii

- To run: `webcam classification.ipynb` : classification of all features of webcam extracted from open face(seprately or all together) 
- To run: `decision fusion - webcam.ipynb` : decision fusion of webcam features (voting classifier)
- **Input** (in emdat and openface clean up): all outputs of openface.ipynb in emdat and openface clean up
- **Output:** results in the folder name openface

- To run: `feature fusion .ipynb` : classification of all features of webcam and eyetracker
- To run: `decision fusion - all features.ipynb` : decision fusion of all features (voting classifier)
- **Input** (in emdat and openface clean up): merged_data10.tsv to merged_data30.tsv in emdat and openface clean up
- **Output:** feature fusion10.csv to feature fusion30.csv and feature selection - feature_fusion10.csv to feature selection - feature_fusion30.csv