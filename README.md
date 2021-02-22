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

## Getting started

This will run everything in localhost to show you the demo:

```
git clone git@github.com:nostalgia-cnt/vibe.git
cd vibe
python3 app.py
```

Now go to 0.0.0.0:5000 in browser and proceed and can see what has been done so far.

## Problem

According to the World Health Organization (WHO), a new case of dementia is diagnosed every 3 seconds. That’s 28,800 per day or over 10 million people per year. 
* **Late diagnosis / poor outcomes** - AD is present up to 20 years before the disease is manifested. 
* **Early treatment** is helpful to delay the progression to improve outcomes and lower costs.
* **Strong need** to detect AD earlier on, allowing for earlier therapies to slow decline of AD symptoms, improve treatment outcomes and ensure patients a greater quality of life.

## Eye tracking + Alzheimer's disease
Below are several studies that indicate the effectiveness of using visual biomarkers for characterizing Alzheimer's disease, MCI, and controls:

![](https://github.com/nostalgia-cnt/vibe/blob/main/assets/Screen%20Shot%202021-02-20%20at%205.25.43%20PM.png)

## Tasks
Describe tasks here.
Proposed here are 3 explicit tasks used to baseline AD and related disorders:
- **picture task** - black and white pictures were selected to prevent color from affecting the stimulus 
- **sentence reading task** - grandfather passage is a standard passage for speech-related research and covers all the major phonemes in the English language and has been proven to work on this population.
- **video task** - we selected a complicated video in black-and-white as a design consideration for AD and related disorders

These tasks are elaborated upon in the demo below.

## Potential confounders
It's of note that using eye tracking features for diagnosing AD can have multiple confounders including: 
* <strong>Oculomotor abnormalities</strong> - Oculomotor abnormalitie may exist in other diseases and so algorithms may have false positives if these diseases are not screened out at onset of the screen (e.g. Multiple System Atrophy has slower prosaccade and increased antisaccade errors)
* <strong>Aging affects saccades</strong> - Eyesight is affecting as you age (e.g. visual acuity changes to have worse vision), as well as reaction time, and so these things may bias or confound any diagnostic marker for the eyes; this is very similar to confounds that exist in other areas like vocal biomarker research studies.
* <strong>Less controlled setups </strong> - Many different setups can affect the recording of eye conditions including brightness, corrective lenses, orientation of the face / angle, and ambient visual noise.

## License
The code in this repository is licensed by the [Apache 2.0 license](https://www.apache.org/licenses/LICENSE-2.0.html).

Some notes:
* [Eyegazer.js](https://webgazer.cs.brown.edu/) has custom licensing, so check that out if you want to use this commercially.
* Images used in the protocol licensed under creative common license using Google search.
* Logo was built using Inkscape and is licensed under the [Apache 2.0 license](https://www.apache.org/licenses/LICENSE-2.0.html).

## References
Some other repositorities that you may like to look into include:
- [eyegazer](https://github.com/brownhci/WebGazer)
- [eyelike](https://github.com/trishume/eyeLike)
- [pupil](https://github.com/pupil-labs/pupil)
- [oculomatic](https://github.com/oculomatic/oculomatic-release)

Research papers that are useful in the space include:
* [Review article on eye tracking research for AD](https://www.hindawi.com/journals/cmmm/2018/2676409/)
* [Nature - eye tracking datasets](https://www.nature.com/articles/sdata2016126)

The most commonly used screening tools for AD diagnosis:
* [MMSE](https://cgatoolkit.ca/Uploads/ContentDocuments/MMSE.pdf)
