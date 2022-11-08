# Udagram Infrastructure Outage Incident Report
Posted: Monday, November 7, 2022

![Flogging a dead horse](post-mortem-meetings.jpg)

On Friday, November 4, the Udagram API went down, making the entire application nonfunctional. This report details the nature of the outage and the response.

## Issue Summary
From 4:32 PM to 5:19 PM (GMT), requests to the Udagram API returned 500 error responses. The issue immediately made the application unavailable. The root cause was an invalid configuration change that caused memory errors.

## Timeline
4:25 PM: Configuration push begins
4:32 PM: Outage begins
4:33 PM: Monitoring agent alerted for the unavailable application
4:49 PM: Failed configuration change rolled back to previous known state
4:51 PM: Begin examining the kubernetes pod log files and pod states
4:53 PM: Realized the deployments contained insufficient memory resources
4:55 PM: Assigned correct memory and pushed new config
5:12 PM: New state deployed
5:19 PM: New state works and 100% of traffic online

## Root Cause And Resolution
A spike in the number of users necessitated the increase in the availability of the application. The first step was to redefine the autoscaling rules of the application, requiring that new pods be created once existing pods surpassed 45% usage. The second step was to increase the deployment memory resources of the pods. The DevOps engineer forgot this step and so when the maximum number of pods that could be created was reached, the application still became entirely unavailable.

The resolution was to first return to the initial state and then begin the process all over. This was done to prevent unpredictable errors from occuring.

## Corrective And Preventative Measures
The most direct method is to automate this change with a script instead of doing it manually one step at a time. Also this script has to be reviewed by a peer involved in the process to ensure nothing is missing. Also, no configuration change should skip testing, no matter the case.

A preventative measure advised is to plan ahead for spikes in the number of users instead of responding to them when they happen. This planning should include proper scaling, resource management and monitoring.
