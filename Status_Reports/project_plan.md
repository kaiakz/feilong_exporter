**Student's Name:** Kai Wong

**Mentor:** Chen ji

**Project:** Enhance zvm Prometheus exporter. 

**Project Description:** Enhance z/vm Prometheus exporter with [Feilong](https://www.openmainframeproject.org/projects/feilong). 

**Problem Definition:** As https://github.com/zvmexporter/zvm_exporter is pretty old and some stuffs like xcat is not maintained anymore, we propose to use Feilong as base to enhance Prometheus exporter and to provide more metrics to help ecosystem build up.

**Deliverables:** 
* Implement a new zvm Prometheus exporter supports more metrics(hosts, guests, CPU, memory, disk, etc.).
* Upgrade the monitoring dashboards.

**Coding Plan**

| Week | Tasks                                                                      | Goals                                                                                               |
|------|----------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|
|   1  | Get to know the team and setup up development environment                  | Familiarize myself with community and developement environment                                      |
|   2  | Read the document of python-zvm-sdk and communicate with mentor            | Understand how the RESTAPI and zvmconnector works app-generator                                     |
|   3  | Get familiar with the Prometheus client library and try other exporters    | Be able to use common functions of the library                                                      |
|   4  | Design the exporter and its metrics                                        | Write a list of metrics the exporter supports                                                       |
|   5  | Prepare the testing: a mock server                                         | The mock server acts like a python-zvm-sdk server and can be requested via standard feilong RESTAPI |
|   6  | Prepare the testing: response & other                                      | Have the test cases                                                                                 |
|   7  | Communicating with mentor for the MVP(minimun viable product)              | Have the plan and design of the MVP                                                                 |
|   8  | Implement the MVP                                                          | Release the MVP                                                                                     |
|   9  | Implement the MVP                                                          | Release the MVP                                                                                     |
|  10  | Finish the MVP, get feedback from mentor                                   | Release the MVP, have the plan and design of the next version                                       |
|  11  | Improve the exporter: performance                                          | Release the V2                                                                                      |
|  12  | Improve the exporter: add new features                                     | Release the V2                                                                                      |
|  13  | Finish the V2, get feedback from mentor                                    | Release the V2, have the plan and design of the next version                                        |
|  14  | Improve the exporter: add new features, dashboards                         | Release the V3                                                                                      |
|  15  | Improve the exporter: fix bugs                                             | Release the V3                                                                                      |
|  16  | Finish the V3, review the code, refactor                                   | Release the V3, pass the tests and code reviewing                                                   |
|  17  | Write the documents                                                        | Documentation for installation & usage                                                              |
|  18  | Write the documents                                                        | Documentation for architeture                                                                       |
|  19  | Write the documents, finish remaining tasks                                | Publish some documents on github wiki                                                               |
|  20  | Finish documentation and make a demo video                                 | Publish the documents and video demo for the project                                                |