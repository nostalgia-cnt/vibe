# vibe

<p align="center">
  <img src="https://github.com/nostalgia-cnt/vibe/blob/main/assets/vibe.gif?raw=true">


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
[![Python](https://img.shields.io/badge/python-v3.6+-blue.svg)](https://github.com/jim-schwoebel/allie/blob/master/Dockerfile)
[![Dependencies](https://img.shields.io/badge/dependencies-up%20to%20date-brightgreen.svg)](https://github.com/jim-schwoebel/allie/blob/master/requirements.txt)
[![GitHub Issues](https://img.shields.io/github/issues/anfederico/Clairvoyant.svg)](https://github.com/jim-schwoebel/allie/issues)
[![Contributions welcome](https://img.shields.io/badge/contributions-welcome-orange.svg)](https://github.com/jim-schwoebel/allie/projects)
[![License](https://img.shields.io/badge/license-GPL%20(%3E%3D%202)-blue)](https://www.gnu.org/licenses/gpl-3.0.html)

</p>

The <strong>Vibe API</strong> is an all-purpose eye tracking web app and API for Alzheimer's disease research.

This was made on behalf of the 2021 CNT Hackathon at the [UW Center for Neurotechnology](http://www.csne-erc.org/).

## Getting started

This will run everything in localhost to show you the demo:

```
git clone git@github.com:nostalgia-cnt/vibe.git
cd vibe
pip3 install -r requirements.txt
python3 app.py
```

Now go to ```https://0.0.0.0:5000``` in browser and you can proceed with a demo.

<em>Note that this works best on linux operating systems and there may be some multi-threading errors on mac operating systems.</em>

## Demo 

You can watch a short demo by clicking [here](https://www.youtube.com/watch?v=_SEmT27oJOc&feature=youtu.be) or the gif below:

[![Vibe demo](https://github.com/nostalgia-cnt/vibe/blob/main/static/pictures/thumbnail.gif)](https://www.youtube.com/watch?v=_SEmT27oJOc&feature=youtu.be)

## Problem

According to the World Health Organization (WHO), a new case of dementia is diagnosed every 3 seconds. That’s 28,800 per day or over 10 million people per year. 
* **Late diagnosis / poor outcomes** - AD is present up to 20 years before the disease is manifested. 
* **Early treatment** is helpful to delay the progression to improve outcomes and lower costs.
* **Strong need** to detect AD earlier on, allowing for earlier therapies to slow decline of AD symptoms, improve treatment outcomes and ensure patients a greater quality of life.

## Solution: eye tracking biomarkers
Eye tracking has emerged as a low-cost, noninvasive tool to diganose and track Alzheimer's disease symptoms.

Eye movements and pupillary reflex have been used for several decades in neurological disease research. Careful examination of both allows to probe the medial temporal lobe memory system, the cholinergic neuronal pathways, the progressive neuropathological changes within the neocortex, and the brain dopamine activity.

Below are several studies that indicate the effectiveness of using visual biomarkers for characterizing Alzheimer's disease, MCI, and controls:

![](https://github.com/nostalgia-cnt/vibe/blob/main/assets/Screen%20Shot%202021-02-20%20at%205.25.43%20PM.png)

## Tasks
Upon reviewing the literature (see above), we built a custom protocol with four tasks that matches onto oculomotor symptoms/memory deficits present in MCI and Alzheimer's disease patients. 

### 1. baseline process
We created a simple baseline process for users to look to the right, down, left, up, and center to help build a regression model on your own eyes using Eyegazer API.

![](https://github.com/nostalgia-cnt/vibe/blob/main/static/pictures/baseline_front.png)

### 2. picture task
Two black and white pictures were selected to prevent color from affecting the stimulus, and the participant is asked to focus in on the rooster.

![](https://github.com/nostalgia-cnt/vibe/blob/main/static/pictures/picture_front.png)

### 3. sentence reading task
The [grandfather passage](https://www.amyspeechlanguagetherapy.com/uploads/7/5/7/4/7574967/grandfatherpassage.pdf) is a standard passage for speech-related research and covers all the major phonemes in the English language and has been proven to work on this population. Therefore, we used this passage and a countdown timer to get a window into how this task may affect cognitive impairment.

![](https://github.com/nostalgia-cnt/vibe/blob/main/static/pictures/text_front.png)
### 4. video task
We selected a complicated video in black-and-white as a design consideration for AD and related disorders.
![](https://github.com/nostalgia-cnt/vibe/blob/main/static/pictures/video_front.gif)

## Reports
After you complete all the tasks, you get a report like the one below showing your X and Y position of each task and how they compare to the average / general population.

![](https://github.com/nostalgia-cnt/vibe/blob/main/static/pictures/report_front.png)

## Potential confounders
It's of note that using eye tracking features for diagnosing AD can have multiple confounders including: 
* <strong>Oculomotor abnormalities</strong> - Oculomotor abnormalitie may exist in other diseases and so algorithms may have false positives if these diseases are not screened out at onset of the screen (e.g. Multiple System Atrophy has slower prosaccade and increased antisaccade errors).
* <strong>Aging affects saccades</strong> - Eyesight is affecting as you age (e.g. visual acuity changes to have worse vision), as well as reaction time, and so these things may bias or confound any diagnostic marker for the eyes.
* <strong>Less controlled setups </strong> - Many different setups can affect the recording of eye conditions including brightness, corrective lenses, orientation of the face / angle, and ambient visual noise.

We hope to address these confounds with additional experiments into the future.

## Contributors / Acknowledgements
First, we'd like to acknowledge the [UW Center for Neurotechnology](http://www.csne-erc.org/) for putting on an awesome virtual hack-a-thon during COVID-19! Without your support none of this work would have been possible - including coordinating user interviews and giving feedback on our report structure.

Second, we would like to sincerely thank the following contributors to this repository:
- [Jim Schwoebel](https://github.com/jim-schwoebel) - created the core survey structure / back-end in Flask/python.
- [Keaton Armentrout](https://github.com/orgs/nostalgia-cnt/people/ksarmentrout) - helped to get Eyegazer.js up-and-running / recording (through a PR).
- [Pamel Kang](https://github.com/orgs/nostalgia-cnt/people/pamelkkang) - helped to coordinate what report structures should look like / mock-ups.
- [Jayant Arora](www.linkedin.com/in/jayant-arora-0709541b7) - helped with selection of images and other protocol design elements.

Pull requests are welcome if you'd like to expand our work! 

## License
The code in this repository is licensed by the [GPL3 License](https://www.gnu.org/licenses/gpl-3.0.html). Because [Webgazer.js](https://webgazer.cs.brown.edu/) is distributed under this license and it is incorporated, we must license it under this license (we'd prefer [Apache 2.0 license](https://www.apache.org/licenses/LICENSE-2.0.html) to make it more widely distributed but [we can't](https://softwareengineering.stackexchange.com/questions/197710/how-to-use-gpl-v3-with-apache-license-2-0#:~:text=So%20if%20the%20code%20was,used%20under%20the%20Apace%20license.)).

Some notes:
* [Webgazer.js](https://webgazer.cs.brown.edu/) has custom licensing, so check that out if you want to use this commercially.
* Images used in the protocol licensed under creative common license using Google search.
* Logo was built using Inkscape and is licensed under the [Apache 2.0 license](https://www.apache.org/licenses/LICENSE-2.0.html).

## References
Some other repositorities that you may like to look into include:
- [webgazer](https://github.com/brownhci/WebGazer)
- [eyelike](https://github.com/trishume/eyeLike)
- [pupil](https://github.com/pupil-labs/pupil)
- [oculomatic](https://github.com/oculomatic/oculomatic-release)

Research papers that are useful in the space include:
* [Review article on eye tracking research for AD](https://www.hindawi.com/journals/cmmm/2018/2676409/)
* [Nature - eye tracking datasets](https://www.nature.com/articles/sdata2016126)
* [Nature - digital biomarkers for Alzheimer's disease](https://www.nature.com/articles/s41746-019-0084-2)

The most commonly used screening tools for AD diagnosis:
* [MMSE](https://cgatoolkit.ca/Uploads/ContentDocuments/MMSE.pdf)
* [Typical Alzheimer's diagnosis pathway](https://www.identifyalz.com/en_us/home/early-detection-and-diagnosis/early-detection-mci-alzheimers-disease.html?cid=PPC-GOOGLE-Healthcare+Industry_Testing_Diagnosis_Unbranded_Phrase~S~PH~UB~NER~HCP~CON-alzheimers+diagnosis-NA-p55497578899&gclsrc=aw.ds&&gclid=CjwKCAiAyc2BBhAaEiwA44-wW483-D4_wAXFhQQd17vU-9Em9yj_Gyqb1yY5BavaU4s1nrgkHManBBoCGNoQAvD_BwE&gclsrc=aw.ds)

Tasks assets (if you want to replicate our work):
* [The Grandfather passage](https://www.amyspeechlanguagetherapy.com/uploads/7/5/7/4/7574967/grandfatherpassage.pdf)
* [Image - rooster](https://github.com/nostalgia-cnt/vibe/blob/main/static/pictures/rooster.png)
* [Image - tree](https://github.com/nostalgia-cnt/vibe/blob/main/static/pictures/tree.png)
* [Video](https://github.com/nostalgia-cnt/vibe/blob/main/static/videos/walking.mp4)
