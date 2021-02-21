# vibe

<p align="center">
  <img src="https://github.com/nostalgia-cnt/vibe/blob/main/assets/vibe.gif?raw=true">


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
[![Python](https://img.shields.io/badge/python-v3.6+-blue.svg)](https://github.com/jim-schwoebel/allie/blob/master/Dockerfile)
[![Dependencies](https://img.shields.io/badge/dependencies-up%20to%20date-brightgreen.svg)](https://github.com/jim-schwoebel/allie/blob/master/requirements.txt)
[![GitHub Issues](https://img.shields.io/github/issues/anfederico/Clairvoyant.svg)](https://github.com/jim-schwoebel/allie/issues)
[![Contributions welcome](https://img.shields.io/badge/contributions-welcome-orange.svg)](https://github.com/jim-schwoebel/allie/projects)
[![License](https://img.shields.io/badge/license-Apache%202-blue)](https://www.apache.org/licenses/LICENSE-2.0.html)
</p>

The <strong>Vibe API</strong> is an all-purpose eye tracking API for Alzheimer's disease research.

This was made on behalf of the 2021 CNT Hackathon at the [UW Center for Neurotechnology](http://www.csne-erc.org/).

## Problem

- Alzheimer's disease affects > worldwide. 
- The diagnosis occurs frequently at late stages of the disease, when symptoms are evident. 
- AD is present up to 20 years before the disease is manifested. 
- Treatment is helpful to delay the progression and improve quality of life. 
- There is a strong need for early diagnosis to improve treatment outcomes. 
- [MMSE exam](http://www.fammed.usouthal.edu/Guides%26JobAids/Geriatric/MMSE.pdf) is the current gold standard to diagnose MCI and dementia; it takes >50 minutes and requires an expert, which limits the ubiquity of AD screening in the population

## Eye tracking 
Read the review article on eye tracking research for AD [here](https://www.hindawi.com/journals/cmmm/2018/2676409/).

Below are several studies that indicate the effectiveness of using visual biomarkers for characterizing Alzheimer's disease, MCI, and controls:

![](https://github.com/nostalgia-cnt/vibe/blob/main/assets/Screen%20Shot%202021-02-20%20at%205.25.43%20PM.png)

## Tasks
Describe tasks here.
Proposed here are 3 explicit tasks used to baseline AD and related disorders:
- picture task 
- sentence reading task
- video task 

These tasks are elaborated upon in the demo below.

### Picture task
- black and white pictures were selected to prevent color from affecting the stimulus 
- images licensed under creative common license using Google search

### Sentence reading task
- reading sentences has been shown to correlate with AD in the eyes and also in the voice
- Grandfather passage is a standard passage for speech-related research and covers all the major phonemes in the English language and has been proven to work on this population.

### Video watch task
- we selected a complicated video in black-and-white as a design consideration for AD and related disorders

## Feature extraction pipeline

Here are the features that are outputted in every frame.
- mean fixation duration, fixation count, and mean saccade amplitude. 


## Potential confounders
It's of note that using eye tracking features for diagnosing AD can have multiple confounders including: 
* <strong>Oculomotor abnormalities</strong> - Oculomotor abnormalitie may exist in other diseases and so algorithms may have false positives if these diseases are not screened out at onset of the screen (e.g. Multiple System Atrophy has slower prosaccade and increased antisaccade errors)
* <strong>Aging affects saccades</strong> - Eyesight is affecting as you age (e.g. visual acuity changes to have worse vision), as well as reaction time, and so these things may bias or confound any diagnostic marker for the eyes; this is very similar to confounds that exist in other areas like vocal biomarker research studies.
* <strong>Less controlled setups </strong> - Many different setups can affect the recording of eye conditions including brightness, corrective lenses, orientation of the face / angle, and ambient visual noise.

## Acknowledgements

Thank you so much for the [UW Center for Neurotechnology](http://www.csne-erc.org/) for sponsoring such an awesome Hack-a-thon! 

We would not have been able to do this project without your support and sponsorship. 

You brought our team together and made this an enjoyable process to build this project.

## Additional reading 
- [eyelike](https://github.com/trishume/eyeLike)
- [pupil](https://github.com/pupil-labs/pupil)
- [oculomatic](https://github.com/oculomatic/oculomatic-release)
