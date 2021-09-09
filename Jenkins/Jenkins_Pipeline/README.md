
# Create Build pipeline and devlivery pipeline
# Installation
1. Setup jenkins
2. Create jobs e.g `Freestyle project`
    ```
    job1: Build_1
    job2: Process_2
    job3: Deploy_3
    ```
3. In job configuration, add build trigger 'e.g check if build_1 is done then executes process_2'
<img src="job_config.png" height=80% width=80%> </img>
3. Install `Build Pipeline` and `Delivery Pipeline` plugin in jenkins
4. Click on  "+" tab for adding views
5. (For Built pipeline) In `Upstream / downstream config` add first build project
<img src="config.png" height=80% width=80%> </img>
6. (For Delivery Pipeline) under `Components` click 'add' to add first build project 
<img src="config2.png" height=80% width=80%> </img>
4. View built Pipeline or see overview with delivery Pipeline

# Build pipeline
<img src="built.png" height=80% width=80%> </img>

# Delivery Pipeline
<img src="deliver.png" height=80% width=80%> </img>